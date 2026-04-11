#!/usr/bin/env python3
"""
Consolidates technical debt items from various sources into a unified
'tech_debt' list in analysis/html/data/architektur.json.

Sources:
  - architektur.json: risks, god_objects, missing_patterns, dependency_cycles, jee_packages
  - sbom_libraries: libraries with known CVEs
  - decompiled source: failed decompilations (CFR errors)
"""

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
JAVA_SRC = ROOT / "decompiled" / "src" / "main" / "java" / "org" / "apache" / "ofbiz"
DATA_DIR = Path(__file__).resolve().parents[1] / "data"

SEVERITY_ORDER = {"Kritisch": 0, "Hoch": 1, "Mittel": 2, "Niedrig": 3}


def sev_from_emoji(text: str) -> str:
    if "🔴" in text or "Hoch" in text:
        return "Hoch"
    if "🟡" in text or "Mittel" in text:
        return "Mittel"
    if "🟢" in text or "Niedrig" in text:
        return "Niedrig"
    return "Mittel"


def count_decompile_failures() -> int:
    count = 0
    for f in JAVA_SRC.rglob("*.java"):
        try:
            if "Exception decompiling" in f.read_text(encoding="utf-8", errors="ignore"):
                count += 1
        except OSError:
            pass
    return count


def main():
    architektur_path = DATA_DIR / "architektur.json"
    data = json.loads(architektur_path.read_text(encoding="utf-8"))

    debts = []

    # 1. Cyclic module dependencies
    for c in data.get("dependency_cycles", []):
        debts.append({
            "kategorie": "Architektur",
            "titel": f"Zyklische Abhängigkeit: {c['cycle']}",
            "schwere": "Hoch",
            "beschreibung": "Gegenseitige Import-Abhängigkeit erschwert modulare Ablösung und erhöht Kompilier-Kopplung.",
        })

    # 2. God Objects
    for g in data.get("god_objects", []):
        try:
            methods = int(g.get("Public Methoden", 0))
        except (ValueError, TypeError):
            methods = 0
        sev = "Kritisch" if methods > 200 else "Hoch"
        debts.append({
            "kategorie": "Komplexität",
            "titel": f"God Object: {g['Klasse']} ({methods} Methoden)",
            "schwere": sev,
            "beschreibung": g.get("Bewertung", ""),
        })

    # 3. Identified risks (excluding god-object and cycle risks already covered)
    skip_keywords = ("God-Object", "God Object", "Zyklisch", "yklisch")
    for r in data.get("risks", []):
        titel = r.get("Risiko", "")
        if any(k in titel for k in skip_keywords):
            continue
        debts.append({
            "kategorie": "Risiko",
            "titel": titel,
            "schwere": sev_from_emoji(r.get("Schwere", "")),
            "beschreibung": r.get("Indikator", ""),
        })

    # 4. Missing modern patterns
    for p in data.get("missing_patterns", []):
        debts.append({
            "kategorie": "Architektur",
            "titel": f"Fehlendes Muster: {p.get('Muster', '')}",
            "schwere": "Mittel",
            "beschreibung": p.get("Implikation", ""),
        })

    # 5. Java EE legacy APIs
    pkgs = data.get("jee_packages", [])
    if pkgs:
        debts.append({
            "kategorie": "Technologie",
            "titel": "Legacy Java-EE-APIs (javax.*)",
            "schwere": "Mittel",
            "beschreibung": f"Migration zu Jakarta EE (jakarta.*) erforderlich: {', '.join(pkgs[:4])}{'…' if len(pkgs) > 4 else ''}.",
        })

    # 6. Libraries with known CVEs
    vuln_libs = [l for l in data.get("sbom_libraries", []) if l.get("vulns")]
    if vuln_libs:
        critical_high = [
            l for l in vuln_libs
            if any(v.get("severity") in ("CRITICAL", "HIGH") for v in l["vulns"])
        ]
        total_cves = sum(len(l["vulns"]) for l in vuln_libs)
        sev = "Hoch" if critical_high else "Mittel"
        examples = ", ".join(f"{l['artifact']}" for l in critical_high[:3])
        debts.append({
            "kategorie": "Security",
            "titel": f"Bekannte CVEs in {len(vuln_libs)} Libraries ({total_cves} gesamt)",
            "schwere": sev,
            "beschreibung": f"{len(critical_high)} Libraries mit CRITICAL/HIGH-Schwachstellen"
                            + (f": {examples}" if examples else "") + ". Siehe SBOM-Seite für Details.",
        })

    # 7. Decompilation failures (irrecoverable source)
    print("Scanning for decompilation failures...", end=" ", flush=True)
    failures = count_decompile_failures()
    print(f"{failures} found")
    if failures:
        debts.append({
            "kategorie": "Technologie",
            "titel": f"Nicht rekonstruierbarer Quellcode ({failures} Klassen)",
            "schwere": "Mittel",
            "beschreibung": f"CFR-Dekompilierung ist bei {failures} Java-Klassen fehlgeschlagen. "
                            "Logik dieser Klassen ist nicht analysierbar.",
        })

    # 8. Groovy source not recoverable
    debts.append({
        "kategorie": "Technologie",
        "titel": "Groovy-Quellcode nicht rekonstruierbar (~30 % der Klassen)",
        "schwere": "Mittel",
        "beschreibung": "Groovy-kompilierte Klassen liegen nur als Bytecode vor. "
                        "Fachliche Logik dieser Scripts ist nur eingeschränkt analysierbar.",
    })

    # Sort: Kritisch → Hoch → Mittel → Niedrig, then by Kategorie
    debts.sort(key=lambda d: (SEVERITY_ORDER.get(d["schwere"], 9), d["kategorie"]))

    data["tech_debt"] = debts
    architektur_path.write_text(
        json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8"
    )

    by_sev: dict[str, int] = {}
    for d in debts:
        by_sev[d["schwere"]] = by_sev.get(d["schwere"], 0) + 1
    print(f"tech_debt: {len(debts)} items")
    for sev in ("Kritisch", "Hoch", "Mittel", "Niedrig"):
        if sev in by_sev:
            print(f"  {sev}: {by_sev[sev]}")


if __name__ == "__main__":
    main()
