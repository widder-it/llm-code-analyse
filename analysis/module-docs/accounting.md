# Modul: accounting

## Überblick

Das `accounting`-Modul ist das zentrale Finanzbuchhaltungsmodul von Apache OFBiz. Es umfasst die gesamte Geschäftslogik für Rechnungsstellung, Zahlungsabwicklung, Hauptbuchhaltung, Steuern, Finanzkonten und Reporting. Besonders hervorzuheben ist die Unterstützung von acht externen Payment-Provider-Integrationen (authorizedotnet, clearcommerce, eway, gosoftware, paypal, sagepay, valuelink, worldpay), die über ein einheitliches Gateway-Framework angebunden sind.

## Submodule

| Paket | Beschreibung |
|---|---|
| `org.apache.ofbiz.accounting` | Basisklassen: generische Exception, GL-Event-Handler |
| `org.apache.ofbiz.accounting.admin` | Administrative Buchhaltungsfunktionen (GL-Konten, Belegfilterung) |
| `org.apache.ofbiz.accounting.agreement` | Vertragsmanagement und Provisionsberechnungen |
| `org.apache.ofbiz.accounting.ap.invoices` | Accounts Payable: Kommissionsbericht und -abrechnung |
| `org.apache.ofbiz.accounting.ar` | Accounts Receivable: Stapelzahlungsverarbeitung |
| `org.apache.ofbiz.accounting.budget` | Budgetverwaltung |
| `org.apache.ofbiz.accounting.chartofaccounts` | Kontenplan und Steuer-GL-Konten |
| `org.apache.ofbiz.accounting.finaccount` | Finanzkonten: Guthaben, Einzahlungen, Abhebungen, Payment-Gateway-Anbindung |
| `org.apache.ofbiz.accounting.fixedasset` | Anlagevermögen und Geolokalisierung |
| `org.apache.ofbiz.accounting.invoice` | Rechnungsstellung für Aufträge, Lieferungen, Retouren; Zahlungsabgleich |
| `org.apache.ofbiz.accounting.ledger` | Hauptbuch: Kostenstellen, GL-Buchungen |
| `org.apache.ofbiz.accounting.order` | Abrechnungskonten-Auftragsübersicht |
| `org.apache.ofbiz.accounting.payment` | Zahlungen: Gateway-Orchestrierung, Zahlungsmethoden, Gutscheine, Abrechnungskonten |
| `org.apache.ofbiz.accounting.period` | Buchungsperioden und Periodenabschluss |
| `org.apache.ofbiz.accounting.rate` | Stunden- und Kostensätze |
| `org.apache.ofbiz.accounting.reports` | Finanzberichte: Bilanz, GuV, Cashflow, Probebilanzen |
| `org.apache.ofbiz.accounting.tax` | Steuerbehörden und Steuerberechnung |
| `org.apache.ofbiz.accounting.transaction` | Transaktionsverwaltung (Autorisierung, Capture, Gateway-Response-Ansicht) |
| `org.apache.ofbiz.accounting.thirdparty.authorizedotnet` | Integration Authorize.Net (AIM-Protokoll) |
| `org.apache.ofbiz.accounting.thirdparty.clearcommerce` | Integration ClearCommerce (XML-basiert) |
| `org.apache.ofbiz.accounting.thirdparty.eway` | Integration eWay (australischer Zahlungsdienstleister) |
| `org.apache.ofbiz.accounting.thirdparty.gosoftware` | Integration GoSoftware PcCharge und RITA |
| `org.apache.ofbiz.accounting.thirdparty.paypal` | Integration PayPal (IPN-basiert) |
| `org.apache.ofbiz.accounting.thirdparty.sagepay` | Integration SagePay (VSP-Protokoll) |
| `org.apache.ofbiz.accounting.thirdparty.valuelink` | Integration ValueLink (Geschenkkarten, DES/3DES-Verschlüsselung) |
| `org.apache.ofbiz.accounting.thirdparty.worldpay` | Integration WorldPay (Redirect-basiert) |
| `org.apache.ofbiz.accounting.util` | Hilfsfunktionen für GL-Konten und Zahlungsklassifizierung |
| `org.apache.ofbiz.accounting.accounting` | Groovy-basierte Integrationstests |
| `org.apache.ofbiz.accounting.test` | Java-basierte Unit-Tests |

---

## Klassen im Detail

---

### Klasse: `AccountingException`
**Paket:** `org.apache.ofbiz.accounting`
**Typ:** Java-Klasse
**Zweck:** Spezialisierte Ausnahme für Buchhaltungsfehler, die von `GenericServiceException` erbt. Wird in der gesamten Buchhaltungslogik geworfen, wenn Konten nicht aufgelöst oder Buchungsregeln verletzt werden.

| Methode | Beschreibung |
|---|---|
| `AccountingException(String, Throwable)` | Erstellt eine Ausnahme mit Fehlermeldung und ursächlicher Exception (typischer Konstruktor für Fehlerweiterleitung) |

---

### Klasse: `GlEvents`
**Paket:** `org.apache.ofbiz.accounting`
**Typ:** Java-Klasse
**Zweck:** HTTP-Event-Handler für GL-bezogene Benutzerinteraktionen. Verarbeitet Multi-Row-Formulare zur Kontenabstimmung direkt aus dem Web-Request.

| Methode | Beschreibung |
|---|---|
| `createReconcileAccount(HttpServletRequest, HttpServletResponse)` | Liest markierte Buchungseinträge aus einem Multi-Row-Formular, berechnet den abgestimmten Saldo (Soll minus Haben) und legt einen neuen `GlReconciliation`-Datensatz mit zugehörigen Einträgen an |

---

### Klasse: `PaymentGatewayServices`
**Paket:** `org.apache.ofbiz.accounting.payment`
**Typ:** Java-Klasse
**Zweck:** Zentrales Orchestrierungsmodul für alle Zahlungsgateway-Operationen. Implementiert den vollständigen Zahlungslebenszyklus (Autorisierung, Capture, Release, Rückerstattung, Gutschrift) und vermittelt zwischen der OFBiz-Bestelllogik und den konkreten Provider-Adaptern. Enthält außerdem Testprozessoren zur Entwicklungszeit-Simulation.

