## Modul: marketing

### Überblick

Das `marketing`-Modul implementiert Kampagnen- und Kontaktlistenverwaltung, Kampagnenauswertung sowie Vertriebsunterstützung (Sales Force Automation) in Apache OFBiz. Es umfasst die Newsletter-Anmeldung und -Abmeldung, das Tracking von Website-Besuchern und Bestellungen über Tracking-Codes sowie SFA-Funktionen zur Lead-Verwaltung, Konvertierung von Leads zu Kontakten und zum Zusammenführen von Kontaktdatensätzen. Ergänzende Groovy-Scripts liefern Berichtsdaten zu E-Mail-Kommunikation, Kampagnenleistung und Tracking-Code-Konversionen.

### Submodule

| Paket | Beschreibung |
|---|---|
| `org.apache.ofbiz.marketing.marketing` | Kernservices für Kontaktlisten: Newsletter-Anmeldung, Mitgliedschaftsverwaltung, Kontaktlistenpflege |
| `org.apache.ofbiz.marketing.marketing.contact` | Groovy-Script zur Ermittlung der Marketing-E-Mail-Adresse des Kontaktlisten-Eigentümers |
| `org.apache.ofbiz.marketing.marketing.reports` | Groovy-Scripts für Kampagnen-, E-Mail-Status- und Tracking-Code-Berichte |
| `org.apache.ofbiz.marketing.marketing.test` | Groovy-basierte Integrationstests für Kontaktlisten-Services |
| `org.apache.ofbiz.marketing.report` | Java-Hilfsklasse zur Berechnung von Konversionsraten für Berichts-Scripts |
| `org.apache.ofbiz.marketing.tracking` | HTTP-Event-Handler für die Erfassung, Verarbeitung und Cookie-Verwaltung von Tracking-Codes |
| `org.apache.ofbiz.marketing.sfa` | SFA-Scripts: Lead-Anlage, Lead-Konvertierung, Kontakt-Zusammenführung und Account-Erstellung |
| `org.apache.ofbiz.marketing.sfa.account` | Groovy-Script zur Anlage von Unternehmenskonten mit Rollen- und Beziehungsverknüpfung |
| `org.apache.ofbiz.marketing.sfa.lead` | Groovy-Script mit vollständiger Lead-Lebenszyklusverwaltung |

---

### Klasse: `MarketingServices`

**Paket:** `org.apache.ofbiz.marketing.marketing`
**Typ:** Java-Klasse (Service)
**Zweck:** Stellt OFBiz-Services für die Verwaltung von Kontaktlisten-Mitgliedschaften bereit. Implementiert die Newsletter-Anmeldung mit E-Mail-Validierung, Duplikatsprüfung und Status-Steuerung sowie das gezielte Löschen ausstehender Anmeldeanforderungen.

| Methode | Beschreibung |
|---|---|
| `signUpForContactList(dctx, context)` | Meldet eine E-Mail-Adresse für eine Kontaktliste an: validiert die E-Mail-Adresse, prüft auf bereits vorhandene Mitgliedschaften im Status `CLPT_ACCEPTED` (Fehler) oder `CLPT_PENDING` (löscht alte Anfrage und legt neue an), legt bei unbekannter Partei einen Platzhalter-Eintrag (`_NA_`) an und erstellt einen `ContactListParty`-Eintrag mit Status `CLPT_PENDING` |
| `deleteContactListParty(dctx, context)` | Löscht einen ausstehenden Kontaktlisten-Eintrag: entfernt zunächst alle verknüpften `ContactListPartyStatus`-Einträge und löscht dann den `ContactListParty`-Datensatz; gibt eine Bestätigungsmeldung mit den Schlüsselfeldern zurück |

---

### Klasse: `ReportHelper`

**Paket:** `org.apache.ofbiz.marketing.report`
**Typ:** Java-Klasse (final, nicht instanziierbar)
**Zweck:** Statische Hilfsklasse zur Berechnung von Konversionsraten. Verbindet Besuchs- und Bestelldaten über einen gemeinsamen Schlüssel und berechnet für jeden Eintrag die Konversionsrate als Quotient aus Bestellanzahl und Besuchsanzahl. Wird von den Berichts-Scripts `MarketingCampaignReport` und `TrackingCodeReport` aufgerufen.

| Methode | Beschreibung |
|---|---|
| `calcConversionRates(visits, orders, keyFieldName)` | Iteriert über eine Liste von Besuchsdatensätzen (aggregiert nach `keyFieldName`), sucht für jeden Eintrag die zugehörigen Bestelldaten, berechnet Besuchsanzahl, Bestellanzahl, Bestellbetrag (`grandTotal`) und Konversionsrate (Bestellungen / Besuche); gibt `0.0` zurück, wenn keine Bestellungen vorhanden oder die Besuchsanzahl null ist |

