#!/usr/bin/env python3
"""
Extracts inter-module dependencies from decompiled Java source files.
Adds 'business_dependencies' to analysis/html/data/architektur.json.
"""

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
DECOMPILED = ROOT / "decompiled" / "src"
JAVA_SRC   = DECOMPILED / "main" / "java" / "org" / "apache" / "ofbiz"
GROOVY_SRC = DECOMPILED / "groovy-origin" / "org" / "apache" / "ofbiz"
DATA_DIR = Path(__file__).resolve().parents[1] / "data"

BUSINESS_MODULES = [
    "party", "order", "product", "accounting", "content",
    "manufacturing", "shipment", "workeffort", "marketing", "humanres", "sfa",
]

IMPORT_RE = re.compile(r"^import org\.apache\.ofbiz\.([a-z]+)\.", re.MULTILINE)


def get_deps(module: str) -> set[str]:
    deps = set()
    for src_root in (JAVA_SRC, GROOVY_SRC):
        mod_dir = src_root / module
        if not mod_dir.exists():
            continue
        for java_file in mod_dir.rglob("*.java"):
            text = java_file.read_text(encoding="utf-8", errors="ignore")
            for m in IMPORT_RE.finditer(text):
                dep = m.group(1)
                if dep != module and dep in BUSINESS_MODULES:
                    deps.add(dep)
    return deps


def main():
    architektur_path = DATA_DIR / "architektur.json"
    data = json.loads(architektur_path.read_text(encoding="utf-8"))

    edges = []
    all_deps: dict[str, list[str]] = {}
    for mod in BUSINESS_MODULES:
        if not (JAVA_SRC / mod).exists():
            continue
        deps = sorted(get_deps(mod))
        all_deps[mod] = deps
        for dep in deps:
            edges.append({"from": mod, "to": dep})

    # Detect cyclic edges: A→B is cyclic if B→A also exists
    edge_set = {(e["from"], e["to"]) for e in edges}
    cyclic_indices = [i for i, e in enumerate(edges) if (e["to"], e["from"]) in edge_set]

    data["business_dependencies"] = edges
    data["business_modules_order"] = BUSINESS_MODULES
    data["cyclic_edge_indices"] = cyclic_indices

    architektur_path.write_text(
        json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8"
    )

    print(f"business_dependencies: {len(edges)} edges, {len(cyclic_indices)} cyclic")
    for mod, deps in all_deps.items():
        if deps:
            print(f"  {mod:15s} → {', '.join(deps)}")


if __name__ == "__main__":
    main()