| Methode | Beschreibung |
|---|---|
| `authOrderPayments(DispatchContext, Map)` | Autorisiert alle ausstehenden Zahlungspräferenzen eines Auftrags; unterstützt Re-Autorisierung bereits autorisierter Präferenzen, wenn deren Gültigkeit abgelaufen ist |
| `authOrderPaymentPreference(DispatchContext, Map)` | Autorisiert eine einzelne `OrderPaymentPreference` durch Aufruf des konfigurierten Provider-Dienstes (Typ `PRDS_PAY_AUTH`) |
| `releaseOrderPayments(DispatchContext, Map)` | Gibt alle autorisierten Zahlungen eines Auftrags frei (z.B. bei Stornierung) |
| `releaseOrderPaymentPreference(DispatchContext, Map)` | Gibt eine einzelne Zahlungspräferenz frei und ruft den Provider-Dienst `PRDS_PAY_RELEASE` auf |
| `captureOrderPayments(DispatchContext, Map)` | Erfasst (bucht) alle autorisierten Zahlungen eines Auftrags; verteilt den Rechnungsbetrag anteilig auf mehrere Zahlungsmethoden |
| `capturePaymentsByInvoice(DispatchContext, Map)` | Steuert den Capture-Prozess rechnungsbasiert: ermittelt offene autorisierte Zahlungen zu einer Rechnung und löst deren Buchung aus |
| `processCaptureSplitPayment(DispatchContext, Map)` | Behandelt aufgeteilte Captures, bei denen ein Teilbetrag einer autorisierten Zahlung erfasst wird |
| `captureBillingAccountPayments(DispatchContext, Map)` | Bucht Zahlungen über Abrechnungskonten (Kreditlinie), inkl. Überprüfung des verfügbaren Guthabens |
| `refundOrderPaymentPreference(DispatchContext, Map)` | Initiiert eine Rückerstattung für eine einzelne Zahlungspräferenz |
| `refundPayment(DispatchContext, Map)` | Führt eine direkte Rückerstattung auf eine Zahlungsmethode aus |
| `processAuthResult(DispatchContext, Map)` | Verarbeitet und persistiert das Ergebnis einer Gateway-Autorisierungsantwort; aktualisiert Status und speichert Gateway-Response |
| `processCaptureResult(DispatchContext, Map)` | Verarbeitet das Ergebnis eines Capture-Vorgangs und aktualisiert die Zahlungsbelege |
| `processRefundResult(DispatchContext, Map)` | Verarbeitet das Ergebnis einer Rückerstattung und legt entsprechende Zahlungsdatensätze an |
| `processReleaseResult(DispatchContext, Map)` | Verarbeitet das Ergebnis eines Release-Vorgangs |
| `processCreditResult(DispatchContext, Map)` | Verarbeitet das Ergebnis einer Kreditbuchung |
| `retryFailedAuths(DispatchContext, Map)` | Batch-Job: wiederholt fehlgeschlagene Autorisierungsversuche für alle offenen Aufträge |
| `retryFailedOrderAuth(DispatchContext, Map)` | Wiederholt fehlgeschlagene Autorisierung für einen einzelnen Auftrag |
| `retryFailedAuthNsfs(DispatchContext, Map)` | Wiederholt fehlgeschlagene NSF-Autorisierungen (Non-Sufficient Funds) |
| `processManualCcAuth(DispatchContext, Map)` | Verarbeitet eine manuell eingegebene Kreditkartenautorisation (z.B. per Telefon erhaltener Auth-Code) |
| `processManualCcTx(DispatchContext, Map)` | Führt eine vollständige manuelle Kreditkartentransaktion durch |
| `verifyCreditCard(DispatchContext, Map)` | Validiert Kreditkartendaten (Format, Ablaufdatum, Luhn-Prüfung) ohne Echttransaktion |
| `savePaymentGatewayResponse(DispatchContext, Map)` | Persistiert eine rohe Gateway-Antwort in der Datenbank |
| `savePaymentGatewayResponseAndMessages(DispatchContext, Map)` | Persistiert Gateway-Antwort inklusive aller Rückgabe-Nachrichten |
| `storePaymentErrorMessage(DispatchContext, Map)` | Speichert Fehlermeldungen aus Gateway-Antworten für spätere Analyse |
| `testProcessor(DispatchContext, Map)` | Simulierter Testprozessor, der Transaktionen immer genehmigt |
| `testProcessorWithCapture(DispatchContext, Map)` | Testprozessor mit sofortigem Capture |
| `testRandomAuthorize(DispatchContext, Map)` | Testprozessor mit zufälligem Autorisierungsergebnis |
| `alwaysApproveProcessor(DispatchContext, Map)` | Testprozessor: genehmigt immer |
| `alwaysDeclineProcessor(DispatchContext, Map)` | Testprozessor: lehnt immer ab |
| `alwaysNsfProcessor(DispatchContext, Map)` | Testprozessor: simuliert immer unzureichende Deckung |
| `alwaysBadExpireProcessor(DispatchContext, Map)` | Testprozessor: simuliert immer abgelaufene Karte |
| `alwaysBadCardNumberProcessor(DispatchContext, Map)` | Testprozessor: simuliert immer ungültige Kartennummer |
| `testRelease(DispatchContext, Map)` | Testprozessor für Release-Operationen |
| `testCapture(DispatchContext, Map)` | Testprozessor für Capture-Operationen |
| `testRefund(DispatchContext, Map)` | Testprozessor für Rückerstattungen |

---

### Klasse: `PaymentWorker`
**Paket:** `org.apache.ofbiz.accounting.payment`
**Typ:** Java-Klasse (Utility, nicht instanziierbar)
**Zweck:** Statische Hilfsmethoden zur Berechnung von Zahlungsbeträgen (angewendet, nicht angewendet) und zum Abruf von Zahlungsmethodeninformationen für Parties.

| Methode | Beschreibung |
|---|---|
| `getPartyPaymentMethodValueMaps(Delegator, String, Boolean)` | Gibt alle Zahlungsmethoden einer Party zurück, optional einschließlich abgelaufener Methoden |
| `getPaymentMethodAndRelated(ServletRequest, String)` | Lädt eine Zahlungsmethode mit allen verknüpften Daten (Kreditkarte, EFT-Konto, Rechnungsadresse) aus dem Request-Kontext |
| `getPaymentsTotal(List)` | Summiert die Beträge einer Liste von Zahlungsdatensätzen |
| `getPaymentApplied(Delegator, String, Timestamp, Boolean)` | Berechnet den auf eine Zahlung angewendeten Betrag, optional zu einem bestimmten Stichtag und in Originalwährung |
| `getPaymentNotApplied(GenericValue, Boolean)` | Berechnet den noch nicht auf Rechnungen angewendeten Restbetrag einer Zahlung |
| `getPaymentAppliedAmount(Delegator, String)` | Gibt den Betrag einer einzelnen `PaymentApplication` zurück |

---

### Klasse: `PaymentMethodServices`
**Paket:** `org.apache.ofbiz.accounting.payment`
**Typ:** Java-Klasse
**Zweck:** CRUD-Dienste für die verschiedenen Zahlungsmethodentypen (Kreditkarten, Geschenkgutscheine, EFT-Konten, Scheckkonten). Enthält Gültigkeitsprüfungen und Sicherheitsvalidierung.

