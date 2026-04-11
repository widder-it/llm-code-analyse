#!/usr/bin/env python3
"""
Parses build.gradle dependency declarations into structured SBOM data.
Adds 'sbom_libraries' to analysis/html/data/architektur.json.
"""

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
GRADLE_PATH = ROOT / "decompiled" / "build.gradle"
DATA_DIR = Path(__file__).resolve().parents[1] / "data"

# Map group prefix → category label
CATEGORIES = [
    (("org.apache.groovy", "org.codehaus.groovy", "org.clojure"), "Scripting"),
    (("org.apache.tomcat",), "Web-Container"),
    (("org.apache.logging",), "Logging"),
    (("org.apache.commons", "commons-codec", "commons-io", "commons-net",
      "commons-fileupload", "commons-validator", "commons-cli"), "Apache Commons"),
    (("com.fasterxml.jackson",), "JSON"),
    (("org.freemarker",), "Template-Engine"),
    (("com.github.ben-manes.caffeine",), "Caching"),
    (("com.google.guava", "com.google.re2j", "com.google.zxing",
      "com.googlecode.libphonenumber", "com.googlecode.concurrentlinkedhashmap"), "Google Libraries"),
    (("com.auth0",), "Authentifizierung"),
    (("org.apache.shiro", "org.owasp",
      "com.googlecode.owasp-java-html-sanitizer"), "Security"),
    (("org.apache.poi",), "Excel / Office"),
    (("org.apache.pdfbox", "com.lowagie", "org.mustangproject"), "PDF"),
    (("org.apache.xmlgraphics",), "XSL-FO / SVG"),
    (("org.apache.httpcomponents",), "HTTP-Client"),
    (("org.jsoup",), "HTML-Parsing"),
    (("com.rometools",), "RSS / Atom"),
    (("org.mnode.ical4j",), "Kalender (iCal)"),
    (("org.apache.tika",), "Dokumenten-Analyse"),
    (("org.jdom",), "XML (JDOM)"),
    (("com.googlecode.ez-vcard",), "vCard"),
    (("com.drewnoakes",), "Bild-Metadaten"),
    (("org.apache.geronimo",), "Transaktionen"),
    (("de.odysseus",), "Expression Language"),
    (("com.sun.mail", "javax.mail"), "E-Mail"),
    (("oro",), "Regex (ORO)"),
    (("org.apache.axis2", "org.apache.ws.commons",
      "org.apache.cxf", "javax.ws.rs", "wsdl4j"), "Web Services / SOAP"),
    (("javax.", "com.ibm.wsdl"), "Java EE (legacy javax.*)"),
    (("com.thoughtworks.xstream",), "XML-Serialisierung"),
    (("com.ibm.icu",), "Unicode / ICU4J"),
    (("org.apache.sshd",), "SFTP / SSH"),
    (("xerces",), "XML-Parser"),
    (("net.lingala.zip4j",), "ZIP"),
    (("org.apache.ant", "org.springframework", "junit"), "Test"),
]


def categorize(group: str) -> str:
    for prefixes, label in CATEGORIES:
        if any(group.startswith(p) for p in prefixes):
            return label
    return "Sonstige"


DEP_RE = re.compile(
    r"(?:implementation|testImplementation)\s+'([^:]+):([^:]+):([^']+)'"
)


def main():
    text = GRADLE_PATH.read_text(encoding="utf-8")
    libraries = []
    for m in DEP_RE.finditer(text):
        group, artifact, version = m.group(1), m.group(2), m.group(3)
        libraries.append({
            "group": group,
            "artifact": artifact,
            "version": version,
            "category": categorize(group),
            "scope": "test" if "testImplementation" in text[max(0, m.start()-20):m.start()] else "main",
        })

    # Sort by category then artifact
    libraries.sort(key=lambda x: (x["category"], x["artifact"]))

    architektur_path = DATA_DIR / "architektur.json"
    data = json.loads(architektur_path.read_text(encoding="utf-8"))
    data["sbom_libraries"] = libraries
    architektur_path.write_text(
        json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8"
    )

    by_cat: dict[str, int] = {}
    for lib in libraries:
        by_cat[lib["category"]] = by_cat.get(lib["category"], 0) + 1
    print(f"sbom_libraries: {len(libraries)} entries")
    for cat, count in sorted(by_cat.items()):
        print(f"  {cat:30s} {count}")


if __name__ == "__main__":
    main()
