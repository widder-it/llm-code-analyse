#!/usr/bin/env python3
"""
Parses ARCHITEKTUR-ANALYSE.md into structured JSON for the index page.
Output: analysis/html/data/architektur.json
"""

import re
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
MD_PATH = ROOT / "ARCHITEKTUR-ANALYSE.md"
DATA_DIR = Path(__file__).resolve().parents[1] / "data"
DATA_DIR.mkdir(exist_ok=True)


def clean(s: str) -> str:
    s = re.sub(r"`([^`]*)`", r"\1", s)
    s = re.sub(r"\*\*([^*]*)\*\*", r"\1", s)
    s = re.sub(r"\*([^*]*)\*", r"\1", s)
    return s.strip()


def parse_table(block: str) -> list[dict]:
    """Parse a markdown table into list of dicts keyed by header."""
    lines = [l for l in block.strip().split("\n") if l.strip().startswith("|")]
    if len(lines) < 3:
        return []
    headers = [clean(h) for h in lines[0].split("|")[1:-1]]
    rows = []
    for line in lines[2:]:
        cells = [clean(c) for c in line.split("|")[1:-1]]
        if len(cells) >= len(headers):
            row = {headers[i]: cells[i] for i in range(len(headers))}
            if any(v for v in row.values()):
                rows.append(row)
    return rows


def extract_section(content: str, heading: str) -> str:
    """Return raw text of a section until next same-level heading."""
    m = re.search(
        rf"^(#{1,3}) {re.escape(heading)}\s*\n([\s\S]*?)(?=^\1 |\Z)",
        content, re.MULTILINE
    )
    return m.group(2).strip() if m else ""


def extract_between(content: str, start_heading: str, stop_heading: str) -> str:
    m = re.search(
        rf"^#{'{1,3}'} {re.escape(start_heading)}\s*\n([\s\S]*?)(?=^#{'{1,3}'} {re.escape(stop_heading)}|\Z)",
        content, re.MULTILINE
    )
    return m.group(1).strip() if m else ""


def find_section(content: str, pattern: str) -> str:
    """Find section by regex pattern in heading, stop at next same-or-higher heading."""
    m = re.search(
        rf"^(#{'{1,3}'})\s[^\n]*{pattern}[^\n]*\n([\s\S]*?)(?=^\1[^#]|\Z)",
        content, re.MULTILINE
    )
    if m:
        # Only return up to the next heading of any level
        body = m.group(2)
        stop = re.search(r"^#{1,3} ", body, re.MULTILINE)
        return body[:stop.start()].strip() if stop else body.strip()
    return ""


def parse_severity(text: str) -> str:
    if "🔴" in text or "Hoch" in text:
        return "high"
    if "🟡" in text or "Mittel" in text:
        return "medium"
    if "🟢" in text or "Niedrig" in text:
        return "low"
    return "info"