| Methode | Beschreibung |
|---|---|
| `deletePaymentMethod(DispatchContext, Map)` | Deaktiviert eine Zahlungsmethode durch Setzen des `thruDate` (kein physisches Löschen) |
| `makeExpireDate(DispatchContext, Map)` | Generiert ein standardisiertes Ablaufdatum-Timestamp aus Monat/Jahr-Eingabe |
| `createCreditCard(DispatchContext, Map)` | Legt eine neue Kreditkarte als Zahlungsmethode an, inklusive Adressverknüpfung |
| `updateCreditCard(DispatchContext, Map)` | Aktualisiert Kreditkartendaten und zugehörige Rechnungsadresse |
| `clearCreditCardData(DispatchContext, Map)` | Löscht sensible Kreditkartendaten (PAN, CVV) aus der Datenbank (PCI-Compliance) |
| `createGiftCard(DispatchContext, Map)` | Legt eine Geschenkkarte als Zahlungsmethode an |
| `updateGiftCard(DispatchContext, Map)` | Aktualisiert Geschenkkartendaten |
| `createEftAccount(DispatchContext, Map)` | Legt ein EFT-Bankkonto (Electronic Funds Transfer) an |
| `updateEftAccount(DispatchContext, Map)` | Aktualisiert EFT-Kontodaten |
| `createCheckAccount(DispatchContext, Map)` | Legt ein Scheckkonto als Zahlungsmethode an |
| `updateCheckAccount(DispatchContext, Map)` | Aktualisiert Scheckkontodaten |

---

### Klasse: `GiftCertificateServices`
**Paket:** `org.apache.ofbiz.accounting.payment`
**Typ:** Java-Klasse
**Zweck:** Vollständiger Lebenszyklus für Geschenkgutscheine (Gift Certificates): Erstellung, Aufladung, Einlösung, Saldoabfrage sowie Payment-Gateway-Integration. Karten- und PIN-Nummern werden per SecureRandom generiert (14- bzw. 6-stellig).

| Methode | Beschreibung |
|---|---|
| `createGiftCertificate(DispatchContext, Map)` | Erstellt einen neuen Geschenkgutschein mit Anfangsguthaben und legt das zugehörige `FinAccount` an |
| `addFundsToGiftCertificate(DispatchContext, Map)` | Lädt einen bestehenden Geschenkgutschein mit einem weiteren Betrag auf |
| `redeemGiftCertificate(DispatchContext, Map)` | Löst einen Betrag vom Geschenkgutschein ein und bucht die Transaktion |
| `checkGiftCertificateBalance(DispatchContext, Map)` | Gibt das aktuelle Guthaben eines Geschenkgutscheins zurück |
| `giftCertificateProcessor(DispatchContext, Map)` | Payment-Gateway-Adapter: autorisiert und erfasst Zahlungen per Geschenkgutschein |
| `giftCertificateAuthorize(DispatchContext, Map)` | Reserviert einen Betrag auf dem Geschenkgutschein (Pre-Authorization) |
| `giftCertificateRefund(DispatchContext, Map)` | Erstattet einen Betrag auf einen Geschenkgutschein |
| `giftCertificateRelease(DispatchContext, Map)` | Gibt eine reservierte Autorisierung frei |
| `giftCertificatePurchase(DispatchContext, Map)` | Verarbeitet den Kauf eines Geschenkgutscheins inklusive Erfüllungslogik |
| `giftCertificateReload(DispatchContext, Map)` | Verarbeitet das Aufladen eines Geschenkgutscheins als Produktkauf |
| `createFulfillmentRecord(DispatchContext, Map)` | Legt einen Erfüllungsdatensatz für einen Geschenkgutschein an |
| `refundGcPurchase(DispatchContext, Map)` | Rückerstattet einen Gutscheinkauf und storniert das Guthaben |

---

### Klasse: `BillingAccountWorker`
**Paket:** `org.apache.ofbiz.accounting.payment`
**Typ:** Java-Klasse (Utility, `final`)
**Zweck:** Berechnung von Abrechnungskonto-Salden, Verfügbarkeitsprüfung und Auflistung offener Aufträge für Kreditlinienverwaltung.

| Methode | Beschreibung |
|---|---|
| `makePartyBillingAccountList(GenericValue, String, String, Delegator, LocalDispatcher)` | Erstellt eine aufbereitete Liste aller Abrechnungskonten einer Party inkl. verfügbarer Guthaben, auch für Agenten-Kunden-Beziehungen |
| `getBillingAccountOpenOrders(Delegator, String)` | Liefert alle offenen Aufträge, die einem Abrechnungskonto belastet werden |
| `getBillingAccountAvailableBalance(GenericValue)` | Berechnet das verfügbare Guthaben eines Abrechnungskontos (Limit minus offene Salden) |
| `getBillingAccountNetBalance(Delegator, String)` | Berechnet den Nettosaldo eines Abrechnungskontos aus allen Zahlungsanwendungen |
| `availableToCapture(GenericValue)` | Prüft den für Capture verfügbaren Betrag auf einem Abrechnungskonto |
| `calcBillingAccountBalance(DispatchContext, Map)` | Service-Methode zur Saldoberechnung, aufrufbar über das Service-Framework |

---

### Klasse: `InvoiceServices`
**Paket:** `org.apache.ofbiz.accounting.invoice`
**Typ:** Java-Klasse
**Zweck:** Umfangreiche Service-Klasse für die Rechnungserzeugung aus verschiedenen Auftragsprozessen (Auftragsabschluss, Lieferungen, Dropshipping, Retouren). Deckt außerdem Zahlungsabgleich, Provisionsrechnungen und CSV-Import ab.

| Methode | Beschreibung |
|---|---|
| `createInvoiceForOrder(DispatchContext, Map)` | Erzeugt eine vollständige Rechnung aus einem Auftrag: Positionen, Anpassungen, Versandkosten und Steuern werden proportional auf die fakturierten Artikel verteilt |
| `createInvoiceForOrderAllItems(DispatchContext, Map)` | Wrapper um `createInvoiceForOrder`, der automatisch alle Auftragspositionen in die Rechnung einschließt |
| `createCommissionInvoices(DispatchContext, Map)` | Erzeugt Provisionsrechnungen für Vertriebsmitarbeiter auf Basis von Vereinbarungen und fakturierten Verkäufen |
| `readyInvoices(DispatchContext, Map)` | Versetzt mehrere Rechnungen gleichzeitig in den Status "Bereit" |
| `createInvoicesFromShipment(DispatchContext, Map)` | Erzeugt Rechnungen auf Basis eines Lieferscheins; berücksichtigt lieferungsbasierte Fakturierungsregeln |
| `setInvoicesToReadyFromShipment(DispatchContext, Map)` | Setzt Rechnungen, die zu einer Lieferung gehören, auf "Bereit" |
| `createSalesInvoicesFromDropShipment(DispatchContext, Map)` | Erzeugt Verkaufsrechnungen für Dropshipping-Bestellungen aus eingehenden Einkaufsrechnungen |
| `createInvoicesFromShipments(DispatchContext, Map)` | Verarbeitet mehrere Lieferungen gleichzeitig und erzeugt die entsprechenden Rechnungen |
| `createInvoicesFromReturnShipment(DispatchContext, Map)` | Erzeugt Gutschriften aus Retourenlieferungen |
| `createInvoiceFromReturn(DispatchContext, Map)` | Erzeugt eine Gutschriftsrechnung aus einem Retourenauftrag |
| `checkInvoicePaymentApplications(DispatchContext, Map)` | Prüft alle Zahlungsanwendungen einer Rechnung und setzt ggf. den Rechnungsstatus auf "Bezahlt" |
| `updatePaymentApplication(DispatchContext, Map)` | Aktualisiert eine Zahlungsanwendung |
| `updatePaymentApplicationDef(DispatchContext, Map)` | Aktualisiert eine Zahlungsanwendung mit Defaultwerten |
| `updatePaymentApplicationDefBd(DispatchContext, Map)` | Aktualisiert eine Zahlungsanwendung mit BigDecimal-Präzision |
| `calculateInvoicedAdjustmentTotal(DispatchContext, Map)` | Berechnet die Gesamtsumme aller fakturierten Auftragskorrekturen |
| `checkPaymentInvoices(DispatchContext, Map)` | Prüft, ob Zahlungen vollständig auf Rechnungen angewendet wurden |
| `importInvoice(DispatchContext, Map)` | Importiert Rechnungsdaten aus einem CSV-Format |

