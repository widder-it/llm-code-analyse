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

    targets = sys.argv[1:] if sys.argv[1:] else [m["id"] for m in modules_meta]

    # --- index.html ---
    write_html(env, "index.html.j2", OUTPUT_DIR / "index.html",
               modules=modules_meta, root=relative_root(0), active_module=None)
    print("  index.html")

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
