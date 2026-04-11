## Modul: shipment

### Überblick

Das Modul `shipment` steuert den gesamten Versandprozess in Apache OFBiz — von der Erstellung und Kostenschätzung von Sendungen über das interaktive Verpacken und Gewichtserfassen bis hin zur Kommunikation mit Carrier-APIs (UPS, FedEx, DHL, USPS). Es bildet die Brücke zwischen Auftragsabwicklung und physischem Warenausgang und enthält sowohl sessionbasierte Zustandsmodelle für den Lagerarbeitsplatz als auch externe Webservice-Integrationen.

### Submodule

| Paket | Beschreibung |
|---|---|
| `org.apache.ofbiz.shipment.shipment` | Kerndienste: Kostenschätzung, Staging-Tabellen für externe Systeme, Benachrichtigungen, Gateway-Konfiguration |
| `org.apache.ofbiz.shipment.packing` | Interaktive Packsitzung: Artikel in Pakete einteilen, Reservierungen prüfen, Sendung abschließen |
| `org.apache.ofbiz.shipment.weightPackage` | Gewichtserfassung nach dem Verpacken: Pakete nachträglich mit Maßen und Gewicht versehen, optionale UPS-Echtzeittarife |
| `org.apache.ofbiz.shipment.verify` | Verifizierung gepickter Ware vor dem Versand: Mengenabgleich mit Reservierungen, Sendungserstellung |
| `org.apache.ofbiz.shipment.picklist` | Hilfsdienste für Picklisten: Auftragsheader-Konvertierung, Vollständigkeitsprüfung von Picklist-Bins |
| `org.apache.ofbiz.shipment.thirdparty.ups` | UPS-Integration: Sendungsbestätigung, Ratenabfrage, Tracking, Adressvalidierung, E-Mail-Rücksendeetiketten |
| `org.apache.ofbiz.shipment.thirdparty.fedex` | FedEx-Integration: Abonnement/Meter-Number-Registrierung, Sendungsbestätigung mit Etikettenabruf |
| `org.apache.ofbiz.shipment.thirdparty.dhl` | DHL-Integration: Ratenabfrage, Registrierung, Sendungsbestätigung mit Etikettenabruf |
| `org.apache.ofbiz.shipment.thirdparty.usps` | USPS-Integration: Inlands- und Internationalraten, Tracking, Adressvalidierung, Lieferbestätigung, Etikettendruck |
| `org.apache.ofbiz.shipment.test` | Integrationstests für Bestandsausgabe und Packsitzungsablauf |

---

### Klasse: `ShipmentServices`

**Paket:** `org.apache.ofbiz.shipment.shipment`
**Typ:** Java-Klasse
**Zweck:** Stellt OFBiz-Services für Versandkostenschätzung, ODBC-Staging-Tabellen und ergänzende Versandfunktionen bereit. Kernklasse für alle nicht-carrier-spezifischen Operationen auf der Sendungsebene.

