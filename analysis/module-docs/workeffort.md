## Modul: workeffort

### Überblick

Das `workeffort`-Modul implementiert die zentrale Arbeitsaufgaben-Verwaltung in Apache OFBiz: von Terminen, Aufgaben und Aktivitäten über iCalendar-basierte Kalenderintegration bis zur Volltextsuche. Es bildet die gemeinsame Grundlage für Projektarbeit, Produktionsaufträge und Workflow-Aktivitäten und verknüpft Personen, Betriebsmittel, Inhalte und Zeitausdrücke in einem einheitlichen Domänenmodell.

### Submodule

| Paket | Beschreibung |
|---|---|
| `org.apache.ofbiz.workeffort.workeffort` | Kernlogik: Services, Worker, Suche, iCalendar-Integration, Party-Zuweisung, Keyword-Indexierung |
| `org.apache.ofbiz.workeffort.content` | Content-Wrapper: sprachabhängige, gecachte Aufbereitung von Inhalten zu Arbeitsaufgaben |
| `org.apache.ofbiz.workeffort.ical` | iCalendar-Berechtigungsprüfung (Groovy-Script) |

---

### Klasse: `WorkEffortContentWrapper`
**Paket:** `org.apache.ofbiz.workeffort.content`
**Typ:** Java-Klasse (Content-Wrapper)
**Zweck:** Stellt lokalisierte und MIME-typ-konforme Inhalte zu einer `WorkEffort`-Entität bereit. Nutzt einen dedizierten Cache (`workeffort.content.rendered`) und delegiert das eigentliche Rendering an `ContentWorker`. Unterstützt Direktfeldzugriff als Fallback, wenn kein verknüpftes `WorkEffortContent`-Objekt vorliegt.

| Methode | Beschreibung |
|---|---|
| `get(workEffortContentId, useCache, encoderType)` | Gibt den gerenderten Inhalt eines bestimmten Content-Typs als String zurück; nutzt optional den internen Cache |
| `get(contentTypeId, encoderType)` | Wrapper-Variante, die den Rückgabewert als `StringUtil.StringWrapper` liefert (kompatibel mit FreeMarker-Templates) |
| `getContentId(contentTypeId)` | Gibt die `contentId` des ersten aktiven `WorkEffortContent`-Eintrags für den angegebenen Typ zurück |
| `getContentName(contentTypeId)` | Gibt den `contentName` des zugeordneten `Content`-Datensatzes zurück |
| `getFromDate(contentTypeId)` | Gibt das `fromDate` der `WorkEffortContent`-Verknüpfung zurück |
| `getDataResourceId(contentTypeId)` | Gibt die `dataResourceId` der dem Inhalt zugeordneten `DataResource` zurück |
| `getList(contentTypeId)` | Liefert eine Liste aller gerenderten Inhalte eines Typs (mehrere Sprachversionen) |
| `getTypeDescription(contentTypeId)` | Gibt die Beschreibung des `WorkEffortContentType`-Eintrags zurück |
| `getContent(contentId, useCache, encoderType)` | Rendert einen Inhalt direkt über seine `contentId` statt über den Content-Typ |
| `getWorkEffortContentAsText(...)` | Statische Methode: rendert `WorkEffortContent` als Text unter Berücksichtigung von Locale, MIME-Typ und Cache |
| `getWorkEffortContentTextList(...)` | Statische Methode: gibt alle gerenderten Textversionen eines Content-Typs als Liste zurück |
| `getFirstWorkEffortContentByType(...)` | Statische Methode: liefert den aktuell gültigen `WorkEffortContent`-Datensatz für einen bestimmten Typ |
| `makeWorkEffortContentWrapper(workEffort, request)` | Fabrikmethode zur Instanziierung aus einem HTTP-Request-Kontext |

---

### Klasse: `ICalConverter`
**Paket:** `org.apache.ofbiz.workeffort.workeffort`
**Typ:** Java-Klasse (Konverter)
**Zweck:** Kernkomponente der iCalendar-Integration. Wandelt `WorkEffort`-Entitäten (Typ `EVENT` und `TASK`) in iCalendar-Komponenten (`VEVENT` / `VTODO`) um und liest importierte iCalendar-Daten zurück in die Datenbank. Bildet OFBiz-Statuswerte, Sichtbarkeitsklassen, Teilnehmerstatus und wiederkehrende Ausdrücke (`TemporalExpression`) auf die entsprechenden iCal4j-Eigenschaften ab.

