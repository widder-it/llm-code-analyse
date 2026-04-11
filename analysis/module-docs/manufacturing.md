## Modul: manufacturing

### Überblick

Das `manufacturing`-Modul implementiert die gesamte Fertigungslogik in Apache OFBiz: von der Stücklisten-Verwaltung (Bill of Materials) über die Materialbedarfsplanung (MRP) bis zur Steuerung von Fertigungsaufträgen (Production Runs). Es bildet den Kern für produzierende Unternehmen und verzahnt Lagerbestände, Verkaufsbedarfe, Einkaufsbestellungen und Produktionskapazitäten zu einem integrierten Planungssystem.

### Submodule

| Paket | Beschreibung |
|---|---|
| `org.apache.ofbiz.manufacturing.bom` | Stücklisten (Bill of Materials): Baumstruktur aus Produktkomponenten, Konfigurations- und Substitutionslogik, BOM-Dienste |
| `org.apache.ofbiz.manufacturing.jobshopmgt` | Fertigungsaufträge (Job Shop Management): Anlage, Statusverwaltung, Aufgabensteuerung, Kostenerfassung |
| `org.apache.ofbiz.manufacturing.mrp` | Materialbedarfsplanung (MRP): Ereignisinitialisierung, Nettobedarfsermittlung, Planungsauftragsvorschläge |
| `org.apache.ofbiz.manufacturing.routing` | Arbeitspläne und Arbeitsplatzkalender: Zeitermittlung, Kalenderprüfung |
| `org.apache.ofbiz.manufacturing.techdata` | Technische Stammdaten: Kapazitätskalender, Vorwärts-/Rückwärtsterminierung |
| `org.apache.ofbiz.manufacturing.reports` | Berichte zu Fertigungsaufträgen, Versandplänen, Produktmerkmalen (Groovy-Scripts) |

---

### Klasse: `BOMNode`
**Paket:** `org.apache.ofbiz.manufacturing.bom`
**Typ:** Java-Klasse
**Zweck:** Repräsentiert einen einzelnen Knoten in einer Stücklistenstruktur. Jeder Knoten kapselt ein Produkt mit seiner Menge, dem Ausschussfaktor und der Verknüpfung zu Eltern- und Kindknoten. Enthält die Konfigurations- und Substitutionslogik für virtuelle Produkte und Varianten.

| Methode | Beschreibung |
|---|---|
| `loadChildren(partBomTypeId, inDate, productFeatures, type)` | Lädt rekursiv die Unterkomponenten aus `ProductAssoc` für den gegebenen Stücklistentyp und Stichtag; bei virtuellen Produkten werden Fertigungsregeln (`ProductManufacturingRule`) ausgewertet und ggf. Ersatzartikel eingesetzt |
| `loadParents(partBomTypeId, inDate, productFeatures)` | Lädt die übergeordneten Produkte (Implosionsrichtung) für die Verwendungsnachweis-Analyse |
| `print(arr, quantity, depth, excludeWIPs)` | Traversiert den Teilbaum und schreibt alle Knoten mit berechneten Mengen in eine flache Liste; optionaler Ausschluss von WIP-Produkten; ruft bei konfigurierten Kalkulationsmethoden einen Custom-Service zur Mengenberechnung auf |
| `getProductsInPackages(arr, quantity, depth, excludeWIPs)` | Sammelt alle Knoten, denen ein Standard-Versandkarton (`defaultShipmentBoxTypeId`) zugewiesen ist, für die Verpackungsplanung |
| `sumQuantity(nodes)` | Aggregiert Mengen gleichartiger Produkte in einer Map für die Gesamtbedarfsermittlung |
| `createManufacturingOrder(facilityId, date, ...)` | Erzeugt rekursiv Fertigungsaufträge für den gesamten Teilbaum; verknüpft untergeordnete mit übergeordneten Aufträgen als Vorgänger-Nachfolger-Beziehung (`WORK_EFF_PRECEDENCY`) |
| `getStartDate(facilityId, requiredBydate, allNodes)` | Berechnet das frühestmögliche Startdatum durch Rückwärtsterminierung über den gesamten Komponentenbaum |
| `isWarehouseManaged(facilityId)` | Prüft, ob das Produkt lagergesteuert ist (Mindestbestand und Bestellmenge in `ProductFacility` vorhanden) |
| `isManufactured(ignoreSupplierProducts)` | Gibt `true` zurück, wenn das Produkt Unterkomponenten besitzt und kein bevorzugter Lieferant (`10_MAIN_SUPPL`) hinterlegt ist |
| `isVirtual()` | Prüft, ob das Produkt virtuell ist (Auslöser für Konfigurationslogik) |
| `isConfigured(arr)` | Sammelt alle virtuellen Knoten, die noch nicht konfiguriert (d.h. noch nicht durch eine Variante ersetzt) sind |