def main():
    content = MD_PATH.read_text(encoding="utf-8")
    result = {}

    # --- Meta / header ---
    meta = {}
    m = re.search(r"\*\*Analysemethode:\*\*\s*([^\n]+)", content)
    if m:
        meta["methode"] = clean(m.group(1))
    m = re.search(r"\*\*Analysewerkzeuge:\*\*\s*([^\n]+)", content)
    if m:
        meta["werkzeuge"] = clean(m.group(1))
    m = re.search(r"\*\*Analysedatum:\*\*\s*([^\n]+)", content)
    if m:
        meta["datum"] = clean(m.group(1))
    m = re.search(r"\*\*Analyseobjekt:\*\*\s*([^\n]+)", content)
    if m:
        meta["objekt"] = clean(m.group(1))
    result["meta"] = meta

    # --- Section 1: Tech foundation table ---
    sec1 = find_section(content, r"Technologisches Fundament")
    rows = parse_table(sec1)
    result["tech_foundation"] = rows

    # --- Section 2: Language split ---
    sec2 = find_section(content, r"Sprachverteilung")
    result["language_split"] = sec2

    # --- Section 3: Dependency cycles + key structure ---
    sec3_obs = find_section(content, r"Architektonische Beobachtungen")
    dep_cycles = []
    for line in sec3_obs.split("\n"):
        m = re.match(r"- `([^`]+)` — (.+)", line)
        if m:
            dep_cycles.append({"cycle": m.group(1), "note": m.group(2).strip()})
    result["dependency_cycles"] = dep_cycles

    sec3_struct = find_section(content, r"Kern-Abhängigkeitsstruktur")
    m = re.search(r"```([\s\S]+?)```", sec3_struct)
    result["dependency_structure"] = m.group(1).strip() if m else ""

    # --- Section 4: SBOM table ---
    sec4 = find_section(content, r"Externe Abhängigkeiten")
    sbom_rows = parse_table(sec4)
    result["sbom"] = sbom_rows

    # Section 4.1: Java EE risk
    sec4_1 = find_section(content, r"Java-EE-Abhängigkeiten")
    jee_packages = re.findall(r"`(javax\.[^`]+)`", sec4_1)
    result["jee_packages"] = jee_packages

    # --- Section 5: Integration points ---
    # 5.1 HTTP entry points top table
    sec5_1 = find_section(content, r"HTTP-Eintrittspunkte")
    result["http_entrypoints"] = parse_table(sec5_1)

    # 5.2 Largest service classes
    sec5_2 = find_section(content, r"Service-Schicht")
    result["top_services"] = parse_table(sec5_2)

    # 5.3 External integrations: payment + shipping
    sec5_3 = find_section(content, r"Externe Integrationspunkte")
    m_pay = re.search(r"\*\*Payment-Gateways[^*]*\*\*[^\n]*\n\n([\s\S]+?)(?=\n\*\*Versand|\Z)", sec5_3)
    result["payment_gateways"] = parse_table(m_pay.group(1)) if m_pay else []
    m_ship = re.search(r"\*\*Versanddienstleister[^*]*\*\*[^\n]*\n\n([\s\S]+?)(?=\n---|\n\*\*|\Z)", sec5_3)
    result["shipping_carriers"] = parse_table(m_ship.group(1)) if m_ship else []

    # 5.4 Key interfaces
    sec5_4 = find_section(content, r"API-Verträge")
    result["key_interfaces"] = parse_table(sec5_4)

    # --- Section 6: Technical debt ---
    # 6.1 God objects
    sec6_1 = find_section(content, r"Komplexitäts-Hotspots")
    result["god_objects"] = parse_table(sec6_1)

    # 6.2 Risks
    sec6_2 = find_section(content, r"Identifizierte Risiken")
    risk_rows = parse_table(sec6_2)
    for row in risk_rows:
        sev_text = row.get("Schwere", "")
        row["severity"] = parse_severity(sev_text)
    result["risks"] = risk_rows

    # --- Section 7: Architecture patterns ---
    sec7 = find_section(content, r"Architekturmuster")
    result["patterns"] = parse_table(sec7)

    sec7_1 = find_section(content, r"Fehlende moderne Muster")
    result["missing_patterns"] = parse_table(sec7_1)

    sec7_2 = find_section(content, r"Integrationskanäle")
    result["integration_channels"] = parse_table(sec7_2)

    sec7_3 = find_section(content, r"MiniLang")
    bullets = re.findall(r"- \*\*([^*]+)\*\*[:\s]+([^\n]+)", sec7_3)
    result["minilang_risks"] = [{"key": k.strip().rstrip(":"), "value": v.strip()} for k, v in bullets]

    # --- Section 8: Replacement assessment ---
    sec8 = find_section(content, r"Bewertung für Ablösung")
    result["replacement_assessment"] = parse_table(sec8)

    sec8_1 = find_section(content, r"Empfohlene Ablöse-Reihenfolge")
    m = re.search(r"```([\s\S]+?)```", sec8_1)
    result["replacement_phases"] = m.group(1).strip() if m else ""

    # Write output
    out_path = DATA_DIR / "architektur.json"
    out_path.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")

    total_keys = sum(
        len(v) if isinstance(v, list) else 1
        for v in result.values()
    )
    print(f"architektur.json written — {len(result)} sections, {total_keys} total entries")


if __name__ == "__main__":
    main()
