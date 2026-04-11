#!/usr/bin/env python3
"""
Parses module documentation markdown files and extracts structured JSON data.

Handles three slightly different formats produced by different documentation agents:
  - party.md:   ### Klasse: `Name` / ### Groovy-Scripts: Group (bullet list submodules)
  - order.md:   ### Klasse: `Name` / ### Klassen: Group (table submodules)
  - product.md: ## Klasse: `Name` + ### `Name` inside Groovy section (table submodules)

Input:  analysis/module-docs/{module}.md
Output: analysis/html/data/{module}.json
        analysis/html/data/index.json
"""

import re
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DOCS_DIR = ROOT / "module-docs"
DATA_DIR = Path(__file__).resolve().parents[1] / "data"
DATA_DIR.mkdir(exist_ok=True)


def clean(s: str) -> str:
    """Strip markdown backticks and extra whitespace."""
    return re.sub(r"`([^`]*)`", r"\1", s).strip()


def slugify(s: str) -> str:
    s = re.sub(r"[^a-zA-Z0-9_-]", "-", s)
    return re.sub(r"-{2,}", "-", s).strip("-")[:80]


def parse_submodules_table(text: str) -> list:
    """Parse a markdown table of submodules: | Paket | Beschreibung |"""
    rows = []
    in_body = False
    for line in text.split("\n"):
        if re.match(r"\|\s*[-:]+", line):
            in_body = True
            continue
        if in_body and line.startswith("|"):
            cells = [c.strip() for c in line.split("|")[1:-1]]
            if len(cells) >= 2:
                name = clean(cells[0])
                desc = clean(cells[1])
                if name and name not in ("Paket", "Submodul", "Name"):
                    rows.append({"name": name, "description": desc})
    return rows


def parse_submodules_bullets(text: str) -> list:
    """Parse a bullet list of submodules: - **`name`** — desc"""
    rows = []
    for line in text.split("\n"):
        m = re.match(r"[-*]\s+\*\*`([^`]+)`\*\*\s*[—–-]+\s*(.*)", line)
        if m:
            rows.append({"name": m.group(1), "description": m.group(2).strip()})
    return rows


def extract_section_text(content: str, heading: str, heading_levels: str = "##?#?") -> str:
    """Return text of a named section until the next heading of same/higher level."""
    pattern = rf"^({heading_levels})\s+{re.escape(heading)}\s*\n([\s\S]*?)(?=\n\1[^#]|\Z)"
    m = re.search(pattern, content, re.MULTILINE)
    return m.group(2) if m else ""


def parse_method_table(section: str) -> list:
    """Extract rows from a | Methode | Beschreibung | table."""
    methods = []
    m = re.search(
        r"\| Methode[^|]*\| Beschreibung[^|]*\|\s*\n\|[-| ]+\|\s*\n([\s\S]+?)(?=\n\n\S|\n#{1,3} |\Z)",
        section,
    )
    if not m:
        # Also try: | Methode / Klasse | Beschreibung |
        m = re.search(
            r"\| Methode[^|]*\|[^|]*\|\s*\n\|[-| ]+\|\s*\n([\s\S]+?)(?=\n\n\S|\n#{1,3} |\Z)",
            section,
        )
    if m:
        for line in m.group(1).split("\n"):
            if not line.startswith("|"):
                break
            cells = [c.strip() for c in line.split("|")[1:-1]]
            if len(cells) >= 2:
                sig = clean(cells[0])
                desc = clean(cells[1])
                if sig and sig not in ("Methode", "Methode / Klasse", "*"):
                    methods.append({"signature": sig, "description": desc})
    return methods


