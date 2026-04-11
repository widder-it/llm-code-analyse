#!/usr/bin/env python3
"""
Generates HTML documentation from JSON data using Jinja2 templates.
Input:  analysis/html/data/{module}.json + data/index.json
Output: analysis/html/output/index.html
        analysis/html/output/{module}/index.html
        analysis/html/output/{module}/{class-id}.html
"""

import json
import sys
from pathlib import Path
from jinja2 import Environment, FileSystemLoader, select_autoescape

SCRIPT_DIR = Path(__file__).resolve().parent
HTML_DIR = SCRIPT_DIR.parent
DATA_DIR = HTML_DIR / "data"
TEMPLATES_DIR = HTML_DIR / "templates"
OUTPUT_DIR = HTML_DIR / "output"


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def write_html(env, template_name: str, out_path: Path, **ctx):
    out_path.parent.mkdir(parents=True, exist_ok=True)
    tmpl = env.get_template(template_name)
    out_path.write_text(tmpl.render(**ctx), encoding="utf-8")


def relative_root(depth: int) -> str:
    return "../" * depth if depth > 0 else "./"


def main():
    env = Environment(
        loader=FileSystemLoader(str(TEMPLATES_DIR)),
        autoescape=select_autoescape(["html"]),
    )
    env.filters["slugify"] = lambda s: s.replace(" ", "-").replace("/", "-")

    index_data = load_json(DATA_DIR / "index.json")
    modules_meta = index_data["modules"]

    architektur = {}
    architektur_path = DATA_DIR / "architektur.json"
    if architektur_path.exists():
        architektur = load_json(architektur_path)

    targets = sys.argv[1:] if sys.argv[1:] else [m["id"] for m in modules_meta]

    # --- index.html ---
    write_html(env, "index.html.j2", OUTPUT_DIR / "index.html",
               modules=modules_meta, architektur=architektur,
               root=relative_root(0), active_module=None)
    print("  index.html")

    # --- sbom.html ---
    libraries = architektur.get("sbom_libraries", [])
    if libraries:
        write_html(env, "sbom.html.j2", OUTPUT_DIR / "sbom.html",
                   modules=modules_meta, libraries=libraries,
                   root=relative_root(0), active_module=None)
        print(f"  sbom.html  ({len(libraries)} libraries)")

    # --- tech-debt.html ---
    tech_debt = architektur.get("tech_debt", [])
    if tech_debt:
        write_html(env, "tech-debt.html.j2", OUTPUT_DIR / "tech-debt.html",
                   modules=modules_meta, debts=tech_debt,
                   root=relative_root(0), active_module="__tech_debt__")
        print(f"  tech-debt.html  ({len(tech_debt)} items)")

    # --- schema.html ---
    schema_entities = architektur.get("schema_entities", [])
    schema_by_module = architektur.get("schema_by_module", [])
    if schema_entities:
        write_html(env, "schema.html.j2", OUTPUT_DIR / "schema.html",
                   modules=modules_meta,
                   schema_entities=schema_entities,
                   schema_by_module=schema_by_module,
                   root=relative_root(0), active_module="__schema__")
        total_fields = sum(e["field_count"] for e in schema_entities)
        print(f"  schema.html  ({len(schema_entities)} entities, {total_fields} fields)")

    # --- database.html ---
    db_summary = architektur.get("db_framework_summary", {})
    module_stats = architektur.get("db_module_stats", [])
    top_entities = architektur.get("db_top_entities", [])
    if db_summary:
        write_html(env, "database.html.j2", OUTPUT_DIR / "database.html",
                   modules=modules_meta,
                   db_summary=db_summary,
                   module_stats=module_stats,
                   top_entities=top_entities,
                   root=relative_root(0), active_module="__database__")
        print(f"  database.html  ({db_summary.get('distinct_entities', 0)} entities)")

    for module_id in targets:
        json_path = DATA_DIR / f"{module_id}.json"
        if not json_path.exists():
            print(f"  SKIP {module_id}.json not found")
            continue

        data = load_json(json_path)
        module_dir = OUTPUT_DIR / module_id

        # --- {module}/index.html ---
        write_html(env, "module.html.j2", module_dir / "index.html",
                   module=data, modules=modules_meta,
                   root=relative_root(1), active_module=module_id)
        print(f"  {module_id}/index.html  ({len(data['classes'])} classes)")

        # --- {module}/{class}.html ---
        for cls in data["classes"]:
            write_html(env, "class.html.j2", module_dir / f"{cls['id']}.html",
                       cls=cls, module=data, modules=modules_meta,
                       root=relative_root(1), active_module=module_id)

        print(f"  {module_id}/  {len(data['classes'])} class pages written")

    print("\nDone.")


if __name__ == "__main__":
    main()