| Methode | Beschreibung |
|---|---|
| `createShipmentEstimate(dctx, context)` | Legt einen neuen Kostenschätzer (`ShipmentCostEstimate`) für eine Versandmethode an, inklusive Gewichts-, Mengen- und Preisbracketing. |
| `removeShipmentEstimate(dctx, context)` | Löscht einen bestehenden Kostenschätzer anhand seiner ID. |
| `calcShipmentCostEstimate(dctx, context)` | Berechnet die Versandkosten für eine konkrete Sendung. Wählt den passendsten Schätzer durch Geo-Filterung und Bracket-Prüfung und summiert Flach-, Gewichts-, Mengen-, Preis- und Übergrößenzuschläge. |
| `fillShipmentStagingTables(dctx, context)` | Schreibt Sendungs- und Paketdaten einer gepackten Sendung in die ODBC-Staging-Tabellen (`OdbcShipmentOut`, `OdbcPackageOut`) für die Übergabe an externe Systeme. |
| `updateShipmentsFromStaging(dctx, context)` | Liest Rückmeldedaten aus `OdbcPackageIn` (Tracking-Nummern, Gewichte, Kosten), aktualisiert die zugehörigen Sendungen und setzt den Status auf versendet oder storniert. |
| `clearShipmentStagingInfo(dctx, context)` | Bereinigt alle ODBC-Staging-Einträge (`OdbcPackageIn`, `OdbcPackageOut`, `OdbcShipmentOut`) für eine Sendung. |
| `updatePurchaseShipmentFromReceipt(dctx, context)` | Verfolgt den Empfangsstatus einer Einkaufssendung: setzt den Status auf `PURCH_SHIP_SHIPPED` bzw. `PURCH_SHIP_RECEIVED`, sobald alle Artikel quittiert wurden. |
| `duplicateShipmentRouteSegment(dctx, context)` | Dupliziert ein bestehendes Routensegment einer Sendung mit gleichen Carrier- und Adressdaten. |
| `quickScheduleShipmentRouteSegment(dctx, context)` | Löst asynchron die Carrier-Bestätigung für ein Routensegment aus (aktuell nur DHL unterstützt). |
| `getShipmentPackageValueFromOrders(dctx, context)` | Ermittelt den Warenwert eines Pakets anhand der fakturierten Bestellpositionen, gewichtet nach gelieferter Menge, mit Währungsumrechnung. |
| `sendShipmentCompleteNotification(dctx, context)` | Sendet eine Versandabschluss-E-Mail an den Empfänger der Sendung gemäß der `ProductStoreEmailSetting`. |
| `getShipmentGatewayConfigFromShipment(delegator, shipmentId, locale)` | Hilfsmethode: Liest `shipmentGatewayConfigId` und `configProps` aus der Versandmethode der primären Bestellung einer Sendung — wird von allen Carrier-Services genutzt. |

---

### Klasse: `ShipmentWorker`

**Paket:** `org.apache.ofbiz.shipment.shipment`
**Typ:** Java-Klasse (Utility, nicht instanziierbar)
**Zweck:** Stellt berechnende Hilfsmethoden bereit, die mehrere Carrier-Integrationen und die Packsitzung verwenden: Paketwertermittlung und gewichtsbasierte Paketsplittung.

| Methode | Beschreibung |
|---|---|
| `getShipmentPackageContentValue(shipmentPackageContent)` | Berechnet den anteiligen Warenwert eines Paketinhalts auf Basis der tatsächlichen Ausgaben (`ItemIssuance`) und des Einheitspreises. |
| `getPackageSplit(dctx, shippableItemInfo, maxWeight)` | Verteilt Bestellpositionen nach Stückzahl und Gewicht auf möglichst wenige Pakete, ohne das Maximalgewicht zu überschreiten. |
| `calcPackageWeight(dctx, packageMap, shippableItemInfo, additionalWeight)` | Berechnet das Gesamtgewicht eines Pakets durch Aufsummierung der Produktgewichte (mit UoM-Konvertierung auf Pfund). |
| `getProductItemInfo(shippableItemInfo, productId)` | Sucht die Produktinformationen eines bestimmten Artikels in der Versandliste. |

---

### Klasse: `ShipmentEvents`

**Paket:** `org.apache.ofbiz.shipment.shipment`
**Typ:** Java-Klasse
**Zweck:** Stellt Controller-Events für HTTP-Anfragen bereit, die nicht über den Service-Layer abgewickelt werden.

| Methode | Beschreibung |
|---|---|
| `viewShipmentPackageRouteSegLabelImage(request, response)` | Liefert das binäre Versandetikett (GIF oder PNG) eines Paket-Routensegments direkt an den Browser. |
| `checkForceShipmentReceived(request, response)` | Setzt den Status einer Einkaufssendung auf `PURCH_SHIP_RECEIVED`, wenn der Parameter `forceShipmentReceived=Y` übergeben wird. |

---

### Klasse: `PackingSession`

**Paket:** `org.apache.ofbiz.shipment.packing`
**Typ:** Java-Klasse (serialisierbar, session-scoped)
**Zweck:** Modelliert eine interaktive Packsitzung für eine oder mehrere Bestellungen. Verwaltet den Zustand aller gepackten Zeilen und Pakete im Arbeitsspeicher und orchestriert beim Abschluss die vollständige Erstellung von Sendung, Paketen, Bestandsausgaben und Statusübergängen in OFBiz. Dies ist die zentrale Zustandsklasse des gesamten Packprozesses.

