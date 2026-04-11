#!/usr/bin/env python3
"""
Derives a database schema from decompiled Java + Groovy sources.

Since no entitymodel*.xml files exist in the decompiled archive, field names
and types are reconstructed from:
  - delegator.makeValue("Entity") followed by .set("field", …)      (write-side)
  - EntityQuery.from("Entity").where/select/orderBy("field", …)     (read-side)
  - GenericValue variable tracking (var = …from("Entity")…queryOne)

Type inference uses:
  1. The getter/setter method name (getTimestamp → datetime, getBigDecimal → decimal, …)
  2. Field name conventions (xxxDate → datetime, xxxId → varchar-id, isXxx → boolean, …)

Per-field output:
  name, type_key, java_type, sql_type, is_pk, fk_hint, refs
"""

import re
from collections import defaultdict
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[3]
JAVA_SRC  = ROOT / "decompiled" / "src" / "main" / "java" / "org" / "apache" / "ofbiz"
GROOVY_SRC = ROOT / "decompiled" / "src" / "main" / "groovy-origin"
DATA_DIR  = Path(__file__).resolve().parents[1] / "data"

# ── Patterns ──────────────────────────────────────────────────────────────────

ENTITY_PAT = r'"([A-Z][A-Za-z]{2,39})"'

RE_MAKE_VALUE  = re.compile(r'delegator\.makeValue\(' + ENTITY_PAT)
RE_FROM        = re.compile(r'\.from\(' + ENTITY_PAT)
RE_FIND_DIRECT = re.compile(
    r'delegator\.(?:findList|findByAnd|findOne|findByPrimaryKey|find|countByAnd)\('
    + ENTITY_PAT
)

# Capture both the accessor method and the field name
RE_FIELD_ACCESS = re.compile(
    r'\.(get|set|getString|getLong|getInteger|getDouble|getBigDecimal'
    r'|getTimestamp|getDate|getBoolean|getFloat'
    r'|where|orderBy|select|fetchFirst|groupBy)\s*\(\s*"([a-z][A-Za-z0-9_]{0,59})"'
)
RE_FIELD_COND = re.compile(r'makeCondition\s*\(\s*"([a-z][A-Za-z0-9_]{0,59})"')

RE_GV_ASSIGN = re.compile(
    r'GenericValue\s+(\w+)\s*=.*?\.from\(' + ENTITY_PAT
)
RE_GV_GET = re.compile(
    r'(\w+)\.(get|getString|getLong|getInteger|getBigDecimal|getTimestamp'
    r'|getDate|getBoolean|getDouble|getFloat)'
    r'\s*\(\s*"([a-z][A-Za-z0-9_]{0,59})"'
)


# ── Type system ───────────────────────────────────────────────────────────────

# OFBiz / Java getter → type_key
METHOD_TYPE: dict[str, str] = {
    "getTimestamp":  "datetime",
    "getDate":       "date",
    "getBigDecimal": "decimal",
    "getDouble":     "decimal",
    "getFloat":      "decimal",
    "getLong":       "integer",
    "getInteger":    "integer",
    "getBoolean":    "boolean",
}

# type_key → (java_type, sql_type, label)
TYPE_META: dict[str, tuple[str, str, str]] = {
    "id":        ("String",     "VARCHAR(20)",    "ID"),
    "id_long":   ("String",     "VARCHAR(60)",    "ID (lang)"),
    "type_ref":  ("String",     "VARCHAR(20)",    "Type-Ref"),
    "datetime":  ("Timestamp",  "DATETIME",       "Datum/Zeit"),
    "date":      ("Date",       "DATE",           "Datum"),
    "decimal":   ("BigDecimal", "DECIMAL(18,2)",  "Dezimal"),
    "integer":   ("Long",       "NUMERIC(20,0)",  "Integer"),
    "boolean":   ("String",     "CHAR(1)",        "Boolean (Y/N)"),
    "text":      ("String",     "VARCHAR(255)",   "Text"),
    "longtext":  ("String",     "LONGVARCHAR",    "Langtext"),
}