---

### Klasse: `BOMTree`
**Paket:** `org.apache.ofbiz.manufacturing.bom`
**Typ:** Java-Klasse
**Zweck:** Kapselt eine vollständige Stücklistenstruktur für ein Produkt. Unterstützt vier Traversierungstypen: vollständige Explosion (EXPLOSION), einstufige Explosion (EXPLOSION_SINGLE_LEVEL), Fertigungsexplosion ohne lagergesteuerte Teile (EXPLOSION_MANUFACTURING) und Implosion (IMPLOSION, für Verwendungsnachweise). Beim Aufbau werden automatisch Produkt-Varianten und `PRODUCT_MANUFACTURED`-Assoziationen aufgelöst.

| Methode | Beschreibung |
|---|---|
| `isConfigured()` | Gibt `true` zurück, wenn der Baum keine unkonfigurierten virtuellen Knoten enthält |
| `print(arr, initialDepth, excludeWIPs)` | Traversiert den Baum und befüllt eine flache Liste aller Komponenten-Knoten mit berechneten Mengen |
| `sumQuantities(quantityPerNode)` | Summiert die Gesamtmengen je Produkt über den gesamten Baum |
| `getAllProductsId()` | Gibt eine Liste aller Produkt-IDs im Baum zurück |
| `createManufacturingOrders(facilityId, date, ...)` | Löst die rekursive Fertigungsauftrags-Erzeugung für den gesamten Baum aus; ermittelt das Lager aus dem Auftrag oder der Lieferung, falls nicht direkt angegeben |
| `getProductsInPackages(arr)` | Liefert alle Knoten mit Versandkarton-Zuordnung für die Verpackungsplanung |

---

### Klasse: `BOMServices`
**Paket:** `org.apache.ofbiz.manufacturing.bom`
**Typ:** Java-Klasse
**Zweck:** Service-Fassade für alle stücklistenbezogenen Operationen. Stellt OFBiz-Services bereit, die über den Service-Dispatcher aufgerufen werden und intern `BOMTree` und `BOMNode` nutzen.

| Methode | Beschreibung |
|---|---|
| `getMaxDepth(dctx, context)` | Ermittelt die maximale Tiefe eines Produkts in allen oder einem bestimmten Stücklistentyp; Grundlage für die Low-Level-Code-Berechnung im MRP |
| `updateLowLevelCode(dctx, context)` | Aktualisiert den `billOfMaterialLevel` eines Produkts sowie optional aller Komponenten und Varianten; steuert die Verarbeitungsreihenfolge im MRP |
| `initLowLevelCode(dctx, context)` | Setzt den Low-Level-Code für alle Produkte im System neu; initialisiert MRP-Voraussetzungen bei Ersteinrichtung |
| `searchDuplicatedAncestor(dctx, context)` | Prüft, ob das Einfügen einer Stücklistenposition zu einem Zirkelschluss führen würde; verhindert zyklische Stücklisten |
| `getBOMTree(dctx, context)` | Erstellt einen `BOMTree` für ein Produkt und gibt ihn als Service-Ergebnis zurück; unterstützt alle Traversierungstypen |
| `getManufacturingComponents(dctx, context)` | Explodiert die Stückliste einstufig und liefert eine flache Liste der Fertigungskomponenten sowie die zugehörige Routing-ID |
| `getNotAssembledComponents(dctx, context)` | Liefert alle Komponenten aus der Fertigungsexplosion, die selbst nicht produziert werden (Kaufteile) |
| `getProductsInPackages(dctx, context)` | Ermittelt die Verpackungseinheiten eines Produkts anhand der BOM-Struktur |
| `createShipmentPackages(dctx, context)` | Erzeugt Lieferpackstücke für eine Lieferung auf Basis der Stücklistenstruktur und der Versandkarton-Abmessungen der Artikel |