| Methode | Beschreibung |
|---|---|
| `addOrIncreaseLine(orderId, orderItemSeqId, shipGroupSeqId, productId, quantity, packageSeqId, weight, update)` | Fügt eine Packzeile hinzu oder erhöht die Menge einer bestehenden. Prüft Inventarreservierungen und verteilt bei mehreren Reservierungen die Menge auf mehrere Zeilen. |
| `findLine(orderId, orderItemSeqId, shipGroupSeqId, productId, inventoryItemId, packageSeq)` | Sucht eine bestehende Packzeile exakt nach allen Schlüsselfeldern. |
| `getPackedQuantity(...)` | Mehrere Überladungen: Gibt die bereits gepackte Menge für eine Bestellposition, ein Produkt oder ein gesamtes Paket zurück. |
| `getCurrentReservedQuantity(orderId, orderItemSeqId, shipGroupSeqId, productId)` | Liest die verfügbare Reservierungsmenge aus der Summenentität für eine Position. |
| `getCurrentShippedQuantity(orderId, orderItemSeqId, shipGroupSeqId)` | Ermittelt die bereits versendete Menge anhand vorhandener `ItemIssuance`-Einträge. |
| `getPackingSessionLinesByPackage()` | Gibt die Packzeilen gruppiert nach Paket-Sequenznummer zurück (Karte + sortierte Schlüsselliste). |
| `complete(force)` | Schließt die Packsitzung ab: prüft Reservierungen, erstellt die Sendung, Pakete, bucht Bestandsausgaben, aktualisiert Routensegmente, setzt Status auf `SHIPMENT_PACKED` und markiert die Pickliste als abgeschlossen. |
| `clear()` | Setzt die gesamte Sitzung zurück, ohne die Sendung zu erstellen (z. B. nach Abbruch). |
| `clearLastPackage()` | Entfernt alle Zeilen des zuletzt hinzugefügten Pakets und dekrementiert den Paket-Zähler. |
| `clearLine(line)` | Entfernt eine einzelne Packzeile und korrigiert das Paketgewicht. |
| `getShipmentCostEstimate(...)` | Berechnet die voraussichtlichen Versandkosten für den aktuellen Sitzungsinhalt über den `calcShipmentCostEstimate`-Service. |
| `registerEvent(event)` | Registriert einen `PackingEvent`-Listener, der bei bestimmten Sitzungsereignissen benachrichtigt wird. |
| `addItemInfo(infos)` | Fügt Anzeigeinformationen (Produkt, Menge) für die UI-Darstellung hinzu oder aktualisiert bestehende. |
| `nextPackageSeq()` | Erhöht den Paket-Sequenz-Zähler und gibt den neuen Wert zurück. |

---

### Klasse: `PackingSessionLine`

**Paket:** `org.apache.ofbiz.shipment.packing`
**Typ:** Java-Klasse (serialisierbar)
**Zweck:** Repräsentiert eine einzelne Zeile innerhalb einer Packsitzung: ein Produkt aus einer Bestellreservierung, das einem bestimmten Paket zugeordnet ist.

| Methode | Beschreibung |
|---|---|
| `isSameItem(line)` | Prüft, ob zwei Packzeilen dasselbe Inventarobjekt und dieselbe Bestellposition referenzieren (unabhängig von Paket und Menge). |
| `issueItemToShipment(shipmentId, picklistBinId, userLogin, quantity, dispatcher)` | Bucht die Warenausgabe (`issueOrderItemShipGrpInvResToShipment`) und setzt den Status des zugehörigen Picklist-Items auf abgeschlossen oder storniert. |
| `applyLineToPackage(shipmentId, userLogin, dispatcher)` | Ordnet die Sendungsposition dem Versandpaket zu (`addShipmentContentToPackage`). |

---

### Klasse: `PackingServices`

**Paket:** `org.apache.ofbiz.shipment.packing`
**Typ:** Java-Klasse
**Zweck:** OFBiz-Service-Fassade für die `PackingSession`. Stellt Einstiegspunkte für Controller und andere Services bereit, die auf der Sitzung operieren.

