### Modul: sfa

### Überblick

Das Modul **sfa** (Sales Force Automation) ergänzt das Marketing-Modul um Funktionen für den Vertriebsinnendienst. Es stellt einen Service zum Import und Export von Kontaktdaten im vCard-Format (RFC 6350) bereit und nutzt dafür die externe Bibliothek ez-vCard.

### Submodule

| Paket | Beschreibung |
|-------|-------------|
| `org.apache.ofbiz.sfa.vcard` | Import/Export von Kontakten im vCard-Format (.vcf) |

---

### Klasse: `VCard`

**Paket:** `org.apache.ofbiz.sfa.vcard`
**Typ:** Java-Klasse (Service)
**Zweck:** Konvertiert OFBiz-Kontaktdaten (Person, Postadresse, Telefon, E-Mail) in das vCard-Format (.vcf) und umgekehrt. Nutzt die ez-vCard-Bibliothek für Serialisierung und Deserialisierung.

| Methode | Beschreibung |
|---------|-------------|
| `importVCard(dctx, context)` | Liest eine .vcf-Datei und importiert die enthaltenen Kontaktdaten als OFBiz-Party-Datensätze. (Dekompilierung fehlgeschlagen — Methodenstruktur aus Signatur und Fehlerkontext abgeleitet.) |
| `exportVCard(dctx, context)` | Exportiert eine Party (Person) als .vcf-Datei: liest Name, Postadresse, Telefonnummer und E-Mail-Adresse aus OFBiz-Entitäten und schreibt sie mit ez-vCard in das konfigurierte Ausgabeverzeichnis (`sfa.save.outgoing.directory`). |