---

### Klasse: `BOMHelper`
**Paket:** `org.apache.ofbiz.manufacturing.bom`
**Typ:** Java-Klasse (final, nicht instanziierbar)
**Zweck:** Interne Hilfsklasse für Stücklistenoperationen. Stellt rekursive Algorithmen zur Tiefenermittlung und Zirkelerkennung bereit sowie einen HTTP-Event-Handler zur Produktionsauftrags-Anlage für eine Lieferung.

| Methode | Beschreibung |
|---|---|
| `getMaxDepth(productId, bomType, inDate, delegator)` | Berechnet rekursiv die maximale Stücklistentiefe eines Produkts durch Traversierung der `ProductAssoc`-Hierarchie nach oben |
| `searchDuplicatedAncestor(productId, productIdKey, bomType, inDate, ...)` | Sucht rekursiv nach Zyklen in der Stückliste, indem geprüft wird, ob ein zukünftiger Elternknoten bereits im Teilbaum des einzufügenden Knotens vorkommt |
| `createProductionRunsForShipment(request, response)` | HTTP-Event-Handler: Legt für alle Positionen einer Lieferung automatisch Fertigungsaufträge an, sofern noch keine vorhanden sind |

---

### Klasse: `BomSimulation` / `EditProductBom` / `FindProductBom`
**Paket:** `org.apache.ofbiz.manufacturing.bom`
**Typ:** Groovy-Script
**Zweck:** View-Scripts für die BOM-Verwaltungsoberfläche. `FindProductBom` stellt Suchergebnisse für Stücklistenpositionen bereit, `EditProductBom` verarbeitet Formulardaten zum Anlegen und Bearbeiten von BOM-Positionen, `BomSimulation` unterstützt die interaktive Simulation von Stücklistenexplosionen.

---

### Klasse: `ProductionRun`
**Paket:** `org.apache.ofbiz.manufacturing.jobshopmgt`
**Typ:** Java-Klasse
**Zweck:** Domänenobjekt für einen Fertigungsauftrag (`WorkEffort` vom Typ `PROD_ORDER_HEADER`). Kapselt den gesamten Fertigungsauftrag mit seinen Aufgaben (`PROD_ORDER_TASK`) und Stücklistenkomponenten, berechnet Termin- und Mengenänderungen und persistiert Änderungen transaktionssicher in einem einzigen `store()`-Aufruf.

| Methode | Beschreibung |
|---|---|
| `exist()` | Prüft, ob der Fertigungsauftrag in der Datenbank existiert |
| `store()` | Persistiert alle geänderten Felder des Fertigungsauftrags, der Aufgaben und der Komponenten; berechnet vor dem Speichern ggf. den Fertigstellungstermin neu |
| `getProductProduced()` | Lädt das Zielprodukt des Fertigungsauftrags aus der `WorkEffortGoodStandard`-Relation (`PRUN_PROD_DELIV`) |
| `setQuantity(newQuantity)` | Ändert die Sollmenge und passt proportional die Komponentenmengen an; markiert den Fertigstellungstermin zur Neuberechnung |
| `recalculateEstimatedCompletionDate(priority, startDate)` | Terminiert alle Aufgaben vorwärts ab dem Startdatum unter Berücksichtigung der Arbeitszeitkalender und berechnet den neuen Fertigstellungstermin |
| `getEstimatedTaskTime(task, quantity, productId, routingId, dispatcher)` | Berechnet die Gesamtdauer einer Aufgabe (Rüst- + Ausführungszeit × Menge); ruft bei konfigurierten Methoden einen Custom-Service zur Zeitermittlung auf |
| `getProductionRunRoutingTasks()` | Liefert die Arbeitsvorgänge des Fertigungsauftrags sortiert nach Priorität |
| `getProductionRunComponents()` | Liefert alle Materialkomponenten aller Arbeitsvorgänge des Fertigungsauftrags |

