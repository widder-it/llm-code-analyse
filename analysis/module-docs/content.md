## Modul: content

### Überblick

Das `content`-Modul ist das zentrale Content-Management-Framework von Apache OFBiz. Es verwaltet strukturierte Inhaltsobjekte (`Content`, `DataResource`) mit Assoziationen, Zugriffskontrolle, Lokalisierung und Rendering. Neben der Kernfunktionalität enthält das Modul spezialisierte Submodule für FTP/SFTP-Dateitransfer, Umfragen (Survey) mit PDF-Integration, Blog-RSS-Feeds, CMS-Verwaltung und FreeMarker-Template-Transformationen.

---

### Submodule

| Paket | Beschreibung |
|---|---|
| `org.apache.ofbiz.content` | Wurzelpaket: übergeordnete Management-Services, Events und Worker |
| `org.apache.ofbiz.content.content` | Kernpaket: Content-Entitäten, Rendering, Suche, Berechtigungen, URL-Filter |
| `org.apache.ofbiz.content.data` | DataResource-Verwaltung: Dateien, Bilder, elektronische Texte |
| `org.apache.ofbiz.content.ftp` | FTP/SFTP-Integration: Clients, Interface, Dienst |
| `org.apache.ofbiz.content.survey` | Umfragen: Rendering, PDF-Import/Export, Antwort-Auswertung |
| `org.apache.ofbiz.content.blog` | Blog-Dienste: RSS-Feed-Generierung |
| `org.apache.ofbiz.content.cms` | CMS-Ereignisse und View-Preparer (Groovy) |
| `org.apache.ofbiz.content.layout` | Layout-Verwaltung: Datei-Upload, Events |
| `org.apache.ofbiz.content.output` | Ausgabe-Dienste: FOP/PDF-Druck, Drucker-Routing |
| `org.apache.ofbiz.content.webapp.ftl` | FreeMarker-Transformationen für Content-Rendering in Templates |
| `org.apache.ofbiz.content.view` | View-Handler für Content-Auslieferung |
| `org.apache.ofbiz.content.permission` | Groovy-basierte Berechtigungsprüfung |
| `org.apache.ofbiz.content.website` | Groovy-Scripts für Website-Verwaltung |
| `org.apache.ofbiz.content.print` | Groovy-Script für Drucker-Suche |
| `org.apache.ofbiz.content.contentsetup` | Setup-Groovy-Script für Content-Initialisierung |
| `org.apache.ofbiz.content.datasetup` | Setup-Groovy-Script für Datenkategorie-Initialisierung |

---

### Klasse: `ContentWorker`

**Paket:** `org.apache.ofbiz.content.content`
**Typ:** Java-Klasse (implementiert `ContentWorkerInterface`)
**Zweck:** Zentrale Rendering- und Traversierungs-Engine für Content-Objekte. Stellt alle statischen Hilfsmethoden bereit, um Inhalte zu suchen, zu rendern, zu lokalisieren, in Baumstrukturen zu traversieren und Berechtigungen zu prüfen.

| Methode | Beschreibung |
|---|---|
| `findContentForRendering(delegator, contentId, locale, partyId, roleTypeId, cache)` | Ermittelt den zu rendernden Content-Datensatz unter Berücksichtigung von Locale-Alternativen, Publish-Points und rollenbasierten Alternativ-Inhalten |
| `renderContentAsText(dispatcher, contentId, out, templateContext, locale, mimeTypeId, partyId, roleTypeId, cache)` | Rendert einen Content-Eintrag als Text in den übergebenen Writer; unterstützt Decorator-Ketten und Custom-Methods |
| `renderContentAsText(dispatcher, contentId, templateContext, locale, mimeTypeId, cache)` | Variante die den gerenderten Text als String zurückgibt; bereinigt HTML-Sonderzeichen via HTML-Encoder |
| `renderSubContentAsText(dispatcher, contentId, out, mapKey, templateContext, locale, mimeTypeId, cache)` | Rendert den per `mapKey` assoziierten Unter-Content eines Eltern-Inhalts |
| `findAlternateLocaleContent(delegator, view, locale)` | Sucht die passende Locale-Alternative eines Content-Eintrags (bevorzugt exakten Match, dann 2-Buchstaben-Fallback) |
| `findAlternateLocaleContents(delegator, view)` | Gibt alle Locale-Alternativen eines Content-Eintrags zurück |
| `traverse(delegator, content, fromDate, thruDate, whenMap, depthIdx, masterNode, contentAssocTypeId, pickList, direction)` | Rekursive Tiefensuche im Content-Baum mit konfigurierbaren Pick/Follow/Return-Bedingungen |
| `traverseSubContent(ctx)` | Iterativer Traversal-Schritt im Node-Trail-Kontext; verwaltet Traversal-Zustand über eine Knotenliste |
| `selectKids(currentNode, ctx)` | Lädt Kindknoten eines Traversal-Knotens und bewertet deren Pick/Follow-Bedingungen |
| `checkConditions(delegator, trailNode, contentAssoc, whenMap)` | Wertet Pick/Follow/Return-Bedingungen für einen Knoten aus; nutzt Groovy-Ausdrücke via `FlexibleStringExpander` |
| `checkWhen(context, whenStr, defaultReturn)` | Wertet einen Groovy-Ausdruck als Boolean aus (wird für When-Conditions verwendet) |
| `getSubContent(delegator, contentId, mapKey, subContentId, userLogin, assocTypes, fromDate)` | Ermittelt einen assoziierten Unter-Content anhand mapKey oder direkter Sub-Content-ID |
| `getSubContentCache(delegator, contentId, mapKey, ...)` | Cache-Variante von `getSubContent`; verwendet `ContentServicesComplex` |
| `getCurrentContent(delegator, trail, userLogin, ctx, nullThruDatesOnly, contentAssocPredicateId)` | Bestimmt den aktuell aktiven Content im Traversal-Kontext |
| `getContentAncestry(delegator, contentId, contentAssocTypeId, direction, list)` | Lädt rekursiv die Ahnen-Kette eines Content-Eintrags |
| `getContentAncestryAll(delegator, contentId, passedContentTypeId, direction, list)` | Lädt alle Vorgänger aller Assoziations-Richtungen eines Content-Eintrags |
| `getContentAncestryNodeTrailCsv(delegator, contentId, contentAssocTypeId, direction)` | Gibt den Vorfahren-Pfad als kommaseparierte Content-ID-Liste zurück |
| `getContentAssocViewList(delegator, contentIdTo, contentId, contentAssocTypeId, statusId, privilegeEnumId)` | Sucht Content-Assoziationen mit optionalen Filtern für Status und Privilege |
| `getAssociatedContent(currentContent, linkDir, assocTypes, contentTypes, fromDate, thruDate)` | Gibt direkt verknüpfte Content-Einträge gefiltert nach Assoziationstyp zurück |
| `callContentPermissionCheck(delegator, dispatcher, context)` | Führt die Service-basierte Berechtigungsprüfung durch und gibt den Permission-Status zurück |
| `prepTargetOperationList(context, md)` | Stellt die Ziel-Operationsliste für Berechtigungsprüfungen zusammen |
| `getMimeTypeId(delegator, view, ctx)` | Ermittelt den MIME-Typ eines Content-Views aus dem Kontext oder Eltern-Content |
| `nodeTrailToCsv(nodeTrail)` | Konvertiert einen Traversal-Node-Trail in eine kommaseparierte Content-ID-Liste |
| `csvToTrail(csv, delegator)` | Konvertiert eine kommaseparierte Content-ID-Liste zurück in einen Node-Trail |
| `makeNode(thisContent)` | Erstellt einen Traversal-Knoten aus einem Content-GenericValue |
| `pullEntityValues(delegator, entityName, context)` | Befüllt ein Entity-Value-Objekt aus einem Kontext-Map |