---

### Klasse: `TrackingCodeEvents`

**Paket:** `org.apache.ofbiz.marketing.tracking`
**Typ:** Java-Klasse (Event-Handler)
**Zweck:** HTTP-Event-Handler für die gesamte Tracking-Code-Verarbeitung in OFBiz. Erfasst Tracking-Codes aus URL-Parametern und Cookies, schreibt Besuchszuordnungen (`TrackingCodeVisit`), setzt nachverfolgbare und abrechenbare Cookies mit konfigurierbarer Lebensdauer, verwaltet Partner-Tracking-Codes durch automatische Anlage fehlender Einträge anhand von Standardwerten und steuert den Zugriff über zugriffsbeschränkte Tracking-Codes.

| Methode | Beschreibung |
|---|---|
| `checkTrackingCodeUrlParam(request, response)` | Liest den Tracking-Code aus den URL-Parametern `autoTrackingCode` oder `atc`, sucht den Datensatz in `TrackingCode` und delegiert an `processTrackingCode()` mit Quelle `TKCDSRC_URL_PARAM` |
| `checkPartnerTrackingCodeUrlParam(request, response)` | Verarbeitet Partner-Tracking-Codes aus dem URL-Parameter `ptc`; legt bei unbekannten Codes einen neuen `TrackingCode`-Eintrag vom Typ `PARTNER_MGD` an – wahlweise basierend auf einem konfigurierbaren Standard-Tracking-Code (`dtc`) oder mit fest hinterlegten Standardwerten |
| `processTrackingCode(trackingCode, request, response, sourceEnumId)` | Kernlogik der Tracking-Code-Verarbeitung: prüft Gültigkeitszeitraum, schreibt `TrackingCodeVisit`, setzt nachverfolgbares Cookie (`TKCDT_*`) und abrechenbares Cookie (`TKCDB_*`) mit der konfigurierten Lebensdauer, speichert optional Site-ID und Zeitstempel-Cookie, setzt Session-Attribute für Logo- und CSS-Überschreibung sowie Produktkatalog, führt ggf. Redirect auf `redirectUrl` aus |
| `checkTrackingCodeCookies(request, response)` | Liest alle Cookies des Typs `TKCDT_*` aus dem Request, prüft Gültigkeit des jeweiligen Tracking-Codes und schreibt für jeden aktiven Code einen `TrackingCodeVisit`-Eintrag mit Quelle `TKCDSRC_COOKIE` |
| `checkAccessTrackingCode(request, response)` | Prüft, ob ein gültiger Zugriffs-Tracking-Code (`ACCESS`-Typ) vorhanden ist – aus URL-Parameter oder Cookie; gibt bei fehlendem oder abgelaufenem Code `":_protect_:"` zurück, um den Zugriff zu verweigern |
| `removeAccesTrackingCodeCookie(request, response)` | Löscht alle Cookies, deren Name auf `_ACCESS` endet, durch Setzen von `maxAge=0` |
| `makeTrackingCodeOrders(request)` | Liest abrechenbare (`TKCDB_*`) und nachverfolgbare (`TKCDT_*`) Cookies sowie Site-ID und Referenzzeitstempel aus dem Request und erzeugt eine Liste von `TrackingCodeOrder`-Werten für die Auftragszuordnung |

---

### Groovy-Scripts: Kontaktlisten-Abfrage (`contact`)

**Paket:** `org.apache.ofbiz.marketing.marketing.contact`
**Typ:** Groovy-Script

| Script | Fachliche Funktion |
|---|---|
| `GetContactListMarketingEmail` | Lädt die Kontaktliste anhand der `contactListId`, ermittelt den zugeordneten Eigentümer-Datensatz (`OwnerParty`) und sucht dessen bevorzugte Marketing-E-Mail-Adresse (`MARKETING_EMAIL`); fällt auf `PRIMARY_EMAIL` zurück, falls keine Marketing-E-Mail hinterlegt ist; gibt das erste gefundene `PartyContactMechPurpose`-Objekt zurück |

---

### Groovy-Scripts: Berichte (`reports`)

**Paket:** `org.apache.ofbiz.marketing.marketing.reports`
**Typ:** Groovy-Scripts (Berichts-Datenbeschaffung)