| Methode | Beschreibung |
|---|---|
| `addPackLine(dctx, context)` | Fügt einen einzelnen Artikel mit Menge und Gewicht in eine bestimmte Paketnummer der Sitzung ein. |
| `packBulk(dctx, context)` | Verarbeitet eine Massenverpackung aus Formulardaten: mehrere Artikel, Pakete und optionale Mengenaufspaltung in einem Aufruf. |
| `incrementPackageSeq(dctx, context)` | Erhöht den Paket-Zähler und gibt die neue Paketnummer zurück. |
| `clearLastPackage(dctx, context)` | Entfernt das zuletzt begonnene Paket aus der Sitzung. |
| `clearPackLine(dctx, context)` | Entfernt eine einzelne Packzeile aus der Sitzung anhand aller Schlüsselfelder. |
| `clearPackAll(dctx, context)` | Löscht alle Packzeilen der Sitzung. |
| `calcPackSessionAdditionalShippingCharge(dctx, context)` | Berechnet die Versandkosten auf Basis der eingegebenen Paketgewichte und speichert sie als Zusatzgebühr in der Sitzung. |
| `completePack(dctx, context)` | Schließt die Packsitzung ab, gibt die erstellte Sendungs-ID zurück oder meldet einen Fehler bei leerer Sitzung. |
| `setSessionPackageWeights(session, packageWeights)` | Überträgt eine Map von Paket-ID zu Gewicht in die Sitzung und summiert das Gesamtgewicht. |
| `setSessionShipmentBoxTypes(session, boxTypes)` | Setzt den Kartontyp für jedes Paket in der Sitzung. |

---

### Klasse: `PackingEvent`

**Paket:** `org.apache.ofbiz.shipment.packing`
**Typ:** Java-Interface (serialisierbar)
**Zweck:** Listener-Schnittstelle für Ereignisse innerhalb einer `PackingSession`. Implementierungen können auf Hinzufügen (`EVENT_CODE_ADD=1`), Registrierung (`EVENT_CODE_EREG=5`), Löschen (`EVENT_CODE_CLEAR=20`) und Abschließen (`EVENT_CODE_COMPLETE=100`) reagieren.

| Methode | Beschreibung |
|---|---|
| `runEvent(session, eventCode)` | Wird von der Sitzung aufgerufen, wenn ein Ereignis eintritt. |
| `receiveMessage()` | Gibt eine Statusmeldung des Events zurück. |
| `getEventStatus()` | Gibt den aktuellen Event-Status als Ganzzahl zurück. |
| `getEventCode()` | Gibt den Event-Code zurück, auf den dieser Listener reagiert. |

---

### Klasse: `WeightPackageSession`

**Paket:** `org.apache.ofbiz.shipment.weightPackage`
**Typ:** Java-Klasse (serialisierbar, session-scoped)
**Zweck:** Sitzungsmodell für die nachgelagerte Gewichtserfassung: Der Nutzer gibt nach dem Verpacken Gewicht und Maße je Paket ein. Unterstützt optionale UPS-Echtzeit-Tarifabfrage (`upsShipmentConfirm`) mit Warnung bei zu großer Abweichung vom geschätzten Preis.

| Methode | Beschreibung |
|---|---|
| `createWeightPackageLine(orderId, weight, length, width, height, boxTypeId)` | Fügt ein neues Paket mit Gewicht und optionalen Dimensionen zur Sitzung hinzu. |
| `complete(orderId, locale, calculateOnlineShippingRateFromUps)` | Führt den vollständigen Abschluss durch: Pakete anlegen, ggf. UPS-Bestätigung einholen, Differenzwarnung prüfen, Bestellstatus setzen, Sendung auf `SHIPMENT_PACKED` setzen. |
| `completeShipment(orderId, calculateOnlineShippingRateFromUps)` | Führt den Abschluss ohne vorherige Differenzwarnung durch (zweiter Schritt nach Benutzerbestätigung). |
| `getShipmentCostEstimate(...)` | Berechnet die Versandkosten für die aktuelle Sitzung über `calcShipmentCostEstimate`. |
| `setPackageWeight/Length/Width/Height(value, seqId)` | Aktualisiert einzelne Maßangaben einer bereits erfassten Paketzeile. |
| `deletePackedLine(seqId)` | Entfernt eine Paketzeile aus der Sitzung. |
| `getShippableWeight(orderId)` | Summiert die Gewichte aller Pakete einer Bestellung. |
| `getPackedLines() / getPackedLines(orderId)` | Gibt alle oder auftragsbezogene Paketzeilen zurück. |
| `clearPackedLines(orderId)` | Entfernt alle Paketzeilen einer Bestellung. |

---

### Klasse: `WeightPackageServices`