| Methode | Beschreibung |
|---|---|
| `getICalendar(workEffortId, context)` | Liest den aktuellen Kalender eines `WorkEffort` aus der Datenbank, ergänzt alle verknüpften Arbeitsaufgaben als `VEVENT`/`VTODO` und gibt das serialisierte iCalendar-Dokument zurück; prüft Sichtbarkeit und Zugriffsrechte |
| `storeCalendar(is, context)` | Liest ein iCalendar-Dokument aus einem InputStream, validiert die Zugriffsrechte, aktualisiert bestehende und legt neue `WorkEffort`-Einträge an; persistiert das Roh-iCalendar in `WorkEffortIcalData` |
| `toCalendarComponent(components, workEffort, context)` | Wandelt eine einzelne `WorkEffort`-Entität in ein `VEVENT`- oder `VTODO`-Objekt um und befüllt alle iCal-Eigenschaften; fügt Alarme und Teilnehmer hinzu |
| `makeCalendar(workEffort, context)` | Erstellt oder deserialisiert ein `net.fortuna.ical4j.model.Calendar`-Objekt, ergänzt Produkt-ID, Zeitzone und Kalender-Skalierung |
| `loadWorkEffort(componentProps, workEffort)` | Überträgt alle Standardfelder einer `WorkEffort`-Entität (Name, Status, Ort, Priorität, Datum) in die Property-Liste einer iCal-Komponente |
| `loadRelatedParties(relatedParties, componentProps, context)` | Befüllt `ATTENDEE`- und `ORGANIZER`-Eigenschaften aus den `WorkEffortPartyAssignView`-Einträgen |
| `storePartyAssignments(workEffortId, component, context)` | Liest `ATTENDEE`/`ORGANIZER`/`CONTACT`-Eigenschaften aus einer iCal-Komponente und legt fehlende `WorkEffortPartyAssignment`-Einträge an |
| `isCalendarPublished(publishProperties)` | Prüft, ob ein `WorkEffort` vom Typ `PUBLISH_PROPS` mit gültigem Zeitraum zur Veröffentlichung freigegeben ist |
| `hasPermission(workEffortId, action, context)` | Prüft über den Service `workEffortICalendarPermission`, ob der angemeldete Benutzer die angegebene Aktion (VIEW, UPDATE, CREATE) ausführen darf |

---

### Klasse: `ICalHandlerFactory`
**Paket:** `org.apache.ofbiz.workeffort.workeffort`
**Typ:** Java-Klasse (WebDAV-Handler-Factory)
**Zweck:** Implementiert `RequestHandlerFactory` für den iCalendar-WebDAV-Endpunkt. Registriert HTTP-Methodenhandler und delegiert GET-, PUT- und PROPFIND-Anfragen an `ICalWorker`. Alle anderen WebDAV-Methoden (COPY, DELETE, LOCK, MOVE usw.) werden mit HTTP 200 quittiert, ohne eine Aktion auszuführen.

| Methode | Beschreibung |
|---|---|
| `getHandler(method)` | Gibt den registrierten `RequestHandler` für die angegebene HTTP-Methode zurück; liefert bei unbekannten Methoden einen Handler, der HTTP 405 zurückgibt |

---

### Klasse: `ICalRecurConverter`
**Paket:** `org.apache.ofbiz.workeffort.workeffort`
**Typ:** Java-Klasse (Visitor)
**Zweck:** Implementiert `TemporalExpressionVisitor` und konvertiert OFBiz-`TemporalExpression`-Objekte (Frequenz, Wochentag-Bereiche, Monat-Bereiche usw.) in iCalendar-`RRULE`-, `EXRULE`-, `RDATE`- und `EXDATE`-Eigenschaften. Verwaltet einen Zustandsstapel zur korrekten Behandlung von Verschachtelungen (`Intersection`, `Difference`, `Union`).