---

### Klasse: `ProductionRunServices`
**Paket:** `org.apache.ofbiz.manufacturing.jobshopmgt`
**Typ:** Java-Klasse
**Zweck:** Zentrale Service-Klasse für die gesamte Lebenszyklusverwaltung von Fertigungsaufträgen. Implementiert alle CRUD-Operationen, Statusübergänge, Komponentenverwaltung und Kostenbuchungen als OFBiz-Services.

| Methode | Beschreibung |
|---|---|
| `createProductionRun(dctx, context)` | Legt einen neuen Fertigungsauftrag an: lädt das Routing, explodiert die Stückliste, erstellt den Auftragskopf (`PROD_ORDER_HEADER`), erzeugt Aufgaben mit berechneten Start- und Endterminen und verknüpft Komponenten mit den Aufgaben |
| `updateProductionRun(dctx, context)` | Ändert Menge, Starttermin, Bezeichnung oder Lager eines Fertigungsauftrags; triggert ggf. die Neuberechnung der Liefertermine für verknüpfte Aufträge |
| `cancelProductionRun(dctx, context)` | Storniert einen Fertigungsauftrag (nur im Status CREATED, DOC_PRINTED, SCHEDULED); prüft Vorgängeraufträge und setzt alle Aufgaben und Warenstandards auf CANCELLED |
| `changeProductionRunStatus(dctx, context)` | Steuert den Statusübergang des Fertigungsauftragskopfs entlang der definierten Reihenfolge: CREATED → SCHEDULED → DOC_PRINTED → RUNNING → COMPLETED → CLOSED; prüft Vorbedingungen (z.B. abgeschlossene Vorgängeraufträge) |
| `changeProductionRunTaskStatus(dctx, context)` | Steuert den Statusübergang einer einzelnen Aufgabe; verbucht bei Abschluss automatisch Aufgabenkosten (`createProductionRunTaskCosts`) und löst den Gesamtabschluss aus, wenn alle Aufgaben fertig sind |
| `getWorkEffortCosts(dctx, context)` | Ermittelt alle Kostenbuchungen (`CostComponent`) eines Arbeitsauftrags und summiert Gesamtkosten sowie Kosten ohne Materialanteil |
| `getProductionRunCost(dctx, context)` | Summiert die Kosten aller Aufgaben eines Fertigungsauftrags zum Gesamtkostenbetrag |
| `createProductionRunTaskCosts(dctx, context)` | Bucht die Ist-Kosten einer abgeschlossenen Aufgabe: Rüst- und Ausführungskosten aus Kalkulationsmethoden, Maschinenkosten aus `FixedAssetStdCost` sowie Materialkosten aus dem tatsächlichen Lagerabgang |
| `addProductionRunComponent(dctx, context)` | Fügt einem Fertigungsauftrag nachträglich eine Materialkomponente hinzu (nur vor Druckfreigabe) |
| `updateProductionRunComponent(dctx, context)` | Ändert die Sollmenge einer bestehenden Komponente eines Fertigungsauftrags |
| `addProductionRunRoutingTask(dctx, context)` | Fügt einen zusätzlichen Arbeitsvorgang in einen bestehenden Fertigungsauftrag ein und passt Termine an |
| `checkUpdatePrunRoutingTask(dctx, context)` | Prüft und aktualisiert Priorität und Zeitparameter einer Aufgabe; passt Fertigstellungstermin des Auftrags an |

---

### Klasse: `ProductionRunEvents`
**Paket:** `org.apache.ofbiz.manufacturing.jobshopmgt`
**Typ:** Java-Klasse
**Zweck:** HTTP-Event-Handler für die Produktionsrückmeldung über die Web-Oberfläche.

| Methode | Beschreibung |
|---|---|
| `productionRunDeclareAndProduce(request, response)` | Verarbeitet die Produktionsrückmeldung aus einem mehrzeiligen Formular (Menge + Lagerorte je Komponente) und ruft den Service `productionRunDeclareAndProduce` auf |

---

### Klasse: `ProductionRunHelper`
**Paket:** `org.apache.ofbiz.manufacturing.jobshopmgt`
**Typ:** Java-Klasse (final, nicht instanziierbar)
**Zweck:** Hilfsklasse für die Strukturanalyse von Fertigungsauftrags-Netzen.