---

### Klasse: `ContentServices`

**Paket:** `org.apache.ofbiz.content.content`
**Typ:** Java-Klasse (Service-Engine-Dispatcher)
**Zweck:** Stellt OFBiz-Service-Endpunkte für Content-Operationen bereit — von der Beziehungsverwaltung und Traversierung über Publishing bis zu Utility-Diensten für String-Manipulation.

| Methode | Beschreibung |
|---|---|
| `findRelatedContent(dctx, context)` | Sucht mit einem Content verknüpfte Inhalte und filtert das Ergebnis optional nach Ziel-Operationen (Berechtigungsprüfung) |
| `findContentParents(dctx, context)` | Traversiert den Content-Baum nach oben und liefert alle Eltern-IDs einer Content-Instanz |
| `traverseContent(dctx, context)` | Service-Wrapper für `ContentWorker.traverse`; gibt NodeMap und PickList zurück |
| `deactivateContentAssoc(dctx, context)` | Setzt das `thruDate` einer Content-Assoziation auf den aktuellen Zeitpunkt (deaktiviert sie) |
| `deactivateAssocs(dctx, context)` | Deaktiviert alle Assoziationen mit passendem mapKey/sequenceNum außer dem aktiven Content |
| `renderSubContentAsText(dctx, context)` | Service-Endpunkt: rendert Sub-Content als Text in den outWriter |
| `renderContentAsText(dctx, context)` | Service-Endpunkt: rendert Content als Text in den outWriter |
| `linkContentToPubPt(dctx, context)` | Verknüpft oder trennt einen Content-Eintrag mit einem Publish-Point (Assoziations-Toggle) |
| `publishContent(dctx, context)` | Setzt den Content-Status auf `CTNT_PUBLISHED` |
| `getPrefixedMembers(dctx, context)` | Extrahiert alle Map-Einträge mit einem bestimmten Präfix aus einer Input-Map |
| `splitString(dctx, context)` | Splittet einen String anhand eines konfigurierbaren Trennzeichens in eine Liste |
| `joinString(dctx, context)` | Fügt eine Liste von Strings mit einem konfigurierbaren Trennzeichen zusammen |
| `urlEncodeArgs(dctx, context)` | URL-kodiert eine Map von Parametern zu einem Query-String |

---

### Klasse: `ContentManagementServices`

**Paket:** `org.apache.ofbiz.content`
**Typ:** Java-Klasse (Service-Engine-Dispatcher)
**Zweck:** Orchestriert komplexe Content-Management-Operationen wie das atomare Anlegen und Verknüpfen von Content+DataResource, die Verwaltung von Site-Rollen, Abonnements, Content-Baum-Umstrukturierung und Cache-Verwaltung.

