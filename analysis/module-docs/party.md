## Modul: party

### Überblick

Das Modul `party` ist die zentrale Stammdatenverwaltung für alle Akteure im OFBiz-System. Es modelliert Personen, Organisationen (PartyGroups) und deren Beziehungen untereinander sowie alle zugehörigen Kontakt- und Kommunikationsdaten. Fachlich deckt das Modul die Verwaltung von Stammdaten für Kunden, Lieferanten, Mitarbeiter und sonstige Geschäftspartner ab, einschließlich Adressen, Telefonnummern, E-Mail-Adressen, Kommunikationsereignissen und Website-Besuchen.

### Submodule

- **`party.communication`** — Kommunikationsereignisse (E-Mail, FTP-Transfer): Versand, Empfang, Archivierung
- **`party.contact`** — Kontaktmechanismen (Postadresse, Telefon, E-Mail, FTP): Verwaltung und Abfrage
- **`party.content`** — Inhalte und Medien, die einem Party-Datensatz zugeordnet sind
- **`party.party`** — Kern-Domäne: Party-Stammdaten, Rollen, Beziehungen, Suche, Berechtigungen
- **`party.visit`** — Website-Besuchererfassung und Session-Tracking

---

### Klasse: `CommunicationEventServices`

**Paket:** `org.apache.ofbiz.party.communication`
**Typ:** Java-Klasse
**Zweck:** Implementiert die OFBiz-Services für die Verwaltung von Kommunikationsereignissen. Stellt den Versand von E-Mails und FTP-Transfers als CommunicationEvent bereit, verarbeitet eingehende E-Mails und persistiert diese als Kommunikationshistorie.

| Methode | Beschreibung |
|---|---|
| `sendCommEventAsEmail(DispatchContext, Map)` | Sendet ein als `EMAIL_COMMUNICATION` erfasstes CommunicationEvent per E-Mail, inkl. Anhänge und CC/BCC-Empfänger aus der Rollenliste des Events. Bei Adressfehlern wird das Event als `COM_BOUNCED` markiert. |
| `sendCommEventAsFtp(DispatchContext, Map)` | Überträgt die Inhalte eines als `FILE_TRANSFER_COMM` erfassten Events per FTP. Bei mehreren Inhalten werden pro Datei Kind-Events angelegt. Fehler werden als Bounce-Status am Event notiert. |
| `sendEmailToContactList(DispatchContext, Map)` | Verschickt ein CommunicationEvent-E-Mail an alle Mitglieder einer Kontaktliste (Massen-E-Mail). |
| `setCommEventComplete(DispatchContext, Map)` | Setzt den Status eines CommunicationEvents auf `COM_COMPLETE` und trägt den Endzeitpunkt ein. |
| `createCommEventFromFtpTransfer(DispatchContext, Map)` | Erstellt ein neues CommunicationEvent vom Typ `FILE_TRANSFER_COMM` für eine bereits vorbereitete FTP-Übertragung, verknüpft den Content-Datensatz. |
| `createCommEventFromEmail(DispatchContext, Map)` | Legt ein neues CommunicationEvent vom Typ `EMAIL_COMMUNICATION` auf Basis von Absender- und Empfängeradressen an. Sucht automatisch die passenden Party- und ContactMech-IDs. |
| `updateCommEventAfterEmail(DispatchContext, Map)` | Aktualisiert ein bestehendes CommunicationEvent nach dem Versand einer E-Mail: trägt Message-ID, Betreff, Versandzeit und E-Mail-Adressen nach und speichert Anhänge. |
| `storeIncomingEmail(DispatchContext, Map)` | Verarbeitet eine eingehende E-Mail und speichert sie als CommunicationEvent (Typ `AUTO_EMAIL_COMM`). Erkennt Spam-Markierungen, Duplikate und löst Absender/Empfänger zu Party-IDs auf. Legt Anhänge und Rollen (TO, CC, BCC) als verknüpfte Datensätze an. |
| `processBouncedMessage(DispatchContext, Map)` | Analysiert eingehende Delivery-Status-Berichte (Bounce-E-Mails), sucht das ursprüngliche CommunicationEvent anhand der Message-ID und markiert es als `COM_BOUNCED`. |
| `logIncomingMessage(DispatchContext, Map)` | Schreibt Metadaten einer eingehenden E-Mail (Betreff, Teileanzahl, Anhänge) zu Diagnosezwecken ins Log. |
| `markCommunicationAsRead(HttpServletRequest, HttpServletResponse)` | HTTP-Event-Handler: Setzt den Lesestatus eines CommunicationEvents für den Empfänger auf "gelesen". Wird per Tracking-Pixel in E-Mails aufgerufen; liefert ein transparentes GIF-Bild zurück. |

---

### Klasse: `CommunicationEventServicesScript`

**Paket:** `org.apache.ofbiz.party.communication`
**Typ:** Groovy-Script
**Zweck:** Groovy-Script — ausgeführt über OFBiz Service-Engine. Stellt ergänzende Kommunikations-Services bereit, die in Groovy implementiert sind, insbesondere für die vollständige CRUD-Verwaltung von CommunicationEvents sowie für Rollen- und Statusoperationen.