---

### Klasse: `InvoiceWorker`
**Paket:** `org.apache.ofbiz.accounting.invoice`
**Typ:** Java-Klasse (Utility, `final`, nicht instanziierbar)
**Zweck:** Statische Berechnungsmethoden für Rechnungsbeträge, Steuern, angewendete und ausstehende Beträge sowie Währungsumrechnung. Wird von nahezu allen anderen Buchhaltungsklassen genutzt.

| Methode | Beschreibung |
|---|---|
| `getInvoiceTotal(Delegator, String, Boolean)` | Berechnet den Gesamtbetrag einer Rechnung, optional in Originalwährung |
| `getInvoiceItemTotal(GenericValue)` | Berechnet den Betrag einer einzelnen Rechnungsposition (Menge × Einzelpreis) |
| `getInvoiceItemDescription(LocalDispatcher, GenericValue, Locale)` | Ermittelt die lesbare Beschreibung einer Rechnungsposition (Produktname, Dienstart etc.) |
| `getTaxableInvoiceItemTypeIds(Delegator)` | Gibt alle Rechnungspositionstypen zurück, die der Steuer unterliegen |
| `getInvoiceTaxTotal(GenericValue)` | Berechnet den gesamten Steuerbetrag einer Rechnung |
| `getInvoiceNoTaxTotal(GenericValue)` | Berechnet den Nettobetrag einer Rechnung ohne Steuern |
| `getInvoiceApplied(Delegator, String, Timestamp, Boolean)` | Berechnet den bereits auf die Rechnung angewendeten Zahlungsbetrag, optional zu einem Stichtag |
| `getInvoiceNotApplied(GenericValue, Timestamp)` | Berechnet den noch offenen Betrag einer Rechnung zu einem Stichtag |
| `getInvoiceItemApplied(GenericValue)` | Berechnet den auf eine einzelne Rechnungsposition angewendeten Zahlungsbetrag |
| `getInvoiceCurrencyConversionRate(GenericValue)` | Ermittelt den Währungsumrechnungskurs aus der Rechnung oder dem verknüpften Auftrag |
| `getInvoiceTaxByTaxAuthGeoAndParty(GenericValue)` | Gibt Steuern aufgegliedert nach Steuerbehörde und geografischer Zuständigkeit zurück |
| `getInvoiceTaxAuthPartyAndGeos(GenericValue)` | Gibt alle Steuerbehörden-Party-Geo-Kombinationen einer Rechnung zurück |
| `getInvoiceTaxTotalForTaxAuthPartyAndGeo(GenericValue, String, String)` | Berechnet den Steuerbetrag für eine spezifische Steuerbehörde |
| `getInvoiceUnattributedTaxTotal(GenericValue)` | Berechnet Steuern, die keiner Steuerbehörde zugeordnet sind |

---

### Klasse: `GeneralLedgerServices`
**Paket:** `org.apache.ofbiz.accounting.ledger`
**Typ:** Java-Klasse
**Zweck:** Hauptbuchdienste zur Verwaltung von Kostenstellen. Orchestriert die Zuweisung von GL-Konten zu Kostenstellenkategorien mit prozentualer Aufteilung.

| Methode | Beschreibung |
|---|---|
| `createUpdateCostCenter(DispatchContext, Map)` | Legt Kostenstellenzuordnungen für ein GL-Konto an oder aktualisiert sie; ruft für jede Kategorie `createGlAcctCatMemFromCostCenters` auf |
| `calculateCostCenterTotal(Map)` | Summiert alle Prozentsätze der Kostenstellen-Zuweisungen zur Validierung (Summe sollte 100% ergeben) |

---

### Klasse: `TaxAuthorityServices`
**Paket:** `org.apache.ofbiz.accounting.tax`
**Typ:** Java-Klasse
**Zweck:** Steuerberechnung für Produkte auf Basis von Steuerbehördendaten, geografischen Regeln und Produktkategorien. Unterstützt displaybezogene Vorabanzeige und exakte Auftragsberechnung.

| Methode | Beschreibung |
|---|---|
| `rateProductTaxCalcForDisplay(DispatchContext, Map)` | Berechnet Steuern für Anzeigezwecke (z.B. Warenkorb) auf Basis von Produktpreis, Menge und Lieferadresse |
| `rateProductTaxCalc(DispatchContext, Map)` | Vollständige Steuerberechnung für einen Auftragsabschluss: berücksichtigt Steuerbehörden-Hierarchien, Geo-Überschneidungen, steuerfreie Kategorien und produkt-spezifische Steuersätze |

---

### Klasse: `AgreementServices`
**Paket:** `org.apache.ofbiz.accounting.agreement`
**Typ:** Java-Klasse
**Zweck:** Berechnet Provisionen für Produkte auf Basis aktiver Vertragsvereinbarungen. Unterstützt Produktvarianten durch Rückfall auf die Elternprodukt-Vereinbarung.

| Methode | Beschreibung |
|---|---|
| `getCommissionForProduct(DispatchContext, Map)` | Ermittelt alle aktiven Provisionsvereinbarungen für ein Produkt und berechnet den Provisionsbetrag unter Berücksichtigung von Mindest-/Höchstbeträgen, Prozentsätzen und Mengenstaffeln |

---

### Klasse: `PeriodServices`
**Paket:** `org.apache.ofbiz.accounting.period`
**Typ:** Java-Klasse
**Zweck:** Verwaltung von Buchungsperioden und Periodenabschlussdaten für organisationsbezogene Buchhaltungsauswertungen.

| Methode | Beschreibung |
|---|---|
| `findLastClosedDate(DispatchContext, Map)` | Ermittelt das letzte Abschlussdatum einer Buchungsperiode für eine Organisation und einen Periodentyp |

---

### Klasse: `FinAccountServices`
**Paket:** `org.apache.ofbiz.accounting.finaccount`
**Typ:** Java-Klasse
**Zweck:** Verwaltung von Finanzkonten (Financial Accounts) für Kundenguthaben, Service-Credits und Bankkonten. Deckt Kontoerstellung, Saldenabfrage, Statusprüfung und Rückerstattungen ab.