| Methode | Beschreibung |
|---|---|
| `persistContentAndAssoc(dctx, context)` | Zentraler Speicherdienst: legt Content, DataResource und ContentAssoc in einem Zug an oder aktualisiert sie; validiert hochgeladene Texte auf Sicherheit |
| `persistDataResourceAndData(dctx, context)` | Prüft Berechtigung und delegiert an `persistDataResourceAndDataMethod`; unterstützt Bilder, Textdateien, Survey-Typen und elektronische Texte |
| `persistDataResourceAndDataMethod(dctx, context)` | Implementierung: legt DataResource und zugehörige Binär-/Text-Daten an oder aktualisiert sie, inkl. Datei-Validierung |
| `getSubContent(dctx, context)` | Lädt einen assoziierten Sub-Content und seinen DataResource-View |
| `getContent(dctx, context)` | Lädt einen Content-Datensatz über den Cache |
| `updateSiteRoles(dctx, context)` | Aktualisiert Blog-Rollen einer Party zu einem Website-Content-Eintrag (anlegen/deaktivieren) |
| `updateSiteRolesDyn(dctx, context)` | Dynamische Variante von `updateSiteRoles`; schreibt Rollen auch für zugehörige UserLogin-Einträge |
| `resequence(dctx, context)` | Nummeriert die Sequenz-Nummern von Content-Assoziationen neu und ermöglicht optionales Verschieben einzelner Elemente |
| `changeLeafToNode(dctx, context)` | Konvertiert einen Content-Blattknoten zu einem Strukturknoten, indem der DataResource-Link als Sub-Content neu verknüpft wird |
| `updateLeafCount(dctx, context)` | Aktualisiert die `childLeafCount`-Statistik eines Content-Baums top-down |
| `updatePageType(dctx, context)` | Setzt Content-Typ (`PAGE_NODE`/`OUTLINE_NODE`) rekursiv für einen Teilbaum |
| `resetToOutlineMode(dctx, context)` | Setzt alle Knoten eines Teilbaums auf `OUTLINE_NODE` zurück |
| `findSubNodes(dctx, context)` | Gibt alle direkten Kindknoten eines Content-Eintrags via `ContentAssocDataResourceViewFrom` zurück |
| `updateContentSubscription(dctx, context)` | Legt oder verlängert eine zeitbasierte `ContentRole`-Mitgliedschaft (Abonnement) |
| `updateContentSubscriptionByProduct(dctx, context)` | Berechnet Abonnement-Dauer aus Produkt-Content-Daten und delegiert an `updateContentSubscription` |
| `updateContentSubscriptionByOrder(dctx, context)` | Verarbeitet alle Bestellpositionen und aktiviert Inhalts-Abonnements für Online-Access-Produkte |
| `followNodeChildren(dctx, context)` | Führt einen Service rekursiv für alle Kindknoten eines Content-Baums aus (benötigt CONTENTMGR_ADMIN) |
| `incrementContentChildStats(dctx, context)` | Erhöht `childLeafCount` und `childBranchCount` bottom-up |
| `decrementContentChildStats(dctx, context)` | Verringert Kind-Statistik-Zähler bottom-up |
| `clearContentAssocViewCache(dctx, context)` | Leert den Entity-Cache für `ContentAssocViewFrom`/`ContentAssocViewTo` |
| `clearContentAssocDataResourceViewCache(dctx, context)` | Leert den Entity-Cache für `ContentAssocViewDataResource`-Views |

---

### Klasse: `ContentManagementWorker`

**Paket:** `org.apache.ofbiz.content`
**Typ:** Java-Klasse (Utility, final, nicht-instantiierbar)
**Zweck:** Stellt Session-basierte MRU-Caches (Most Recently Used), Baum-Statistik-Updates und statische Hilfsmethoden für die Content-Management-UI bereit.

| Methode | Beschreibung |
|---|---|
| `mruAdd(request/session, pk)` | Fügt einen Entity-Primärschlüssel in den sitzungslokalen MRU-Cache ein (nach Entitätsname gruppiert) |
| `mostRecentlyViewedIterator(entityName, lookupCaches)` | Gibt einen Iterator über zuletzt betrachtete Einträge eines Entitätstyps zurück |
| `getWebSitePublishPoint(delegator, contentId, ignoreCache)` | Lädt den Website-Publish-Point zu einer Content-ID (mit Caching) |
| `updateStatsTopDown(delegator, contentId, typeList)` | Aktualisiert `childLeafCount`/`childBranchCount` rekursiv top-down im Baum |
| `updateStatsBottomUp(delegator, contentId, typeList, changeBranchCount, changeLeafCount)` | Propagiert Statistik-Änderungen nach oben in der Vorfahrenkette |

---

### Klasse: `DataResourceWorker`

**Paket:** `org.apache.ofbiz.content.data`
**Typ:** Java-Klasse (implementiert `DataResourceWorkerInterface`)
**Zweck:** Kernklasse für die Verwaltung und das Rendering von DataResource-Objekten in verschiedenen Formaten (elektronischer Text, Dateien, Bilder, FreeMarker-Templates, XML/XSLT, Screen-Widgets). Fungiert als Schnittstelle zwischen Content-System und Widget-Framework.

