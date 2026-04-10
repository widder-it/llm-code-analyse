# Architektur-Analyse: Apache OFBiz
**Analysemethode:** Statische Analyse aus Java Class-Files (kein Quellcode vorhanden)  
**Analysewerkzeuge:** `jdeps` (JDK 21), `javap` (JDK 21), CFR 0.152, eigene Skripte  
**Analysedatum:** April 2026  
**Analyseobjekt:** `/java/org/` — 2.932 Class-Files

---

## 1. Technologisches Fundament

Das System basiert auf **Apache OFBiz** (Open For Business), einem quelloffenen Java-ERP-Framework der Apache Software Foundation.

| Eigenschaft | Wert |
|---|---|
| Framework | Apache OFBiz (erkennbar an Paketstruktur `org.apache.ofbiz.*`) |
| Java-Version (Kompilat) | Java 17 (Class-File Major Version 61) |
| Kompiliert am | 06.01.2026 |
| Sprachen | Java + Groovy (ca. 70 / 30 %) |
| Gesamtklassen | 2.932 (inkl. innere Klassen und Groovy-Closures) |
| Top-Level-Klassen | 1.568 |
| Module | 25 |

> **Bedeutung:** Da Apache OFBiz Open Source ist, ist der Quellcode vollständig auf  
> [github.com/apache/ofbiz-framework](https://github.com/apache/ofbiz-framework) verfügbar.  
> Die vorliegenden Class-Files entsprechen dem OFBiz-Framework-Core ohne erkennbare  
> proprietäre Erweiterungen im `org.apache.ofbiz.*`-Namensraum.

---

## 2. Modulstruktur und Umfang

### 2.1 Klassen und API-Umfang pro Modul

| Modul | Klassen | Public Methoden | Typ | Beschreibung |
|---|---:|---:|---|---|
| **product** | 181 | 1.218 | Business | Produktkatalog, Kategorien, Preise, Varianten, Lager, Promotions, Lieferanten |
| **order** | 147 | 1.974 | Business | Bestellverwaltung, Warenkorb, Checkout, Rückgaben, Angebote, Shopping-Listen |
| **entity** | 146 | 1.882 | Kern-Framework | Proprietäres ORM: `Delegator`, `GenericEntity`, `EntityQuery`, Transaktionen, Kryptographie |
| **base** | 155 | 1.611 | Kern-Framework | Utilities (DateTime, HTTP, XML, Cache), Konfiguration, Container-Lifecycle, Konvertierungen |
| **service** | 126 | 1.078 | Kern-Framework | Service-Engine: Dispatching, Job-Scheduler, JMS-Integration, RMI, Service-Metadaten |
| **minilang** | 125 | 520 | Script-Engine | Interpreter für proprietäre XML-DSL (MiniLang); seit OFBiz 18.12 deprecated |
| **accounting** | 113 | 955 | Business | Buchhaltung, Rechnungen, Zahlungen, Hauptbuch, Budgets, Anlagevermögen, 8 Payment-Provider |
| **widget** | 95 | 939 | UI-Framework | Deklarative UI-Engine: Screen-, Form-, Menu- und Tree-Renderer (FreeMarker/FO/Macro) |
| **content** | 77 | 602 | Business | Content-Management, Datei-Verwaltung, Surveys, Blog, SFTP-Client, FTP-Integration |
| **webapp** | 75 | 370 | Web-Infrastruktur | Servlet-Controller, Request-Routing, Login, Session, WebDAV, CSRF-Schutz, JWT |
| **webtools** | 54 | 370 | Web-Infrastruktur | Admin-Werkzeuge: Cache-Verwaltung, DB-Tools, Service-Browser, Testausführung, FO-Druck |
| **party** | 52 | 362 | Business | Stammdaten für Personen/Organisationen, Kontaktdaten, Kommunikation, Einladungen |
| **common** | 54 | 332 | Querschnitt | E-Mail, Geo-Daten, Login-Services, Portal-Seiten, Einstellungen, QR-Code, Status |
| **manufacturing** | 44 | 302 | Business | Fertigung: Stücklisten (BOM), Produktionsaufträge, Routing, MRP, Kostenkalkulation |
| **shipment** | 25 | 301 | Business | Versand, Kommissionierung, Verpackung, Carrier-Integration (UPS, FedEx, DHL, USPS) |
| **workeffort** | 23 | 120 | Business | Aufgaben, Projekte, Kalender-Events, Ressourcenzuweisung, Arbeitszeiterfassung |
| **entityext** | 18 | 119 | Framework-Erweiterung | Entity-Synchronisation zwischen Instanzen, Cache-Services, Daten-Import/Export, Upgrades |
| **datafile** | 9 | 124 | Dateiverarbeitung | Strukturierte Dateiimporte (CSV, Fixlänge) über konfigurierbare Metadaten-Definitionen |
| **marketing** | 13 | 55 | Business | Marketing-Kampagnen, Tracking-Codes, SFA-Leads und Account-Management |
| **security** | 10 | 61 | Querschnitt | Berechtigungsprüfung, CSRF-Strategien; enthält auch ZUGFeRD/E-Rechnung (Mustang) |
| **testtools** | 7 | 31 | Test-Infrastruktur | Basis-Testklassen für OFBiz-Services und Groovy-basierte Integrationstests |
| **catalina** | 7 | 17 | Tomcat-Integration | Tomcat-spezifische Klassen: SSO-Valve, HTTPS-Redirect, Servlet-Container-Hooks |
| **commonext** | 7 | 36 | Querschnitt | System-Info-Services, Setup-Assistent für neue OFBiz-Instanzen |
| **securityext** | 2 | 10 | Querschnitt | Erweiterte Login-Events, Zertifikat-Services (SSL-Client-Zertifikate) |
| **humanres** | 2 | 6 | Business | Personalwesen: Mitarbeiterdaten und HR-Events (minimale Implementierung) |
| **sfa** | 1 | 3 | Business | Sales Force Automation: Kontakt-Export via vCard (ezvcard) |
| **Gesamt** | **1.568** | **13.398** | | |

### 2.2 Sprachverteilung

Von den 2.932 Class-Files stammen:
- **~70 % (≈2.050)** aus Java-Quellcode — sauber dekompilierbar
- **~30 % (≈880)** aus Groovy-Skripten — als `.class` vorhanden, Quellcode nicht rekonstruierbar

Die Groovy-Klassen sind Groovy-Skripte des OFBiz-Service-Frameworks (Business-Logik als Groovy-Scripts konfiguriert), erkennbar an `extends groovy.lang.Script` und Closure-Klassen (`$_run_closure`).

---

## 3. Interne Modul-Abhängigkeiten

### 3.1 Dependency-Graph

Die vollständige Grafik liegt unter `analysis/diagrams/module-deps.png`.

**Legende:**
- 🔵 **Blau** — Kern-Module (base, entity, service, security)
- 🟢 **Grün** — Business-Module (accounting, order, party, product, ...)
- 🟠 **Orange** — Infrastruktur (webapp, webtools, catalina, widget, common)
- ⚫ **Grau** — Support (content, datafile, minilang, entityext, ...)

### 3.2 Kern-Abhängigkeitsstruktur (163 interne Abhängigkeiten)

```
Kern-Framework (Basis aller Module):
  base ← entity ← service ← security
         ↓           ↓
       minilang    testtools

Business-Module (bauen aufeinander auf):
  accounting → entity, service, order, party, product, security
  order      → accounting, entity, service, party, product, marketing, content
  product    → entity, service, party, order, shipment, content
  party      → entity, service, accounting, product, content

Infrastruktur (querschnittlich):
  webapp   → base, entity, service, security, widget, minilang
  widget   → entity, service, security, minilang
  webtools → entity, service, webapp, testtools
```

### 3.3 Architektonische Beobachtungen

**Zyklische Abhängigkeiten (kritisch):**
- `order ↔ accounting` — gegenseitige Abhängigkeit
- `order ↔ product` — gegenseitige Abhängigkeit
- `party ↔ accounting` — gegenseitige Abhängigkeit
- `party ↔ product` — gegenseitige Abhängigkeit

Diese Zyklen sind ein klassisches Zeichen hoher **Kopplung** und erschweren die modulare Ablösung einzelner Komponenten.

**Zentrale Knoten (hoher Fan-in):**
`entity` und `service` werden von fast allen Modulen genutzt — sie sind die eigentliche Kern-API.

---

## 4. Externe Abhängigkeiten (SBOM)

191 externe Pakete aus Drittbibliotheken, klassifiziert nach Kategorie:

| Kategorie | Pakete | Wichtigste Bibliotheken |
|---|---:|---|
| **Web / HTTP** | 41 | Tomcat 10.x (Catalina, Coyote, Jasper), Commons FileUpload |
| **Utilities** | 31 | Apache Commons (Lang3, IO, Collections4, CSV, Pool2, DBCP2), Guava, Jackson |
| **Scripting** | 15 | Groovy 4.x, Clojure, Apache Oro (Regex) |
| **Integration** | 11 | Apache Axis2 (SOAP), Apache CXF (REST/JAX-RS), Axiom, WSDL4J, ROME |
| **Messaging** | 10 | JavaMail, JMS, Apache MINA SSHD |
| **Security** | 9 | Apache Shiro, OWASP ESAPI, OWASP HTML Sanitizer, Auth0 JWT |
| **XML/Daten** | 9 | Xerces, JDOM, JAXB |
| **Dokumente** | 12 | Apache FOP (PDF), Apache POI (Excel), PDFBox, iText, Batik (SVG), Mustang (ZUGFeRD) |
| **Templating** | 8 | Apache FreeMarker |
| **Kalender/Kontakt** | 8 | iCal4j, ez-vcard |
| **Persistenz** | 6 | Geronimo Transaction Manager, Commons DBCP2/Pool2 |
| **Testing** | 3 | JUnit 4, Spring Test |
| **Sonstiges** | 28 | ICU4J, ZXing (QR), libphonenumber, Tika, ConcurrentLinkedHashMap, ... |

### 4.1 Java-EE-Abhängigkeiten (Risiko)

Das System nutzt die **alte `javax.*`-Namespace** (Java EE, vor Jakarta EE):
- `javax.servlet.*` — Servlet-API
- `javax.mail.*` — JavaMail
- `javax.jms.*` — JMS
- `javax.xml.bind.*` — JAXB

Dies bedeutet: **kein direkter Einsatz moderner Jakarta-EE-Container** ohne Migration.

---

## 5. Schnittstellenpunkte und Integrations-Architektur

### 5.1 HTTP-Eintrittspunkte (`*Events`-Klassen)

39 Event-Handler-Klassen bilden die HTTP-Schnittstelle des Systems. Jede `public static`-Methode ist ein HTTP-Request-Endpunkt.

| Events-Klasse | Modul | Endpunkte |
|---|---|---:|
| `ShoppingCartEvents` | order | 42 |
| `CheckOutEvents` | order | 25 |
| `ProductEvents` | product | 22 |
| `ShoppingListEvents` | order | 17 |
| `ShippingEvents` | order | 16 |
| `ExpressCheckoutEvents` (PayPal) | order | 9 |
| `CoreEvents` | webapp | 9 |
| `TrackingCodeEvents` | marketing | 8 |
| `LayoutEvents` | content | 8 |
| `LoginEvents` | securityext | 7 |
| `ProductSearchEvents` | product | 7 |
| `CommonEvents` | common | 10 |
| *(weitere 27 Events-Klassen)* | diverse | je 1–5 |

**Gesamt: ~250 HTTP-Request-Endpunkte** über das OFBiz Widget-Controller-Framework.

### 5.2 Service-Schicht (`*Services`-Klassen)

120+ Service-Klassen bilden die interne Anwendungslogik. Sie werden über die OFBiz Service-Engine aufgerufen (nicht direkt per HTTP).

**Größte Service-Klassen:**

| Service-Klasse | Modul | Public Methoden |
|---|---|---:|
| `ModelService` | service | 114 |
| `OrderServices` | order | 84 |
| `PaymentGatewayServices` | accounting | 47 |
| `PaymentServices` | accounting | 30 |
| `ContentManagementServices` | content | 30 |
| `OrderReturnServices` | order | 29 |
| `ValueLinkServices` (Gift Cards) | accounting | 22 |
| `PartyServices` | party | 23 |
| `ProductionRunServices` | manufacturing | 32 |
| `ShipmentServices` | product | 36 |

### 5.3 Externe Integrationspunkte

**Payment-Gateways (8 Provider):**

| Provider | Klassen | Typ |
|---|---|---|
| PayPal Express Checkout | `ExpressCheckoutEvents`, `PayPalEvents` | REST/NVP |
| Authorize.Net AIM | `AIMPaymentServices`, `AuthorizeResponse` | HTTP-POST |
| ClearCommerce | `CCPaymentServices` | XML/HTTPS |
| eWay | `EwayServices`, `GatewayConnector`, `GatewayRequest` | HTTP |
| GoSoftware (PcCharge, Rita) | `PcChargeServices`, `RitaServices` | proprietär |
| SagePay | `SagePayPaymentServices`, `SagePayServices` | Form/Server |
| ValueLink (Gift Cards) | `ValueLinkApi`, `ValueLinkServices` | proprietär |
| WorldPay | `WorldPayEvents` | Redirect |

**Versanddienstleister (4 Carrier):**

| Carrier | Klasse | Methoden |
|---|---|---:|
| UPS | `UpsServices` | 20 |
| USPS | `UspsServices` | 14 |
| DHL | `DhlServices` | 10 |
| FedEx | `FedexServices` | 6 |

### 5.4 API-Verträge (Interfaces)

71 Interfaces definieren die internen API-Verträge:

| Interface | Methoden | Bedeutung |
|---|---:|---|
| `Delegator` | 108 | Zentraler Datenzugriffs-Kontrakt |
| `FormStringRenderer` | 58 | Formular-Rendering-Pipeline |
| `LocalDispatcher` | 45 | Service-Dispatching-Kontrakt |
| `ScreenStringRenderer` | 31 | Screen-Rendering |
| `ModelWidgetVisitor` | 33 | Widget-Tree-Traversal |
| `EntityCondition` | 22 | Query-Builder-Kontrakt |
| `Security` | 13 | Autorisierungs-Kontrakt |
| `RemoteDispatcher` | 15 | RMI-Service-Kontrakt |
| `IShoppingCartItems` | 14 | ShoppingCart-Komponente |
| `GenericHelper` | 14 | DB-Zugriffskontrakt |

---

## 6. Technische Schulden und Risiko-Indikatoren

### 6.1 Komplexitäts-Hotspots (God Objects)

Klassen mit dem größten API-Umfang — starker Proxy für Komplexität und Wartbarkeitsrisiko:

| Klasse | Modul | Public Methoden | Bewertung |
|---|---|---:|---|
| `ShoppingCart` | order | **388** | Extremes God-Object — enthält Warenkorb, Pricing, Tax, Shipping, Payment-State |
| `OrderReadHelper` | order | 192 | Lese-Fassade für Bestellungen |
| `ShoppingCartItem` | order | 180 | Item-Level God-Object |
| `ModelEntity` | entity | 145 | Kern-Entity-Metadaten |
| `ModelService` | service | 114 | Service-Definition/Metadaten |
| `Delegator` (Interface) | entity | 108 | Datenzugriffs-Kontrakt |
| `UtilDateTime` | base | 105 | Date/Time-Utility (God-Util) |
| `ModelForm` | widget | 99 | Formular-Metadaten |
| `GenericDelegator` | entity | 114 | Zentrale Datenzugriffs-Fassade |
| `UtilHttp` | base | 84 | HTTP-Utility |
| `OrderServices` | order | 84 | Monolithischer Bestell-Service |

> **Kritisch:** `ShoppingCart` mit 388 public Methoden ist das größte God-Object — weit über das OFBiz-Standard-Niveau hinaus und ein primäres Refactoring-Risiko.

### 6.2 Identifizierte Risiken

| Risiko | Schwere | Indikator |
|---|---|---|
| Zyklische Modul-Abhängigkeiten | 🔴 Hoch | order↔accounting, order↔product, party↔accounting, party↔product |
| God-Object `ShoppingCart` (388 Methoden) | 🔴 Hoch | Unverhältnismäßige Konzentration von Geschäftslogik |
| Monolithische Services (`OrderServices` 84 Methoden) | 🔴 Hoch | Schwer testbar, schwer isoliert ablösbar |
| Veraltete Java-EE-APIs (`javax.*`) | 🟡 Mittel | 5 `javax.*`-Pakete — Migration zu Jakarta EE erforderlich |
| Groovy-Code nicht rekonstruierbar | 🟡 Mittel | ~30 % der Logik nur als `.class` vorhanden, Quelltext verloren |
| Hohe externe Dependency-Zahl (191 Pakete) | 🟡 Mittel | Supply-Chain-Risiko, viele Updates nötig |
| Keine erkennbare Schichtentrennung | 🟡 Mittel | Business-Module greifen direkt auf DB-Engine zu |
| 8 Payment-Provider eingebaut | 🟡 Mittel | Jeder Provider: eigene API, Update-Pflicht, PCI-DSS-Scope |
| Legacy-Kryptographie in `EntityCrypto` | 🟡 Mittel | DES-basierte `LegacyStorageHandler` noch aktiv als Fallback |

---

## 7. Architekturmuster

Aus den Klassen-Namen, Paketstrukturen und Abhängigkeiten erkennbare Muster:

| Muster | Fundstelle | Bewertung |
|---|---|---|
| **Service-Layer** | `*Services.java`, `service`-Modul | OFBiz Service-Engine (120+ Service-Klassen) |
| **Repository/DAO** | `GenericDelegator`, `EntityQuery` | Proprietäres ORM (kein JPA/Hibernate) |
| **MVC** | `webapp`, `widget`, Controller-Klassen | OFBiz Widget-Framework |
| **Script-Engine** | `minilang`, Groovy-Scripts | Konfigurierbare Business-Regeln (~30% der Klassen) |
| **Event-System** | `*Events.java`-Klassen | HTTP-Request-Handler (39 Klassen, ~250 Endpunkte) |
| **Visitor-Pattern** | `ModelWidgetVisitor`, `ModelConditionVisitor` | Widget-Tree-Traversal |
| **Strategy-Pattern** | `StorageHandler` in `EntityCrypto` | Krypto-Strategie (Shiro/DES/Legacy) |
| **Job Scheduler** | `PersistedServiceJob`, `JobManager`, `JobPoller` in `service` | Interner OFBiz-eigener Scheduler (kein Quartz/Spring Batch) |
| **Plugin/Gateway** | `thirdparty.*` in accounting, shipment | Austauschbare externe Integrationen |

### 7.1 Fehlende moderne Muster

Das System zeigt keine Anzeichen moderner Architekturpraktiken:

| Muster | Status | Implikation |
|---|---|---|
| Dependency Injection | **Nicht vorhanden** | Kein Spring, kein CDI — manuelle Objekt-Verdrahtung |
| REST-Controller-Schicht | **Nicht vorhanden** | Nur Servlet-basierte Controller in `webapp` |
| Reaktive Programmierung | **Nicht vorhanden** | Klassisches blocking I/O |
| Event Sourcing / CQRS | **Nicht vorhanden** | Klassisches CRUD-Muster |
| API-Versionierung | **Nicht erkennbar** | Kein versioning in Events-Klassen sichtbar |

### 7.2 Integrationskanäle (Integrations-relevant)

Für die Batch-Ingestion-Funktion (Batch-Ingestion, Datenaustausch) relevante Kanäle:

| Kanal | Technologie | Fundstelle |
|---|---|---|
| **SFTP** | Apache MINA SSHD (`sshd-core`, `sshd-sftp`) | tief in `content`-Modul eingebettet |
| **JMS** | `javax.jms`, `service.jms` | direkt in Service-Engine integriert |
| **SOAP** | Apache Axis2 | `integration`-relevante SOAP-Dienste |
| **REST/JAX-RS** | Apache CXF | JAX-RS-Schnittstellen (begrenzt) |
| **E-Mail** | JavaMail, SMTP | `common.email`-Modul |
| **FTP** | Apache Commons Net | `content.ftp.FtpServices` |

> **Hinweis:** SFTP- und JMS-Implementierungen liegen in allgemeinen Framework-Modulen (`content`, `service`) — keine dedizierte Integrationsschicht. Anpassungen für den Batch-Prozess sind vermutlich tief in diesen Modulen verankert.

### 7.3 MiniLang — Veraltete Script-Engine mit Sicherheitsrisiko

Das `minilang`-Modul implementiert eine **proprietäre XML-basierte DSL** ohne statische Typisierung.

- **Abhängig von 10+ Modulen** — weit verbreitet im System
- **Seit OFBiz 18.12 offiziell als Deprecated markiert** — vorliegender Code nutzt es noch aktiv
- **Sicherheitsrisiko:** unkontrollierter Datenfluss aus externen Quellen in MiniLang-Ausdrücke kann Injection-Angriffe ermöglichen
- **Analyse-Blocker:** MiniLang-Scripts liegen als XML-Konfiguration vor (nicht in Class-Files) — statische Analyse nicht möglich

---

## 8. Bewertung für Ablösung

| Aspekt | Befund |
|---|---|
| **Modularisierbarkeit** | Schwierig wegen Zyklen; Entity- und Service-Kern müssten zuerst extrahiert werden |
| **HTTP-API-Oberfläche** | ~250 Endpunkte in 39 Events-Klassen — dokumentierbar und testbar |
| **Service-API-Oberfläche** | 120+ Service-Klassen = interne Schnittstellen bei Strangler-Fig-Migration |
| **Testabdeckung** | `testtools`-Modul vorhanden; Groovy-Testklassen für alle Module erkennbar |
| **Ablöse-Kandidaten** | Payment-Gateway-Modul (klar abgegrenzt), Shipment-Carrier (isoliert) |
| **Risiko-Kandidaten** | `ShoppingCart` (388 Methoden), `OrderServices` (84 Methoden) — zuletzt ablösen |
| **Empfehlung** | Strangler-Fig-Pattern: schrittweise Ablösung über Events-Layer von außen nach innen |

### 8.1 Empfohlene Ablöse-Reihenfolge

```
Phase 1 (Niedrigstes Risiko):
  → Shipment-Carrier-Integrationen (UPS/FedEx/DHL/USPS)
  → Payment-Gateway-Adapter (8 Provider, klar isoliert)
  → Reporting/Content-Module

Phase 2 (Mittleres Risiko):
  → Party-Modul (Stammdaten)
  → Product-Katalog-Funktionen
  → Manufacturing/WorkEffort

Phase 3 (Höchstes Risiko — zuletzt):
  → Order/ShoppingCart-Kern (God-Objects)
  → Entity-Engine (zentrale DB-Abstraktion)
  → Service-Engine (Framework-Kern)
```

---

## Anhang: Analysedateien

| Datei | Inhalt |
|---|---|
| `analysis/metrics/class-metrics.json` | Metriken pro Modul (Klassen, Methoden, Top-5) |
| `analysis/jdeps/ofbiz-module-deps-clean.txt` | 163 interne Modul-Abhängigkeiten |
| `analysis/jdeps/package-deps-full.txt` | Vollständige jdeps-Ausgabe (2.986 Zeilen) |
| `analysis/jdeps/internal-module-deps.txt` | Modul-Level Dependency-Map |
| `analysis/sbom/sbom-classified.json` | 191 externe Pakete nach Kategorie |
| `analysis/sbom/external-packages.txt` | Rohliste externe Pakete |
| `analysis/api/class-inventory-raw.txt` | javap-Ausgabe aller Klassen (29.113 Zeilen) |
| `analysis/api/public-api-catalog.md` | Strukturierter API-Katalog nach Modul |
| `analysis/diagrams/module-deps.dot` | GraphViz-Quelle des Modul-Dependency-Graphs |
| `analysis/diagrams/module-deps.png` | Gerenderte Modul-Abhängigkeitsgrafik |