| Methode | Beschreibung |
|---|---|
| `createCommunicationEvent()` | Legt ein neues CommunicationEvent in der Datenbank an (mit Berechtigungsprüfung). |
| `createCommunicationEventWithoutPermission()` | Erstellt ein CommunicationEvent ohne vorherige Berechtigungsprüfung, z. B. für automatisierte Systemprozesse. |
| `updateCommunicationEvent()` | Aktualisiert die Felder eines bestehenden CommunicationEvents. |
| `deleteCommunicationEvent()` | Löscht ein CommunicationEvent samt zugehöriger Rollen und Inhaltsverknüpfungen. |
| `deleteCommunicationEventWorkEffort()` | Entfernt die Verknüpfung zwischen einem CommunicationEvent und einem WorkEffort (Aufgabe). |
| `createCommunicationEventRole()` | Fügt eine Partei mit einer definierten Rolle (TO, CC, BCC, ADDRESSEE) zu einem CommunicationEvent hinzu. |
| `removeCommunicationEventRole()` | Entfernt eine Partei-Rolle aus einem CommunicationEvent. |
| `sendEmailDated()` | Löst den E-Mail-Versand für ein datumsbeschränktes CommunicationEvent aus. |
| `setCommunicationEventStatus()` | Setzt den Status eines CommunicationEvents auf einen gewünschten Zielstatus. |
| `setCommEventRoleToRead()` | Markiert die Rolle einer Partei an einem CommunicationEvent als gelesen. |
| `setCommunicationEventRoleStatus()` | Setzt den Status der Rollenzugehörigkeit einer Partei zu einem CommunicationEvent. |
| `sendContactUsEmailToCompany()` | Sendet eine Kontaktformular-E-Mail an die Unternehmens-E-Mail-Adresse. |

---

### Groovy-Scripts: Abfrage-Scripts im Subpaket `party.communication`

**Paket:** `org.apache.ofbiz.party.communication`
**Typ:** Groovy-Scripts (Datenbankabfragen / Ansichtsvorbereitungen)

Die folgenden Scripts werden über die OFBiz Service-Engine ausgeführt und stellen Daten für Views bereit:

| Klasse | Fachliche Funktion |
|---|---|
| `FindCommEventContactMechs` | Ermittelt die Kontaktmechanismen (E-Mail-Adressen, Telefonnummern) aller an einem CommunicationEvent beteiligten Parteien für die Anzeige im UI. |
| `GetMyCommunicationEventRole` | Liest die Rolle der aktuell angemeldeten Partei an einem CommunicationEvent aus (z. B. Absender, Empfänger). |
| `GetPartyEmailAttachment` | Lädt Anhänge zu einer E-Mail eines Party-Kommunikationsereignisses für die Anzeige oder den Download. |
| `GetPartyEmailFromCommEventInfo` | Ermittelt die E-Mail-Adresse einer Partei anhand der Informationen eines CommunicationEvents. |
| `ListCommunications` | Listet alle CommunicationEvents für eine Partei oder einen Filter auf (Kommunikationsübersicht). |
| `RecentVisitor` | Liefert Informationen zu kürzlich auf der Webseite aktiven Besuchern für die Anzeige in Kommunikations-Dashboards. |

---

### Klasse: `ContactHelper`

**Paket:** `org.apache.ofbiz.party.contact`
**Typ:** Java-Klasse (finale Utility-Klasse, nicht instanziierbar)
**Zweck:** Stellt Hilfsmethoden bereit, um Kontaktmechanismen einer Partei nach Typ oder Verwendungszweck abzufragen sowie Kreditkartendaten für die Anzeige zu formatieren.

| Methode | Beschreibung |
|---|---|
| `getContactMech(GenericValue party, boolean includeOld)` | Liefert alle Kontaktmechanismen einer Partei, wahlweise einschließlich historisch abgelaufener Einträge. |
| `getContactMechByType(GenericValue party, String contactMechTypeId, boolean includeOld)` | Filtert die Kontaktmechanismen einer Partei auf einen bestimmten Typ (z. B. `POSTAL_ADDRESS`, `EMAIL_ADDRESS`). |
| `getContactMechByPurpose(GenericValue party, String contactMechPurposeTypeId, boolean includeOld)` | Filtert die Kontaktmechanismen einer Partei auf einen definierten Verwendungszweck (z. B. Rechnungsadresse, Lieferadresse). |
| `getContactMech(GenericValue party, String purposeTypeId, String typeId, boolean includeOld)` | Kombinierte Filterung nach Typ und Verwendungszweck; bildet die Grundlage aller anderen `getContactMech`-Varianten. |
| `formatCreditCard(GenericValue creditCardInfo)` | Formatiert Kreditkarteninformationen für die Anzeige: Kartentyp, die letzten vier Stellen der Kartennummer und das Ablaufdatum. |

---

### Klasse: `ContactMechServices`

**Paket:** `org.apache.ofbiz.party.contact`
**Typ:** Java-Klasse
**Zweck:** Implementiert die OFBiz-Service-Engine-Methoden für die vollständige Lebenszyklusverwaltung von Kontaktmechanismen (Adressen, Telefonnummern, E-Mail-Adressen). Arbeitet mit der OFBiz-Historienpflege: Änderungen erzeugen neue Datensätze mit neuer ID, der alte Datensatz wird mit einem `thruDate` deaktiviert.