| Methode | Beschreibung |
|---|---|
| `getProductionRun(delegator, productionRunId)` | Lädt einen Fertigungsauftrag mit Produkt, Komponenten und Aufgaben als Map-Struktur |
| `hasTask(delegator, taskName, workEffortId)` | Prüft, ob ein Fertigungsauftrag eine Aufgabe mit dem gegebenen Namen enthält |
| `getLinkedProductionRuns(delegator, dispatcher, productionRunId, productionRuns)` | Sammelt rekursiv alle Vorgänger-Fertigungsaufträge über `WORK_EFF_PRECEDENCY`-Verknüpfungen |
| `getRootProductionRun(delegator, productionRunId)` | Traversiert die Vorgänger-Kette und gibt die ID des übergeordneten Wurzel-Fertigungsauftrags zurück |

---

### Groovy-Scripts: Fertigungsauftrags-Ansichten (`jobshopmgt`)

**Paket:** `org.apache.ofbiz.manufacturing.jobshopmgt`
**Typ:** Groovy-Script (View-Layer)

Die folgenden Scripts bereiten Daten für die Fertigungsauftrags-Oberfläche auf:

| Script | Zweck |
|---|---|
| `ShowProductionRun` / `ViewProductionRun` | Detailansicht eines Fertigungsauftrags |
| `ProductionRunComponents` | Anzeige der Materialkomponenten eines Auftrags |
| `ProductionRunActualComponents` | Tatsächlich verbrauchte Komponenten (Ist-Daten) |
| `ProductionRunTasks` | Auflistung der Arbeitsvorgänge |
| `ProductionRunDeclaration` | Eingabemaske für die Mengenrückmeldung |
| `ProductionRunCosts` | Kostenübersicht eines Fertigungsauftrags |
| `ProductionRunContent` | Dokumente und Anhänge zum Fertigungsauftrag |
| `ProductionRunFixedAssets` / `ProductionRunAllFixedAssets` | Zugeordnete Betriebsmittel |
| `ProductionRunTaskParties` | Zugewiesene Personen je Aufgabe |
| `WorkWithShipmentPlans` | Versandplan-Übersicht mit Fertigungsauftrags-Verknüpfung |
| `ProductionRunServicesScript` | Ergänzende Service-Aufrufe im View-Kontext |

---

### Klasse: `MrpServices`
**Paket:** `org.apache.ofbiz.manufacturing.mrp`
**Typ:** Java-Klasse
**Zweck:** Implementiert den vollständigen MRP-Algorithmus (Materialbedarfsplanung) als zweiphasigen Prozess: Initialisierung der Planungsereignisse aus Verkaufsaufträgen, Einkaufsbestellungen, laufenden Fertigungsaufträgen und Absatzprognosen (Phase 1), gefolgt von der stufenweisen Nettobedarfsrechnung über alle Stücklistenstufen (Phase 2) mit automatischer Erzeugung von Planungsvorschlägen.

| Methode | Beschreibung |
|---|---|
| `initMrpEvents(ctx, context)` | Initialisiert alle MRP-Ereignisse in der `MrpEvent`-Tabelle: löscht veraltete Vorschläge, importiert Bedarfe aus Verkaufsaufträgen (`SALES_ORDER_SHIP`), genehmigten Anforderungen (`PROD_REQ_RECP`), Einkaufsbestellungen (`PUR_ORDER_RECP`), laufenden Fertigungsaufträgen (`MANUF_ORDER_REQ` / `MANUF_ORDER_RECP`) und Absatzprognosen (`SALES_FORECAST`); setzt Mindestbestandsbedarfe |
| `executeMrp(ctx, context)` | Führt den vollständigen MRP-Lauf durch: Initialisiert Ereignisse, durchläuft alle Stücklistenstufen (Low-Level-Code), berechnet je Produkt den rollierenden Lagerbestand und erzeugt bei Unterschreitung des Mindestbestands Planungsaufträge (`ProposedOrder`) als Fertigungs- oder Beschaffungsvorschlag |
| `findProductMrpQoh(mrpId, productId, facilityId, dispatcher, delegator)` | Ermittelt den verfügbaren Lagerbestand eines Produkts im Planungslager über den `getInventoryAvailableByFacility`-Service |
| `processBomComponent(mrpId, product, eventQuantity, startDate, routingTaskStartDate, listComponent)` | Erzeugt MRP-Anforderungsereignisse (`MRP_REQUIREMENT`) für alle Stücklistenkomponenten eines geplanten Fertigungsauftrags; berücksichtigt aufgabenbezogene Startzeitpunkte aus dem Routing |
| `logMrpError(mrpId, productId, eventDate, errorMessage, delegator)` | Schreibt Fehler als MRP-Ereignis des Typs `ERROR` in die Ereignistabelle |