| Script | Fachliche Funktion |
|---|---|
| `EmailStatusReport` | Stellt gefilterte `CommunicationEventAndRole`-Datensätze für den E-Mail-Statusbericht bereit; unterstützt Filter auf `entryDate` (Von/Bis), `partyIdTo`, `partyIdFrom`, `statusId` und `roleStatusId`; schränkt das Ergebnis auf Einträge mit `roleTypeId = ADDRESSEE` ein |
| `MarketingCampaignReport` | Berechnet die Konversionsraten einer Kampagne: fragt `MarketingCampaignAndVisit` und `MarketingCampaignAndOrderHeader` gefiltert nach Kampagnen-ID und Zeitraum ab, aggregiert Besuche und Bestellungen je Kampagne und ruft `ReportHelper.calcConversionRates()` auf |
| `PartyStatusReport` | Stellt gefilterte `ContactListPartyStatus`-Datensätze bereit; unterstützt Filter auf Eintrittsdatum (`fromDate`), Statusdatum (`statusDate`), Ablaufdatum (`thruDate`), `contactListId` und `statusId` |
| `TrackingCodeReport` | Berechnet die Konversionsraten je Tracking-Code: fragt `TrackingCodeAndVisit` und `TrackingCodeAndOrderHeader` gefiltert nach Tracking-Code-ID und Zeitraum ab und ruft `ReportHelper.calcConversionRates()` auf |

---

### Groovy-Scripts: Tests (`test`)

**Paket:** `org.apache.ofbiz.marketing.marketing.test`
**Typ:** Groovy-Script (Integrationstest, erweitert `OFBizTestCase`)

| Script | Fachliche Funktion |
|---|---|
| `MarketingTests` | Integrationstest `testCreateAndUpdateContactList`: legt eine Kontaktliste vom Typ `ANNOUNCEMENT` mit `contactMechTypeId = EMAIL_ADDRESS` an, prüft die Persistenz über `ServiceUtil.isSuccess()` und eine direkte Entity-Abfrage, aktualisiert die Liste auf `contactMechTypeId = POSTAL_ADDRESS` und prüft die Aktualisierung nach `contactList.refresh()` |

---

### Groovy-Scripts: SFA – Account-Verwaltung (`sfa.account`)

**Paket:** `org.apache.ofbiz.marketing.sfa.account`
**Typ:** Groovy-Script (Service)

| Script | Fachliche Funktion |
|---|---|
| `AccountServices` | Stellt die Funktion `createAccount()` bereit: ruft `createPartyGroupRoleAndContactMechs` mit der Rolle `ACCOUNT` auf, stellt anschließend über `ensurePartyRole` die `OWNER`-Rolle des eingeloggten Benutzers sicher und legt eine `ACCOUNT`-Parteienbeziehung zwischen Eigentümer und dem neuen Konto an |

---

### Groovy-Scripts: SFA – Lead-Verwaltung (`sfa` und `sfa.lead`)

**Paket:** `org.apache.ofbiz.marketing.sfa` / `org.apache.ofbiz.marketing.sfa.lead`
**Typ:** Groovy-Scripts (Services und Datenbeschaffung)

| Script | Fachliche Funktion |
|---|---|
| `LeadServices` (`createLead()`) | Legt einen neuen Lead an: validiert, dass mindestens Vor- und Nachname oder ein Firmenname angegeben sind; erstellt Person und Rolle (`LEAD`) über `createPersonRoleAndContactMechs`, verknüpft den Lead mit dem Eigentümer via `LEAD_OWNER`-Beziehung, setzt den Status `LEAD_ASSIGNED`; legt bei Vorhandensein eines Firmennamens optional eine Unternehmensgruppe (`ACCOUNT_LEAD`) an und verknüpft beide Datensätze über eine `EMPLOYMENT`-Beziehung; speichert bei Bedarf eine Datenquelle (`PartyDataSource`) |
| `LeadServices` (`convertLeadToContact()`) | Konvertiert einen Lead zu einem Kontakt: setzt auslaufende `LEAD_OWNER`- und `EMPLOYMENT`-Beziehungen durch `thruDate = now`, stellt die `ACCOUNT`-Rolle des Unternehmens sicher, legt neue `ACCOUNT`-Eigentümerbeziehung und `EMPLOYMENT`-Beziehung zwischen Konto und Kontakt an und setzt den Status aller beteiligten Parteien auf `LEAD_CONVERTED` |
| `LeadServices` (`resolvePartyProcessMap()`) | Hilfsmethode: wandelt Formulardaten über `SimpleMapProcessor` mit dem `partyGroup`-Prozessor aus `PartyMapProcs.xml` in eine für `createPartyGroup` geeignete Map um |
| `CloneLead` | Liest alle relevanten Stammdaten eines bestehenden Leads (Person, Stellenbezeichnung, Unternehmensgruppe, Postanschrift, E-Mail, Telefon, Datenquelle) und stellt sie als `contactDetailMap` im Kontext bereit, um das Formular für einen geklonten Lead vorzubefüllen |
| `MergeContacts` | Bereitet die Zusammenführungsansicht zweier Kontakte vor: iteriert über eine Liste mit `partyIdFrom` und `partyIdTo`, lädt für jeden Kontakt Person, Postanschrift (inkl. Geo-Daten für Bundesland und Land), primäre E-Mail und Telefon und sammelt die Detaildaten als `contactInfoList` im Kontext |