| Methode | Beschreibung |
|---|---|
| `createContactMech(DispatchContext, Map)` | Legt einen neuen allgemeinen Kontaktmechanismus an (nicht für Postadresse oder Telefon, da dafür eigene Services vorgesehen sind). Prüft Schreibberechtigung (`PARTYMGR_PCM_CREATE`). |
| `updateContactMech(DispatchContext, Map)` | Aktualisiert einen allgemeinen Kontaktmechanismus mit Historisierung: Der alte Eintrag wird abgelaufen, ein neuer mit aktuellen Daten angelegt. |
| `deleteContactMech(DispatchContext, Map)` | Deaktiviert die Verknüpfung eines Kontaktmechanismus zur Partei durch Setzen des `thruDate` auf jetzt. |
| `createPostalAddress(DispatchContext, Map)` | Erstellt eine neue Postadresse (Straße, PLZ, Ort, Land) als Kontaktmechanismus für eine Partei. |
| `updatePostalAddress(DispatchContext, Map)` | Ändert eine bestehende Postadresse mit vollständiger Historisierung (alter Eintrag wird archiviert). |
| `createTelecomNumber(DispatchContext, Map)` | Legt eine neue Telefonnummer (Ländervorwahl, Ortsvorwahl, Nummer) als Kontaktmechanismus an. |
| `updateTelecomNumber(DispatchContext, Map)` | Ändert eine bestehende Telefonnummer mit Historisierung. |
| `createEmailAddress(DispatchContext, Map)` | Legt eine neue E-Mail-Adresse als Kontaktmechanismus an (delegiert an `createContactMech` mit Typ `EMAIL_ADDRESS`). |
| `updateEmailAddress(DispatchContext, Map)` | Ändert eine bestehende E-Mail-Adresse (delegiert an `updateContactMech`). |
| `createPartyContactMechPurpose(DispatchContext, Map)` | Verknüpft einen bereits bestehenden Kontaktmechanismus mit einem Verwendungszweck (z. B. Rechnungsadresse, Lieferadresse). Verhindert Doppelzuordnungen. |
| `getPartyContactMechValueMaps(DispatchContext, Map)` | Liefert alle Kontaktmechanismen einer Partei als strukturierte Map-Liste, die UI-Formulare direkt befüllen kann. |
| `copyPartyContactMechs(DispatchContext, Map)` | Kopiert alle aktiven Kontaktmechanismen einer Quellpartei auf eine Zielpartei, einschließlich der Verwendungszwecke. |
| `createEmailAddressVerification(DispatchContext, Map)` | Erzeugt einen kryptografisch gesicherten Verifikations-Hash für eine E-Mail-Adresse und speichert ihn mit einem Ablaufdatum für den E-Mail-Bestätigungsprozess. |

---

### Klasse: `ContactMechServicesScript`

**Paket:** `org.apache.ofbiz.party.contact`
**Typ:** Groovy-Script
**Zweck:** Groovy-Script — ausgeführt über OFBiz Service-Engine. Ergänzt die Java-seitigen ContactMechServices um Groovy-implementierte Services, insbesondere für die Verwaltung von FTP-Adressen, State/Province-Validierung und E-Mail-Verifikationsbenachrichtigungen.

| Methode | Beschreibung |
|---|---|
| `updateContactMech()` | Aktualisiert einen allgemeinen Kontaktmechanismus (Groovy-Variante mit zusätzlicher Validierungslogik). |
| `hasValidStateProvince(String countryGeoId, String stateProvinceGeoId)` | Prüft, ob eine Bundesland/Provinz-Angabe für das angegebene Land gültig ist. |
| `createPostalAddress()` | Legt eine neue Postadresse an (Groovy-Variante). |
| `updatePostalAddress()` | Ändert eine bestehende Postadresse (Groovy-Variante). |
| `createTelecomNumber()` | Legt eine neue Telefonnummer an (Groovy-Variante). |
| `updateTelecomNumber()` | Ändert eine bestehende Telefonnummer (Groovy-Variante). |
| `createEmailAddress()` | Legt eine neue E-Mail-Adresse an (Groovy-Variante). |
| `updateEmailAddress()` | Ändert eine bestehende E-Mail-Adresse (Groovy-Variante). |
| `createFtpAddress()` | Legt eine neue FTP-Server-Adresse als Kontaktmechanismus an. |
| `updateFtpAddressWithHistory()` | Ändert eine FTP-Adresse mit Historisierung: Der alte Eintrag wird archiviert, ein neuer angelegt. |
| `createPartyFtpAddress()` | Verknüpft eine FTP-Adresse direkt mit einer Partei. |
| `updatePartyFtpAddress()` | Aktualisiert die Verknüpfung einer FTP-Adresse mit einer Partei. |
| `sendVerifyEmailAddressNotification()` | Verschickt eine Bestätigungs-E-Mail mit Verifikationslink an eine neu eingetragene E-Mail-Adresse. |
| `verifyEmailAddress()` | Prüft einen E-Mail-Verifikations-Hash und markiert die Adresse bei Gültigkeit als bestätigt. |

---

### Klasse: `ContactMechWorker`

**Paket:** `org.apache.ofbiz.party.contact`
**Typ:** Java-Klasse (finale Utility-Klasse, nicht instanziierbar)
**Zweck:** Stellt Low-Level-Abfragemethoden bereit, um Kontaktmechanismen für Parteien, Lagerorte (Facilities), Bestellungen und Arbeitsaufgaben (WorkEfforts) als strukturierte Maps zu laden. Wird von Services und View-Preparern verwendet.