| Methode | Beschreibung |
|---|---|
| `renderDataResourceAsText(dispatcher, dataResourceId, out, templateContext, locale, mimeTypeId, cache)` | Rendert eine DataResource als Text — je nach Typ als FreeMarker-Template, XML+XSLT, Screen-Widget, URL-Inhalt oder direkt aus dem Datenbanktext |
| `renderDataResourceAsText(dispatcher, delegator, dataResourceId, out, templateContext, locale, mimeTypeId, cache, webAnalytics)` | Variante mit Web-Analytics-Unterstützung |
| `getDataResourceStream(dataResource, prefix, context, locale, rootDir, useCache)` | Gibt einen InputStream für den Rohdaten-Inhalt einer DataResource zurück |
| `getContentFile(dataResourceTypeId, objectInfo, contextRoot)` | Löst den Dateipfad einer DataResource auf (`LOCAL_FILE`, `OFBIZ_FILE`, `CONTEXT_FILE`) |
| `getDataResourceMimeType(delegator, dataResourceId, view)` | Ermittelt den MIME-Typ einer DataResource |
| `getDataCategoryMap(delegator, depth, categoryNode, categoryTypeIds, getAll)` | Baut eine hierarchische Datenkategorie-Baumstruktur auf |
| `getDataCategoryAncestry(delegator, dataCategoryId, categoryTypeIds)` | Traversiert Datenkategorie-Vorfahren rekursiv |
| `clearAssociatedRenderCache(delegator, dataResourceId)` | Invalidiert alle Render-Caches, die mit einer DataResource verknüpft sind |
| `buildList(nd, lst, depth)` | Flacht einen Kategorie-Baum mit Einrückung in eine lineare Liste um |

---

### Klasse: `DataServices`

**Paket:** `org.apache.ofbiz.content.data`
**Typ:** Java-Klasse (Service-Engine-Dispatcher)
**Zweck:** Stellt CRUD-Dienste für DataResource-Objekte und ihre assoziierten Datentypen (elektronische Texte, Dateien, Bilder, Binärdaten) bereit. Validiert Datei-Uploads sicherheitstechnisch via `SecuredUpload`.

| Methode | Beschreibung |
|---|---|
| `createDataResource(dctx, context)` | Legt eine neue DataResource an, setzt fehlenden Status automatisch auf den ersten verfügbaren Content-Status |
| `createDataResourceAndText(dctx, context)` | Legt DataResource und zugehörigen elektronischen Text in einem Schritt an |
| `createElectronicText(dctx, context)` | Legt einen `ElectronicText`-Datensatz mit Textinhalt an |
| `createFile(dctx, context)` | Schreibt Text- oder Binärdaten in eine Datei; validiert den Dateipfad und -typ |
| `createFileNoPerm(dctx, context)` | Datei-Erstellung ohne Berechtigungsprüfung, aber mit Sicherheitsvalidierung via `SecuredUpload` |
| `createImage(dctx, context)` | Speichert Bilddaten als `ImageDataResource`-Datenbankdatensatz |
| `createBinaryFile(dctx, context)` | Schreibt Binärdaten in eine Datei auf dem Dateisystem, validiert das Format |
| `updateDataResource(dctx, context)` | Aktualisiert Metadaten einer bestehenden DataResource |
| `updateDataResourceAndText(dctx, context)` | Aktualisiert DataResource und zugehörigen elektronischen Text |
| `updateElectronicText(dctx, context)` | Aktualisiert oder legt neu an: den Textinhalt eines `ElectronicText`-Datensatzes |
| `updateFile(dctx, context)` | Überschreibt den Inhalt einer vorhandenen Datei (Text oder Binär) |
| `updateImage(dctx, context)` | Aktualisiert Bilddaten in `ImageDataResource`; legt neu an falls nicht vorhanden |
| `updateBinaryFile(dctx, context)` | Überschreibt eine Binärdatei auf dem Dateisystem |
| `renderDataResourceAsText(dctx, context)` | Service-Endpunkt: rendert eine DataResource als Text in den outWriter |
| `clearAssociatedRenderCache(dctx, context)` | Service-Endpunkt: invalidiert den Render-Cache einer DataResource |

---

### FTP-Integration: Pakete `org.apache.ofbiz.content.ftp`

Das FTP-Submodul stellt eine erweiterbare, protokoll-abstrakte Schnittstelle für Dateiübertragungen bereit. Es unterstützt einfaches FTP und SFTP; FTPS ist als Platzhalter vorhanden.

---

### Klasse: `FtpClientInterface`

**Paket:** `org.apache.ofbiz.content.ftp`
**Typ:** Java-Interface
**Zweck:** Gemeinsame Abstraktion aller FTP-Client-Implementierungen; definiert Verbinden, Kopieren, Auflisten und Verbindungsmanagement.

| Methode | Beschreibung |
|---|---|
| `connect(hostname, username, password, port, timeout)` | Baut die Verbindung zum FTP/SFTP-Server auf |
| `copy(path, fileName, inputStream)` | Überträgt eine Datei aus einem InputStream in das Remote-Verzeichnis |
| `list(path)` | Gibt die Dateinamen im angegebenen Remote-Verzeichnis zurück |
| `setBinaryTransfer(isBinary)` | Schaltet den Übertragungsmodus zwischen binär und ASCII um |
| `setPassiveMode(isPassive)` | Aktiviert oder deaktiviert den passiven FTP-Modus |
| `closeConnection()` | Schließt die Verbindung und meldet sich ab |

---

### Klasse: `SimpleFtpClient`

**Paket:** `org.apache.ofbiz.content.ftp`
**Typ:** Java-Klasse (implementiert `FtpClientInterface`)
**Zweck:** FTP-Client auf Basis von `org.apache.commons.net.ftp.FTPClient`. Verbindet sich mit Standard-FTP-Servern, überträgt Dateien und unterstützt aktiven/passiven Modus sowie binäre und ASCII-Übertragung.

---

### Klasse: `SshFtpClient`

