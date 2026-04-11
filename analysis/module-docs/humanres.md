### Modul: humanres

### Überblick

Das Modul **humanres** (Human Resources) verwaltet Organisationsstrukturen, Stellen und Mitarbeiterzuordnungen im OFBiz-HR-Bereich. Es stellt Event-Handler für die UI-seitige Darstellung von Organigrammen bereit und nutzt dabei die OFBiz-Entitäten `EmplPosition`, `EmplPositionFulfillment` und `PartyRelationship`.

### Submodule

| Paket | Beschreibung |
|-------|-------------|
| `org.apache.ofbiz.humanres` | Event-Handler für HR-Organigramm-Aufrufe |
| `org.apache.ofbiz.humanres.category` | Groovy-Scripts zur Aufbereitung von Kategoriebäumen |

---

### Klasse: `HumanResEvents`

**Paket:** `org.apache.ofbiz.humanres`
**Typ:** Java-Klasse (Event-Handler)
**Zweck:** Baut einen JSON-kompatiblen Baum der Organisationshierarchie auf, bestehend aus aktuellen Stelleninhabern, untergeordneten Organisationseinheiten und Positionen. Das Ergebnis wird als Request-Attribut `hrTree` für die View-Schicht bereitgestellt.

| Methode | Beschreibung |
|---------|-------------|
| `getChildHRCategoryTree(request, response)` | Ermittelt für eine gegebene `partyId` rekursiv: aktuelle Stelleninhaber (`EmplPositionFulfillment`), untergeordnete Abteilungen (`PartyRelationship` mit Typ `GROUP_ROLLUP`) und offene Stellen (`EmplPosition`). Schreibt das Ergebnis als Liste von Map-Objekten in das Request-Attribut `hrTree`. |

---

### Groovy-Scripts: category

**Paket:** `org.apache.ofbiz.humanres.category`
**Typ:** Groovy-Scripts

| Script | Fachliche Funktion |
|--------|-------------------|
| `CategoryTree` | Baut einen vollständigen Organisationsbaum ausgehend von einer Party auf. Folgt `GROUP_ROLLUP`-Beziehungen, liest den `PartyGroup`-Namen und gibt eine hierarchische Liste mit `completedTree` (Gesamtbaum) und `subtopLists` (direkte Unterknoten) zurück. |