| Methode | Beschreibung |
|---|---|
| `convert(expr, eventProps)` | Statische Einstiegsmethode: akzeptiert einen `TemporalExpression`-Baum und schreibt die konvertierten Wiederholungsregeln direkt in eine iCal-`PropertyList` |
| `consolidateRecurs(recurList)` | Fasst mehrere `Recur`-Objekte aus einem `Intersection`-Knoten zu einem einzigen zusammengesetzten `Recur` zusammen, indem Monat-, Tag- und Stundenlisten vereint werden |
| `visit(TemporalExpressions.Frequency)` | Konvertiert ein Frequenz-Intervall (SECONDLY bis YEARLY) in eine `RRULE` |
| `visit(TemporalExpressions.DayOfWeekRange)` | Konvertiert einen Wochentag-Bereich in eine tägliche `RRULE` mit `BYDAY`-Liste |
| `visit(TemporalExpressions.DayOfMonthRange)` | Konvertiert einen Monats-Tag-Bereich in eine tägliche `RRULE` mit `BYMONTHDAY`-Liste |
| `visit(TemporalExpressions.DayInMonth)` | Konvertiert einen „n-ten Wochentag im Monat"-Ausdruck in eine monatliche `RRULE` |
| `visit(TemporalExpressions.MonthRange)` | Konvertiert einen Monatsbereich in eine monatliche `RRULE` mit `BYMONTH`-Liste |
| `visit(TemporalExpressions.HourRange)` | Konvertiert einen Stundenbereich in eine stündliche `RRULE` mit `BYHOUR`-Liste |
| `visit(TemporalExpressions.MinuteRange)` | Konvertiert einen Minutenbereich in eine minütliche `RRULE` mit `BYMINUTE`-Liste |
| `visit(TemporalExpressions.DateRange)` | Konvertiert einen konkreten Datumszeitraum in eine `RDATE`-Periode |
| `visit(TemporalExpressions.Difference)` | Verarbeitet Differenzausdrücke: der eingeschlossene Teil wird als `RRULE`, der ausgeschlossene als `EXRULE` ausgegeben |
| `visit(TemporalExpressions.Intersection)` | Verarbeitet Schnittmengen-Ausdrücke durch Zustandsstapelung und abschließende Zusammenfassung via `consolidateRecurs` |
| `visit(TemporalExpressions.Union)` | Verarbeitet Vereinigungsmengen-Ausdrücke durch sequenzielle Delegation an alle Kindausdrücke |

---

### Klasse: `ICalWorker`
**Paket:** `org.apache.ofbiz.workeffort.workeffort`
**Typ:** Java-Klasse (HTTP-Handler, final)
**Zweck:** HTTP-Einstiegspunkt für den iCalendar-WebDAV-Endpunkt. Verarbeitet GET- (Kalender abrufen), PUT- (Kalender speichern) und PROPFIND-Anfragen (WebDAV-Metadaten). Extrahiert die `workEffortId` aus dem URL-Pfad, authentifiziert den Benutzer per HTTP Basic Auth und delegiert die eigentliche Verarbeitung an `ICalConverter`. Definiert die innere Klasse `ResponseProperties` zur strukturierten HTTP-Antwort.

| Methode | Beschreibung |
|---|---|
| `handleGetRequest(request, response, context)` | Verarbeitet eine HTTP-GET-Anfrage: prüft die Anfrage, ruft `ICalConverter.getICalendar` auf und schreibt das Ergebnis mit Content-Type `text/calendar` in die Antwort |
| `handlePutRequest(request, response, context)` | Verarbeitet eine HTTP-PUT-Anfrage: prüft Content-Type (`text/calendar`), ruft `ICalConverter.storeCalendar` auf und schreibt den HTTP-Status in die Antwort |
| `handlePropFindRequest(request, response, context)` | Verarbeitet eine WebDAV-PROPFIND-Anfrage: parst den XML-Body, beantwortet `getetag`- und `getlastmodified`-Eigenschaften und liefert eine `207 Multi-Status`-Antwort |
| `createOkResponse(statusMessage)` | Erstellt eine `ResponseProperties`-Instanz mit HTTP 200 |
| `createNotAuthorizedResponse(statusMessage)` | Erstellt eine `ResponseProperties`-Instanz mit HTTP 401 |
| `createForbiddenResponse(statusMessage)` | Erstellt eine `ResponseProperties`-Instanz mit HTTP 403 |
| `createNotFoundResponse(statusMessage)` | Erstellt eine `ResponseProperties`-Instanz mit HTTP 404 |
| `createPartialContentResponse(statusMessage)` | Erstellt eine `ResponseProperties`-Instanz mit HTTP 206 (bei partiellen Fehlern beim Speichern) |