**Paket:** `org.apache.ofbiz.content.ftp`
**Typ:** Java-Klasse (implementiert `FtpClientInterface`)
**Zweck:** SFTP-Client auf Basis von Apache MINA SSHD (`org.apache.sshd`). Verbindet sich per SSH/Password-Auth, erstellt eine SFTP-Session und überträgt Dateien via SFTP-Protokoll. Nutzt eine Singleton-SSH-Client-Instanz über `SshClientHelper`.

| Methode | Beschreibung |
|---|---|
| `connect(hostname, username, password, port, timeout)` | Baut SSH-Session auf, authentifiziert per Passwort und öffnet SFTP-Client |
| `copy(path, fileName, inputStream)` | Schreibt Dateiinhalt per SFTP in das Remote-Verzeichnis |
| `list(path)` | Listet Dateien eines Remote-Verzeichnisses via SFTP `readDir` |
| `closeConnection()` | Schließt SFTP-Session und SSH-Session |

---

### Klasse: `SshClientHelper`

**Paket:** `org.apache.ofbiz.content.ftp`
**Typ:** Java-Klasse (abstrakt, Singleton-Factory)
**Zweck:** Verwaltet eine gemeinsam genutzte, gestartete `SshClient`-Instanz mit konfigurierten Key-Exchange-Algorithmen und Signatur-Factories. Verhindert mehrfache Client-Initialisierungen.

---

### Klasse: `SecureFtpClient`

**Paket:** `org.apache.ofbiz.content.ftp`
**Typ:** Java-Klasse (implementiert `FtpClientInterface`)
**Zweck:** Platzhalter für FTPS-Unterstützung (FTP über TLS/SSL). Alle Methoden sind leer implementiert; FTPS wird laut `FtpServices` noch nicht unterstützt.

---

### Klasse: `FtpServices`

**Paket:** `org.apache.ofbiz.content.ftp`
**Typ:** Java-Klasse (Service-Engine-Dispatcher)
**Zweck:** OFBiz-Service zum Versenden von Content-Daten via FTP oder SFTP an eine über `FtpAddress`-ContactMech konfigurierte Gegenstelle. Unterstützt optionale ZIP-Komprimierung, konfigurierbares Umleitungs-Ziel und optionale Transfer-Verifikation.

| Methode | Beschreibung |
|---|---|
| `sendContentToFtp(dctx, context)` | Lädt einen Content-Datenstrom (aus DataResource) auf einen FTP/SFTP-Server; unterstützt ZIP-Komprimierung, Redirect-Konfiguration und optionale Transfer-Verifikation durch Re-Login und Verzeichnis-Listing |

---

### Klasse: `SurveyWrapper`

**Paket:** `org.apache.ofbiz.content.survey`
**Typ:** Java-Klasse
**Zweck:** Kapselt die Darstellung und Auswertung von OFBiz-Umfragen (`Survey`). Rendert Fragebögen via FreeMarker-Templates, lädt Antworten und berechnet Ergebnis-Statistiken (Boolean, Zahlen, Text, Optionslisten).

| Methode | Beschreibung |
|---|---|
| `render(templateUrl)` | Rendert die Umfrage mit dem angegebenen FreeMarker-Template in einen Writer |
| `render(url, writer)` | Rendert die Umfrage direkt in einen übergebenen Writer |
| `getSurvey()` | Lädt den Survey-GenericValue aus der Datenbank |
| `getSurveyQuestionAndAppls()` | Gibt alle Fragen der Umfrage mit ihren Anwendungs-Einstellungen zurück |
| `getResponseAnswers(responseId)` | Lädt alle Antworten einer bestimmten Survey-Response |
| `getSurveyResponses(surveyQuestion)` | Gibt alle Antworten zu einer bestimmten Frage zurück |
| `getQuestionResponses(question, startIndex, number)` | Gibt paginierte Antworten zu einer Frage zurück |
| `getNumberResponses()` | Gibt die Gesamtanzahl von Antworten auf die Umfrage zurück |
| `getResults(questions)` | Berechnet Ergebnis-Statistiken für alle Fragen der Umfrage |
| `getResultInfo(question)` | Berechnet Statistik für eine einzelne Frage (Typ-abhängig: Boolean, Zahl, Text, Option) |
| `setEdit(edit)` | Schaltet den Bearbeitungsmodus ein (ermöglicht Antwort-Bearbeitung) |

---

### Klasse: `PdfSurveyServices`

**Paket:** `org.apache.ofbiz.content.survey`
**Typ:** Java-Klasse (Service-Engine-Dispatcher)
**Zweck:** Ermöglicht den Import von PDF-AcroForms als OFBiz-Umfragen und den Export von Umfrage-Antworten zurück in PDF-Formulare. Nutzt die iText/LoWaGie PDF-Bibliothek.

| Methode | Beschreibung |
|---|---|
| `buildSurveyFromPdf(dctx, context)` | Analysiert ein PDF-AcroForm-Dokument, legt eine neue `Survey` an und erstellt `SurveyQuestion`-Datensätze für jedes Formularfeld |
| `getFilledInSurveyAsPdf(dctx, context)` | Füllt ein PDF-Formular mit gespeicherten Umfrage-Antworten aus und gibt das gefüllte PDF zurück |

---

### Klasse: `SurveyEvents`

**Paket:** `org.apache.ofbiz.content.survey`
**Typ:** Java-Klasse (Web-Event-Handler)
**Zweck:** Verarbeitet Web-Events für Survey-Antworten im HTTP-Request-Kontext.