| Methode | Beschreibung |
|---|---|
| `getPartyContactMechValueMaps(Delegator, String partyId, boolean showOld)` | Lädt alle Kontaktmechanismen einer Partei als Liste von Maps, die jeweils ContactMech, PartyContactMech, den typspezifischen Untertyp (PostalAddress, TelecomNumber, FtpAddress) und die zugeordneten Verwendungszwecke enthalten. |
| `getPartyContactMechValueMaps(Delegator, String partyId, Timestamp date, String contactMechTypeId)` | Wie oben, jedoch mit Stichtagsfilterung und optionaler Einschränkung auf einen Kontaktmechanismus-Typ. |
| `getFacilityContactMechValueMaps(Delegator, String facilityId, boolean showOld)` | Lädt alle Kontaktmechanismen eines Lagerorts (Facility) analog zur Party-Variante. |
| `getOrderContactMechValueMaps(Delegator, String orderId)` | Liefert die Kontaktmechanismen einer Bestellung (Liefer- und Rechnungsadressen). |
| `getWorkEffortContactMechValueMaps(Delegator, String workEffortId)` | Liefert die Kontaktmechanismen zu einer Arbeitsaufgabe (aktive Einträge). |
| `getContactMechAndRelated(ServletRequest, String partyId, Map target)` | Befüllt eine View-Ziel-Map mit allen für das Kontaktmechanismus-Bearbeiten-Formular benötigten Daten: aktueller Eintrag, Typ, Verwendungszwecke, verfügbare Aktionen. |
| `getFacilityContactMechByPurpose(Delegator, String facilityId, List purposeTypes)` | Sucht für einen Lagerort den ersten aktiven Kontaktmechanismus für einen der angegebenen Verwendungszwecke (z. B. Versandadresse). |
| `getFacilityContactMechAndRelated(ServletRequest, String facilityId, Map target)` | Befüllt eine View-Ziel-Map für das Bearbeiten von Facility-Kontaktmechanismen. |
| `getPartyPostalAddresses(ServletRequest, String partyId, String curContactMechId)` | Liefert alle aktiven Postadressen einer Partei außer der aktuell bearbeiteten, für Auswahlfelder im Formular. |
| `getCurrentPostalAddress(ServletRequest, String partyId, String curContactMechId)` | Lädt die aktuell ausgewählte Postadresse einer Partei zusammen mit Verwendungszwecken für die Formularanzeige. |
| `isUspsAddress(GenericValue postalAddress)` | Prüft anhand eines konfigurierbaren Musters, ob eine Adresse dem USPS-Format entspricht. |
| `isCompanyAddress(GenericValue postalAddress, String companyPartyId)` | Prüft, ob eine Adresse mit einer der Firmenadressen einer bestimmten Organisation übereinstimmt (normalisierter Adressvergleich). |
| `getContactMechAttribute(Delegator, String contactMechId, String attrName)` | Liest einen benannten Zusatzattributwert eines Kontaktmechanismus aus der `ContactMechAttribute`-Tabelle. |
| `getPostalAddressPostalCodeGeoId(GenericValue postalAddress, Delegator)` | Ermittelt die Geo-ID für die Postleitzahl einer Adresse; aktualisiert den Datensatz bei Treffer automatisch. |
| `urlEncodePostalAddress(GenericValue postalAddress)` | Formatiert eine Postadresse als URL-kodierte Zeichenkette (z. B. für die Übergabe an Kartendienste). |

---

### Klasse: `PartyContentWrapper`

**Paket:** `org.apache.ofbiz.party.content`
**Typ:** Java-Klasse (implementiert `ContentWrapper`)
**Zweck:** Kapselt den Zugriff auf die dem Party-Datensatz zugeordneten Content-Elemente (z. B. Profilbilder, Beschreibungstexte). Stellt gecachte Render-Methoden bereit, die Content-Typen auflösen, rendern und als String zurückgeben.

| Methode | Beschreibung |
|---|---|
| `get(String contentTypeId, boolean useCache, String encoderType)` | Rendert den Inhalt eines bestimmten Content-Typs der Partei (z. B. Beschreibungstext) und gibt ihn mit optionaler Ausgabe-Kodierung zurück. |
| `get(String contentTypeId, String encoderType)` | Wie oben, immer mit Cache; liefert einen `StringWrapper` für sichere Template-Ausgabe. |
| `getId(String contentTypeId)` | Liefert die Content-ID des ersten aktiven Inhalts eines bestimmten Content-Typs für diese Partei. |
| `getList(String contentTypeId)` | Gibt alle gerenderten Inhalte eines Content-Typs als String-Liste zurück (z. B. mehrere Fotos oder Dokumente). |
| `getContent(String contentId, boolean useCache, String encoderType)` | Rendert einen Inhalt direkt anhand seiner Content-ID (unabhängig vom Typ). |
| `getPartyContentAsText(GenericValue party, String partyContentTypeId, ...)` | Statische Variante: Rendert einen Party-Inhalt als Text, löst bei fehlendem Content-Datensatz auf Direkt-Feldwerte des Party-Datensatzes zurück (z. B. Vorname, Gruppenname). |
| `getPartyContentTextList(GenericValue party, String partyContentTypeId, ...)` | Rendert alle Inhalte eines Content-Typs als Liste (z. B. für Mehrsprachigkeit). |
| `getFirstPartyContentByType(String partyId, GenericValue party, String partyContentTypeId, Delegator)` | Sucht den jüngsten aktiven Content-Datensatz eines Party-Inhaltstyps. |
| `makePartyContentWrapper(GenericValue party, HttpServletRequest request)` | Factory-Methode: Erstellt eine `PartyContentWrapper`-Instanz aus einem HTTP-Request-Kontext. |

---

### Klasse: `HasPartyPermissions`

**Paket:** `org.apache.ofbiz.party`
**Typ:** Groovy-Script
**Zweck:** Groovy-Script — ausgeführt über OFBiz Service-Engine. Prüft im Rahmen von View-Berechtigungen, ob der angemeldete Benutzer die für einen bestimmten Party-Eintrag notwendigen Rechte besitzt. Das Ergebnis steuert, welche UI-Aktionen (Bearbeiten, Löschen) sichtbar geschaltet werden.

---

### Klasse: `PartyHelper`

**Paket:** `org.apache.ofbiz.party.party`
**Typ:** Java-Klasse (finale Utility-Klasse, nicht instanziierbar)
**Zweck:** Formatiert Anzeigenamen von Parteien für die Darstellung in Listen, Briefköpfen und Suchtreffern — sowohl für natürliche Personen (Vor-/Nachname) als auch für Organisationen (Gruppenname).

| Methode | Beschreibung |
|---|---|
| `getPartyName(GenericValue partyObject)` | Liefert den Anzeigenamen einer Partei in Normalreihenfolge (Vorname Nachname bzw. Gruppenname). |
| `getPartyName(Delegator delegator, String partyId, boolean lastNameFirst)` | Lädt den Anzeigenamen einer Partei direkt per ID aus der `PartyNameView`, wahlweise in der Reihenfolge Nachname, Vorname. |
| `getPartyName(GenericValue partyObject, boolean lastNameFirst)` | Ermittelt den Anzeigenamen aus einem bestehenden `PartyGroup`- oder `Person`-Objekt, ohne Datenbankzugriff. |
| `formatPartyNameObject(GenericValue partyValue, boolean lastNameFirst)` | Formatiert Vor-, Mittel- und Nachname bzw. Gruppenname eines Parteidatensatzes zu einer lesbaren Zeichenkette, mit optionaler Nachname-zuerst-Anordnung. |