---

### Klasse: `WorkEffortKeywordIndex`
**Paket:** `org.apache.ofbiz.workeffort.workeffort`
**Typ:** Java-Klasse (Indexierung)
**Zweck:** Erstellt und aktualisiert den Keyword-Index für `WorkEffort`-Entitäten in der Tabelle `WorkEffortKeyword`. Extrahiert Schlüsselwörter aus Name, Typ, Status, Notizen, Attributen und verknüpften Inhalten; gewichtet jedes Feld separat über Properties (`index.weight.*`) und speichert alle Begriffe mit ihrem Relevanzgewicht.

| Methode | Beschreibung |
|---|---|
| `indexKeywords(workEffort)` | Baut den vollständigen Keyword-Index für eine `WorkEffort`-Entität auf: löscht alte Einträge implizit durch `storeAll`, verarbeitet alle konfigurierten Quellfelder und Content-Typen und speichert die gewichteten Schlüsselwörter |
| `addWeightedDataResourceString(dataResource, weight, strings, delegator, workEffort)` | Rendert den Text einer `DataResource` und fügt ihn entsprechend dem Gewichtungsfaktor mehrfach in die Quellliste ein |
| `addWeightedKeywordSourceString(value, fieldName, strings)` | Liest einen Feldwert aus einer `GenericValue`-Instanz und fügt ihn gewichtet in die Quellliste ein |

---

### Klasse: `WorkEffortPartyAssignmentServices`
**Paket:** `org.apache.ofbiz.workeffort.workeffort`
**Typ:** Java-Klasse (Service)
**Zweck:** Verknüpft Statusänderungen an `WorkEffortPartyAssignment`-Einträgen mit dem Workflow-Engine. Wenn eine Zuweisung zu einer Aktivität (`ACTIVITY`) akzeptiert, abgeschlossen oder abgelehnt wird, werden die entsprechenden Workflow-Services (`wfAcceptAssignment`, `wfCompleteAssignment`, `wfDeclineAssignment`) aufgerufen.

| Methode | Beschreibung |
|---|---|
| `updateWorkflowEngine(wepa, userLogin, dispatcher)` | Prüft, ob die zugehörige `WorkEffort`-Entität eine Aktivität ist, und löst anhand des neuen Zuweisungsstatus den passenden Workflow-Service aus |

---

### Klasse: `WorkEffortSearch`
**Paket:** `org.apache.ofbiz.workeffort.workeffort`
**Typ:** Java-Klasse (Suche)
**Zweck:** Implementiert die vollständige Suchmaschinerie für `WorkEffort`-Entitäten auf Basis dynamischer View-Entities und Keyword-Indizes. Stellt eine Constraint-basierte Architektur bereit: Suchbedingungen werden als typisierte Objekte modelliert und durch `WorkEffortSearchContext` zu einer einzigen Datenbankabfrage kombiniert. Suchergebnisse werden in `WorkEffortSearchResult` protokolliert.

| Methode | Beschreibung |
|---|---|
| `searchWorkEfforts(constraintList, resultSortOrder, delegator, visitId)` | Führt eine vollständige Suche durch: kombiniert die angegebenen Constraints, führt die Abfrage aus und gibt eine Liste von `workEffortId`-Werten zurück |
| `getAllSubWorkEffortIds(workEffortId, workEffortIdSet, delegator, nowTimestamp)` | Sammelt rekursiv alle untergeordneten `WorkEffort`-IDs über `WORK_EFF_BREAKDOWN`-Assoziationen und `workEffortParentId`-Verknüpfungen |

Die Klasse enthält folgende innere Klassen:

| Klasse | Beschreibung |
|---|---|
| `WorkEffortSearchContext` | Hält den Zustand einer laufenden Suche: dynamische View-Entity, Bedingungsliste, Sortiervorgaben und Keyword-Sets; führt die Abfrage aus und protokolliert das Ergebnis |
| `KeywordConstraint` | Suchbedingung auf Basis von Schlüsselwörtern (AND/OR, Präfix/Suffix, Stemming) gegen den `WorkEffortKeyword`-Index |
| `WorkEffortAssocConstraint` | Schränkt auf `WorkEffort`-Entitäten ein, die mit einem bestimmten anderen `WorkEffort` assoziiert sind (optional inkl. aller untergeordneten Elemente) |
| `PartyAssignmentConstraint` | Schränkt auf `WorkEffort`-Entitäten ein, denen eine bestimmte Partei mit optionalem Rollentyp zugewiesen ist |
| `ProductSetConstraint` | Schränkt auf `WorkEffort`-Entitäten ein, denen über `WorkEffortGoodStandard` mindestens ein Produkt aus einer Menge zugeordnet ist |
| `LastUpdatedRangeConstraint` | Schränkt auf `WorkEffort`-Entitäten ein, die innerhalb eines Zeitraums zuletzt geändert wurden |
| `WorkEffortReviewConstraint` | Schränkt auf `WorkEffort`-Entitäten ein, die einen Bewertungstext enthalten (Volltextsuche in `WorkEffortReview`) |
| `SortKeywordRelevancy` | Sortierordnung nach absteigender Keyword-Relevanz |
| `SortWorkEffortField` | Sortierordnung nach einem beliebigen Datenbankfeld der `WorkEffort`-Entität |

---

### Klasse: `WorkEffortSearchEvents`
**Paket:** `org.apache.ofbiz.workeffort.workeffort`
**Typ:** Java-Klasse (HTTP-Event-Handler)
**Zweck:** Bindeglied zwischen der Web-Oberfläche und der Suchlogik. Liest die aktuellen Suchoptionen aus der HTTP-Session, führt die Suche mit Paginierung durch und bereitet alle für die Ergebnisseite benötigten Daten als Map auf.

| Methode | Beschreibung |
|---|---|
| `getWorkEffortSearchResult(request, delegator)` | Ermittelt die Suchoptionen aus der Session, führt die paginierte Suche aus und gibt eine Map mit `workEffortIds`, Paginierungsindizes sowie lesbaren Constraint- und Sortierbeschreibungen zurück |

---

### Klasse: `WorkEffortSearchSession`
**Paket:** `org.apache.ofbiz.workeffort.workeffort`
**Typ:** Java-Klasse (Session-Management)
**Zweck:** Verwaltet den Suchzustand (Constraints, Sortierung, Paginierung) in der HTTP-Session unter dem Attribut `_WORK_EFFORT_SEARCH_OPTIONS_CURRENT_`. Führt eine History-Liste vergangener Suchzustände und stellt Hilfsmethoden zur Verarbeitung von Request-Parametern bereit.

| Methode | Beschreibung |
|---|---|
| `getWorkEffortSearchOptions(session)` | Gibt die aktuellen `WorkEffortSearchOptions` aus der Session zurück; legt eine neue Instanz an, wenn noch keine vorhanden ist |
| `processSearchParameters(parameters, request)` | Verarbeitet Formularparameter (Suchbegriff, Assoziations-ID, Party-ID, Produkt-ID, Datumsbereich) und fügt entsprechende Constraints zur Session hinzu; idempotent bei Mehrfachaufruf pro Request |
| `searchAddConstraint(constraint, session)` | Fügt einen Constraint zur aktuellen Suchoption hinzu, wenn er noch nicht enthalten ist |
| `searchSetSortOrder(resultSortOrder, session)` | Setzt die Sortierordnung in der aktuellen Suchoption |
| `searchGetConstraintStrings(detailed, session, delegator)` | Gibt eine lesbare Darstellung aller aktiven Constraints für die Oberfläche zurück |
| `searchGetSortOrderString(detailed, request)` | Gibt eine lesbare Darstellung der aktuellen Sortierordnung zurück |
| `checkSaveSearchOptionsHistory(session)` | Speichert die aktuellen Suchoptionen in der History-Liste, wenn sie seit der letzten Suche geändert wurden |
| `searchRemoveConstraint(index, session)` | Entfernt einen Constraint anhand seines Index aus der aktuellen Suchoption |
| `searchClear(session)` | Setzt alle Suchoptionen (Constraints und Sortierung) zurück |
| `getSearchOptionsHistoryList(session)` | Gibt die Liste der zuletzt verwendeten Suchoptionen zurück |

---