**Paket:** `org.apache.ofbiz.shipment.weightPackage`
**Typ:** Java-Klasse
**Zweck:** OFBiz-Service-Fassade für `WeightPackageSession`.

| Methode | Beschreibung |
|---|---|
| `setPackageInfo(dctx, context)` | Validiert und speichert Gewicht und Maße eines neuen Pakets. Verhindert mehr Pakete als bestellte Artikel. |
| `updatePackedLine(dctx, context)` | Aktualisiert Gewicht und Maße einer bestehenden Paketzeile. |
| `deletePackedLine(dctx, context)` | Entfernt eine Paketzeile aus der Sitzung. |
| `completePackage(dctx, context)` | Schließt die Sitzung ab und löst ggf. UPS-Tarifabfrage aus; gibt bei Preisabweichung `showWarningForm` zurück. |
| `completeShipment(dctx, context)` | Führt den finalen Abschluss nach Benutzerbestätigung durch. |
| `savePackagesInfo(dctx, context)` | Legt die Pakete in OFBiz an und löst ggf. UPS-Bestätigung aus, ohne den Sendungsstatus zu setzen. |

---

### Klasse: `WeightPackageSessionLine`

**Paket:** `org.apache.ofbiz.shipment.weightPackage`
**Typ:** Java-Klasse (serialisierbar)
**Zweck:** Datencontainer für eine einzelne Paketzeile in der Gewichtserfassungssitzung (Gewicht, Länge, Breite, Höhe, Kartontyp).

| Methode | Beschreibung |
|---|---|
| `applyLineToPackage(shipmentId, userLogin, dispatcher, shipPackSeqId)` | Ordnet den Sendungsartikel dem Versandpaket zu (`addShipmentContentToPackage`). |

---

### Klasse: `VerifyPickSession`

**Paket:** `org.apache.ofbiz.shipment.verify`
**Typ:** Java-Klasse (serialisierbar, session-scoped)
**Zweck:** Sitzungsmodell für die Pickverifizierung: Ein Lagerarbeiter bestätigt, welche Mengen er gepickt hat. Die Sitzung prüft die Übereinstimmung mit den Reservierungen und erstellt am Ende eine fertige Sendung mit Status `SHIPMENT_PICKED`.

| Methode | Beschreibung |
|---|---|
| `createRow(orderId, orderItemSeqId, shipGroupSeqId, productId, originGeoId, quantity, locale)` | Erfasst eine verifizierte Menge für eine Bestellposition. Löst automatisch die Bestellpositions-ID auf, wenn nur die Produkt-ID übergeben wird. |
| `complete(orderId, locale)` | Schließt die Verifikationssitzung ab: prüft reservierte und verifizierte Mengen, erstellt die Sendung, bucht Warenausgaben, aktualisiert Produkt-Herkunft und setzt den Sendungsstatus. |
| `getReadyToVerifyQuantity(orderId, orderSeqId)` | Gibt die bisher verifizierte Menge für eine Bestellposition zurück. |
| `getVerifiedQuantity(orderId, orderItemSeqId, shipGroupSeqId, productId, inventoryItemId)` | Summiert verifizierte Mengen über alle Zeilen für eine Positions-Inventar-Kombination. |
| `getReservedQty(orderId, orderItemSeqId, shipGroupSeqId)` | Liest die reservierte Gesamtmenge aus der Summenentität. |
| `getPickRow(orderId, orderItemSeqId, shipGroupSeqId, productId, inventoryItemId)` | Sucht eine bestehende Verifikationszeile. |
| `clearAllRows()` | Verwirft alle Verifikationszeilen (z. B. bei Abbruch). |

---

### Klasse: `VerifyPickServices`

**Paket:** `org.apache.ofbiz.shipment.verify`
**Typ:** Java-Klasse
**Zweck:** OFBiz-Service-Fassade für `VerifyPickSession`.

| Methode | Beschreibung |
|---|---|
| `verifySingleItem(dctx, context)` | Erfasst die verifizierte Menge eines einzelnen Artikels in der Sitzung. |
| `verifyBulkItem(dctx, context)` | Verarbeitet Massenverifikation aus Formulardaten mit mehreren Positionen. |
| `completeVerifiedPick(dctx, context)` | Schließt die Sitzung ab, erstellt die Sendung und leert die Sitzungszeilen. |
| `cancelAllRows(dctx, context)` | Verwirft alle erfassten Verifikationszeilen. |