---

### Klasse: `PartyRelationshipHelper`

**Paket:** `org.apache.ofbiz.party.party`
**Typ:** Java-Klasse (finale Utility-Klasse, nicht instanziierbar)
**Zweck:** Stellt Hilfsmethoden für die Suche nach aktiven Beziehungen zwischen Parteien bereit.

| Methode | Beschreibung |
|---|---|
| `getActivePartyRelationships(Delegator delegator, Map partyRelationshipValues)` | Sucht alle aktuell gültigen Beziehungseinträge zwischen zwei Parteien mit gegebenen Rollen und Beziehungstyp. Berücksichtigt `fromDate`/`thruDate` zum Stichtag jetzt. |

---

### Klasse: `PartyRelationshipServices`

**Paket:** `org.apache.ofbiz.party.party`
**Typ:** Java-Klasse
**Zweck:** Implementiert Services zur Verwaltung von Parteienbeziehungen, einschließlich der Idempotenz-Logik bei Anlage neuer Beziehungen.

| Methode | Beschreibung |
|---|---|
| `createUpdatePartyRelationshipAndRoles(DispatchContext, Map)` | Legt eine neue Parteienbeziehung an und stellt sicher, dass die notwendigen Rollen (`PartyRole`) auf beiden Seiten existieren. Bestehende gleichartige Beziehungen werden mit einem `thruDate` archiviert, bevor die neue angelegt wird. Ist bereits eine identische aktive Beziehung vorhanden, wird kein neuer Eintrag angelegt. |

---

### Klasse: `PartyServices`

**Paket:** `org.apache.ofbiz.party.party`
**Typ:** Java-Klasse
**Zweck:** Zentraler Service-Container für die grundlegende CRUD-Verwaltung von Party-Stammdaten (Personen, Organisationen, Notizen), Parteiensuche und den CSV-Import von Adress-Normalisierungsregeln.

| Methode | Beschreibung |
|---|---|
| `createPerson(DispatchContext, Map)` | Legt einen neuen Personendatensatz an — erstellt `Party`, `Person` und einen initialen `PartyStatus`-Eintrag. Verhindert rein numerische IDs. |
| `updatePerson(DispatchContext, Map)` | Aktualisiert Stammdaten einer Person; löst bei geändertem Status automatisch `setPartyStatus` aus. |
| `createPartyGroup(DispatchContext, Map)` | Erstellt eine neue Organisation (`PARTY_GROUP`); unterstützt benutzerdefinierte Party-Typ-IDs innerhalb der Gruppe. |
| `updatePartyGroup(DispatchContext, Map)` | Aktualisiert Stammdaten einer Organisation. |
| `setPartyStatus(DispatchContext, Map)` | Setzt den Status einer Partei (z. B. `PARTY_ENABLED`, `PARTY_DISABLED`). Prüft erlaubte Statusübergänge, schreibt Historieninträge und deaktiviert bei `PARTY_DISABLED` automatisch alle zugehörigen Benutzeranmeldungen. |
| `createAffiliate(DispatchContext, Map)` | Legt einen Affiliate-Eintrag für eine Partei an. |
| `updateAffiliate(DispatchContext, Map)` | Aktualisiert den Affiliate-Eintrag einer Partei. |
| `createPartyNote(DispatchContext, Map)` | Erstellt eine Notiz und verknüpft sie mit einer Partei. |
| `getPartiesFromExactEmail(DispatchContext, Map)` | Sucht alle Parteien mit einer exakt übereinstimmenden E-Mail-Adresse. |
| `getPartiesFromPartOfEmail(DispatchContext, Map)` | Sucht Parteien über eine Teilübereinstimmung der E-Mail-Adresse (Wildcardsuche). |
| `getPartiesFromPartOfUserloginId(DispatchContext, Map)` | Sucht Parteien anhand eines Teilstrings der Benutzerkennung. |
| `getPartiesFromPerson(DispatchContext, Map)` | Sucht Parteien anhand von Personenfeldern (Vor-/Nachname). |
| `getPartiesFromPartyGroup(DispatchContext, Map)` | Sucht Parteien anhand des Organisationsnamens. |
| `getPartiesFromExternalId(DispatchContext, Map)` | Sucht Parteien anhand einer externen Kennung (z. B. ERP-Nummer). |
| `getPerson(DispatchContext, Map)` | Lädt den vollständigen Personendatensatz zu einer Party-ID. |
| `findParty(DispatchContext, Map)` | Kombinierte Suche nach einer Partei über verschiedene Kriterien. |
| `performFindParty(DispatchContext, Map)` | Führt eine gefilterte Parteiensuche mit OFBiz-Suchkriterien aus. |
| `linkParty(DispatchContext, Map)` | Verknüpft zwei Parteien miteinander (z. B. für Deduplizierung oder Zusammenführung). |
| `importAddressMatchMapCsv(DispatchContext, Map)` | Importiert Adress-Normalisierungsregeln (Abkürzungsersetzungen wie "Str." → "Strasse") aus einer CSV-Datei. |
| `findPartyById(DispatchContext, Map)` | Sucht eine Partei anhand der internen Party-ID oder einer externen Identifikationsnummer. |
| `importParty(DispatchContext, Map)` | Massenimport von Parteien-Stammdaten inkl. Kontaktmechanismen aus einer strukturierten Map. |

---

### Klasse: `PartyServicesScript`

**Paket:** `org.apache.ofbiz.party.party`
**Typ:** Groovy-Script
**Zweck:** Groovy-Script — ausgeführt über OFBiz Service-Engine. Enthält erweiterte Party-Services, die in Groovy implementiert sind: Namenshistorie, Beziehungsnavigation, Kontaktdaten-Abfragen, E-Mail-Benachrichtigungen und Adressverwaltung.