| Methode | Beschreibung |
|---|---|
| `createAccountAndCredit(DispatchContext, Map)` | Erstellt ein Finanzkonto (Standard: Service-Credit-Konto) und schreibt sofort einen Anfangsbetrag gut |
| `createFinAccountForStore(DispatchContext, Map)` | Erstellt ein shopbezogenes Finanzkonto mit den für den jeweiligen Produktshop konfigurierten Standardwerten |
| `checkFinAccountBalance(DispatchContext, Map)` | Gibt den aktuellen Saldo eines Finanzkontos zurück |
| `checkFinAccountStatus(DispatchContext, Map)` | Prüft und aktualisiert den Status eines Finanzkontos (z.B. von "Aktiv" auf "Mangelkonto") |
| `refundFinAccount(DispatchContext, Map)` | Erstattet das gesamte Guthaben eines Finanzkontos an den Kontoinhaber |

---

### Klasse: `FinAccountPaymentServices`
**Paket:** `org.apache.ofbiz.accounting.finaccount`
**Typ:** Java-Klasse
**Zweck:** Payment-Gateway-Adapter für Finanzkonten. Ermöglicht Finanzkonten als vollwertige Zahlungsmethode im OFBiz-Gateway-Framework (Pre-Auth, Capture, Release, Refund, Einzahlung, Abhebung, Nachfüllung).

| Methode | Beschreibung |
|---|---|
| `finAccountPreAuth(DispatchContext, Map)` | Reserviert einen Betrag auf dem Finanzkonto (Pre-Authorization) |
| `finAccountReleaseAuth(DispatchContext, Map)` | Gibt eine Reservierung auf dem Finanzkonto frei |
| `finAccountCapture(DispatchContext, Map)` | Bucht einen zuvor reservierten Betrag vom Finanzkonto ab |
| `finAccountRefund(DispatchContext, Map)` | Erstattet einen Betrag zurück auf das Finanzkonto |
| `finAccountWithdraw(DispatchContext, Map)` | Führt eine direkte Abbuchung vom Finanzkonto durch |
| `finAccountDeposit(DispatchContext, Map)` | Schreibt einen Betrag dem Finanzkonto gut |
| `finAccountReplenish(DispatchContext, Map)` | Füllt ein Finanzkonto automatisch auf den konfigurierten Mindestsaldo auf |

---

### Klasse: `FinAccountProductServices`
**Paket:** `org.apache.ofbiz.accounting.finaccount`
**Typ:** Java-Klasse
**Zweck:** Verknüpft Produktkäufe mit der Erstellung von Finanzkonten (z.B. Guthabenkarten-Produkt erzeugt automatisch ein Finanzkonto).

| Methode | Beschreibung |
|---|---|
| `createPartyFinAccountFromPurchase(DispatchContext, Map)` | Erstellt bei Kauf eines bestimmten Produkts automatisch ein Finanzkonto für den Käufer und schreibt den Produktwert als Guthaben gut |

---

### Klasse: `UtilAccounting`
**Paket:** `org.apache.ofbiz.accounting.util`
**Typ:** Java-Klasse (Utility, `final`, nicht instanziierbar)
**Zweck:** Zentrale Hilfsmethoden zur GL-Kontenauflösung und zur Klassifizierung von Konten und Zahlungen. Dient als gemeinsame Basis für alle Module, die GL-Konten zuordnen müssen.

| Methode | Beschreibung |
|---|---|
| `getProductOrgGlAccountId(String, String, String, Delegator)` | Löst das GL-Konto für ein Produkt auf: prüft erst produkt-spezifische Zuordnungen, fällt dann auf den organisationsweiten Default zurück |
| `getDefaultAccountId(String, String, Delegator)` | Gibt das Standard-GL-Konto für einen Kontotyp und eine Organisation zurück |
| `getDescendantGlAccountClassIds(GenericValue)` | Gibt rekursiv alle untergeordneten GL-Kontenklassen-IDs zurück |
| `isPaymentType(GenericValue, String)` | Prüft, ob eine Zahlung einem bestimmten Zahlungstyp angehört |
| `isTaxPayment(GenericValue)` | Prüft, ob eine Zahlung eine Steuerzahlung ist |
| `isDisbursement(GenericValue)` | Prüft, ob eine Zahlung eine Auszahlung ist |
| `isReceipt(GenericValue)` | Prüft, ob eine Zahlung ein Eingang ist |
| `isDebitAccount(GenericValue)` / `isCreditAccount(GenericValue)` | Klassifiziert ein GL-Konto als Soll- oder Habenkonto |
| `isAssetAccount(GenericValue)` / `isLiabilityAccount(GenericValue)` / `isEquityAccount(GenericValue)` | Prüft die Kontenklasse eines GL-Kontos |
| `isIncomeAccount(GenericValue)` / `isRevenueAccount(GenericValue)` / `isExpenseAccount(GenericValue)` | Klassifiziert Ertrags-, Umsatz- und Aufwandskonten |
| `isPurchaseInvoice(GenericValue)` / `isSalesInvoice(GenericValue)` | Klassifiziert Rechnungen nach Einkauf/Verkauf |

---

## Payment-Provider-Integrationen

### Klasse: `AIMPaymentServices` (Authorize.Net)
**Paket:** `org.apache.ofbiz.accounting.thirdparty.authorizedotnet`
**Typ:** Java-Klasse
**Zweck:** Anbindung an Authorize.Net über das AIM-Protokoll (Advanced Integration Method) per HTTP-POST. Unterstützt alle Standard-Gateway-Operationen inkl. Void für bestimmte Antwortcodes (z.B. Code 50/54).

| Methode | Beschreibung |
|---|---|
| `ccAuth(DispatchContext, Map)` | Autorisiert eine Kreditkartenzahlung via AIM (`AUTH_ONLY`-Transaktion) |
| `ccCapture(DispatchContext, Map)` | Erfasst eine zuvor autorisierte Zahlung (`PRIOR_AUTH_CAPTURE`) |
| `ccRefund(DispatchContext, Map)` | Erstattet eine abgeschlossene Transaktion (`CREDIT`) |
| `ccRelease(DispatchContext, Map)` | Gibt eine Autorisierung frei (`VOID`) |
| `ccCredit(DispatchContext, Map)` | Führt eine ungebundene Gutschrift durch |
| `ccAuthCapture(DispatchContext, Map)` | Autorisiert und erfasst in einem Schritt (`AUTH_CAPTURE`) |

**Hilfsklassen:**
- `AuthorizeResponse`: Parst die pipe-delimitierte AIM-Antwort und bietet typisierte Getter für Transaktions-ID, Auth-Code, AVS/CVV-Ergebnisse
- `AIMRespPositions`, `CPRespPositions`: Definieren die Positionen der Antwortfelder im AIM- bzw. CP-Response-Format

---