| Methode | Beschreibung |
|---|---|
| `createSurveyResponseAndRestoreParameters(request, response)` | Speichert eine Umfrage-Antwort via `createSurveyResponse`-Service und stellt ggf. zuvor gespeicherte Request-Parameter wieder her |

---

### Klasse: `BlogRssServices`

**Paket:** `org.apache.ofbiz.content.blog`
**Typ:** Java-Klasse (Service-Engine-Dispatcher)
**Zweck:** Generiert RSS-Feeds für OFBiz-Blogs. Sammelt veröffentlichte Blog-Artikel (PUBLISH_LINK-Assoziationen mit Status CTNT_PUBLISHED), rendert deren Summary-Sub-Content und baut einen ROME-SyndFeed auf.

| Methode | Beschreibung |
|---|---|
| `generateBlogRssFeed(dctx, context)` | Erstellt einen RSS-/Atom-Feed für einen Blog-Content-Eintrag; Feedtyp, Links und Titel werden aus dem Blog-Content übernommen |
| `generateEntryList(dispatcher, delegator, contentId, entryLink, locale, userLogin)` | Lädt alle veröffentlichten Artikel eines Blogs, rendert deren SUMMARY-Sub-Content als Text und erstellt `SyndEntry`-Objekte |

---

### Klasse: `ContentSearch`

**Paket:** `org.apache.ofbiz.content.content`
**Typ:** Java-Klasse (Suchmaschine)
**Zweck:** Implementiert eine strukturierte Volltextsuche über Content-Objekte mit konfigurierbaren Suchconstraints und Sortieroptionen. Nutzt dynamische Datenbankabfragen via `DynamicViewEntity`.

| Methode | Beschreibung |
|---|---|
| `searchContents(contentSearchConstraintList, resultSortOrder, delegator, visitId)` | Führt eine strukturierte Content-Suche mit beliebigen Constraint-Kombinationen durch und gibt eine Liste von Content-IDs zurück |
| `getAllSubContentIds(contentId, contentIdSet, delegator, nowTimestamp)` | Sammelt rekursiv alle Sub-Content-IDs eines Eltern-Contents (für Hierarchie-Suche) |

Innere Klassen: `ContentSearchContext` (Suchausführung), `ContentSearchConstraint` (abstrakte Basis), `KeywordConstraint` (Keyword-Suche), `ContentAssocConstraint` (Assoziations-Filter), `LastUpdatedRangeConstraint` (Zeitraum-Filter), `ResultSortOrder` (abstrakt), `SortContentField` (Feldbasierte Sortierung), `SortKeywordRelevancy` (Relevanz-Sortierung).

---

### Klasse: `ContentSearchSession`

**Paket:** `org.apache.ofbiz.content.content`
**Typ:** Java-Klasse (Session-Manager)
**Zweck:** Speichert und verwaltet Content-Suchanfragen im HTTP-Session-Kontext; hält Constraint-Listen, Sortieroptionen und Such-Historien.

| Methode | Beschreibung |
|---|---|
| `getContentSearchOptions(session)` | Lädt oder erstellt die aktuellen Suchoptionen aus der Session |
| `searchAddConstraint(constraint, session)` | Fügt einen neuen Suchfilter zur aktuellen Suche hinzu |
| `searchSetSortOrder(sortOrder, session)` | Setzt die Sortierreihenfolge für die aktuelle Suche |
| `getSearchOptionsHistoryList(session)` | Gibt die Liste vergangener Suchanfragen in der Session zurück |

---

### Klasse: `ContentMapFacade`

**Paket:** `org.apache.ofbiz.content.content`
**Typ:** Java-Klasse (implementiert `Map<Object, Object>`)
**Zweck:** Stellt Content-Daten als Map für FreeMarker-Templates bereit. Ermöglicht lazy-geladenen Zugriff auf Content-Felder, Sub-Content, DataResource-Daten und Metadaten direkt aus Templates heraus (`thisContent.fields`, `thisContent.subContent`, `thisContent.dataResource`).

---

### Klasse: `ContentPermissionServices`

**Paket:** `org.apache.ofbiz.content.content`
**Typ:** Java-Klasse (Service-Engine-Dispatcher)
**Zweck:** Implementiert rollenbasierte Berechtigungsprüfungen für Content-Operationen. Prüft Ziel-Operationen gegen Content-Rollen und -Zwecke mit Unterstützung für detaillierte Fehlerprotokollierung via `PermissionRecorder`.

| Methode | Beschreibung |
|---|---|
| `checkContentPermission(dctx, context)` | Prüft Berechtigungen für eine Content-Operation; veraltet, wird von `genericContentPermission` abgelöst |
| `checkAssocPermission(dctx, context)` | Prüft Berechtigungen für Content-Assoziations-Operationen |

---

### Klasse: `PermissionRecorder`

**Paket:** `org.apache.ofbiz.content.content`
**Typ:** Java-Klasse
**Zweck:** Protokolliert den Verlauf von Berechtigungsprüfungen detailliert für Debug-Zwecke; kann das Prüfprotokoll als HTML ausgeben.

---

### Klasse: `ContentWrapper`

**Paket:** `org.apache.ofbiz.content.content`
**Typ:** Java-Interface
**Zweck:** Definiert das Contract für Content-Wrapper-Implementierungen in anderen Modulen (Order, Party, Product, WorkEffort). Stellt statische Hilfsmethoden für MIME-Typ-Ermittlung, Feld-Wert-Suche und HTML-Encoding bereit.