| Methode | Beschreibung |
|---|---|
| `savePartyNameChange()` | Speichert eine Namensänderung für eine Partei mit Zeitstempel in der Namenshistorie. |
| `getPartyNameForDate()` | Ermittelt den historischen Namen einer Partei zu einem bestimmten Stichtag. |
| `getPostalAddressBoundary()` | Liefert die geographischen Grenzen (Geo-Polygon) zu einer Postleitzahl einer Partei. |
| `createPartyIdentifications()` | Legt mehrere externe Identifikationsnummern für eine Partei an (z. B. Steuer-ID, Registernummer). |
| `setPartyProfileDefaults()` | Setzt Standardwerte im Profil einer Partei (z. B. bevorzugte Währung, Sprache). |
| `getPartiesByRelationship()` | Gibt alle Parteien zurück, die über einen bestimmten Beziehungstyp mit einer Ausgangspartei verknüpft sind. |
| `getParentOrganizations()` | Ermittelt alle übergeordneten Organisationen einer Partei entlang der Beziehungshierarchie. |
| `getRelatedParties()` | Liefert alle Parteien, die in einer beliebigen Beziehung zur Ausgangspartei stehen. |
| `getChildRoleTypes()` | Bestimmt die gültigen Rollentypen, die einer untergeordneten Partei in einer Beziehung zugewiesen werden dürfen. |
| `getPartyEmail()` | Lädt die primäre E-Mail-Adresse einer Partei. |
| `getPartyTelephone()` | Lädt die primäre Telefonnummer einer Partei. |
| `getPartyPostalAddress()` | Lädt die primäre Postadresse einer Partei. |
| `createAddressMatchMap()` | Legt einen neuen Adress-Normalisierungseintrag (Abkürzungsregel) an. |
| `clearAddressMatchMap()` | Löscht alle vorhandenen Adress-Normalisierungseinträge. |
| `createPartyRelationship()` | Legt eine neue Beziehung zwischen zwei Parteien an. |
| `updatePartyRelationship()` | Aktualisiert eine bestehende Parteienbeziehung. |
| `deletePartyRelationship()` | Deaktiviert eine Parteienbeziehung durch Setzen des Enddatums. |
| `createPartyRelationshipContactAccount()` | Legt eine Kunden-Konto-Beziehung (Kontakt → Konto) zwischen zwei Parteien an. |
| `sendCreatePartyEmailNotification()` | Versendet eine Willkommensnachricht bei Neuanlage einer Partei per E-Mail. |
| `sendUpdatePersonalInfoEmailNotification()` | Benachrichtigt eine Partei per E-Mail über Änderungen an ihren persönlichen Stammdaten. |
| `sendAccountActivatedEmailNotification()` | Versendet eine Bestätigungs-E-Mail, wenn ein Benutzerkonto aktiviert wurde. |
| `createUpdatePerson()` | Erstellt oder aktualisiert eine Person idempotent (Upsert-Logik). |
| `quickCreateCustomer()` | Legt eine Partei mit minimalen Pflichtfeldern als Schnellerfassung für neue Kunden an. |
| `getPartyMainRole()` | Ermittelt die primäre Rolle einer Partei im System (z. B. Kunde, Lieferant). |
| `followPartyRelationshipsInline(...)` | Traversiert Parteienbeziehungen rekursiv für die Strukturdarstellung einer Hierarchie (z. B. Kontenbaum). |
| `getChildRoleTypesInline(List)` | Hilfsmethode zur rekursiven Ermittlung erlaubter Kindrollen innerhalb einer Beziehungsstruktur. |

---

### Klasse: `PartySimpleMethods`

**Paket:** `org.apache.ofbiz.party.party`
**Typ:** Groovy-Script
**Zweck:** Groovy-Script — ausgeführt über OFBiz Service-Engine. Vereinfachte Service-Methoden für die Anlage von Party-Gruppen mit Rollen und Kontaktmechanismen sowie für die strukturierte Auflösung von Kontaktdaten aus Map-Parametern.

| Methode | Beschreibung |
|---|---|
| `createPartyGroupRoleAndContactMechs()` | Legt eine Organisationspartei zusammen mit ihrer Rolle und allen Kontaktmechanismen in einem einzigen Serviceaufruf an. |
| `resolvePartyGroupMap()` | Extrahiert und validiert die Felder einer Organisation aus einem Eingabe-Parameter-Map und bereitet sie für die Datenbankpersistierung vor. |
| `resolvePostalAddressMap()` | Extrahiert und validiert Postadressfelder aus einem Eingabe-Parameter-Map. |
| `resolveTelecomNumberMap()` | Extrahiert und validiert Telefonnummernfelder aus einem Eingabe-Parameter-Map. |
| `resolveEmailAddressMap()` | Extrahiert und validiert E-Mail-Adressfelder aus einem Eingabe-Parameter-Map. |
| `resolvePartyProcessMap(String, String)` | Generische Hilfsmethode zur Auflösung und Validierung beliebiger Party-Kontaktdaten-Maps für unterschiedliche Kontakttypen. |

---

### Klasse: `PartyTypeHelper`

**Paket:** `org.apache.ofbiz.party.party`
**Typ:** Java-Klasse (finale Utility-Klasse, nicht instanziierbar)
**Zweck:** Überprüft den Typen einer Partei in der Typhierarchie des OFBiz-Party-Modells.

| Methode | Beschreibung |
|---|---|
| `checkPartyType(Delegator delegator, String partyId, String checkedPartyType)` | Prüft, ob eine Partei dem angegebenen Typ oder einem seiner Untertypen entspricht. Gibt `true` zurück, wenn der tatsächliche Partytyp ein Subtyp des geprüften Typs in der OFBiz-Typhierarchie ist. |

---

### Klasse: `PartyWorker`

**Paket:** `org.apache.ofbiz.party.party`
**Typ:** Java-Klasse (finale Utility-Klasse, nicht instanziierbar)
**Zweck:** Stellt Suchmethoden für Parteien über verschiedene Identifikatoren bereit und verwaltet parteibezogene Hilfsdaten wie letzten Login-Zeitpunkt, Geolokation und die Generierung von Club-IDs.

