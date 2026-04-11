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


# Map artifact ID → short description
DESCRIPTIONS: dict[str, str] = {
    # Scripting
    "groovy":               "Dynamische JVM-Skriptsprache; wird für OFBiz-Groovy-Scripts (Service-Layer, Views) benötigt.",
    "groovy-json":          "Groovy-Erweiterung für JSON-Parsing und -Erzeugung.",
    "clojure":              "Funktionale Lisp-Dialekt-Sprache auf der JVM; wird für einzelne OFBiz-Komponenten genutzt.",
    # Web-Container
    "tomcat-embed-core":    "Eingebetteter Apache Tomcat-Server (Servlet-Container, HTTP-Verarbeitung).",
    "tomcat-embed-jasper":  "JSP-Compiler und -Runtime für den eingebetteten Tomcat.",
    "tomcat-jdbc":          "Hochperformante JDBC-Connection-Pool-Implementierung von Tomcat.",
    "tomcat-catalina-ha":   "Hochverfügbarkeits-Clustering-Modul für Tomcat (Session-Replikation).",
    "tomcat-tribes":        "Gruppen-Kommunikationsframework, das Tomcat-HA zugrunde liegt.",
    # Logging
    "log4j-api":            "API-Schicht von Apache Log4j 2 — entkoppelt Logging-Aufrufe von der Implementierung.",
    "log4j-core":           "Kern-Implementierung von Apache Log4j 2 mit Appender, Layout und Filtern.",
    # Apache Commons
    "commons-codec":        "Kodierungs-/Dekodierungsroutinen (Base64, Hex, URL, Digest).",
    "commons-collections4": "Erweiterte Collection-Typen und -Utilities (Multimap, Bag, BidiMap u.a.).",
    "commons-csv":          "Lesen und Schreiben von CSV-Dateien nach RFC 4180.",
    "commons-io":           "Hilfsmethoden für Datei- und Stream-Operationen (FileUtils, IOUtils).",
    "commons-lang3":        "Utility-Klassen für String-, Array-, Reflection- und Datumsoperationen.",
    "commons-text":         "Textverarbeitungs-Utilities (StringSubstitutor, Levenshtein, Escape-Funktionen).",
    "commons-net":          "Client-Implementierungen für FTP, SMTP, POP3, Telnet und weitere Protokolle.",
    "commons-pool2":        "Generisches Object-Pool-Framework (Basis für DBCP2).",
    "commons-dbcp2":        "JDBC-Connection-Pool auf Basis von Commons Pool 2.",
    "commons-fileupload":   "Multipart-HTTP-Upload-Verarbeitung für Servlets.",
    "commons-validator":    "Validierungsframework für E-Mail, URL, Kreditkartennummern u.a.",
    "commons-cli":          "Parser für Kommandozeilenargumente.",
    "commons-imaging":      "Lesen und Schreiben diverser Bildformate (PNG, TIFF, BMP, ICNS u.a.).",
    # JSON
    "jackson-databind":     "De-/Serialisierung zwischen Java-Objekten und JSON (ObjectMapper).",
    # Template-Engine
    "freemarker":           "Template-Engine für HTML, XML und Textgenerierung; zentral für OFBiz-Views.",
    # Caching
    "caffeine":             "Hochperformanter In-Process-Cache (Ersatz für Guava Cache) mit W-TinyLFU-Eviction.",
    # Google Libraries
    "guava":                "Google-Basisbibliotek: Collections, Caching, Preconditions, Hashing, I/O-Helpers.",
    "libphonenumber":       "Internationales Parsing, Formatierung und Validierung von Telefonnummern.",
    "re2j":                 "Lineare Regex-Engine (Port von Google RE2) ohne Backtracking-Risiko.",
    "core":                 "ZXing Kern-Bibliothek zum Lesen und Erzeugen von Barcodes (QR, EAN, Code128 u.a.).",
    "javase":               "ZXing Java-SE-Erweiterung (BufferedImage-Support, CLI-Tool).",
    "concurrentlinkedhashmap-lru": "Thread-sicherer LRU-Cache auf Basis einer verketteten HashMap.",
    # Authentifizierung
    "java-jwt":             "Erstellen, Signieren und Verifizieren von JSON Web Tokens (JWT/JWS).",
    # Security
    "shiro-core":           "Apache Shiro: Authentifizierung, Autorisierung, Session-Management und Kryptografie.",
    "esapi":                "OWASP Enterprise Security API — Bibliothek für sichere Kodierung und Input-Validierung.",
    "owasp-java-html-sanitizer": "Bereinigt HTML-Input nach OWASP-Richtlinien und entfernt XSS-Vektoren.",
    # Excel / Office
    "poi":                  "Apache POI: Lesen und Schreiben von Microsoft-Office-Formaten (XLS, DOC, PPT).",
    "poi-ooxml":            "Apache POI OOXML-Erweiterung für XLSX, DOCX und PPTX (Open XML).",
    # PDF
    "pdfbox":               "Apache PDFBox: Erstellen, Bearbeiten und Extrahieren von PDF-Dokumenten.",
    "itext":                "iText 2.x (Legacy): PDF-Erstellung und -Manipulation (ältere API).",
    "library":              "Mustang: Erzeugt und liest ZUGFeRD/Factur-X-konforme elektronische Rechnungen.",
    # XSL-FO / SVG
    "fop":                  "Apache FOP: Rendert XSL-FO-Dokumente zu PDF, PS und anderen Ausgabeformaten.",
    "batik-all":            "Apache Batik: SVG-Rendering, -Transcodierung und -DOM-Unterstützung.",
    # HTTP-Client
    "httpclient":           "Apache HttpComponents Client 4.x für HTTP/HTTPS-Anfragen mit Verbindungspool.",
    # HTML-Parsing
    "jsoup":                "HTML-Parser mit CSS-Selektor-API und eingebautem HTML-Sanitizer.",
    # RSS / Atom
    "rome":                 "Parsing und Erzeugen von RSS- und Atom-Feeds.",
    # Kalender
    "ical4j":               "Parsing und Erzeugung von iCalendar-Daten (RFC 5545); Basis für OFBiz-Kalender.",
    # Dokumenten-Analyse
    "tika-core":            "Apache Tika Kern-API: erkennt MIME-Typen und extrahiert Metadaten aus Dateien.",
    "tika-parsers-standard-package": "Tika-Parser-Bundle für Office, PDF, Bilder, Audio, Video und weitere Formate.",
    # XML (JDOM)
    "jdom2":                "JDOM 2: Einfache Java-API für DOM-ähnliche XML-Verarbeitung.",
    "jdom":                 "JDOM 1 (Legacy): ältere Java-XML-API, noch von einzelnen OFBiz-Komponenten verwendet.",
    # vCard
    "ez-vcard":             "Parsing und Erzeugen von vCard-Dateien (RFC 6350) für Kontaktdaten-Import/Export.",
    # Bild-Metadaten
    "metadata-extractor":   "Extrahiert EXIF-, IPTC- und XMP-Metadaten aus JPEG, PNG, RAW und weiteren Bildformaten.",
    # Transaktionen
    "geronimo-transaction":  "JTA-Transaktionsmanager aus dem Apache-Geronimo-Projekt.",
    # Expression Language
    "juel-api":             "JUEL API: Java Unified Expression Language (EL 2.2) nach JSR-245.",
    "juel-impl":            "JUEL Implementierung der Expression Language mit Caching und Method-Invocation.",
    # E-Mail
    "jakarta.mail":         "Jakarta Mail 2.x: Senden und Empfangen von E-Mails über SMTP, IMAP, POP3.",
    "javax.mail":           "Jakarta Mail 1.x (javax.*-Namespace, Legacy): wird für ältere OFBiz-Komponenten benötigt.",
    # Regex
    "oro":                  "Apache ORO: Perl5-kompatible Regular Expressions (Legacy-Bibliothek).",
    # Web Services / SOAP
    "axis2-kernel":         "Apache Axis2: SOAP-Web-Service-Framework (Client und Server).",
    "axiom-api":            "Apache Axiom: Streaming-XML-Objektmodell, Basis für Axis2.",
    "cxf-core":             "Apache CXF Kern: Framework für JAX-WS- und JAX-RS-Web-Services.",
    "cxf-rt-frontend-jaxrs":"Apache CXF JAX-RS-Frontend: REST-API-Implementierung nach JAX-RS-Standard.",
    "javax.ws.rs-api":      "JAX-RS 2.1 API (javax.*-Namespace): Annotationen für REST-Endpunkte.",
    "wsdl4j":               "WSDL4J: Lesen und Schreiben von WSDL-Dokumenten (Web Service Definition Language).",
    # Java EE Legacy
    "jaxb-api":             "JAXB 2.x API (javax.*-Namespace): XML-Binding-Annotationen für Java-Objekte.",
    "javax.mail-api":       "Jakarta Mail API (javax.*-Namespace, Legacy).",
    "javax.jms-api":        "JMS 2.0 API (javax.*-Namespace): Java Message Service für Messaging-Systeme.",
    "javax.servlet.jsp-api":"JSP 2.3 API (javax.*-Namespace): JavaServer Pages Tag- und Expression-Klassen.",
    "activation":           "JavaBeans Activation Framework (javax.activation, Legacy): MIME-Typ-Handling.",
    # XML-Serialisierung
    "xstream":              "XStream: Serialisierung von Java-Objekten nach XML und JSON ohne Annotationen.",
    # Unicode
    "icu4j":                "IBM ICU4J: Unicode- und Internationalisierungs-Unterstützung (Collation, Datum, Zahl).",
    # SFTP / SSH
    "sshd-core":            "Apache MINA SSHD: SSH-2-Server- und -Client-Implementierung.",
    "sshd-sftp":            "Apache MINA SSHD SFTP-Erweiterung für Dateiübertragungen über SSH.",
    # XML-Parser
    "xercesImpl":           "Apache Xerces2: validierender XML-Parser mit DOM- und SAX-Unterstützung.",
    # ZIP
    "zip4j":                "Zip4j: Lesen und Schreiben von ZIP-Archiven mit AES-Verschlüsselung.",
    # Test
    "ant":                  "Apache Ant: Build-Tool; wird für Test-Support-Klassen in OFBiz verwendet.",
    "ant-junit":            "Apache Ant JUnit-Task: Führt JUnit-Tests innerhalb von Ant-Builds aus.",
    "spring-test":          "Spring Test: MockHttpServletRequest und weitere Test-Utilities.",
    "junit":                "JUnit 4: Standard-Framework für Unit-Tests in Java.",
}


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
            "description": DESCRIPTIONS.get(artifact, ""),
        })

    # Sort by category then artifact
    libraries.sort(key=lambda x: (x["category"], x["artifact"]))

    architektur_path = DATA_DIR / "architektur.json"
    data = json.loads(architektur_path.read_text(encoding="utf-8"))

    # Preserve existing fields (e.g. vulns) added by later scripts
    existing = {f"{l['group']}:{l['artifact']}": l for l in data.get("sbom_libraries", [])}
    for lib in libraries:
        key = f"{lib['group']}:{lib['artifact']}"
        if key in existing:
            for field in ("vulns",):
                if field in existing[key]:
                    lib[field] = existing[key][field]

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