---

### Klasse: `VerifyPickSessionRow`

**Paket:** `org.apache.ofbiz.shipment.verify`
**Typ:** Java-Klasse (serialisierbar)
**Zweck:** Datencontainer für eine einzelne verifizierte Pickzeile (Bestellposition, Inventar-ID, Herkunfts-Geo, verifizierte Menge).

| Methode | Beschreibung |
|---|---|
| `isSameItem(line)` | Prüft Übereinstimmung von Inventar-ID, Bestellposition und Versandgruppe. |
| `issueItemToShipment(shipmentId, picklistBinId, userLogin, quantity, dispatcher, locale)` | Bucht die Warenausgabe und aktualisiert den Picklist-Item-Status. |

---

### Klasse: `PickListServices`

**Paket:** `org.apache.ofbiz.shipment.picklist`
**Typ:** Java-Klasse
**Zweck:** Hilfsdienste für die Picklisten-Verwaltung.

| Methode | Beschreibung |
|---|---|
| `convertOrderIdListToHeaders(dctx, context)` | Wandelt eine Liste von Auftrags-IDs in die zugehörigen `OrderHeader`-Entitäten um (nur genehmigte Kundenbestellungen). |
| `isBinComplete(delegator, picklistBinId)` | Prüft, ob alle Picklist-Items eines Bins den Status abgeschlossen oder storniert haben. |

---

### Klasse: `UpsServices`

**Paket:** `org.apache.ofbiz.shipment.thirdparty.ups`
**Typ:** Java-Klasse
**Zweck:** Vollständige UPS-Carrier-Integration über XML-Webservices. Unterstützt den gesamten Lebenszyklus einer UPS-Sendung: Tarifabfrage, Sendungsbestätigung (mit Etikettenabruf), Akzeptanz, Stornierung, Tracking, Adressvalidierung und E-Mail-Rücksendeetiketten. Konfiguration erfolgt über `ShipmentGatewayUps` oder `shipment.properties`.

| Methode | Beschreibung |
|---|---|
| `upsShipmentConfirm(dctx, context)` | Sendet eine UPS-Sendungsbestätigungsanfrage (ShipConfirm). Baut das XML aus Adress-, Gewichts- und Paketdaten zusammen; unterstützt COD, Nachnahme-Zuschläge und Zertifizierungsdateispeicherung. |
| `handleUpsShipmentConfirmResponse(responseDocument, routeSegment, locale)` | Verarbeitet die UPS-Bestätigungsantwort und speichert Digest und Status im Routensegment. |
| `upsShipmentAccept(dctx, context)` | Sendet die UPS-Akzeptanzanfrage (ShipAccept), ruft Tracking-Nummern und Etiketten (Base64-kodiert) ab und speichert sie in `ShipmentPackageRouteSeg`. |
| `handleUpsShipmentAcceptResponse(responseDocument, routeSegment, packageRouteSegs, ...)` | Verarbeitet die UPS-Akzeptanzantwort, dekodiert Etiketten und schreibt Tracking-Nummern. |
| `upsVoidShipment(dctx, context)` | Storniert eine bestätigte UPS-Sendung (Void). |
| `upsTrackShipment(dctx, context)` | Fragt den aktuellen Tracking-Status einer UPS-Sendung ab und aktualisiert das Routensegment. |
| `upsRateInquire(dctx, context)` | Fragt UPS-Tarife für eine Sendung ab und gibt den geschätzten Betrag zurück. |
| `upsRateInquireByPostalCode(dctx, context)` | Tarifabfrage nur anhand von PLZ und Gewicht (ohne vollständige Sendungsstruktur). |
| `upsAddressValidation(dctx, context)` | Validiert eine US-Adresse über den UPS-Adressvalidierungsservice. |
| `upsEmailReturnLabel(dctx, context)` | Generiert ein UPS-Rücksendeetikett und sendet es per E-Mail an den Empfänger. |
| `upsShipmentAlternateRatesInquiry(dctx, context)` | Fragt alternative UPS-Tarife für verschiedene Serviceklassen in einem Aufruf ab. |
| `sendUpsRequest(action, xmlString, ...)` | Interne HTTP-Übertragungsmethode: baut die UPS-XML-Anfrage mit Authentifizierungsheader zusammen und sendet sie per HTTP-POST. |