| Methode | Beschreibung |
|---|---|
| `getPartyOtherValues(ServletRequest, String partyId, ...)` | Lädt Party-, Person- und PartyGroup-Datensätze einer Partei gleichzeitig und befüllt damit benannte View-Attribute im Request. |
| `createClubId(Delegator, String prefix, int length)` | Generiert eine eindeutige Club-Mitgliedsnummer mit konfigurierbarem Präfix, laufender Sequenznummer und Luhn-Prüfziffer. |
| `findPartyLatestContactMech(String partyId, String contactMechTypeId, Delegator)` | Liefert den neuesten aktiven Kontaktmechanismus eines bestimmten Typs für eine Partei. |
| `findPartyLatestPostalAddress(String partyId, Delegator)` | Liefert die aktuellste Postadresse einer Partei. |
| `findPartyLatestPostalAddressGeoPoint(String partyId, Delegator)` | Liefert den geografischen Koordinatenpunkt (`GeoPoint`) der aktuellsten Postadresse einer Partei. |
| `findPartyLatestTelecomNumber(String partyId, Delegator)` | Liefert die aktuellste Telefonnummer einer Partei. |
| `findPartyLatestUserLogin(String partyId, Delegator)` | Liefert den zuletzt aktualisierten Benutzerzugang einer Partei. |
| `findPartyLastLoginTime(String partyId, Delegator)` | Ermittelt den Zeitstempel des letzten erfolgreichen Logins einer Partei aus der Login-Historie. |
| `findPartyLastLocale(String partyId, Delegator)` | Ermittelt die zuletzt verwendete Sprach- und Regionseinstellung einer Partei anhand des letzten Benutzerlogins. |
| `findFirstMatchingPartyId(Delegator, String address1, ...)` | Sucht die erste Partei, die zu den angegebenen Postadress- und Personenfeldern passt; gibt nur die Party-ID zurück. |
| `findFirstMatchingPartyAndContactMechId(Delegator, ...)` | Wie oben, gibt zusätzlich die ContactMech-ID der gefundenen Adresse zurück. |
| `findMatchingPersonPostalAddresses(Delegator, ...)` | Sucht alle natürlichen Personen, deren Name und Postadresse zu den angegebenen Feldern passen (Dublettenprüfung). |
| `findMatchingPartyPostalAddress(Delegator, ...)` | Sucht Parteien eines bestimmten Typs (z. B. `PERSON`) anhand normalisierter Adressfelder. |
| `makeMatchingString(Delegator, String address)` | Normalisiert eine Adresszeile für den Vergleich: Großbuchstaben, Entfernung von Sonderzeichen, Ersetzung von Abkürzungen anhand der konfigurierten `AddressMatchMap`. |
| `getAssociatedPartyIdsByRelationshipType(Delegator, String partyIdFrom, String relationshipTypeId)` | Traversiert transitiv alle Parteien, die über einen Beziehungstyp mit einer Ausgangspartei verbunden sind (Beziehungsbaum). |
| `findPartiesById(Delegator, String idToFind, String partyIdentificationTypeId, boolean searchPartyFirst, boolean searchAllId)` | Flexibler Parteiensucher: sucht zuerst über die interne Party-ID, dann über externe Identifikationsnummern. |
| `findPartyId(Delegator, String idToFind, String partyIdentificationTypeId)` | Liefert die interne Party-ID zu einer internen oder externen Kennung. |
| `findParty(Delegator, String idToFind, String partyIdentificationTypeId)` | Liefert den ersten gefundenen Party-Datensatz zu einer Kennung. |
| `findParties(Delegator, String idToFind, String partyIdentificationTypeId)` | Liefert alle Partei-Datensätze zu einer Kennung als vollständige `Party`-Entity-Liste. |

---

### Klasse: `PartyPermissionServices`

**Paket:** `org.apache.ofbiz.party.party`
**Typ:** Groovy-Script
**Zweck:** Groovy-Script — ausgeführt über OFBiz Service-Engine. Implementiert fein granulare Berechtigungsprüfungen für alle Operationen im Party-Modul. Bestimmt, ob ein angemeldeter Benutzer eine bestimmte Aktion auf einem Party-Datensatz durchführen darf.

| Methode | Beschreibung |
|---|---|
| `basePermissionCheck()` | Grundlegende Berechtigungsprüfung: testet, ob der Benutzer die allgemeine `PARTYMGR`-Berechtigung besitzt. |
| `partyIdPermissionCheck(Map)` | Prüft, ob der Benutzer auf einen konkreten Party-Datensatz zugreifen darf (entweder als Eigentümer oder via Admin-Berechtigung). |
| `basePlusPartyIdPermissionCheck()` | Kombiniert Basis- und Party-ID-Prüfung in einem Aufruf. |
| `partyStatusPermissionCheck()` | Prüft, ob der Benutzer den Status einer Partei ändern darf. |
| `partyGroupPermissionCheck()` | Prüft die Berechtigung für Operationen auf Organisationsdatensätzen. |
| `partyDatasourcePermissionCheck()` | Prüft, ob der Benutzer auf parteibezogene Datenquellen-Einstellungen zugreifen darf. |
| `partyRolePermissionCheck()` | Prüft die Berechtigung zum Anlegen, Ändern oder Löschen von Parteirollen. |
| `partyRelationshipPermissionCheck()` | Prüft die Berechtigung für Beziehungsverwaltungsoperationen zwischen Parteien. |
| `partyContactMechPermissionCheck()` | Prüft die Berechtigung zum Anlegen, Ändern oder Löschen von Kontaktmechanismen einer Partei. |
| `accAndDecPartyInvitationPermissionCheck()` | Prüft, ob der Benutzer eine Parteieinladung annehmen oder ablehnen darf. |
| `cancelPartyInvitationPermissionCheck()` | Prüft die Berechtigung zum Stornieren einer Parteieinladung. |
| `partyCommunicationEventPermissionCheck()` | Prüft die Berechtigung für den Zugriff auf Kommunikationsereignisse einer Partei. |