def parse_member_table(section: str) -> list:
    """Extract rows from a | Klasse | Fachliche Funktion | table."""
    members = []
    for col1 in ("Klasse", "Script", "Name", "Gruppe"):
        m = re.search(
            rf"\| {col1}[^|]*\|[^|]*\|\s*\n\|[-| ]+\|\s*\n([\s\S]+?)(?=\n\n\S|\n#{1,3} |\Z)",
            section,
        )
        if m:
            for line in m.group(1).split("\n"):
                if not line.startswith("|"):
                    break
                cells = [c.strip() for c in line.split("|")[1:-1]]
                if len(cells) >= 2:
                    name = clean(cells[0])
                    desc = clean(cells[1])
                    if name and name != col1 and not name.startswith("*"):
                        members.append({"name": name, "description": desc})
            break
    return members


def extract_class_meta(name: str, section: str) -> dict:
    """Extract package, type, description from a class section."""
    pkg = ""
    m = re.search(r"\*\*Paket:\*\*\s*`([^`]+)`", section)
    if m:
        pkg = m.group(1)

    typ = ""
    m = re.search(r"\*\*Typ:\*\*\s*([^\n]+)", section)
    if m:
        typ = clean(m.group(1))

    # Infer type from name if not explicitly stated
    if not typ:
        if name.endswith("Script") or "ServicesScript" in name:
            typ = "Groovy-Script"
        elif re.search(r"\bextends groovy\.lang\.Script\b", section):
            typ = "Groovy-Script"
        elif name.endswith("Events"):
            typ = "Java-Klasse (Event-Handler)"
        elif name.endswith("Services") or name.endswith("Service"):
            typ = "Java-Klasse (Service)"
        elif name.endswith("Worker") or name.endswith("Helper"):
            typ = "Java-Klasse (Utility)"
        else:
            typ = "Java-Klasse"

    desc = ""
    for label in ("Zweck", "Funktion", "Beschreibung"):
        m = re.search(rf"\*\*{label}:\*\*\s*([\s\S]+?)(?=\n\||\n\n\*\*|\Z)", section)
        if m:
            desc = " ".join(m.group(1).strip().split())
            break

    # Determine section: Test > Groovy > Java
    if "test" in pkg.lower() or re.search(r"[Tt]est(s|Case)?$", name):
        section = "test"
    elif "Groovy" in typ or name.endswith("Script"):
        section = "groovy"
    else:
        section = "java"

    return {
        "id": slugify(name),
        "name": name,
        "package": pkg,
        "type": typ,
        "description": desc,
        "section": section,
    }