---

### Klasse: `UpsConnectException`

**Paket:** `org.apache.ofbiz.shipment.thirdparty.ups`
**Typ:** Java-Klasse (Exception)
**Zweck:** Paketeigene Ausnahme für Verbindungsfehler zum UPS-Webservice; erweitert `GeneralException`.

---

### Klasse: `FedexServices`

**Paket:** `org.apache.ofbiz.shipment.thirdparty.fedex`
**Typ:** Java-Klasse
**Zweck:** FedEx-Carrier-Integration über XML-Webservices mit FreeMarker-Templates für die Anfragegenerierung. Unterstützt die initiale Meter-Number-Registrierung und die vollständige Sendungsbestätigung mit Etikettenempfang. Konfiguration über `ShipmentGatewayFedex` oder `shipment.properties`. Aktuell nur Einzelpaketsendungen unterstützt.

| Methode | Beschreibung |
|---|---|
| `sendFedexRequest(xmlString, delegator, configId, resource, locale)` | Sendet eine XML-Anfrage an den FedEx-Endpunkt per HTTP-POST mit konfigurierbarem Timeout. |
| `fedexSubscriptionRequest(dctx, context)` | Registriert das Unternehmen bei FedEx und erhält eine Meter-Number. Baut die Anfrage aus Adress-, Telefon- und E-Mail-Daten der Company-Party zusammen. |
| `fedexShipRequest(dctx, context)` | Sendet eine FedEx-Sendungsanfrage (FDXShipRequest) auf Basis eines FreeMarker-Templates. Validiert Gewicht, Dimensionen, Servicetype und Adressen; verarbeitet Home-Delivery-Optionen. |
| `handleFedexShipReply(replyString, routeSegment, packageRouteSegs, locale)` | Parst die FedEx-Antwort, speichert Tracking-Nummer und Base64-dekodiertes Etikett im Routensegment. |
| `handleErrors(rootElement, errorList, locale)` | Extrahiert Fehlercodes und -meldungen aus dem FedEx-XML-Antwortelement. |

---

### Klasse: `FedexConnectException`

**Paket:** `org.apache.ofbiz.shipment.thirdparty.fedex`
**Typ:** Java-Klasse (Exception)
**Zweck:** Paketeigene Ausnahme für Verbindungs- und Protokollfehler beim FedEx-Webservice; erweitert `GeneralException`.

---

### Klasse: `DhlServices`

**Paket:** `org.apache.ofbiz.shipment.thirdparty.dhl`
**Typ:** Java-Klasse
**Zweck:** DHL-Carrier-Integration über XML-Webservices mit FreeMarker-Templates. Unterstützt Ratenabfrage, Registrierung (Account-Nummer-Aktivierung) und Sendungsbestätigung mit Etikettenempfang. Arbeitet ausschließlich mit Gewichten in Pfund (`WT_lb`). Konfiguration über `ShipmentGatewayDhl` oder `shipment.properties`.

| Methode | Beschreibung |
|---|---|
| `sendDhlRequest(xmlString, delegator, configId, resource, locale)` | Sendet eine XML-Anfrage an den DHL-Endpunkt per HTTP-POST mit konfigurierbarem Timeout. |
| `dhlRateEstimate(dctx, context)` | Fragt DHL-Tarife für eine Sendung ab und gibt den geschätzten Versandpreis zurück. |
| `handleDhlRateResponse(rateResponseDocument, locale)` | Verarbeitet die DHL-Tarifrückmeldung und extrahiert den Preis. |
| `dhlRegisterInquire(dctx, context)` | Aktiviert eine DHL-Account-Nummer (DHL-Registrierungsanfrage). |
| `handleDhlRegisterResponse(responseDocument, locale)` | Verarbeitet die DHL-Registrierungsantwort. |
| `dhlShipmentConfirm(dctx, context)` | Sendet eine DHL-Sendungsanfrage, empfängt das Etikett (Base64) und speichert Tracking-Nummer und Etikettenbild im Routensegment. |
| `handleDhlShipmentConfirmResponse(responseString, routeSegment, packageRouteSegs, locale)` | Parst die DHL-Sendungsantwort und persistiert Etikett und Tracking-Daten. |
| `handleErrors(responseElement, errorList, locale)` | Extrahiert Fehlermeldungen aus der DHL-XML-Antwort. |