---

### Klasse: `ProposedOrder`
**Paket:** `org.apache.ofbiz.manufacturing.mrp`
**Typ:** Java-Klasse
**Zweck:** Repräsentiert einen vom MRP erzeugten Planungsauftrag (Beschaffungs- oder Fertigungsvorschlag). Kapselt Produkt, Menge, Bedarfstermin und berechnet den Anfangstermin durch Rückwärtsterminierung über das Routing bzw. den Lieferzeitraum.

| Methode | Beschreibung |
|---|---|
| `calculateStartDate(daysToShip, routing, delegator, dispatcher, userLogin)` | Terminiert rückwärts vom Bedarfstermin: Bei Eigenfertigung werden die Routing-Aufgaben in umgekehrter Reihenfolge über den Arbeitszeitkalender terminiert; bei Fremdvergabe wird der Lieferzeitkalender (`SUPPLIER`) genutzt |
| `calculateQuantityToSupply(reorderQuantity, minimumStock, listIterIEP)` | Rundet die Planungsmenge auf die Mindestbestellmenge auf |
| `create(ctx, userLogin)` | Erzeugt eine formale Anforderung (`Requirement`) in der Datenbank mit Typ `INTERNAL_REQUIREMENT` (Eigenfertigung) oder `PRODUCT_REQUIREMENT` (Fremdbezug) und Status `REQ_PROPOSED` |

---

### Klasse: `InventoryEventPlannedServices`
**Paket:** `org.apache.ofbiz.manufacturing.mrp`
**Typ:** Java-Klasse
**Zweck:** Verwaltung der MRP-Ereignis-Tabelle (`MrpEvent`). Stellt eine atomare Upsert-Operation bereit, die beim MRP-Lauf tausendfach aufgerufen wird.

| Methode | Beschreibung |
|---|---|
| `createMrpEvent(ctx, context)` | OFBiz-Service-Wrapper für die Upsert-Operation |
| `createOrUpdateMrpEvent(mrpEventKeyMap, newQuantity, facilityId, eventName, isLate, delegator)` | Legt ein neues MRP-Ereignis an oder addiert bei bestehendem Eintrag die Menge; setzt das `isLate`-Flag, wenn der Planungsbedarf in der Vergangenheit liegt |

---

### Groovy-Script: `FindInventoryEventPlan`
**Paket:** `org.apache.ofbiz.manufacturing.mrp`
**Typ:** Groovy-Script
**Zweck:** Bereitet die MRP-Ereignisliste für die Planungsübersicht in der Web-Oberfläche auf und stellt Filter- und Sortierfunktionalität bereit.

---

### Klasse: `RoutingServices`
**Paket:** `org.apache.ofbiz.manufacturing.routing`
**Typ:** Java-Klasse
**Zweck:** Service für die Zeitermittlung von Routing-Aufgaben. Delegiert die Berechnung an `ProductionRun.getEstimatedTaskTime()`.

| Methode | Beschreibung |
|---|---|
| `getEstimatedTaskTime(ctx, context)` | Berechnet die Gesamtdauer einer Routing-Aufgabe (Rüst + Ausführung × Menge) und gibt Gesamtzeit, Rüstzeit und Stückzeit separat zurück |

---

### Groovy-Scripts: Routing-Verwaltung

**Paket:** `org.apache.ofbiz.manufacturing.routing`
**Typ:** Groovy-Script