def infer_type_key(field: str, methods: set[str]) -> str:
    """Combine method evidence and naming conventions."""
    # Method evidence wins
    for method in methods:
        if method in METHOD_TYPE:
            return METHOD_TYPE[method]

    f = field.lower()

    # Boolean by name
    if f.startswith("is") or f.startswith("has") or f in {
        "taxable", "returnable", "enabled", "active", "required",
        "exported", "confirmed", "autoCreateKeywords", "includeInPromotions",
        "chargeShipping",
    }:
        return "boolean"

    # Date / time
    if f.endswith("date") or f.endswith("stamp"):
        return "datetime"
    if f.endswith("time") and not f.endswith("overtime") and not f.endswith("leadtime"):
        return "datetime"

    # Currency amounts
    if f.endswith("amount") or f.endswith("price") or f.endswith("total") \
            or f.endswith("cost") or f.endswith("rate") or f.endswith("discount"):
        return "decimal"

    # Quantities / counts
    if f.endswith("qty") or f.endswith("quantity") or f.endswith("count") \
            or f.endswith("num") or f.endswith("number") or f.endswith("seqid"):
        return "integer"

    # Type references (xxxTypeId)
    if f.endswith("typeid") or f.endswith("type_id"):
        return "type_ref"

    # Regular ID fields
    if f.endswith("id") or f.endswith("_id"):
        # Long IDs (e.g. partyContactMechId)
        if len(field) > 20:
            return "id_long"
        return "id"

    # Long text hints
    if f in {"description", "comments", "internalNote", "content", "details",
             "textData", "longDescription"}:
        return "longtext"

    return "text"


def sql_type(type_key: str) -> str:
    return TYPE_META.get(type_key, ("String", "VARCHAR(255)", "Text"))[1]

def java_type(type_key: str) -> str:
    return TYPE_META.get(type_key, ("String", "VARCHAR(255)", "Text"))[0]

def type_label(type_key: str) -> str:
    return TYPE_META.get(type_key, ("String", "VARCHAR(255)", "Text"))[2]


# ── Module helpers ────────────────────────────────────────────────────────────

def module_of(path: Path) -> str:
    try:
        return path.relative_to(JAVA_SRC).parts[0]
    except ValueError:
        pass
    if GROOVY_SRC.exists():
        try:
            return path.relative_to(GROOVY_SRC).parts[0]
        except ValueError:
            pass
    return "unknown"

MODULE_ENTITY_HINTS = {
    "order":       {"OrderHeader","OrderItem","OrderRole","OrderStatus",
                    "OrderItemShipGroup","OrderPaymentPreference",
                    "OrderAdjustment","OrderItemBilling","OrderShipment",
                    "OrderItemShipGroupAssoc","OrderContactMech"},
    "product":     {"Product","ProductAssoc","ProductPrice","ProductCategory",
                    "ProductCategoryMember","ProductFeature","ProductStore",
                    "ProductStoreShipmentMeth","ProductContent","ProductAttribute",
                    "ProductFacility","ProductKeyword"},
    "party":       {"Party","PartyRole","PartyRelationship","Person","PartyGroup",
                    "UserLogin","ContactMech","PartyContactMech","PostalAddress",
                    "TelecomNumber","PartyAttribute","PartyContent"},
    "accounting":  {"Invoice","InvoiceItem","Payment","PaymentApplication",
                    "GlAccount","GlAccountType","FinAccount","AcctgTrans",
                    "AcctgTransEntry","BillingAccount","PaymentGatewayResponse"},
    "content":     {"Content","ContentAssoc","DataResource","ContentRole",
                    "ContentPurpose","ElectronicText","ContentKeyword",
                    "ContentAttribute","SubContentDataResourceView"},
    "shipment":    {"Shipment","ShipmentItem","ShipmentRoute","ShipmentRouteSegment",
                    "ShipmentCostEstimate","CarrierShipmentMethod","ShipmentPackage",
                    "ShipmentPackageContent"},
    "manufacturing":{"WorkEffort","WorkEffortGoodStandard","WorkEffortStatus",
                     "WorkEffortPartyAssignment","WorkRequirementFulfillment",
                     "WorkEffortInventoryProduced","WorkEffortInventoryAssign"},
    "workeffort":  {"WorkEffortICalData","WorkEffortAttribute","WorkEffortContactMech",
                    "WorkEffortEventReminder","WorkEffortSkillStandard"},
    "humanres":    {"EmplPosition","EmplPositionType","Employment","PayGrade",
                    "PerformanceNote","EmploymentApp","EmplPositionFulfillment"},
    "marketing":   {"MarketingCampaign","ContactList","ContactListParty",
                    "TrackingCode","TrackingCodeOrder","TrackingCodeVisit"},
}

