#!/usr/bin/env python3
"""
Extracts database / data-access patterns from decompiled Java + Groovy sources.

Metrics collected per module and globally:
  - entity_access_counts  : {entity_name: total_access_count}
  - module_db_stats       : per-module breakdown of:
        entity_query, delegator_crud, cache_hits, streaming, tx_begin, svc_error, svc_success
  - top_entities          : sorted list of most-queried entity names
  - db_framework_summary  : global totals
"""

import re
from collections import defaultdict
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[3]
JAVA_SRC = ROOT / "decompiled" / "src" / "main" / "java" / "org" / "apache" / "ofbiz"
GROOVY_SRC = ROOT / "decompiled" / "src" / "main" / "groovy-origin"
DATA_DIR = Path(__file__).resolve().parents[1] / "data"

# ── Regex patterns ──────────────────────────────────────────────────────────

RE_ENTITY_FROM = re.compile(r'\.from\(\s*"([A-Za-z][A-Za-z0-9_]+)"\s*\)')
RE_ENTITY_FIND = re.compile(
    r'delegator\.(?:findList|findByAnd|findOne|findByPrimaryKey|findByPrimaryKeyPartial'
    r'|find|countByAnd)\s*\(\s*"([A-Za-z][A-Za-z0-9_]+)"'
)
RE_ENTITY_QUERY   = re.compile(r'EntityQuery\.use\(')
RE_DELEGATOR_CRUD = re.compile(
    r'delegator\.(?:create|store|storeAll|remove|removeByAnd|removeAll|update|makeValue)\s*\('
)
RE_CACHE          = re.compile(r'\.cache\(\s*(?:true)?\s*\)')
RE_STREAMING      = re.compile(r'\.queryIterator\(\)')
RE_TX_BEGIN       = re.compile(r'TransactionUtil\.begin\(')
RE_TX_COMMIT      = re.compile(r'TransactionUtil\.commit\(')
RE_TX_ROLLBACK    = re.compile(r'TransactionUtil\.rollback\(')
RE_SVC_ERROR      = re.compile(r'ServiceUtil\.returnError\(')
RE_SVC_FAIL       = re.compile(r'ServiceUtil\.returnFailure\(')
RE_SVC_SUCCESS    = re.compile(r'ServiceUtil\.returnSuccess\(')


def module_of(path: Path) -> str:
    """Return the top-level OFBiz module name for a source file."""
    try:
        rel = path.relative_to(JAVA_SRC)
        return rel.parts[0] if rel.parts else "unknown"
    except ValueError:
        pass
    if GROOVY_SRC.exists():
        try:
            rel = path.relative_to(GROOVY_SRC)
            return rel.parts[0] if rel.parts else "unknown"
        except ValueError:
            pass
    return "unknown"


def scan_file(path: Path, entity_counts: dict, module_stats: dict):
    try:
        text = path.read_text(encoding="utf-8", errors="ignore")
    except OSError:
        return

    mod = module_of(path)
    stats = module_stats[mod]

    # Entity names accessed
    for m in RE_ENTITY_FROM.finditer(text):
        entity_counts[m.group(1)] += 1
    for m in RE_ENTITY_FIND.finditer(text):
        entity_counts[m.group(1)] += 1

    # Per-module counters
    stats["entity_query"]   += len(RE_ENTITY_QUERY.findall(text))
    stats["delegator_crud"] += len(RE_DELEGATOR_CRUD.findall(text))
    stats["cache"]          += len(RE_CACHE.findall(text))
    stats["streaming"]      += len(RE_STREAMING.findall(text))
    stats["tx_begin"]       += len(RE_TX_BEGIN.findall(text))
    stats["tx_commit"]      += len(RE_TX_COMMIT.findall(text))
    stats["tx_rollback"]    += len(RE_TX_ROLLBACK.findall(text))
    stats["svc_error"]      += len(RE_SVC_ERROR.findall(text))
    stats["svc_fail"]       += len(RE_SVC_FAIL.findall(text))
    stats["svc_success"]    += len(RE_SVC_SUCCESS.findall(text))
    stats["files"]          += 1


def default_stats():
    return {
        "entity_query": 0, "delegator_crud": 0, "cache": 0, "streaming": 0,
        "tx_begin": 0, "tx_commit": 0, "tx_rollback": 0,
        "svc_error": 0, "svc_fail": 0, "svc_success": 0, "files": 0,
    }


def main():
    entity_counts: dict[str, int] = defaultdict(int)
    module_stats: dict[str, dict] = defaultdict(default_stats)

    sources = list(JAVA_SRC.rglob("*.java"))
    if GROOVY_SRC.exists():
        sources += list(GROOVY_SRC.rglob("*.groovy"))

    print(f"Scanning {len(sources)} source files…")
    for path in sources:
        scan_file(path, entity_counts, module_stats)

    # ── Top entities (filter out framework noise) ──────────────────────────
    SKIP_ENTITIES = {
        "String", "Map", "List", "Object", "Class", "Integer", "Long",
        "Boolean", "Set", "Date", "Timestamp", "BigDecimal",
    }
    top_entities = [
        {"entity": e, "count": c}
        for e, c in sorted(entity_counts.items(), key=lambda x: -x[1])
        if e not in SKIP_ENTITIES and c >= 2
    ][:60]

    # ── Global summary ─────────────────────────────────────────────────────
    totals = default_stats()
    for s in module_stats.values():
        for k in totals:
            totals[k] += s[k]

    db_framework_summary = {
        "entity_query_calls":   totals["entity_query"],
        "delegator_crud_calls": totals["delegator_crud"],
        "cache_calls":          totals["cache"],
        "streaming_calls":      totals["streaming"],
        "tx_begin_calls":       totals["tx_begin"],
        "tx_commit_calls":      totals["tx_commit"],
        "tx_rollback_calls":    totals["tx_rollback"],
        "svc_error_returns":    totals["svc_error"],
        "svc_fail_returns":     totals["svc_fail"],
        "svc_success_returns":  totals["svc_success"],
        "distinct_entities":    len(top_entities),
    }

    # ── Per-module sorted by entity_query desc ─────────────────────────────
    module_db_stats = [
        {"module": mod, **stats}
        for mod, stats in sorted(
            module_stats.items(),
            key=lambda x: -(x[1]["entity_query"] + x[1]["delegator_crud"])
        )
        if stats["files"] > 0
    ]

    # ── Write to architektur.json ──────────────────────────────────────────
    architektur_path = DATA_DIR / "architektur.json"
    data = json.loads(architektur_path.read_text(encoding="utf-8"))
    data["db_top_entities"]       = top_entities
    data["db_module_stats"]       = module_db_stats
    data["db_framework_summary"]  = db_framework_summary
    architektur_path.write_text(
        json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8"
    )

    print(f"\ndb_framework_summary:")
    for k, v in db_framework_summary.items():
        print(f"  {k:30s} {v}")
    print(f"\nTop 10 entities:")
    for e in top_entities[:10]:
        print(f"  {e['entity']:40s} {e['count']}")


if __name__ == "__main__":
    main()