| Script | Zweck |
|---|---|
| `RoutingServicesScript` | Ergänzende Service-Aufrufe für Routing-Verwaltungsfunktionen im View-Layer |
| `EditCalendar` | Bearbeitungsmaske für Arbeitszeitkalender |
| `EditCalendarExceptionDay` | Pflege von Ausnahmetagen im Kalender |
| `EditCalendarExceptionWeek` | Pflege von Ausnahmewochen im Kalender |

---

### Klasse: `TechDataServices`
**Paket:** `org.apache.ofbiz.manufacturing.techdata`
**Typ:** Java-Klasse
**Zweck:** Kernkomponente der Kapazitätsterminierung. Implementiert die kalenderbasierte Vorwärts- und Rückwärtsterminierung unter Berücksichtigung von Arbeitszeiten, Wochenplänen und Ausnahmen. Wird von `ProductionRun`, `ProposedOrder` und `ProductionRunServices` zur Terminberechnung verwendet.

| Methode | Beschreibung |
|---|---|
| `lookupRoutingTask(ctx, context)` | Sucht aktive Routing-Aufgaben (`ROU_TASK` / `ROU_ACTIVE`) nach Name und Betriebsmittel |
| `checkRoutingTaskAssoc(ctx, context)` | Prüft, ob eine Sequenznummer für eine Routing-Aufgabenzuordnung bereits belegt ist (Zeitraumüberschneidung) |
| `getTechDataCalendar(routingTask)` | Ermittelt den zutreffenden Arbeitszeitkalender für eine Aufgabe: primär über das zugeordnete Betriebsmittel (`FixedAsset`), sekundär über untergeordnete Maschinen, als Fallback über den `DEFAULT`-Kalender |
| `addForward(techDataCalendar, dateFrom, amount)` | Terminiert vorwärts: berechnet den Endzeitpunkt, wenn ab `dateFrom` eine Arbeitsdauer von `amount` Millisekunden verstreicht; springt dabei automatisch über arbeitsfreie Zeiten |
| `addBackward(techDataCalendar, dateFrom, amount)` | Terminiert rückwärts: berechnet den Startzeitpunkt, wenn vor `dateFrom` eine Arbeitsdauer von `amount` Millisekunden benötigt wird |
| `capacityRemaining(techDataCalendar, dateFrom)` | Gibt die verbleibende Arbeitskapazität im aktuellen Tageszeitraum ab `dateFrom` zurück |
| `capacityRemainingBackward(techDataCalendar, dateFrom)` | Gibt die bereits vergangene Arbeitskapazität im aktuellen Tageszeitraum bis `dateFrom` zurück |
| `dayStartCapacityAvailable(techDataCalendarWeek, dayStart)` | Sucht vorwärts den nächsten Arbeitstag ab `dayStart` mit positiver Kapazität |
| `dayEndCapacityAvailable(techDataCalendarWeek, dayEnd)` | Sucht rückwärts den vorherigen Arbeitstag ab `dayEnd` mit positiver Kapazität |

---

### Groovy-Scripts: Berichte (`reports`)

**Paket:** `org.apache.ofbiz.manufacturing.reports`
**Typ:** Groovy-Script (Berichts-Datenbeschaffung)

Die folgenden Scripts bereiten Daten für Druck- und Exportberichte auf:

| Script | Zweck |
|---|---|
| `CuttingListReport` | Zuschnittliste für Fertigungsaufträge |
| `PackageContentsAndOrder` | Paketinhalt mit Auftragsbezug |
| `PRunsInfoAndOrder` | Fertigungsauftrags-Übersicht mit Auftragsdaten |
| `PRunsComponentsByFeature` | Komponentenliste gefiltert nach Produktmerkmalen |
| `PRunsProductsAndOrder` | Fertigprodukte mit Auftragszuordnung |
| `PRunsProductsByFeature` | Fertigprodukte gruppiert nach Merkmalen |
| `PRunsProductsStacks` | Stapelübersicht produzierter Artikel |
| `ShipmentLabel` | Versandetiketten-Daten |
| `ShipmentPlanStockReport` | Lagerbestandsbericht für Versandplanung |
| `ShipmentWorkEffortTasks` | Aufgabenliste mit Versandbezug |