---

### Klasse: `PartyInvitationServices`

**Paket:** `org.apache.ofbiz.party.party`
**Typ:** Groovy-Script
**Zweck:** Groovy-Script — ausgeführt über OFBiz Service-Engine. Verwaltet den Lebenszyklus von Parteieinladungen: Erstellen, Aktualisieren und Annehmen einer Einladung, die eine noch nicht im System erfasste Person zur Registrierung auffordert.

| Methode | Beschreibung |
|---|---|
| `createPartyInvitation()` | Legt eine neue Einladung für eine externe Person an, inkl. Einladungstoken und Ablaufdatum. |
| `updatePartyInvitation()` | Aktualisiert Status oder Gültigkeitsdaten einer bestehenden Einladung. |
| `acceptPartyInvitation()` | Verknüpft eine angenommene Einladung mit dem neu erstellten Party-Datensatz und schließt den Einladungsprozess ab. |

---

### Groovy-Scripts: Daten- und View-Helfer im Subpaket `party.party`

**Paket:** `org.apache.ofbiz.party.party`
**Typ:** Groovy-Scripts (View-Vorbereitung, Datenabfragen)

Die folgenden Scripts werden über die OFBiz Service-Engine ausgeführt und stellen Daten für Views bereit:

| Klasse | Fachliche Funktion |
|---|---|
| `EditContactMech` | Lädt alle für das Kontaktmechanismus-Bearbeiten-Formular notwendigen Daten in den View-Kontext. |
| `EditPaymentMethod` | Lädt Daten für das Zahlungsmethoden-Bearbeiten-Formular (Kreditkarte, Bankeinzug) einer Partei. |
| `EditShoppingList` | Lädt Daten für die Bearbeitung einer Einkaufsliste einer Partei. |
| `FindLookUp` | Führt eine Partei-Suche für Lookup-Felder im UI durch und liefert Treffer für die Auswahlliste. |
| `FindMatches` | Sucht potenzielle Duplikate zu einer Partei anhand von Name und Adresse. |
| `FindParty` | Führt eine allgemeine Parteiensuche anhand verschiedener Suchfelder aus. |
| `GetContactMechs` | Lädt alle Kontaktmechanismen einer Partei für die Profilansicht. |
| `GetCurrentCart` | Ermittelt den aktiven Warenkorb des aktuell angemeldeten Benutzers. |
| `GetGeoLocation` | Löst die geografischen Koordinaten (Lat/Long) für die Adresse einer Partei auf. |
| `GetLoyaltyPoints` | Ermittelt den aktuellen Treuepunkte-Stand einer Partei. |
| `GetMyCompany` | Lädt den Organisationsdatensatz, der dem aktuell angemeldeten Benutzer zugeordnet ist. |
| `GetPaymentMethods` | Lädt alle hinterlegten Zahlungsmethoden einer Partei für die Profilansicht. |
| `GetPostalAddressTemplate` | Ermittelt das länderspezifische Anzeigeformat für Postadressen. |
| `GetUserLoginPrimaryEmail` | Liefert die primäre E-Mail-Adresse des Benutzerlogins der angemeldeten Partei. |
| `LookupServices` | Stellt eine `lookupParty()`-Methode für die Autocomplete-Suche im UI bereit. |
| `PartyFinancialHistory` | Lädt die Finanzhistorie einer Partei (offene Rechnungen, Zahlungen, Guthaben). |
| `PartyGeoLocation` | Speichert oder liest die Geolokation einer Partei (Koordinaten der Hauptadresse). |
| `SetRoleVars` | Setzt Rollenvariablen im View-Kontext (z. B. ob die aktuelle Partei ein Kunde oder Lieferant ist). |
| `StatusCondition` | Prüft, ob ein bestimmter Statusübergang für eine Partei erlaubt ist (Bedingungsauswertung für UI-Sichtbarkeit von Aktionen). |
| `UnAppliedInvoicesForParty` | Liefert alle noch nicht ausgeglichenen Rechnungen einer Partei. |
| `UnAppliedPaymentsForParty` | Liefert alle noch nicht zugeordneten Zahlungseingänge einer Partei. |
| `ViewProfile` | Bereitet alle Daten für die vollständige Profilansicht einer Partei auf (Stammdaten, Kontakte, Rollen, Beziehungen). |

---

### Test-Klassen: Subpaket `party.party.test`

**Paket:** `org.apache.ofbiz.party.party.test`
**Typ:** Groovy-Tests (OFBizTestCase)

Vier Testklassen decken automatisierte Integrationstests für die Kern-Funktionalität des Moduls ab:

| Klasse | Getestete Szenarien |
|---|---|
| `ContactMechWorkerTests` | Auflösung von Kontaktmechanismen für Parteien, Bestellungen und Arbeitsaufgaben |
| `PartyContactMechTests` | Anlage und Aktualisierung von E-Mail-Adressen, Telefonnummern und Postadressen einer Partei |
| `PartyStatusChangeTests` | Statusübergänge einer Partei (Aktivieren, Deaktivieren) |
| `PartyTests` | Grundlegende Party-Operationen (Anlage einer Postadresse) |

---

### Groovy-Scripts: Besuchererfassung im Subpaket `party.visit`

**Paket:** `org.apache.ofbiz.party.visit`
**Typ:** Groovy-Scripts

| Klasse | Fachliche Funktion |
|---|---|
| `ShowVisits` | Listet die Website-Besuche (Sessions) auf, die einer Partei zugeordnet sind. |
| `VisitDetails` | Lädt die vollständigen Details eines einzelnen Website-Besuchs (Zeitpunkt, verwendeter Browser, besuchte Seiten) für die Anzeige im Parteiprofil. |