### Klasse: `CCPaymentServices` (ClearCommerce)
**Paket:** `org.apache.ofbiz.accounting.thirdparty.clearcommerce`
**Typ:** Java-Klasse
**Zweck:** XML-basierte Integration mit dem ClearCommerce-Zahlungsgateway. Aufbau und Übermittlung von XML-Anfragen; Auswertung der XML-Antworten inklusive Schweregrad-Prüfung.

| Methode | Beschreibung |
|---|---|
| `ccAuth(DispatchContext, Map)` | Sendet eine Pre-Authorization-Anfrage als XML-Dokument |
| `ccCredit(DispatchContext, Map)` | Führt eine Kreditbuchung (Rückgabe ohne Referenz) durch |
| `ccCapture(DispatchContext, Map)` | Erfasst eine autorisierte Zahlung |
| `ccRelease(DispatchContext, Map)` | Gibt eine Autorisierung frei |
| `ccReleaseNoop(DispatchContext, Map)` | Leere Release-Implementierung (kein Netzwerkaufruf, direkte Erfolgsrückgabe) |
| `ccRefund(DispatchContext, Map)` | Erstattet eine erfasste Zahlung |
| `ccReAuth(DispatchContext, Map)` | Re-autorisiert eine abgelaufene Autorisierung |
| `ccReport(DispatchContext, Map)` | Ruft Transaktionsberichte vom Gateway ab |

**Hilfsklasse:** `ClearCommerceException` — interne Exception für Gateway-Kommunikationsfehler.

---

### Klassen: `EwayServices`, `GatewayRequest`, `GatewayResponse`, `GatewayConnector` (eWay)
**Paket:** `org.apache.ofbiz.accounting.thirdparty.eway`
**Typ:** Java-Klassen
**Zweck:** Integration des australischen Zahlungsdienstleisters eWay über XML-API. `GatewayRequest` kapselt alle Felder einer eWay-Anfrage; `GatewayConnector` sendet die XML-Anfrage per HTTP; `GatewayResponse` parst die XML-Antwort.

| Klasse/Methode | Beschreibung |
|---|---|
| `EwayServices.ewayCharge(DispatchContext, Map)` | Verarbeitet eine Kreditkartenzahlung (kombiniert Auth und Capture); befüllt `GatewayRequest` mit Kundendaten, Adresse und CVN |
| `EwayServices.ewayRefund(DispatchContext, Map)` | Erstattet eine Zahlung über die eWay-Refund-URL |
| `EwayServices.ewayRelease(DispatchContext, Map)` | Gibt eine Autorisierung frei (leere Implementierung, da eWay kein separates Release kennt) |
| `GatewayConnector.sendRequest(GatewayRequest)` | Sendet die XML-Anfrage an die eWay-API-URL und gibt die geparste Antwort zurück |

---

### Klassen: `PcChargeServices`, `PcChargeApi`, `RitaServices`, `RitaApi` (GoSoftware)
**Paket:** `org.apache.ofbiz.accounting.thirdparty.gosoftware`
**Typ:** Java-Klassen
**Zweck:** Integration zweier GoSoftware-Produkte: PcCharge (XML-basiertes Terminal-Gateway über lokale Socket-Verbindung) und RITA (Remote Internet Transaction Authorization, HTTP-basiert). Beide nutzen XML-Anfragen mit identischer Struktur.

| Klasse/Methode | Beschreibung |
|---|---|
| `PcChargeServices.ccAuth(DispatchContext, Map)` | Autorisiert über PcCharge-API |
| `PcChargeServices.ccCapture(DispatchContext, Map)` | Erfasst über PcCharge-API |
| `PcChargeServices.ccRelease(DispatchContext, Map)` | Gibt Autorisierung über PcCharge frei |
| `PcChargeServices.ccRefund(DispatchContext, Map)` | Erstattet über PcCharge-API |
| `RitaServices.ccAuth(DispatchContext, Map)` | Autorisiert über RITA-HTTP-API |
| `RitaServices.ccCapture(DispatchContext, Map)` | Erfasst über RITA-HTTP-API |
| `RitaServices.ccVoidRelease(DispatchContext, Map)` | Storniert eine Autorisierung |
| `RitaServices.ccVoidRefund(DispatchContext, Map)` | Storniert eine Rückerstattung |
| `RitaServices.ccCreditRefund(DispatchContext, Map)` | Führt eine Kredit-Rückerstattung durch |
| `RitaServices.ccRefund(DispatchContext, Map)` | Erstattet über RITA-API |
| `PcChargeApi` | Kapselt XML-Aufbau und Socket-Kommunikation mit dem PcCharge-Terminal; definiert alle Anfrage-/Antwortfelder als Konstanten |
| `RitaApi` | Kapselt XML-Aufbau und HTTP-Kommunikation mit dem RITA-Server; definiert alle Protokollfelder als Konstanten |

---

### Klasse: `PayPalEvents` (PayPal)
**Paket:** `org.apache.ofbiz.accounting.thirdparty.paypal`
**Typ:** Java-Klasse
**Zweck:** PayPal-Integration über das klassische Redirect-Verfahren (Website Payments Standard) mit IPN (Instant Payment Notification). Leitet Kunden zu PayPal weiter und verarbeitet asynchrone Zahlungsbestätigungen.

| Methode | Beschreibung |
|---|---|
| `callPayPal(HttpServletRequest, HttpServletResponse)` | Baut den PayPal-Weiterleitungs-Request auf (Betrag, Auftrag, Return-URLs) und leitet den Browser zu PayPal um |
| `payPalIPN(HttpServletRequest, HttpServletResponse)` | Empfängt und validiert PayPal-IPN-Nachrichten; bestätigt den Eingang zurück an PayPal und aktualisiert Auftragsstatus und Zahlungsbelege |
| `cancelPayPalOrder(HttpServletRequest, HttpServletResponse)` | Verarbeitet den Rücksprung nach Abbruch des Bezahlvorgangs bei PayPal und setzt den Auftrag zurück |

---

### Klassen: `SagePayPaymentServices`, `SagePayServices`, `SagePayUtil` (SagePay)
**Paket:** `org.apache.ofbiz.accounting.thirdparty.sagepay`
**Typ:** Java-Klassen
**Zweck:** Integration des SagePay-Gateways (heute Opayo) über das VSP-Direktprotokoll per HTTPS-POST. `SagePayPaymentServices` implementiert den Gateway-Adapter; `SagePayServices` kapselt die Low-Level-HTTP-Kommunikation; `SagePayUtil` bietet Hilfsklassen für Antwort-Strukturierung.