def parse_module_md(path: Path) -> dict:
    content = path.read_text(encoding="utf-8")

    # --- Module name ---
    module_name = path.stem
    m = re.search(r"^#{1,3}\s+Modul:\s*(\w+)", content, re.MULTILINE)
    if m:
        module_name = m.group(1)

    # --- Overview ---
    overview = ""
    m = re.search(r"^#{1,3}\s+Überblick\s*\n\n([\s\S]+?)(?=\n#{1,3} |\n---|\Z)", content, re.MULTILINE)
    if m:
        overview = m.group(1).strip()

    # --- Submodules (table or bullet list) ---
    submodules = []
    m = re.search(r"^#{1,3}\s+Submodule\s*\n\n([\s\S]+?)(?=\n#{1,3} |\n---|\Z)", content, re.MULTILINE)
    if m:
        block = m.group(1)
        if "|" in block:
            submodules = parse_submodules_table(block)
        else:
            submodules = parse_submodules_bullets(block)

    # --- Classes ---
    classes = []

    # Strategy: split content into blocks separated by --- or same-level headings,
    # then identify class blocks by presence of **Paket:** or **Typ:**

    # Collect all heading positions with their level, text, and content
    # We look for sections that contain class/group metadata

    # Split by horizontal rules (---) first
    raw_sections = re.split(r"\n---\n", content)

    for section in raw_sections:
        section = section.strip()
        if not section:
            continue

        # Find all sub-sections within this block (### level headings)
        # This handles the case where product.md has ### `Name` inside a ## section
        sub_sections = re.split(r"\n(?=#{2,3} )", section)

        for sub in sub_sections:
            sub = sub.strip()
            if not sub:
                continue

            has_paket = bool(re.search(r"\*\*Paket:\*\*", sub))
            has_method_table = bool(re.search(r"\| Methode", sub))
            has_member_table = bool(re.search(r"\| Klasse\b", sub))

            # Get heading
            h = re.match(r"^(#{1,3})\s+(.*)", sub)
            if not h:
                continue
            heading_text = h.group(2).strip()

            # Extract class name from heading variants:
            # "Klasse: `Name`" / "Klassen: `Name`" / "`Name`" / "Klasse: Name"
            cls_name = None
            hm = re.match(r"Klassen?:\s*`([^`]+)`", heading_text)
            if hm:
                cls_name = hm.group(1)
            elif re.match(r"`([^`]+)`$", heading_text):
                cls_name = re.match(r"`([^`]+)`$", heading_text).group(1)
            elif re.match(r"Groovy-Scripts?[:\s]", heading_text):
                cls_name = None  # handled as group below
            elif has_paket or has_method_table:
                # Fallback: use heading as name
                cls_name = clean(heading_text)

            # Group heading (Groovy-Scripts: ... or Klassen: ... with member table)
            is_group_heading = bool(
                re.match(r"Groovy-Scripts?", heading_text)
                or re.match(r"Testklassen", heading_text)
                or (re.match(r"Klassen?:", heading_text) and has_member_table and not has_method_table)
            )

            if is_group_heading or (has_member_table and not has_method_table and not has_paket):
                members = parse_member_table(sub)
                if not members:
                    continue
                pkg = ""
                pm = re.search(r"\*\*Paket:\*\*\s*`([^`]+)`", sub)
                if pm:
                    pkg = pm.group(1)
                typ = "Groovy-Scripts"
                tm = re.search(r"\*\*Typ:\*\*\s*([^\n]+)", sub)
                if tm:
                    typ = clean(tm.group(1))
                desc = ""
                dm = re.search(r"\*\*Typ:\*\*[^\n]+\n\n([\s\S]+?)(?=\n\||\Z)", sub)
                if dm:
                    desc = " ".join(dm.group(1).strip().split("\n")).strip()
                grp_section = "test" if re.match(r"Testklassen", heading_text) else "groovy"
                classes.append({
                    "id": slugify(heading_text),
                    "name": heading_text,
                    "package": pkg,
                    "type": typ,
                    "description": desc,
                    "is_group": True,
                    "members": members,
                    "section": grp_section,
                })
                continue

            if cls_name and (has_paket or has_method_table or has_member_table):
                meta = extract_class_meta(cls_name, sub)
                methods = parse_method_table(sub)
                # Maybe it's actually a group (has member table but identified as class)
                if has_member_table and not has_method_table:
                    members = parse_member_table(sub)
                    meta["is_group"] = True
                    meta["members"] = members
                else:
                    meta["is_group"] = False
                    meta["methods"] = methods
                classes.append(meta)

    return {
        "module": module_name,
        "overview": overview,
        "submodules": submodules,
        "classes": classes,
        "stats": {
            "classes": len(classes),
            "methods": sum(len(c.get("methods", [])) for c in classes if not c.get("is_group")),
        },
    }


def main():
    targets = sys.argv[1:] if sys.argv[1:] else [p.stem for p in DOCS_DIR.glob("*.md")]

    modules_index = []
    for module_name in targets:
        md_path = DOCS_DIR / f"{module_name}.md"
        if not md_path.exists():
            print(f"  SKIP {module_name}.md not found")
            continue

        print(f"  Parsing {md_path.name} ...", end=" ")
        data = parse_module_md(md_path)
        out = DATA_DIR / f"{module_name}.json"
        out.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
        print(f"→ {len(data['classes'])} classes, {data['stats']['methods']} methods")

        modules_index.append({
            "id": module_name,
            "name": data["module"] or module_name,
            "overview": data["overview"][:200] + ("…" if len(data["overview"]) > 200 else ""),
            "stats": data["stats"],
        })

    index_path = DATA_DIR / "index.json"
    index_path.write_text(json.dumps({"modules": modules_index}, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"\nindex.json written with {len(modules_index)} module(s).")


if __name__ == "__main__":
    main()