def dominant_module(entity: str, refs: dict[str, int]) -> str:
    for mod, entities in MODULE_ENTITY_HINTS.items():
        if entity in entities:
            return mod
    if not refs:
        return "common"
    return max(refs, key=refs.get)


# ── PK / FK detection ─────────────────────────────────────────────────────────

def probable_pk(entity: str, fields: list[dict]) -> str | None:
    """
    OFBiz PK naming: first char of entity lowercase + rest + "Id".
    e.g. OrderHeader → orderId, Product → productId
    Also handles composite PKs: we return the most likely single PK.
    """
    # Canonical: lowercase first letter of entity + "Id"
    canonical = entity[0].lower() + entity[1:] + "Id"
    for f in fields:
        if f["name"] == canonical:
            return canonical
    # Fallback: any field whose name IS inside the entity name and ends with Id
    e_lower = entity.lower()
    for f in fields:
        fname = f["name"].lower()
        if fname.endswith("id") and e_lower.startswith(fname[:-2]):
            return f["name"]
    return None

def fk_hint(field: str, known_entities: set[str]) -> str | None:
    """
    If field ends with 'Id', try to find an entity it references.
    orderId → OrderHeader (check 'Order*' in known entities)
    """
    if not field.lower().endswith("id"):
        return None
    base = field[:-2]               # strip trailing "Id"
    # Exact match: base capitalised == entity name
    candidate = base[0].upper() + base[1:]
    if candidate in known_entities:
        return candidate
    # Prefix match (e.g. productStoreId → ProductStore)
    for entity in known_entities:
        if entity.lower() == base.lower():
            return entity
    return None


# ── Collection ────────────────────────────────────────────────────────────────

# entity → field → {"count": int, "methods": set[str]}
entity_fields: dict[str, dict[str, dict]] = \
    defaultdict(lambda: defaultdict(lambda: {"count": 0, "methods": set()}))
entity_module_refs: dict[str, dict[str, int]] = defaultdict(lambda: defaultdict(int))
entity_access: dict[str, int] = defaultdict(int)

NOISE = {
    "responseMessage","errorMessage","successMessage","errorMessageList",
    "userLogin","locale","timeZone","serviceName","resource",
    "permissionErrorMessage","entityName","conditionList",
}

def record_field(entity: str, field: str, method: str, module: str):
    if not field or field in NOISE or len(field) < 3:
        return
    entity_fields[entity][field]["count"] += 1
    if method:
        entity_fields[entity][field]["methods"].add(method)


def extract_from_window(entity: str, lines: list[str], start: int,
                        window: int, module: str):
    chunk = "\n".join(lines[start : start + window])
    for m in RE_FIELD_ACCESS.finditer(chunk):
        record_field(entity, m.group(2), m.group(1), module)
    for m in RE_FIELD_COND.finditer(chunk):
        record_field(entity, m.group(1), "", module)
    entity_module_refs[entity][module] += 1
    entity_access[entity] += 1