| Methode | Beschreibung |
|---|---|
| `get(contentTypeId, encoderType)` | Liefert den lokalisierten Content-Wert für einen Content-Typ als HTML-sicherer `StringWrapper` |
| `getDefaultMimeTypeId(delegator)` | Gibt den konfigurierten Standard-MIME-Typ aus `content.properties` zurück |
| `getCandidateFieldValue(modelObject, contentTypeId)` | Sucht einen Feldwert direkt im Entity-Objekt wenn das Feld vorhanden ist |
| `encodeContentValue(value, encoderType)` | Bereinigt einen Content-Wert mit dem angegebenen Encoder-Typ |

---

### Klasse: `ContentUrlFilter`

**Paket:** `org.apache.ofbiz.content.content`
**Typ:** Java-Klasse (implementiert `javax.servlet.Filter`)
**Zweck:** Servlet-Filter der alternative Content-URLs (mit Suffix `-content`) auf die echte Content-ID auflöst und die Anfrage intern weiterleitet. Ermöglicht SEO-freundliche URLs für Content-Objekte.

---

### Klasse: `ContentKeywordIndex`

**Paket:** `org.apache.ofbiz.content.content`
**Typ:** Java-Klasse (Suchindex-Builder)
**Zweck:** Indexiert Schlüsselwörter eines Content-Objekts für die Volltext-Suche. Extrahiert Keywords aus Content-ID, Name, Beschreibung, Attributen, Metadaten und dem gerenderten DataResource-Text.

| Methode | Beschreibung |
|---|---|
| `indexKeywords(content)` | Indexiert Schlüsselwörter eines Content-Eintrags; überspringt bereits indexierte |
| `forceIndexKeywords(content)` | Erzwingt Neu-Indexierung unabhängig vom vorhandenen Index |

---

### Klasse: `OutputServices`

**Paket:** `org.apache.ofbiz.content.output`
**Typ:** Java-Klasse (Service-Engine-Dispatcher)
**Zweck:** Rendert OFBiz-Screens via Apache FOP zu PDF oder XSL-FO und sendet das Ergebnis an einen Drucker oder speichert es als Datei. Integriert sich in das Widget-Framework für Screen-Rendering.

| Methode | Beschreibung |
|---|---|
| `createAsciiDoc(dctx, context)` | Erstellt ein AsciiDoc-Dokument aus einem Screen-Widget-Rendering |
| `createPdf(dctx, context)` | Rendert einen Screen als PDF via FOP; kann die Ausgabe als Datei speichern oder in einen Output-Stream schreiben |
| `sendPdfToPrinter(dctx, context)` | Sendet ein gerendertes PDF an einen konfigurierten Netzwerkdrucker via Java Print Service |

---

### Klasse: `LayoutWorker`

**Paket:** `org.apache.ofbiz.content.layout`
**Typ:** Java-Klasse (Utility, final)
**Zweck:** Hilfsmethoden für den Upload und die Verarbeitung von Bild- und Formulardaten im Layout-Kontext.

| Methode | Beschreibung |
|---|---|
| `uploadImageAndParameters(request, uploadField)` | Verarbeitet Multipart-Datei-Upload und Formularparameter; gibt Bild-Bytes und Formularfelder als Map zurück |

---

### Klasse: `SimpleContentViewHandler`

**Paket:** `org.apache.ofbiz.content.view`
**Typ:** Java-Klasse (extends `AbstractViewHandler`)
**Zweck:** View-Handler für die direkte Auslieferung von Content-Objekten als HTTP-Response. Rendert Content via `ContentWorker.renderContentAsText` und schreibt das Ergebnis in den HTTP-Response-Stream.

---

### FreeMarker-Transformationen: Paket `org.apache.ofbiz.content.webapp.ftl`

Alle Klassen dieses Pakets implementieren `freemarker.template.TemplateTransformModel` und stellen FreeMarker-Direktiven bereit, die in `.ftl`-Templates genutzt werden können. Sie ermöglichen das Rendering von Content-Hierarchien direkt aus Templates.

| Klasse | FreeMarker-Direktive | Funktion |
|---|---|---|
| `RenderContentTransform` | `@ofbizContentTransform` | Rendert einen einzelnen Content-Eintrag |
| `RenderContentAsText` | (Text-Variante) | Rendert Content direkt als Klartext |
| `RenderContentAndSubContent` | (kombiniert) | Rendert Content und seinen Sub-Content |
| `RenderSubContentTransform` | `@renderSubContent` | Rendert einen Sub-Content über mapKey |
| `RenderSubContentCacheTransform` | (Cache-Variante) | Wie `RenderSubContentTransform` mit Caching |
| `RenderSubContentAsText` | (Text-Variante) | Rendert Sub-Content als Text |
| `EditRenderSubContentTransform` | (Edit-Variante) | Rendert Sub-Content im Bearbeitungsmodus |
| `EditRenderSubContentCacheTransform` | (Edit+Cache) | Wie Edit-Variante mit Caching |
| `TraverseSubContentTransform` | `@traverseSubContent` | Traversiert Sub-Content-Baum iterativ |
| `TraverseSubContentCacheTransform` | (Cache-Variante) | Traversal mit Caching |
| `LoopSubContentTransform` | `@loopSubContent` | Schleife über alle Sub-Contents |
| `LimitedSubContentCacheTransform` | `@limitedSubContent` | Begrenzte Sub-Content-Schleife mit Caching |
| `WrapSubContentCacheTransform` | `@wrapSubContent` | Umhüllt Sub-Content mit Template-Block |
| `InjectNodeTrailCsvTransform` | `@injectNodeTrailCsv` | Injiziert CSV-Node-Trail in Template-Kontext |
| `CheckPermissionTransform` | `@checkPermission` | Bedingte Ausgabe abhängig von Content-Berechtigung |
| `OfbizContentAltUrlTransforms` | `@ofbizContentAltUrl` | Generiert alternative (SEO-freundliche) URLs für Content |