| Klasse/Methode | Beschreibung |
|---|---|
| `SagePayPaymentServices.ccAuth(DispatchContext, Map)` | Führt eine VSP-Direktautorisierung durch; liest Kreditkartendaten und Rechnungsadresse aus dem Kontext |
| `SagePayPaymentServices.ccCapture(DispatchContext, Map)` | Erfasst eine autorisierte SagePay-Transaktion |
| `SagePayPaymentServices.ccRefund(DispatchContext, Map)` | Erstattet über SagePay |
| `SagePayPaymentServices.ccRelease(DispatchContext, Map)` | Gibt eine Autorisierung frei |
| `SagePayServices.paymentAuthentication(DispatchContext, Map)` | Sendet eine Authentifizierungsanfrage (3D-Secure-Vorstufe) |
| `SagePayServices.paymentAuthorisation(DispatchContext, Map)` | Autorisiert eine Zahlung nach erfolgreicher Authentifizierung |
| `SagePayServices.paymentRelease(DispatchContext, Map)` | Gibt eine Autorisierung frei |
| `SagePayServices.paymentVoid(DispatchContext, Map)` | Storniert eine Transaktion |
| `SagePayServices.paymentRefund(DispatchContext, Map)` | Erstattet eine erfasste Zahlung |
| `SagePayUtil.buildCardAuthorisationPaymentResponse(...)` | Erstellt die standardisierte OFBiz-Gateway-Antwort-Map aus den SagePay-Rohdaten |

---

### Klassen: `ValueLinkServices`, `ValueLinkApi` (ValueLink)
**Paket:** `org.apache.ofbiz.accounting.thirdparty.valuelink`
**Typ:** Java-Klassen
**Zweck:** Integration der ValueLink-Geschenkkartenplattform (First Data). `ValueLinkApi` implementiert die vollständige kryptografische Infrastruktur: Schlüsselaustausch per Diffie-Hellman, Verschlüsselung per DES/3DES, PIN-Verschlüsselung. Unterstützt Aktivierung, Einlösung, Aufladung, Saldenabfrage und Transaktionshistorie.

| Klasse/Methode | Beschreibung |
|---|---|
| `ValueLinkServices.createKeys(DispatchContext, Map)` | Generiert KEK (Key Encryption Key) und Working Keys für die sichere Kommunikation |
| `ValueLinkServices.assignWorkingKey(DispatchContext, Map)` | Hinterlegt einen Working Key nach Schlüsselaustausch |
| `ValueLinkServices.activate(DispatchContext, Map)` | Aktiviert eine neue Geschenkkarte |
| `ValueLinkServices.linkPhysicalCard(DispatchContext, Map)` | Verknüpft eine physische Karte mit einem digitalen Konto |
| `ValueLinkServices.redeem(DispatchContext, Map)` | Löst einen Betrag von einer Geschenkkarte ein |
| `ValueLinkServices.reload(DispatchContext, Map)` | Lädt eine Geschenkkarte mit Guthaben auf |
| `ValueLinkServices.balanceInquire(DispatchContext, Map)` | Fragt den Saldo einer Geschenkkarte ab |
| `ValueLinkServices.transactionHistory(DispatchContext, Map)` | Ruft die Transaktionshistorie einer Karte ab |
| `ValueLinkServices.refund(DispatchContext, Map)` | Erstattet einen Betrag auf eine Karte |
| `ValueLinkServices.voidRedeem(DispatchContext, Map)` | Storniert eine Einlösung |
| `ValueLinkServices.giftCardProcessor(DispatchContext, Map)` | Payment-Gateway-Adapter: autorisiert Geschenkkartenzahlungen im OFBiz-Framework |
| `ValueLinkServices.giftCardRefund(DispatchContext, Map)` | Erstattet eine Geschenkkartenzahlung |
| `ValueLinkServices.giftCardPurchase(DispatchContext, Map)` | Verarbeitet den Kauf einer Geschenkkarte als Produkt |
| `ValueLinkApi.encryptPin(String)` | Verschlüsselt eine PIN mit dem aktuellen Working Key |
| `ValueLinkApi.decryptPin(String)` | Entschlüsselt eine PIN |
| `ValueLinkApi.send(String, Map)` | Sendet eine signierte und verschlüsselte Anfrage an den ValueLink-Server |
| `ValueLinkApi.outputKeyCreation(boolean, String)` | Generiert und gibt den Schlüssel-Setup-Output für die Ersteinrichtung aus |
| `ValueLinkApi.getInitialRequestMap(Map)` | Erstellt die Basis-Map für eine ValueLink-Anfrage (Merchant-ID, Datum, Terminal-ID) |

---

### Klasse: `WorldPayEvents` (WorldPay)
**Paket:** `org.apache.ofbiz.accounting.thirdparty.worldpay`
**Typ:** Java-Klasse
**Zweck:** WorldPay-Integration über das Redirect-/Hosted-Payment-Page-Verfahren. Leitet Kunden zur WorldPay-Zahlungsseite weiter und verarbeitet asynchrone Zahlungsbenachrichtigungen.

| Methode | Beschreibung |
|---|---|
| `worldPayRequest(HttpServletRequest, HttpServletResponse)` | Baut den WorldPay-Redirect-Request auf: liest Auftragsdaten, berechnet den Zahlungsbetrag, formatiert die WorldPay-URL und leitet den Browser um |
| `worldPayNotify(HttpServletRequest, HttpServletResponse)` | Empfängt asynchrone Zahlungsbenachrichtigungen von WorldPay (äquivalent zu PayPal IPN), validiert die Anfrage und aktualisiert Auftragsstatus sowie Zahlungsbelege |

---

## Groovy-Scripts nach Themengruppen

Die folgenden Klassen sind Groovy-Scripts (`extends groovy.lang.Script`) und liegen nur als kompiliertes Bytecode vor. Sie implementieren View-Logik, Daten-Aufbereitungen und leichtgewichtige Service-Delegates, die über das Groovy-Service-Framework aufgerufen werden.

### Rechnungsverarbeitung (invoice)

| Klasse | Funktion |
|---|---|
| `invoice.InvoiceServicesScript` | Groovy-Pendant zu `InvoiceServices`; delegiert Rechnungs-Services ans Service-Framework |
| `invoice.InvoiceEvents` | Event-Handler für rechnungsbezogene Benutzeraktionen |
| `invoice.EditInvoice` | Aufbereitung der Daten für die Rechnungsbearbeitungsmaske |
| `invoice.DisplayInvoiceAmounts` | Berechnet und stellt Rechnungsbeträge für die Anzeige bereit |
| `invoice.CreateApplicationList` | Erstellt die Liste offener Zahlungsanwendungen für eine Rechnung |
| `invoice.ListNotAppliedPayments` | Listet nicht zugeordnete Zahlungen zu einer Rechnung |
| `invoice.InvoiceReport` | Aufbereitung von Daten für Rechnungsberichte |
| `invoice.PrintInvoices` | Druckvorbereitung für Rechnungen |
| `invoice.GetAccountOrganizationAndClass` | Ermittelt Organisationskonto und -klasse für einen Rechnungskontext |
| `invoice.SampleServices` | Beispiel-Service-Implementierung (Referenz/Demo) |

### Zahlungsverarbeitung (payment)