### Klasse: `WorkEffortServices`
**Paket:** `org.apache.ofbiz.workeffort.workeffort`
**Typ:** Java-Klasse (Service)
**Zweck:** Sammlung von OFBiz-Services für Abfragen und Datenaggregation rund um `WorkEffort`-Entitäten. Deckt Kalenderabfragen (Ereignisse nach Zeitraum mit Wiederholungsregel-Auflösung), Aufgaben- und Aktivitätslisten je Benutzer, Fertigungsauftrags-Zusammenfassungen je Lager sowie die Verarbeitung von Erinnerungs-Benachrichtigungen ab.

| Methode | Beschreibung |
|---|---|
| `getWorkEffortAssignedEventsForRole(ctx, context)` | Gibt alle aktiven Kalendereinträge (Typ `EVENT`) zurück, die dem angemeldeten Benutzer in einer bestimmten Rolle zugewiesen sind, ausgenommen abgelehnte, delegierte, abgeschlossene und stornierte |
| `getWorkEffortAssignedEventsForRoleOfAllParties(ctx, context)` | Gibt alle aktiven Kalendereinträge (Typ `EVENT`) für alle Parteien in einer bestimmten Rolle zurück |
| `getWorkEffortAssignedTasks(ctx, context)` | Gibt alle aktiven Aufgaben (Typ `TASK` und `PROD_ORDER_TASK`) zurück, die dem angemeldeten Benutzer zugewiesen sind |
| `getWorkEffortAssignedActivities(ctx, context)` | Gibt alle aktiven Workflow-Aktivitäten (Typ `ACTIVITY`) zurück, die dem angemeldeten Benutzer direkt zugewiesen sind |
| `getWorkEffortAssignedActivitiesByRole(ctx, context)` | Gibt alle aktiven Workflow-Aktivitäten zurück, die dem Benutzer über eine Rollengruppe zugewiesen sind |
| `getWorkEffortAssignedActivitiesByGroup(ctx, context)` | Gibt alle aktiven Workflow-Aktivitäten zurück, die dem Benutzer über eine Parteigruppe zugewiesen sind |
| `getWorkEffort(ctx, context)` | Lädt eine `WorkEffort`-Entität und prüft die Zugriffsberechtigung des angemeldeten Benutzers anhand seiner Party-Zuweisungen oder des `WORKEFFORTMGR_VIEW`-Berechtigungsbits |
| `getWorkEffortEventsByPeriod(ctx, context)` | Gibt alle Kalendereinträge innerhalb eines definierten Zeitraums zurück, aufgeteilt nach Perioden; löst `TemporalExpression`-Wiederholungen auf und berechnet `periodSpan` für die Darstellung in Kalender-Views; unterstützt Filterung nach Party, Betriebsmittel, Lager und Kalendertyp |
| `getProductManufacturingSummaryByFacility(ctx, context)` | Aggregiert offene eingehende und ausgehende Fertigungsaufträge für ein Produkt nach Lager und gibt Mengen-Summaries zurück |
| `processWorkEffortEventReminders(ctx, context)` | Verarbeitet fällige `WorkEffortEventReminder`-Einträge: löst Wiederholungsausdrücke auf, versendet E-Mail-Erinnerungen und aktualisiert den nächsten Erinnerungszeitpunkt |
| `processWorkEffortEventReminder(dctx, context)` | Versendet eine einzelne Erinnerung per E-Mail über das Template `WEFF_EVENT_REMINDER`, sofern ein gültiger E-Mail-Kontaktweg hinterlegt ist |
| `removeDuplicateWorkEfforts(ctx, context)` | Service-Wrapper: entfernt doppelte `WorkEffort`-Einträge aus einem Iterator oder einer Liste und gibt eine deduplizierte Liste zurück |

---

### Klasse: `WorkEffortWorker`
**Paket:** `org.apache.ofbiz.workeffort.workeffort`
**Typ:** Java-Klasse (Worker, final, nicht instanziierbar)
**Zweck:** Hilfsklasse mit allgemeinen Traversierungs- und Bereinigungsoperationen auf `WorkEffort`-Assoziationsgraphen. Wird von mehreren anderen Klassen und Services verwendet.