def process_file(path: Path):
    try:
        text = path.read_text(encoding="utf-8", errors="ignore")
    except OSError:
        return
    module = module_of(path)
    lines = text.splitlines()

    for m in RE_MAKE_VALUE.finditer(text):
        ln = text[:m.start()].count("\n")
        extract_from_window(m.group(1), lines, ln, 80, module)

    for m in RE_FROM.finditer(text):
        ln = text[:m.start()].count("\n")
        extract_from_window(m.group(1), lines, ln, 20, module)

    for m in RE_FIND_DIRECT.finditer(text):
        ln = text[:m.start()].count("\n")
        extract_from_window(m.group(1), lines, ln, 15, module)

    for m in RE_GV_ASSIGN.finditer(text):
        var_name, entity = m.group(1), m.group(2)
        ln = text[:m.start()].count("\n")
        chunk = "\n".join(lines[ln : ln + 60])
        for gm in RE_GV_GET.finditer(chunk):
            if gm.group(1) == var_name:
                record_field(entity, gm.group(3), gm.group(2), module)


# ── Main ──────────────────────────────────────────────────────────────────────

FALSE_POSITIVES = {
    "String","Map","List","Set","Object","Integer","Long","Boolean",
    "BigDecimal","Timestamp","Date","Exception","Collection","Locale",
    "HashMap","ArrayList","LinkedList","LinkedHashMap",
    "EntityCondition","EntityExpr","EntityQuery","GenericValue",
    "DispatchContext","ModelService","ModelField","ModelEntity",
    "GenericDelegator","LocalDispatcher","ServiceUtil","UtilMisc",
    "UtilValidate","UtilDateTime","UtilProperties","UtilHttp",
    "FastMap","FastList",
}

def main():
    sources = list(JAVA_SRC.rglob("*.java"))
    if GROOVY_SRC.exists():
        sources += list(GROOVY_SRC.rglob("*.groovy"))
    print(f"Scanning {len(sources)} files…")
    for path in sources:
        process_file(path)

    known_entities = {e for e in entity_fields if e not in FALSE_POSITIVES}

    schema_entities = []
    for entity, fields_raw in sorted(entity_fields.items()):
        if entity in FALSE_POSITIVES:
            continue
        if entity_access[entity] < 2:
            continue
        if len(fields_raw) < 3:
            continue

        # Build field list with full metadata
        fields: list[dict] = []
        for fname, meta in fields_raw.items():
            if fname in NOISE or len(fname) < 3:
                continue
            tk = infer_type_key(fname, meta["methods"])
            fields.append({
                "name":      fname,
                "type_key":  tk,
                "java_type": java_type(tk),
                "sql_type":  sql_type(tk),
                "type_label":type_label(tk),
                "refs":      meta["count"],
                "is_pk":     False,     # filled below
                "fk_to":     fk_hint(fname, known_entities),
            })

        # Sort: PKs first, then by name
        fields.sort(key=lambda f: (0 if f["type_key"] in ("id","id_long") else 1, f["name"]))

        # Mark probable PK
        pk_name = probable_pk(entity, fields)
        for f in fields:
            if f["name"] == pk_name:
                f["is_pk"] = True
                f["fk_to"] = None   # PK is not a FK in its own table

        mod = dominant_module(entity, entity_module_refs.get(entity, {}))
        schema_entities.append({
            "entity":       entity,
            "module":       mod,
            "access_count": entity_access[entity],
            "fields":       fields,
            "field_count":  len(fields),
        })

    schema_entities.sort(key=lambda e: -e["access_count"])

    # Group by module
    by_module: dict[str, list] = defaultdict(list)
    for e in schema_entities:
        by_module[e["module"]].append(e)
    for lst in by_module.values():
        lst.sort(key=lambda e: -e["access_count"])

    schema_by_module = [
        {"module": mod, "entities": lst}
        for mod, lst in sorted(by_module.items())
    ]

    architektur_path = DATA_DIR / "architektur.json"
    data = json.loads(architektur_path.read_text(encoding="utf-8"))
    data["schema_entities"]  = schema_entities
    data["schema_by_module"] = schema_by_module
    architektur_path.write_text(
        json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8"
    )

    total_fields = sum(e["field_count"] for e in schema_entities)
    print(f"\nEntities: {len(schema_entities)}   Fields: {total_fields}")
    print("\nTop 15 by access count:")
    for e in schema_entities[:15]:
        print(f"  {e['entity']:40s} {e['access_count']:4d}×  {e['field_count']:3d} Felder  [{e['module']}]")


if __name__ == "__main__":
    main()