---

### Klasse: `DhlConnectException`

**Paket:** `org.apache.ofbiz.shipment.thirdparty.dhl`
**Typ:** Java-Klasse (Exception)
**Zweck:** Paketeigene Ausnahme für Verbindungsfehler zum DHL-Webservice; erweitert `GeneralException`.

---

### Klasse: `UspsServices`

**Paket:** `org.apache.ofbiz.shipment.thirdparty.usps`
**Typ:** Java-Klasse
**Zweck:** USPS-Carrier-Integration über den USPS-Web-Tools-XML-API. Bietet den breitesten Funktionsumfang aller vier Carrier-Integrationen: Inlands- und Auslandstarifabfrage, Sendungsverfolgung, Adressvalidierung, Postleitzahl-Lookup, Lieferbestätigung und Etikettendruck. Nutzt `ShipmentWorker.getPackageSplit()` für die Paketaufteilung bei Gewichtsüberschreitung. Konfiguration über `ShipmentGatewayUsps` oder `shipment.properties`.

| Methode | Beschreibung |
|---|---|
| `uspsRateInquire(dctx, context)` | Fragt Inlandstarife für eine oder mehrere Pakete ab. Teilt automatisch bei Überschreitung des Maximalgewichts auf und summiert die Teilbeträge. |
| `uspsInternationalRateInquire(dctx, context)` | Fragt internationale USPS-Tarife ab. |
| `uspsTrackConfirm(dctx, context)` | Ruft den aktuellen Tracking-Status einer USPS-Sendung ab. |
| `uspsAddressValidation(dctx, context)` | Validiert eine US-Adresse und normalisiert PLZ und Staat. |
| `uspsCityStateLookup(dctx, context)` | Gibt Stadt und Bundesstaat für eine US-PLZ zurück. |
| `uspsPriorityMailStandard(dctx, context)` | Berechnet Standardlieferzeiten für USPS Priority Mail. |
| `uspsPackageServicesStandard(dctx, context)` | Berechnet Standardlieferzeiten für USPS Package Services. |
| `uspsDomesticRate(dctx, context)` | Allgemeine Inlandstarifabfrage für konfigurierte USPS-Dienste. |
| `uspsUpdateShipmentRateInfo(dctx, context)` | Aktualisiert Versandkosteninformationen für eine bestehende Sendung nach USPS-Tarifabfrage. |
| `uspsDeliveryConfirmation(dctx, context)` | Generiert eine USPS-Lieferbestätigungsnummer (Delivery Confirmation) für eine Sendung. |
| `uspsDumpShipmentLabelImages(dctx, context)` | Exportiert gespeicherte USPS-Etikettenbilder als Datei. |
| `uspsPriorityMailInternationalLabel(dctx, context)` | Erstellt ein USPS Priority Mail International-Etikett und speichert es in der Datenbank. |

---

### Klasse: `UspsRequestException`

**Paket:** `org.apache.ofbiz.shipment.thirdparty.usps`
**Typ:** Java-Klasse (Exception)
**Zweck:** Paketeigene Ausnahme für Fehler bei USPS-API-Anfragen; erweitert `GeneralException`.

---

### Klasse: `UspsMockApiServlet`

**Paket:** `org.apache.ofbiz.shipment.thirdparty.usps`
**Typ:** Java-Klasse (HttpServlet)
**Zweck:** Test-Servlet, das den USPS-XML-API simuliert. Ermöglicht Integration-Tests ohne echte USPS-Verbindung, indem es vordefinierte XML-Antworten zurückliefert.

---

### Test-Klassen

Die folgenden Klassen enthalten Integrationstests und gehören nicht zum produktiven Code.

| Klasse | Paket | Beschreibung |
|---|---|---|
| `IssuanceTest` | `org.apache.ofbiz.shipment.test` | Testet den vollständigen Packing-Session-Ablauf: Artikel packen, Sendung abschließen und korrekte Erstellung von `ItemIssuance`-, `OrderShipment`- und `OrderHeader`-Einträgen. Prüft insbesondere die Verteilung auf mehrere Inventarquellen. |
| `UspsServicesTests` | `org.apache.ofbiz.shipment.thirdparty.usps` | Integrationstests für ausgewählte USPS-Service-Methoden gegen den Mock-API-Servlet. |