| Methode | Beschreibung |
|---|---|
| `getLowestLevelWorkEfforts(delegator, workEffortId, workEffortAssocTypeId)` | Traversiert den `WorkEffortAssoc`-Graphen in Tiefensuche und gibt alle Blattknoten (niedrigste Ebene) des Baums zurück, sortiert nach Traversierungsreihenfolge |
| `getLowestLevelWorkEfforts(delegator, workEffortId, workEffortAssocTypeId, left, right)` | Erweiterte Variante mit konfigurierbaren Schlüsselfeldern (`workEffortIdFrom`/`workEffortIdTo`) für bidirektionale Graphen |
| `removeDuplicateWorkEfforts(workEfforts)` | Entfernt doppelte `WorkEffort`-Einträge aus einer Liste in-place, behält die erste Occurrence und gibt die bereinigte Liste zurück |

---

### Groovy-Scripts: iCalendar-Berechtigungsprüfung (`ical`)

**Paket:** `org.apache.ofbiz.workeffort.ical`
**Typ:** Groovy-Script

| Script | Fachliche Funktion |
|---|---|
| `IsCalOwner` | Prüft, ob der angemeldete Benutzer Eigentümer eines iCalendar-Kalenders (`CAL_OWNER`) ist, und setzt das Ergebnis als Request-Attribut für die Zugriffskontrolle |

---

### Groovy-Scripts: Kalender-Ansichten (`calendar`)

**Paket:** `org.apache.ofbiz.workeffort.workeffort.calendar`
**Typ:** Groovy-Scripts (View-Layer)

| Script | Fachliche Funktion |
|---|---|
| `CreateUrlParam` | Erzeugt URL-Parameter für Kalender-Navigationslinks (z. B. Monats-/Wochennavigation) |
| `Days` | Bereitet Daten für die Tagesansicht des Kalenders auf; ermittelt alle Arbeitsaufgaben des gewählten Tages |
| `Month` | Bereitet Daten für die Monatsansicht auf; aggregiert Arbeitsaufgaben je Kalendertag |
| `Upcoming` | Listet bevorstehende Termine und Aufgaben des angemeldeten Benutzers auf, sortiert nach Startdatum |
| `Week` | Bereitet Daten für die Wochenansicht auf; ermittelt alle Arbeitsaufgaben der gewählten Woche |

---

### Groovy-Scripts: Content-Wrapper (`content`)

**Paket:** `org.apache.ofbiz.workeffort.workeffort.content`
**Typ:** Groovy-Script (View-Layer)

| Script | Fachliche Funktion |
|---|---|
| `WorkEffortContentWrapperScript` | Instanziiert einen `WorkEffortContentWrapper` für die aktuelle Arbeitsaufgabe und stellt ihn im View-Kontext bereit |

---

### Groovy-Scripts: Suche (`find`)

**Paket:** `org.apache.ofbiz.workeffort.workeffort.find`
**Typ:** Groovy-Scripts (View-Layer)

| Script | Fachliche Funktion |
|---|---|
| `WorkEffortSearchOptions` | Verarbeitet Suchformular-Parameter, aktualisiert die Session-Suchoptionen und leitet zur Ergebnisseite weiter |
| `WorkEffortSearchResults` | Ruft `WorkEffortSearchEvents.getWorkEffortSearchResult` auf und stellt Ergebnisliste sowie Paginierungsdaten für die Darstellung bereit |

---

### Groovy-Scripts: Anforderungsliste (`request`)

**Paket:** `org.apache.ofbiz.workeffort.workeffort.request`
**Typ:** Groovy-Script (View-Layer)

| Script | Fachliche Funktion |
|---|---|
| `RequestList` | Lädt und filtert eine Liste von Anforderungen (`WorkEffort` mit Typ `ROU_TASK` oder ähnlich), die als offene Anfragen verwaltet werden, für die Listendarstellung |

---

### Groovy-Scripts: Service-Ergänzungen (`workeffort`)

**Paket:** `org.apache.ofbiz.workeffort.workeffort.workeffort`
**Typ:** Groovy-Script (View-Layer)

| Script | Fachliche Funktion |
|---|---|
| `WorkEffortServicesScript` | Ruft ergänzende Services im View-Kontext auf (z. B. Parteizuweisungen, Inhalte, verknüpfte Entitäten) und stellt die Ergebnisse für die Detailansicht einer Arbeitsaufgabe bereit |
