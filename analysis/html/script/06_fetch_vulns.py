#!/usr/bin/env python3
"""
Queries the OSV API (https://api.osv.dev) for known vulnerabilities
for each library in sbom_libraries and adds 'vulns' field to each entry.
Updates analysis/html/data/architektur.json in-place.
"""

import json
import time
import urllib.request
import urllib.error
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parents[1] / "data"
OSV_BATCH_URL = "https://api.osv.dev/v1/querybatch"
BATCH_SIZE = 20  # OSV allows up to 1000, but keep batches manageable


def osv_query_batch(libraries: list[dict]) -> list[list[str]]:
    """Query OSV for a batch of libraries. Returns list of vuln-ID lists."""
    queries = []
    for lib in libraries:
        queries.append({
            "version": lib["version"],
            "package": {
                "name": f"{lib['group']}:{lib['artifact']}",
                "ecosystem": "Maven",
            }
        })

    payload = json.dumps({"queries": queries}).encode("utf-8")
    req = urllib.request.Request(
        OSV_BATCH_URL,
        data=payload,
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            data = json.loads(resp.read())
            return [
                [v.get("id", "") for v in r.get("vulns", [])]
                for r in data.get("results", [])
            ]
    except urllib.error.URLError as e:
        print(f"  OSV API error: {e}")
        return [[] for _ in libraries]


def osv_fetch_vuln(vuln_id: str) -> dict:
    """Fetch full vulnerability details from OSV."""
    url = f"https://api.osv.dev/v1/vulns/{vuln_id}"
    try:
        with urllib.request.urlopen(url, timeout=15) as resp:
            return json.loads(resp.read())
    except urllib.error.URLError:
        return {"id": vuln_id}


def summarize_vuln(vuln: dict) -> dict:
    """Extract relevant fields from an OSV vulnerability object."""
    vuln_id = vuln.get("id", "")
    aliases = vuln.get("aliases", [])
    cves = [a for a in aliases if a.startswith("CVE-")]
    summary = vuln.get("summary", "")
    details = vuln.get("details", "")
    db = vuln.get("database_specific", {})
    # OSV GitHub Advisory DB uses database_specific.severity (CRITICAL/HIGH/MODERATE/LOW)
    severity = db.get("severity", "").upper()
    cwe_ids = db.get("cwe_ids", [])
    return {
        "id": vuln_id,
        "cves": cves,
        "summary": summary,
        "details": details[:300] if details else "",
        "severity": severity,
        "cwe_ids": cwe_ids,
    }


def main():
    architektur_path = DATA_DIR / "architektur.json"
    data = json.loads(architektur_path.read_text(encoding="utf-8"))
    libraries = data.get("sbom_libraries", [])

    if not libraries:
        print("No sbom_libraries found — run 05_parse_sbom.py first.")
        return

    print(f"Querying OSV API for {len(libraries)} libraries...")
    all_ids: list[list[str]] = []

    for i in range(0, len(libraries), BATCH_SIZE):
        batch = libraries[i:i + BATCH_SIZE]
        print(f"  Batch {i // BATCH_SIZE + 1}: {len(batch)} libraries...", end=" ", flush=True)
        results = osv_query_batch(batch)
        all_ids.extend(results)
        total = sum(len(r) for r in results)
        print(f"{total} vuln IDs")
        if i + BATCH_SIZE < len(libraries):
            time.sleep(0.3)

    # Collect unique vuln IDs and fetch full details
    unique_ids = {vid for ids in all_ids for vid in ids}
    print(f"\nFetching details for {len(unique_ids)} unique vulnerabilities...")
    vuln_cache: dict[str, dict] = {}
    for j, vid in enumerate(sorted(unique_ids)):
        vuln_cache[vid] = osv_fetch_vuln(vid)
        if (j + 1) % 10 == 0:
            print(f"  {j + 1}/{len(unique_ids)} fetched")
        time.sleep(0.1)
    print(f"  {len(unique_ids)}/{len(unique_ids)} fetched")

    # Attach full vulnerability details to each library
    total_vulns = 0
    for lib, ids in zip(libraries, all_ids):
        lib["vulns"] = [summarize_vuln(vuln_cache[vid]) for vid in ids if vid in vuln_cache]
        total_vulns += len(ids)

    data["sbom_libraries"] = libraries
    architektur_path.write_text(
        json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8"
    )

    affected = sum(1 for lib in libraries if lib.get("vulns"))
    print(f"\nDone. {total_vulns} vulnerabilities across {affected}/{len(libraries)} libraries.")
    for lib in libraries:
        if lib.get("vulns"):
            ids = ", ".join(v["id"] for v in lib["vulns"][:3])
            more = f" (+{len(lib['vulns'])-3} more)" if len(lib["vulns"]) > 3 else ""
            print(f"  {lib['group']}:{lib['artifact']}:{lib['version']}")
            print(f"    → {ids}{more}")


if __name__ == "__main__":
    main()