| Klasse | Funktion |
|---|---|
| `payment.PaymentServices` | Groovy-Service-Delegate für Zahlungsdienste |
| `payment.DepositWithdrawPayments` | Verarbeitet Ein- und Auszahlungen über die UI |
| `payment.FindInvoicesByDueDate` | Listet Rechnungen nach Fälligkeitsdatum für Zahlungsläufe |
| `payment.ListNotAppliedInvoices` | Listet nicht bezahlte Rechnungen für die Zahlungszuordnungs-UI |
| `payment.ListNotAppliedPayments` | Listet nicht zugeordnete Zahlungen für die Zahlungszuordnungs-UI |
| `payment.BillingAccounts` | Aufbereitung der Abrechnungskonto-Übersicht |
| `payment.ManualTx` | Manuelle Transaktionserfassung über die UI |
| `payment.PrintChecks` | Druckvorbereitung für Schecks |

### Hauptbuch und Berichte (ledger/reports)

| Klasse | Funktion |
|---|---|
| `ledger.GeneralLedgerServicesScript` | Groovy-Delegate für GL-Dienste |
| `ledger.PartyPreferenceTooltipLabels` | Aufbereitung von Tooltip-Labels für Partei-Buchhaltungspräferenzen |
| `reports.BalanceSheet` | Berechnet Bilanz-Daten (Aktiva/Passiva) für einen Stichtag |
| `reports.ComparativeBalanceSheet` | Vergleichsbilanz für zwei Perioden |
| `reports.IncomeStatement` | Gewinn-und-Verlust-Rechnung |
| `reports.ComparativeIncomeStatement` | Vergleichs-GuV für zwei Perioden |
| `reports.CashFlowStatement` | Kapitalflussrechnung |
| `reports.ComparativeCashFlowStatement` | Vergleichende Kapitalflussrechnung |
| `reports.GlAccountTrialBalance` | Probebilanz für ein einzelnes GL-Konto |
| `reports.TrialBalance` | Gesamte Probebilanz |
| `reports.CostCenters` | Kostenstellenauswertung |
| `reports.TransactionTotals` | Buchungsgesamtbeträge |
| `reports.MonthSelection` | UI-Helper zur Monatsauswahl in Berichtsmasken |
| `reports.SalesInvoiceByProductCategorySummary` | Umsatzauswertung nach Produktkategorie |
| `reports.InvoiceAcctgTransEntryParameters` | Aufbereitung der Parameter für Rechnungs-Buchungseintrags-Berichte |

**Hilfsklassen (GroovyObject, kein Script):**
- `reports.AccountBalance`: Datenklasse zur Speicherung eines GL-Kontostandbetrags mit Sortierlogik
- `reports.AccountEntrySum`: Aggregationsklasse für Buchungseinträge
- `reports.RootClass` (Enum): Definiert die Wurzelkontenklassen (Aktiva, Passiva, Eigenkapital, Ertrag, Aufwand) für die Berichtshierarchie

### Administration (admin)

| Klasse | Funktion |
|---|---|
| `admin.AcctgAdminServices` | Administrative Buchhaltungsdienste (GL-Konto-Setup, Organisationskonfiguration) |
| `admin.FilterOutReceipts` | Filtert Zahlungseingänge aus Belegen für administrative Auswertungen heraus |
| `admin.ListInvoiceItemTypesGlAccount` | Listet GL-Konto-Zuordnungen für Rechnungspositionstypen |

### Transaktionen und Period-Management

| Klasse | Funktion |
|---|---|
| `transaction.AuthorizeTransaction` | UI-Script zur Autorisierung einer Transaktion |
| `transaction.CaptureTransaction` | UI-Script zur Erfassung einer Transaktion |
| `transaction.ViewGatewayResponse` | Aufbereitung der Gateway-Response-Details für die Anzeige |
| `period.GPeriodServices` | Groovy-Delegate für Periodenabschluss-Dienste |
| `period.EditCustomTimePeriod` | UI-Helper für die Pflege benutzerdefinierter Buchungsperioden |

### Weitere thematische Gruppen

| Klasse | Funktion |
|---|---|
| `agreement.AgreementServicesScript` | Groovy-Delegate für Vertragsdienste |
| `agreement.GetPartyNameForDate` | Ermittelt den Parteinamen zu einem Stichtag für Vertragsanzeigen |
| `ap.invoices.CommissionReport` | Aufbereitung von Kommissionsberichten (Accounts Payable) |
| `ap.invoices.CommissionRun` | Ausführung eines Provisionsabrechnungslaufs |
| `ar.BatchPayments` | Stapelverarbeitung von eingehenden Zahlungen (Accounts Receivable) |
| `budget.BudgetServices` | Groovy-Delegate für Budgetverwaltungsdienste |
| `chartofaccounts.TaxAuthorityGlAccounts` | Aufbereitung der GL-Konto-Zuordnungen für Steuerbehörden im Kontenplan |
| `fixedasset.FixedAssetServices` | Groovy-Delegate für Anlagevermögensdienste (Abschreibungen, Umbuchungen) |
| `fixedasset.FixedAssetGeoLocation` | Verwaltet Geolokalisierungsdaten für Anlagegüter |
| `order.BillingAccountOrders` | Listet Aufträge zu einem Abrechnungskonto |
| `rate.RateServices` | Dienste für Stunden- und Kostensätze |
| `tax.TaxAuthorityServicesScript` | Groovy-Delegate für Steuerbehörden-Dienste |

---

## Test-Klassen (Zusammenfassung)

### Java-Tests (`org.apache.ofbiz.accounting.test`)

| Klasse | Beschreibung |
|---|---|
| `FinAccountTests` | Integrationstests für Finanzkonto-Operationen: Erstellung, Einzahlung (100 EUR), Abhebung (50 EUR) mit Saldo-Validierung |

### Groovy-Tests (`org.apache.ofbiz.accounting.accounting`)

Alle Klassen erben von `OFBizTestCase` und sind automatisch generierte Testklassen (erkennbar am `Auto`-Präfix). Sie testen die Buchungslogik über das Service-Framework und decken folgende Bereiche ab:

| Klasse | Getesteter Bereich |
|---|---|
| `AutoAcctgAdminTests` | Administrative Buchhaltungsdienste |
| `AutoAcctgAgreementTests` | Vertragsmanagement und Provisionen |
| `AutoAcctgBudgetTests` | Budgetverwaltung |
| `AutoAcctgCostTests` | Kostenrechnung |
| `AutoAcctgFinAccountTests` | Finanzkonten |
| `AutoAcctgFixedAssetTests` | Anlagevermögen |
| `AutoAcctgInvoiceTests` | Rechnungsstellung |
| `AutoAcctgLedgerTests` | Hauptbuch |
| `AutoAcctgPaymentGatewayTests` | Payment-Gateway-Operationen |
| `AutoAcctgPaymentTests` | Zahlungsverarbeitung |
| `AutoAcctgTransPurchaseTests` | Einkaufsbuchungen |
| `AutoAcctgTransSalesTests` | Verkaufsbuchungen |
| `AutoInvoiceTests` | Rechnungsautomatisierung |
| `AutoPaymentTests` | Zahlungsautomatisierung |
| `FixedAssetTests` | Anlagevermögen (manuell) |
| `InvoicePerShipmentTests` | Lieferungsbasierte Fakturierung |
| `PaymentApplicationTests` | Zahlungsabgleich |
| `RateTests` | Kostensatzverwaltung |