---

### Groovy-Scripts: Gruppiert nach Funktion

**Typ:** Groovy-Script (extends `groovy.lang.Script`) — kein Java-Quelltext verfügbar

#### CMS-Preparer (`org.apache.ofbiz.content.cms`)

Diese Scripts bereiten Daten für CMS-Verwaltungsseiten vor:

| Klasse | Funktion |
|---|---|
| `CmsEditAddPrep` | Bereitet den Edit/Add-Kontext für CMS-Content-Objekte vor |
| `FeaturePrep` | Bereitet Featured-Content-Daten für die Darstellung auf |
| `GetMenuContext` | Lädt Navigationsmenü-Kontextdaten für CMS-Views |
| `MostRecentPrep` | Ermittelt die zuletzt bearbeiteten/erstellten Contents |
| `UserPermPrep` | Bereitet Benutzerberechtigungsdaten für CMS-Views auf |

#### Content-Verwaltungs-Scripts (`org.apache.ofbiz.content.content`)

| Klasse | Funktion |
|---|---|
| `ContentServicesScript` | Groovy-basierte Content-Services (Ergänzung zu `ContentServices.java`) |
| `ContentSearchOptions` | Script zum Verwalten von Suchoptionen in der Session |
| `ContentSearchResults` | Script zur Darstellung von Content-Suchergebnissen |
| `GetContentLookupList` | Lädt eine Liste von Contents für Lookup-Komponenten |
| `PrepSeqNo` | Bereitet Sequenznummern für Content-Assoziationen vor |

#### Data-Scripts (`org.apache.ofbiz.content.data`)

| Klasse | Funktion |
|---|---|
| `DataServicesScript` | Groovy-basierte DataResource-Services |

#### Survey-Scripts (`org.apache.ofbiz.content.survey`)

| Klasse | Funktion |
|---|---|
| `EditSurveyQuestions` | Verwaltet die Bearbeitung von Umfragefragen |
| `EditSurveyResponse` | Verwaltet die Bearbeitung von Umfrage-Antworten |
| `ViewSurveyResponses` | Bereitet Survey-Antworten für die Anzeige auf |

#### Website-Scripts (`org.apache.ofbiz.content.website`)

| Klasse | Funktion |
|---|---|
| `EditWebSiteParties` | Verwaltet Parties (Rollen) einer Website |
| `WebSiteCMSMetaInfo` | Verwaltet CMS-Metainformationen einer Website |
| `WebSitePublishPoint` | Verwaltet Website-Publish-Points |

#### Sonstige Scripts

| Klasse | Paket | Funktion |
|---|---|---|
| `BlogServices` | `org.apache.ofbiz.content` | Groovy-basierte Blog-Services |
| `ContentPermissionServices` | `org.apache.ofbiz.content.permission` | Berechtigungsprüfung via Groovy |
| `FindPrinters` | `org.apache.ofbiz.content.print` | Sucht verfügbare Netzwerkdrucker |
| `EditSubContent` | `org.apache.ofbiz.content.layout` | Bearbeitung von Layout-Sub-Contents |
| `UserPermPrep` | `org.apache.ofbiz.content.contentsetup` | Setup: Benutzerberechtigungs-Vorbereitung |
| `DataCategoryPrep` | `org.apache.ofbiz.content.datasetup` | Setup: Datenkategorie-Initialisierung |

---

### Tests

**Typ:** Groovy-OFBiz-Testklasse (`extends OFBizTestCase implements GroovyObject`)

| Klasse | Paket | Inhalt |
|---|---|---|
| `ContentTests` | `org.apache.ofbiz.content.content` | Integrationstests für Content-Services und Worker-Funktionalität |

---

### Weitere Java-Klassen

| Klasse | Paket | Typ | Beschreibung |
|---|---|---|---|
| `ContentEvents` | `.content.content` | Java | HTTP-Event-Handler für Content-bezogene Web-Requests (Upload, CRUD-Events) |
| `ContentSearchEvents` | `.content.content` | Java | HTTP-Event-Handler für Content-Suchanfragen |
| `ContentServicesComplex` | `.content.content` | Java | Komplex-Abfragen für Content-Assoziationen mit DataResource-Join (genutzt von `ContentWorker`) |
| `UploadContentAndImage` | `.content.content` | Java | Event-Handler für kombinierte Content+Bild-Uploads |
| `ContentManagementEvents` | `.content` | Java | HTTP-Event-Handler für Content-Management-UI-Aktionen |
| `ConvertTree` | `.content` | Java | Hilfsmethoden zur Konvertierung von Content-Baumstrukturen |
| `DataEvents` | `.content.data` | Java | HTTP-Event-Handler für DataResource-bezogene Web-Requests |
| `CmsEvents` | `.content.cms` | Java | HTTP-Event-Handler für CMS-UI-Aktionen |
| `ContentJsonEvents` | `.content.cms` | Java | HTTP-Event-Handler für JSON-basierte CMS-API-Endpunkte |
| `LayoutEvents` | `.content.layout` | Java | HTTP-Event-Handler für Layout-bezogene Aktionen |
