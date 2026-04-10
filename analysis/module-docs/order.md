## Modul: order

### Überblick

Das Modul `order` ist der Kern des Bestellwesens in Apache OFBiz und deckt den vollständigen Order-to-Cash-Prozess ab. Es umfasst die Verwaltung des Warenkorbs, die Auftragserfassung und -verarbeitung (für Verkaufs- und Einkaufsbestellungen), das Retourenmanagement, die Angebotserstellung, Einkaufsanforderungen und Einkaufslisten. Das Modul stellt sowohl die Geschäftslogik (Java-Services) als auch UI-Skripte (Groovy) für alle order-bezogenen Screens bereit.

### Submodule

| Paket | Beschreibung |
|---|---|
| `org.apache.ofbiz.order.shoppingcart` | Warenkorb-Kernlogik: ShoppingCart, ShoppingCartItem, Checkout-Prozess, Events und Services für den sessionbasierten Warenkorb |
| `org.apache.ofbiz.order.shoppingcart.component` | Interfaces (IShoppingCart*) für die komponentenbasierte Architektur des Warenkorbs |
| `org.apache.ofbiz.order.shoppingcart.components` | Konkrete Implementierungen der Warenkorb-Komponenten (Shipping, Taxes, Pricing, Payment, Promotion, Validator, ItemManager, Persistence) |
| `org.apache.ofbiz.order.shoppingcart.product` | Produktbezogene Hilfsfunktionen im Warenkorb-Kontext: Promotionsberechnung, Produktanzeige |
| `org.apache.ofbiz.order.shoppingcart.shipping` | Versandkostenberechnung und Versand-Events |
| `org.apache.ofbiz.order.order` | Auftragsverarbeitung: Erstellen, Lesen, Ändern, Löschen von Orders; Rückgabe-Services; Events und UI-Skripte |
| `org.apache.ofbiz.order.order.test` | Automatisierte Groovy-Testklassen für Order-Funktionalitäten |
| `org.apache.ofbiz.order.quote` | Angebotsverwaltung: Erstellen, Versenden und Verwalten von Angeboten |
| `org.apache.ofbiz.order.requirement` | Beschaffungsanforderungen: Generierung und Konsolidierung von Einkaufsanforderungen |
| `org.apache.ofbiz.order.shoppinglist` | Einkaufslisten: Gespeicherte, automatisch wiederkehrende und öffentliche Listen |
| `org.apache.ofbiz.order.finaccount` | Hilfsfunktionen für Finanzkonten (Gift Cards, Geschenkgutscheine) |
| `org.apache.ofbiz.order.task` | Aufgaben- und Workflow-Management zu Bestellprozessen |
| `org.apache.ofbiz.order.allocationplan` | Groovy-Scripts zur Zuteilungsplanung |
| `org.apache.ofbiz.order.communications` | Groovy-Script für bestellbezogene Kommunikationsdienste |
| `org.apache.ofbiz.order.entry` | Groovy-Scripts für die Auftragserfassung (Checkout, Warenkorb-Anzeige, Katalog, Zahlungseinstellungen) |
| `org.apache.ofbiz.order.lookup` | Groovy-Script zur Produktverknüpfungssuche |
| `org.apache.ofbiz.order.orderReturn` | Groovy-Scripts für Retourenvorgänge und Rücksendungshistorie |
| `org.apache.ofbiz.order.reports` | Groovy-Script für offene-Positionen-Report |
| `org.apache.ofbiz.order.request` | Groovy-Scripts für Kundenanfragen und CRM-Quoten |
| `org.apache.ofbiz.order.setup` | Groovy-Script für Zahlungskonfiguration |
| `org.apache.ofbiz.order.thirdparty.paypal` | PayPal ExpressCheckout-Integration |
| `org.apache.ofbiz.order.thirdparty.zipsales` | Steuerberechnung über ZIP-Code-basierte Steuertabellen |
| `org.apache.ofbiz.order.test` | Java-Testklassen für das gesamte Order-Modul |

---

### Klasse: `ShoppingCart`

**Paket:** `org.apache.ofbiz.order.shoppingcart`
**Typ:** Java-Klasse (implementiert `Iterable<ShoppingCartItem>`, `Serializable`)
**Zweck:** Zentrales Datenobjekt des Bestellprozesses. Der ShoppingCart repräsentiert eine laufende Bestellung — entweder als Verkaufsauftrag (SALES_ORDER) oder Einkaufsbestellung (PURCHASE_ORDER). Die Klasse hält alle Positionen, Zahlungsinformationen, Versandgruppen, Werbeaktionen und Bestellmetadaten für die gesamte Lebensdauer einer Bestellung im Speicher. Sie ist über eine komponentenbasierte Architektur (8 IShoppingCart*-Interfaces) aufgebaut, sodass einzelne Verhaltensaspekte ausgetauscht werden können.

| Methode | Beschreibung |
|---|---|
| `addOrIncreaseItem(productId, quantity, ...)` | Fügt ein Produkt zum Warenkorb hinzu oder erhöht die Menge einer bereits vorhandenen identischen Position; prüft dabei Mindestbestellmengen, Verfügbarkeit (für Mietartikel) und Lieferanteninformationen (bei Einkaufsbestellungen) |
| `addNonProductItem(itemType, description, ...)` | Fügt eine nicht-produktgebundene Position (z.B. Gebühren, Dienstleistungen) zum Warenkorb hinzu |
| `addItem(index, item)` | Fügt eine bereits erstellte ShoppingCartItem-Instanz an einem bestimmten Index ein; prüft Kompatibilität mit Rechnungsadresse und ProductGeos-Regeln |
| `addItemToEnd(productId, amount, quantity, ...)` | Fügt ein Produkt am Ende der Positionsliste hinzu; in vielen überladenen Varianten für Mietartikel, konfigurierbare Produkte, Beherbergung etc. |
| `removeCartItem(item/index, dispatcher)` | Entfernt eine Position aus dem Warenkorb und setzt deren Menge auf null (löst Neukalkulation aus) |
| `findCartItem(productId, features, ...)` | Sucht eine Warenkorb-Position anhand von Produkt-ID, Features und Attributen |
| `findAllCartItems(productId, groupNumber)` | Liefert alle Positionen für eine bestimmte Produkt-ID, optional gefiltert nach Positionsgruppe |
| `findAllCartItemsInCategory(productCategoryId, groupNumber)` | Liefert alle Positionen, deren Produkt einer bestimmten Produktkategorie angehört |
| `removeEmptyCartItems()` | Entfernt alle Positionen mit Menge null aus dem Warenkorb |
| `addItemGroup(groupName, parentGroupNumber)` | Erstellt eine neue Positionsgruppe (z.B. für Bundles) und gibt die neue Gruppennummer zurück |
| `deleteItemGroup(groupNumber)` | Löscht eine Positionsgruppe und hebt die Gruppenzuordnung aller enthaltenen Positionen auf |
| `setUserLogin(userLogin, dispatcher)` | Setzt den angemeldeten Benutzer und löst eine Neuberechnung aller Preise sowie eine Überprüfung aller Aktionscodes aus |
| `handleNewUser(dispatcher)` | Reagiert auf einen Benutzerwechsel: aktualisiert Preise aller Positionen und entfernt nicht mehr gültige Promotion-Codes |
| `setCurrency(dispatcher, currencyUom)` | Wechselt die Währung des Warenkorbs und aktualisiert alle Positionspreise |
| `setOrderType(orderType)` | Setzt den Bestelltyp (SALES_ORDER oder PURCHASE_ORDER) |
| `addPaymentAmount(id, amount, ...)` | Fügt eine Zahlungsart (Kreditkarte, Geschenkkarte etc.) mit Betrag zum Warenkorb hinzu; prüft ProductGeos-Kompatibilität der Rechnungsadresse |
| `addPaymentRef(id, ref, authCode)` | Hinterlegt eine Transaktionsreferenz und Autorisierungscode für eine Zahlungsart |
| `clearPayments()` | Entfernt alle Zahlungsinformationen und läuft Single-Use-Zahlungsmittel ab |
| `clearDeclinedPaymentMethods(delegator)` | Entfernt alle als abgelehnt markierten Zahlungsmittel anhand gespeicherter OrderPaymentPreference-Datensätze |
| `setShippingContactMechId(idx, contactMechId)` | Setzt die Lieferadresse für eine Versandgruppe; prüft ProductGeos-Kompatibilität der Produkte |
| `setShipmentMethodTypeId(idx, methodTypeId)` | Setzt die Versandmethode für eine Versandgruppe |
| `setItemShipGroupQty(item, quantity, idx)` | Weist einer bestimmten Versandgruppe eine Teilmenge einer Position zu |
| `positionItemToGroup(item, quantity, fromIndex, toIndex, ...)` | Verschiebt eine Teilmenge einer Position von einer Versandgruppe in eine andere |
| `addShipInfo()` | Erstellt eine neue (zusätzliche) Versandgruppe |
| `cleanUpShipGroups()` | Entfernt leere Versandgruppen |
| `createDropShipGroups(dispatcher)` | Erstellt automatisch Versandgruppen für Direktlieferungen (Drop-Shipment) bei mehreren Lieferanten |
| `getSubTotal()` | Berechnet die Positionssumme (Summe aller Zeilensummen vor Anpassungen) |
| `getGrandTotal()` | Berechnet den Gesamtbetrag inklusive Versand, Steuern und aller Anpassungen |
| `getDisplaySubTotal()` | Liefert die Anzeigesumme (kann bereits enthaltene Steuern beinhalten) |
| `getTotalSalesTax()` | Summiert die Verkaufssteuern aller Versandgruppen |
| `getTotalShipping()` | Summiert die Versandkosten aller Versandgruppen |
| `getProductPromoTotal()` | Berechnet den Gesamtrabatt durch Promotionsanpassungen |
| `getSubTotalForPromotions()` | Liefert die für Promotionsberechnungen relevante Basissumme |
| `addProductPromoCode(promoCodeId, dispatcher)` | Überprüft einen Aktionscode auf Gültigkeit und Nutzungsberechtigung und wendet ihn auf den Warenkorb an |
| `addProductPromoUse(promoId, promoCodeId, ...)` | Erfasst die Nutzung einer Promotion mit Rabattbetrag und Mengendetails |
| `clearAllPromotionInformation()` | Entfernt alle Promotions-Anpassungen, Free-Shipping-Aktionen und Promotion-Nutzungshistorie |
| `addOrderTerm(termTypeId, termValue, termDays, ...)` | Fügt Bestellbedingungen (z.B. Zahlungsziele) zum Auftrag hinzu |
| `makeOrderItems(explodeItems, replaceAggregatedId, dispatcher)` | Wandelt alle Warenkorb-Positionen in persistierbare OrderItem-GenericValues um; bei Bedarf werden konfigurierte Produkte als aggregierte Instanzen angelegt |
| `makeAllAdjustments()` | Sammelt alle Anpassungen (Rabatte, Aufschläge, Steuern) aus Kopf und Positionen für die Persistierung |
| `makeAllShipGroupInfos(dispatcher)` | Erstellt alle Versandgruppen-Datensätze mit Positionszuordnungen für die Persistierung |
| `makeAllOrderPaymentInfos(dispatcher)` | Erstellt alle Zahlungspräferenz-Datensätze mit automatischer Restbetragsverteilung |
| `makeCartMap(dispatcher, explodeItems)` | Erzeugt eine vollständige Map-Repräsentation des Warenkorbs als Eingabe für den `createOrder`-Service |
| `getSupplierProduct(productId, quantity, dispatcher)` | Ermittelt Lieferantenproduktdaten (inkl. Preis) für den aktuellen Lieferanten und eine bestimmte Bestellmenge |
| `getMinimumOrderQuantity(delegator, basePrice, productId)` | Prüft konfigurierte Mindestbestellmengen für ein Produkt |
| `setDefaultCheckoutOptions(dispatcher)` | Befüllt Versandadresse, -methode und -präferenzen mit sinnvollen Standardwerten für den Checkout |
| `clear()` | Setzt den gesamten Warenkorb zurück (löscht alle Positionen, Zahlungen, Versandgruppen, Notizen etc.) |
| `isPurchaseOrder() / isSalesOrder()` | Gibt an, ob es sich um eine Einkaufs- oder Verkaufsbestellung handelt |
| `isReadOnlyCart()` | Gibt an, ob der Warenkorb schreibgeschützt ist (z.B. bei abgeschlossenen Orders) |

---

### Klasse: `ShoppingCartItem`

**Paket:** `org.apache.ofbiz.order.shoppingcart`
**Typ:** Java-Klasse (implementiert `Serializable`)
**Zweck:** Repräsentiert eine einzelne Position im Warenkorb. Hält alle positionsspezifischen Daten: Produkt-ID, Menge, Basis- und Listenpreis, Sonderpreise, Features, Attribute, Versanddaten, Reservierungsinformationen (für Mietartikel), Anpassungen und Promotionsnutzung. Enthält Fabrikmethoden (`makeItem`, `makePurchaseOrderItem`) zur Validierung und Initialisierung aus dem Produktkatalog.

| Methode | Beschreibung |
|---|---|
| `makeItem(...)` | Statische Fabrikmethode: Erstellt eine neue Verkaufsposition mit vollständiger Produktvalidierung (Verfügbarkeit, Preisberechnung, Produktkonfiguration, externe Operationen) |
| `makePurchaseOrderItem(...)` | Statische Fabrikmethode: Erstellt eine Einkaufsposition mit Lieferantenpreisen |
| `setQuantity(quantity, dispatcher, cart)` | Setzt die Menge und löst Neuberechnung von Preisen und Bestand aus |
| `updatePrice(dispatcher, cart)` | Berechnet den Preis der Position neu anhand der aktuellen Warenkorb- und Benutzerinformationen |
| `getItemSubTotal()` | Berechnet die Zeilensumme (Basispreis × Menge + Anpassungen) |
| `getDisplayItemSubTotal()` | Liefert die angezeigte Zeilensumme (kann enthaltene Steuern umfassen) |
| `checkAvailability(productId, quantity, ...)` | Statische Methode: Prüft die Verfügbarkeit eines Mietprodukts für einen Reservierungszeitraum |
| `equals(productId, features, attributes, ...)` | Vergleicht die Position mit einem Produktbezeichner zur Erkennung identischer Positionen (für die addOrIncreaseItem-Logik) |
| `explodeItem(cart, dispatcher)` | Zerlegt eine Position in Einzelpositionen (Quantity-Explosion) für Lagerentnahmen |
| `getProduct()` | Gibt das zugehörige Produkt-Entity zurück (lazy loaded) |
| `getAdjustments()` | Liefert die Liste der positionsspezifischen Anpassungen (Rabatte, Steuern) |
| `addProductPromoAdjustment(adjustment)` | Fügt einen Promotionsrabatt zur Position hinzu |
| `resetPromoRuleUse(promoId, ruleId)` | Setzt den Promotions-Regelnutzungszähler zurück (für Neuberechnung) |
| `confirmPromoRuleUse(promoId, ruleId)` | Bestätigt die Nutzung einer Promotionsregel (nach erfolgreicher Berechnung) |
| `getOrderItemPriceInfos()` | Liefert Preisdetail-Datensätze (Rabattketten, Preisregeln) für die Persistierung |
| `getPurchaseOrderItemDescription(product, supplierProduct, locale, dispatcher)` | Ermittelt die Positionsbeschreibung für Einkaufsbestellungen aus Lieferantendaten |
| `setStatusId(statusId)` | Setzt den Status der Bestellposition |

---

### Klasse: `CheckOutHelper`

**Paket:** `org.apache.ofbiz.order.shoppingcart`
**Typ:** Java-Klasse
**Zweck:** Koordiniert den mehrstufigen Checkout-Prozess. Nimmt einen bestehenden ShoppingCart und führt sequenzielle Validierungs- und Berechnungsschritte durch: Lieferadresse setzen, Versandmethode wählen, Zahlungsdaten validieren, Steuer berechnen und schließlich den Auftrag platzieren.

| Methode | Beschreibung |
|---|---|
| `setCheckOutShippingAddress(shippingContactMechId)` | Setzt die Lieferadresse für den Checkout und validiert ihre Vollständigkeit |
| `setCheckOutShippingOptions(shippingMethod, shippingInstructions, ...)` | Setzt Versandmethode, Sonderhinweise, Lieferzeitfenster und Geschenkoptionen für alle Versandgruppen |
| `setCheckOutPayment(selectedPaymentMethods, singleUsePayments, billingAccountId)` | Weist Zahlungsmethoden mit Beträgen zu und validiert die Gesamtdeckung der Bestellsumme |
| `setCheckOutOptions(shippingMethod, shippingContactMechId, selectedPaymentMethods, ...)` | Fasst das Setzen aller Checkout-Optionen in einem Schritt zusammen |
| `calcAndAddTax()` | Berechnet die Verkaufssteuer über den externen Steuer-Service und trägt sie als Anpassungen in den Warenkorb ein |
| `createOrder(userLogin)` | Überführt den Warenkorb in eine persistente Bestellung durch Aufruf des `createOrder`-Services |
| `processPayment(productStore, userLogin, ...)` | Autorisiert alle Zahlungsmittel der Bestellung über die konfigurierten Zahlungs-Services |
| `availableAccountBalance(billingAccountId, dispatcher)` | Statische Hilfsmethode: Ermittelt den verfügbaren Saldo eines Rechnungskontos |

---

### Klasse: `ShoppingCartFactory`

**Paket:** `org.apache.ofbiz.order.shoppingcart`
**Typ:** Java-Klasse (Factory)
**Zweck:** Zentraler Einstiegspunkt zur Erzeugung von ShoppingCart-Instanzen. Abstrahiert die Konstruktoraufrufe und ermöglicht über den Builder-Pattern-Einstieg (`builder()`) die vollständige Konfiguration aller Komponenten vor dem Anlegen des Warenkorbs.

| Methode | Beschreibung |
|---|---|
| `createShoppingCart(delegator, productStoreId, locale, currencyUom)` | Erzeugt einen Standard-Warenkorb für einen gegebenen Store |
| `createSalesOrderCart(...)` | Erzeugt einen Warenkorb explizit als Verkaufsauftrag |
| `createPurchaseOrderCart(...)` | Erzeugt einen Warenkorb explizit als Einkaufsbestellung |
| `cloneShoppingCart(cart)` | Erstellt eine vollständige Kopie eines bestehenden Warenkorbs (Deep Copy aller Positionen und Einstellungen) |
| `createShoppingCartWithComponents(...)` | Erzeugt einen Warenkorb mit individuell angegebenen Komponent-Implementierungen (für Anpassungen im Projekt) |
| `builder()` | Gibt einen ShoppingCartBuilder zurück für den fluenten Aufbau eines konfigurierten Warenkorbs |

---

### Klasse: `ShoppingCartBuilder`

**Paket:** `org.apache.ofbiz.order.shoppingcart`
**Typ:** Java-Klasse (Builder)
**Zweck:** Implementiert das Builder-Pattern für die Erstellung von ShoppingCart-Instanzen. Erlaubt die schrittweise Konfiguration aller Pflicht- und optionalen Parameter sowie die Auswahl individueller Komponenten-Implementierungen vor dem `build()`-Aufruf.

---

### Klasse: `WebShoppingCart`

**Paket:** `org.apache.ofbiz.order.shoppingcart`
**Typ:** Java-Klasse (erweitert `ShoppingCart`)
**Zweck:** Web-spezifische Unterklasse des ShoppingCart. Initialisiert sich direkt aus einem `HttpServletRequest` — liest Store, Website, Locale, Währung und Benutzerinformationen aus der HTTP-Session aus, ohne dass diese Parameter explizit übergeben werden müssen.

---

### Klasse: `ShoppingCartHelper`

**Paket:** `org.apache.ofbiz.order.shoppingcart`
**Typ:** Java-Klasse
**Zweck:** Hilfsfunktionen für häufige Warenkorb-Operationen aus dem Web-Kontext, insbesondere das Verarbeiten von Form-Parametern (Massenzuordnung von Produkten, Mengenänderungen, Produktkonfigurationen) und das Anwenden von Bestellbedingungen.

---

### Klasse: `ShoppingCartEvents`

**Paket:** `org.apache.ofbiz.order.shoppingcart`
**Typ:** Java-Klasse (Event-Handler)
**Zweck:** Implementiert HTTP-Event-Handler für alle Warenkorb-Aktionen im Web-Frontend: Produkt hinzufügen, Menge ändern, Position entfernen, Aktionscode eingeben, Warenkorb leeren, Warenkorb aus der Session lesen/schreiben. Dient als Schicht zwischen Web-Requests und der ShoppingCart-Geschäftslogik.

---

### Klasse: `CheckOutEvents`

**Paket:** `org.apache.ofbiz.order.shoppingcart`
**Typ:** Java-Klasse (Event-Handler)
**Zweck:** HTTP-Event-Handler für den Checkout-Ablauf: Validierung und Weiterleitung bei jedem Checkout-Schritt (Adresse, Versand, Zahlung, Bestätigung), Integration von Single-Page-Checkout und Schnittstelle zu externen Checkout-Providern (z.B. PayPal).

---

### Klasse: `ShoppingCartServices`

**Paket:** `org.apache.ofbiz.order.shoppingcart`
**Typ:** Java-Klasse (Service-Implementierungen)
**Zweck:** OFBiz-Services rund um den Warenkorb: Positionen zwischen Versandgruppen verschieben, Warenkorb aus einer bestehenden Bestellung wiederherstellen und Warenkorb-Zustände persistieren.

| Methode | Beschreibung |
|---|---|
| `assignItemShipGroup(dctx, context)` | Verschiebt eine Warenkorb-Position von einer Versandgruppe in eine andere |
| `loadCartFromOrder(dctx, context)` | Lädt einen bestehenden Auftrag zurück in einen ShoppingCart (z.B. für Nachbestellungen oder Änderungen) |
| `getShoppingCartData(dctx, context)` | Serialisiert relevante Warenkorb-Daten für externe Verwendung |

---

### Klasse: `CartEventListener`

**Paket:** `org.apache.ofbiz.order.shoppingcart`
**Typ:** Java-Klasse (implementiert `HttpSessionListener`)
**Zweck:** Reagiert auf das Ablaufen einer HTTP-Session: Speichert den aktuellen Warenkorb automatisch in eine Shopping-Liste (Auto-Save), sofern der Produktstore dies konfiguriert hat, sodass der Benutzer beim nächsten Login seinen Warenkorb wiederherstellen kann.

---

### Klassen: Warenkorb-Komponenten-Interfaces und -Implementierungen

**Pakete:** `org.apache.ofbiz.order.shoppingcart.component` (Interfaces) und `org.apache.ofbiz.order.shoppingcart.components` (Implementierungen)
**Typ:** Interfaces und Java-Klassen

Der ShoppingCart ist über 8 ausgetauschbare Komponenten-Interfaces strukturiert. Jedes Interface kapselt einen abgegrenzten Verhaltensaspekt:

| Interface / Implementierung | Verantwortlichkeit |
|---|---|
| `IShoppingCartItems` / `ShoppingCartItemManager` | Verwaltung der Positionsliste: Hinzufügen, Entfernen, Sortieren, Iterieren von Warenkorb-Positionen; verwaltet auch Item-Gruppen |
| `IShoppingCartPricing` / `ShoppingCartPricing` | Preisberechnungen auf Positions- und Kopfebene |
| `IShoppingCartTaxes` / `ShoppingCartTaxes` | Steuerberechnungslogik |
| `IShoppingCartShipping` / `ShoppingCartShipping` | Versandgruppen-Verwaltung und -Kalkulation; hält `ShipInfo`-Unterobjekte |
| `IShoppingCartPromotion` / `ShoppingCartPromotion` | Promotions-Tracking: Nutzungshistorie und angewendete Aktions-Codes; hält `ProductPromoUseInfo`-Objekte |
| `IShoppingCartValidator` / `ShoppingCartValidator` | Validierungsregeln (z.B. ProductGeos, Zahlungsadresse); liefert `ValidationError`- und `ValidationWarning`-Objekte |
| `IShoppingCartPayment` / `ShoppingCartPayment` | Zahlungsinformationen (Methoden, Beträge, Referenzen); hält `CartPaymentInfo`-Objekte |
| `IShoppingCartPersistence` / `ShoppingCartPersistence` | Sammelt alle persistierbaren GenericValue-Listen für den `createOrder`-Service-Aufruf |

---

### Klasse: `ProductPromoWorker`

**Paket:** `org.apache.ofbiz.order.shoppingcart.product`
**Typ:** Java-Klasse (Utility, final, nur statische Methoden)
**Zweck:** Motor für die gesamte Promotionsberechnung. Wertet Promotionsregeln gegen den Warenkorb aus, wendet Aktionen an (Rabatte, Gratis-Versand, Geschenkartikel) und verwaltet die Nutzungsgrenzen von Aktionscodes.

| Methode | Beschreibung |
|---|---|
| `doPromotions(cart, dispatcher)` | Haupteinstiegspunkt: Wertet alle für den Produktstore gültigen Promotionen der Reihe nach gegen den Warenkorb aus und trägt die Ergebnisse (Anpassungen, Gratis-Artikel) ein |
| `getStoreProductPromos(delegator, dispatcher, request)` | Lädt alle aktiven Promotionen für den aktuellen Store aus der Datenbank |
| `checkCanUsePromoCode(promoCodeId, partyId, delegator, cart, locale)` | Prüft ob ein Aktionscode für den Kunden gültig ist (Nutzungslimit, Party-Zugehörigkeit, Gültigkeit) |
| `runProductPromoRules(cart, cartTotal, productPromo, ...)` | Wendet alle Regeln einer einzelnen Promotion gegen den Warenkorb an und löst die zugehörigen Aktionen aus |

---

### Klasse: `ProductDisplayWorker`

**Paket:** `org.apache.ofbiz.order.shoppingcart.product`
**Typ:** Java-Klasse
**Zweck:** Hilfsfunktionen für die Produktanzeige im Store-Kontext: Sortierung von Produktlisten, Ermittlung von empfohlenen Produkten und Berechnung von Mengenpreisen für die Darstellung.

---

### Klasse: `ProductStoreCartAwareEvents`

**Paket:** `org.apache.ofbiz.order.shoppingcart.product`
**Typ:** Java-Klasse (Event-Handler)
**Zweck:** Store-spezifische Event-Handler, die den Warenkorb-Zustand berücksichtigen, z.B. beim Wechsel des Produktstores innerhalb einer Session.

---

### Klasse: `ShippingEstimateWrapper`

**Paket:** `org.apache.ofbiz.order.shoppingcart.shipping`
**Typ:** Java-Klasse
**Zweck:** Berechnet und zwischenspeichert Versandkostenschätzungen für alle verfügbaren Versandmethoden eines Warenkorbs. Wird im Checkout zur Anzeige der Versandoptionen mit Preisvorschau eingesetzt.

| Methode | Beschreibung |
|---|---|
| `getWrapper(dispatcher, cart, shipGroupIndex)` | Statische Fabrikmethode: Erstellt und initialisiert den Wrapper für eine Versandgruppe |
| `getShippingMethods()` | Liefert alle verfügbaren Versandmethoden für den aktuellen Store |
| `getShippingEstimate(carrierShipmentMethod)` | Gibt die berechneten Versandkosten für eine bestimmte Methode zurück |

---

### Klasse: `ShippingEvents`

**Paket:** `org.apache.ofbiz.order.shoppingcart.shipping`
**Typ:** Java-Klasse (Event-Handler und Services)
**Zweck:** Event-Handler und Service-Methoden für Versandkostenberechnungen; koordiniert die Kommunikation mit externen Versanddienstleistern-Services.

---

### Klasse: `OrderServices`

**Paket:** `org.apache.ofbiz.order.order`
**Typ:** Java-Klasse (Service-Implementierungen)
**Zweck:** Kernservices für die Auftragsverarbeitung. Implementiert den kompletten Lebenszyklus einer Bestellung: Erstellen, Statusänderungen, Anpassungen, Storno, Inventarbuchungen und Zahlungsabwicklung. Mit 84 öffentlichen Methoden ist dies nach dem ShoppingCart die komplexeste Klasse des Moduls.

| Methode | Beschreibung |
|---|---|
| `createOrder(ctx, context)` | Erstellt einen neuen Auftrag aus einem Warenkorb-Daten-Map: Validiert Produkte (Verfügbarkeit, Einführungs-/Auslaufdaten), reserviert Lagerbestand, erstellt alle Datenbankdatensätze (Order-Header, -Positionen, -Rollen, -Kontaktdaten, -Zahlungen, -Versandgruppen, Tracking-Codes) in einer Transaktion |
| `updateOrderItems(ctx, context)` | Aktualisiert Mengen und Attribute bestehender Bestellpositionen mit Neuberechnung |
| `cancelOrderItem(ctx, context)` | Storniert eine einzelne Bestellposition und gibt reservierten Bestand frei |
| `cancelOrderItemShipGrpInvRes(ctx, context)` | Hebt Bestandsreservierungen für eine Versandgruppen-Position auf |
| `updateOrderStatus(ctx, context)` | Ändert den Status eines Auftrags-Headers |
| `updateOrderItemStatus(ctx, context)` | Ändert den Status einzelner Bestellpositionen |
| `quickChangeItemStatus(ctx, context)` | Schnelle Statusänderung einer Bestellposition ohne aufwändige Validierungskette |
| `addOrderItemShipGroup(ctx, context)` | Fügt einem bestehenden Auftrag eine neue Versandgruppe hinzu |
| `updateOrderItemShipGroup(ctx, context)` | Aktualisiert Versandadresse und -methode einer bestehenden Versandgruppe |
| `deleteOrderItemShipGroup(ctx, context)` | Löscht eine Versandgruppe aus einem Auftrag |
| `addOrderItem(ctx, context)` | Fügt nachträglich eine Position zu einem bestehenden Auftrag hinzu |
| `removeOrderItem(ctx, context)` | Entfernt eine Position aus einem Auftrag und korrigiert Bestandsreservierungen |
| `adjustOrderItems(ctx, context)` | Wendet Preisanpassungen auf Bestellpositionen an |
| `resetGrandTotal(ctx, context)` | Neuberechnung des Gesamtbetrags eines Auftrags anhand aller aktuellen Positionen und Anpassungen |
| `createOrderNote(ctx, context)` | Hängt eine Notiz an einen Auftrag an |
| `sendOrderConfirmation(ctx, context)` | Sendet die Auftragsbestätigungs-E-Mail an den Kunden |
| `massChangeOrderStatus(ctx, context)` | Ändert den Status mehrerer Aufträge auf einmal (Massenverarbeitung) |
| `checkOrderExternalInventory(ctx, context)` | Prüft externe Lagerverfügbarkeit und gibt Meldungen bei Engpässen zurück |
| `processOrderPayments(ctx, context)` | Löst die Zahlungsabwicklung für einen Auftrag aus (Autorisierung und ggf. Buchung) |
| `countProductQuantityOrdered(ctx, context)` | Zählt die bisher bestellte Gesamtmenge eines Produkts (für Limits) |
| `getOrderItemInvoicedAmountAndQuantity(ctx, context)` | Ermittelt die bereits in Rechnung gestellten Beträge und Mengen einer Bestellposition |
| `getOrderItemShippedQuantity(ctx, context)` | Liefert die tatsächlich versendete Menge einer Bestellposition |
| `getOrderItemsTotalNumber(ctx, context)` | Gibt die Gesamtanzahl der Bestellpositionen zurück |

---

### Klasse: `OrderReadHelper`

**Paket:** `org.apache.ofbiz.order.order`
**Typ:** Java-Klasse (Read-Only-Zugriff)
**Zweck:** Zentrales Lesehilfsobjekt für gespeicherte Aufträge. Kapselt alle Datenbankzugriffe auf einen persistierten Auftrag und bietet berechnete Aggregatwerte. Wird überall dort verwendet, wo auf Bestelldaten lesend zugegriffen werden muss, ohne einen ShoppingCart zu laden.

| Methode | Beschreibung |
|---|---|
| `getOrderId() / getOrderTypeId() / getOrderName()` | Liefert Basis-Metadaten des Auftrags aus dem OrderHeader |
| `getOrderItems()` | Lädt alle Positionen des Auftrags |
| `getAdjustments()` | Lädt alle Preisanpassungen des Auftrags |
| `getPaymentPreferences()` | Lädt alle Zahlungspräferenzen des Auftrags |
| `getOrderPayments(orderPaymentPreference)` | Liefert alle Zahlungstransaktionen, optional gefiltert nach Zahlungspräferenz |
| `getReceivedPaymentTotalsByPaymentMethod()` | Summiert eingegangene Zahlungen gruppiert nach Zahlungsmethode |
| `getReturnedTotalsByPaymentMethod()` | Summiert Rückerstattungen gruppiert nach Zahlungsmethode |
| `getOrderStatuses()` | Liefert die Statushistorie des Auftrags |
| `getOrderTerms() / getOrderTermNetDays()` | Liefert Zahlungsbedingungen; berechnet das Nettozahlungsziel in Tagen |
| `getShippingMethod(shipGroupSeqId)` | Gibt die Versandmethode einer Versandgruppe als lesbaren String zurück |
| `getShippingAddress(shipGroupSeqId)` | Liefert die Lieferadresse einer bestimmten Versandgruppe |
| `getShippingLocations()` | Liefert alle Lieferadressen des Auftrags (über alle Versandgruppen) |
| `getBillingLocations()` | Liefert alle Rechnungsadressen des Auftrags |
| `getOrderItemShipGroups()` | Gibt alle Versandgruppen des Auftrags zurück |
| `hasPhysicalProductItems()` | Prüft, ob der Auftrag physische (versendbare) Produkte enthält |
| `getOrderContactMechs(contactMechPurposeTypeId)` | Liefert Kommunikationswege eines bestimmten Zwecks (Rechnungsadresse, Lieferadresse etc.) |
| `getPlacingParty() / getEndUserParty() / getBillToParty()` | Ermittelt die jeweilige Partei in ihrer spezifischen Rolle im Auftrag |
| `getProductStoreFromOrder(delegator, orderId)` | Statische Hilfsmethode: Lädt den Produktstore zu einem Auftrag |
| `calcOrderAdjustments(adjustments, subTotal, ...)` | Statische Methode: Berechnet den Gesamtwert von Anpassungen (Rabatt, Versand, Sonstiges) |
| `getOrderItemAdjustmentTotal(orderItem, adjustments)` | Berechnet die Summe aller Anpassungen für eine einzelne Bestellposition |
| `getOrderItemSubTotal(orderItem, adjustments)` | Berechnet die Zeilensumme einer Position inklusive Anpassungen |
| `getOrderGrandTotal(orderItems, adjustments)` | Berechnet den Gesamtbetrag eines Auftrags |
| `getItemStatusString(orderItem, locale)` | Liefert den lesbaren Status einer Bestellposition |

---

### Klasse: `OrderReturnServices`

**Paket:** `org.apache.ofbiz.order.order`
**Typ:** Java-Klasse (Service-Implementierungen)
**Zweck:** Services für die Retourenabwicklung: Rückgabeanträge erstellen und verwalten, Erstattungsbeträge berechnen, Rückgabepositionen verwalten und Gutschriften/Rückerstattungen auslösen.

| Methode | Beschreibung |
|---|---|
| `getReturnItemInitialCost(dctx, context)` | Ermittelt die ursprünglichen Kosten einer Rückgabeposition aus den Bestelldaten |
| `getOrderAvailableReturnedTotal(dctx, context)` | Berechnet den noch erstattbaren Betrag für eine Bestellung abzüglich bereits genehmigter Rückgaben |
| `createReturnHeader(dctx, context)` | Erstellt einen neuen Rückgabeantrag (ReturnHeader) |
| `createReturnItem(dctx, context)` | Fügt eine Position einem Rückgabeantrag hinzu |
| `updateReturnHeader(dctx, context)` | Aktualisiert Metadaten eines Rückgabeantrags |
| `updateReturnItem(dctx, context)` | Ändert Menge oder Rückgabegrund einer Rückgabeposition |
| `processReturn(dctx, context)` | Verarbeitet einen genehmigten Rückgabeantrag: löst Gutschriften, Rückzahlungen und ggf. Lagereinbuchungen aus |
| `updateReturnToBillingAccount(dctx, context)` | Schreibt Rückerstattungsbeträge einem Rechnungskonto gut |
| `getReturnAmountByOrder(dctx, context)` | Summiert alle Rückgabebeträge zu einer Bestellung |

---

### Klasse: `OrderChangeHelper`

**Paket:** `org.apache.ofbiz.order.order`
**Typ:** Java-Klasse (Utility, final, nur statische Methoden)
**Zweck:** Workflow-Hilfsmethoden für Auftragsstatusübergänge: Genehmigen, Ablehnen und Stornieren von Aufträgen mit den zugehörigen Folgeoperationen (Bestandsreservierungen, Zahlungsfreigaben).

| Methode | Beschreibung |
|---|---|
| `approveOrder(dispatcher, userLogin, orderId, holdOrder)` | Genehmigt einen Auftrag und setzt Header- und Positions-Status entsprechend der Store-Konfiguration |
| `rejectOrder(dispatcher, userLogin, orderId)` | Lehnt einen Auftrag ab, setzt Status auf REJECTED und gibt Bestandsreservierungen sowie Zahlungsautorisierungen frei |
| `cancelOrder(dispatcher, userLogin, orderId)` | Storniert einen Auftrag vollständig |
| `orderStatusChanges(dispatcher, userLogin, orderId, ...)` | Führt koordinierte Statusänderungen über mehrere OrderItem-Status-Update-Services durch |
| `cancelInventoryReservations(dispatcher, userLogin, orderId)` | Gibt alle Bestandsreservierungen für einen Auftrag frei |
| `releasePaymentAuthorizations(dispatcher, userLogin, orderId)` | Gibt alle Zahlungsautorisierungen eines abgelehnten Auftrags frei |

---

### Klasse: `OrderEvents`

**Paket:** `org.apache.ofbiz.order.order`
**Typ:** Java-Klasse (Event-Handler)
**Zweck:** HTTP-Event-Handler für auftragsgebundene Aktionen: Download digitaler Produkte nach Bestellabschluss und Stornierung ausgewählter Positionen.

| Methode | Beschreibung |
|---|---|
| `downloadDigitalProduct(request, response)` | Prüft die Kaufberechtigung des Benutzers und liefert das digitale Produkt als Datei-Download aus |
| `cancelSelectedOrderItems(request, response)` | Storniert ausgewählte Bestellpositionen über den zugehörigen Service |

---

### Klasse: `OrderLookupServices`

**Paket:** `org.apache.ofbiz.order.order`
**Typ:** Java-Klasse (Service-Implementierungen)
**Zweck:** Flexibler Auftrags-Suchdienst mit umfangreichen Filtermöglichkeiten: Suche nach Auftrags-ID, Kundennummer, Produkt-ID, Status, Store, Datumsbereich, Tracking-Code, interner Nummer und weiteren Kriterien. Liefert paginierte Ergebnisse.

| Methode | Beschreibung |
|---|---|
| `findOrders(dctx, context)` | Führt eine dynamische Auftrags-Suche mit beliebig kombinierbaren Filterkriterien durch und liefert eine paginierte Ergebnisliste |

---

### Klasse: `OrderListState`

**Paket:** `org.apache.ofbiz.order.order`
**Typ:** Java-Klasse (implementiert `Serializable`)
**Zweck:** Persistente Session-Repräsentation des Zustands einer Auftragslisten-Anzeige (aktive Filter, aktuelle Seite, Sortierung). Wird als Session-Attribut gespeichert, damit der Benutzer zwischen Auftrags-Detail und -Liste navigieren kann ohne den Filterkontext zu verlieren.

---

### Klasse: `OrderContentWrapper`

**Paket:** `org.apache.ofbiz.order.order`
**Typ:** Java-Klasse (implementiert `ContentWrapper`)
**Zweck:** Stellt lokalisierte Content-Inhalte (z.B. Beschreibungen) für Auftragsobjekte bereit, integriert in das OFBiz-Content-Framework.

---

### Klasse: `QuoteServices`

**Paket:** `org.apache.ofbiz.order.quote`
**Typ:** Java-Klasse (Service-Implementierungen)
**Zweck:** Services für die Angebotsverwaltung: Angebots-E-Mails versenden, Angebote in Aufträge umwandeln und Angebots-Preisdetails berechnen.

| Methode | Beschreibung |
|---|---|
| `sendQuoteReportMail(dctx, context)` | Versendet ein Angebot per E-Mail an einen Empfänger unter Verwendung des Store-E-Mail-Templates |
| `createQuoteFromCart(dctx, context)` | Erstellt ein Angebot aus einem bestehenden Warenkorb |
| `createOrderFromQuote(dctx, context)` | Wandelt ein genehmigtes Angebot in eine Bestellung um |
| `calculateQuoteCoefficients(dctx, context)` | Berechnet Deckungsbeiträge und Marge für ein Angebot |

---

### Klasse: `RequirementServices`

**Paket:** `org.apache.ofbiz.order.requirement`
**Typ:** Java-Klasse (Service-Implementierungen)
**Zweck:** Services für die Einkaufsanforderungsverwaltung: Anforderungen für einen Lieferanten zusammenstellen, in Einkaufsbestellungen überführen und offene Anforderungen verwalten.

| Methode | Beschreibung |
|---|---|
| `getRequirementsForSupplier(ctx, context)` | Listet alle offenen genehmigten Produktanforderungen für einen Lieferanten auf, optional nach Status gefiltert |
| `createAutoRequirementsForMfgTasks(ctx, context)` | Erstellt automatisch Materialanforderungen für geplante Fertigungsaufgaben |
| `createRequirementFromShoppingList(ctx, context)` | Konvertiert Einkaufslisten-Einträge in Einkaufsanforderungen |

---

### Klasse: `ShoppingListServices`

**Paket:** `org.apache.ofbiz.order.shoppinglist`
**Typ:** Java-Klasse (Service-Implementierungen)
**Zweck:** Services für persistente Einkaufslisten: automatisch gespeicherte Listen (Auto-Save), Wunschlisten, wiederkehrende Einkaufslisten mit konfigurierbaren Wiederholungsintervallen und Listen-zu-Warenkorb-Konvertierung.

| Methode | Beschreibung |
|---|---|
| `setShoppingListRecurrence(dctx, context)` | Konfiguriert die Wiederholungsregel (täglich, wöchentlich, monatlich) für eine Einkaufsliste |
| `addListToCart(dctx, context)` | Überträgt alle Positionen einer Einkaufsliste in den aktiven Warenkorb |
| `calculateShoppingListTotal(dctx, context)` | Berechnet den Gesamtpreis einer Einkaufsliste |
| `createShoppingListsFromOrder(dctx, context)` | Erstellt aus einem abgeschlossenen Auftrag eine neue Einkaufsliste für Nachbestellungen |
| `makeShoppingListFromOrder(dctx, context)` | Konvertiert eine Bestellung direkt in eine wiederverwendbare Einkaufsliste |
| `updateShoppingListQuantitiesFromOrder(dctx, context)` | Aktualisiert Mengen in einer gespeicherten Einkaufsliste anhand einer Bestellung |

---

### Klasse: `ShoppingListEvents`

**Paket:** `org.apache.ofbiz.order.shoppinglist`
**Typ:** Java-Klasse (Event-Handler)
**Zweck:** HTTP-Event-Handler für Einkaufslisten-Operationen im Web-Frontend: Liste in Warenkorb übertragen, Auto-Save-Logik bei Seitenaufruf, Listen-Verwaltung.

---

### Klasse: `FinAccountHelper`

**Paket:** `org.apache.ofbiz.order.finaccount`
**Typ:** Java-Klasse (Utility, final)
**Zweck:** Hilfsmethoden für Finanzkonten (Geschenkgutscheine, Store-Kredite): Validierung, Kontonummern-Generierung und Saldoberechnungen.

| Methode | Beschreibung |
|---|---|
| `addFirstEntryAmount(initialValue, transactions, fieldName, ...)` | Addiert den Betrag des ersten Eintrags aus einer Transaktionsliste auf einen Startwert |
| `getRandomString(length)` | Generiert einen kryptographisch sicheren Zufallsstring für Kontonummern und PINs |
| `getZeroAmount(delegator)` | Liefert den gerundeten Nullbetrag gemäß Systemkonfiguration |
| `getGiftCertFinAccountTypeId()` | Gibt die konfigurierte Geschenkgutschein-Kontenart-ID zurück |

---

### Klasse: `OrderManagerEvents`

**Paket:** `org.apache.ofbiz.order`
**Typ:** Java-Klasse (Event-Handler)
**Zweck:** Event-Handler für den Order-Manager im Back-Office: Auftragsübersichten filtern, Statusänderungen aus der Listansicht heraus, Massenfunktionen.

---

### Klasse: `ExpressCheckoutEvents`

**Paket:** `org.apache.ofbiz.order.thirdparty.paypal`
**Typ:** Java-Klasse (Event-Handler)
**Zweck:** Integration des PayPal-ExpressCheckout-Verfahrens: Weiterleitung zu PayPal, Rückverarbeitung nach PayPal-Bestätigung, Fehlerbehandlung und Konvertierung der PayPal-Antwortdaten in OFBiz-Zahlungseinträge.

---

### Klasse: `ZipSalesServices`

**Paket:** `org.apache.ofbiz.order.thirdparty.zipsales`
**Typ:** Java-Klasse (Service-Implementierungen)
**Zweck:** Steuerberechnung anhand von ZIP-Code-basierten Steuertabellen (US-spezifisch): Importiert Steuertabellen-Daten und berechnet Verkaufssteuern auf Basis der Lieferpostleitzahl.

---

### Klasse: `TaskEvents`

**Paket:** `org.apache.ofbiz.order.task`
**Typ:** Java-Klasse (Event-Handler)
**Zweck:** Event-Handler für auftragsbezogene Aufgaben (Tasks): Bearbeitung und Statusänderung von aufgabengebundenen Bestellprozessen.

---

### Klasse: `TaskWorker`

**Paket:** `org.apache.ofbiz.order.task`
**Typ:** Java-Klasse (Utility)
**Zweck:** Hilfsmethoden für die Aufgaben-/Workflow-Verarbeitung zu Bestellungen.

---

### Ausnahme-Klassen

| Klasse | Paket | Beschreibung |
|---|---|---|
| `CartItemModifyException` | `shoppingcart` | Ausnahme für ungültige Warenkorb-Änderungen (ReadOnly-Cart, Geo-Verletzungen, Mindestmengen) |
| `ItemNotFoundException` | `shoppingcart` | Ausnahme wenn ein gesuchtes Produkt nicht im Katalog oder Warenkorb gefunden wird |

---

### Groovy-Scripts: Auftragserfassung (`org.apache.ofbiz.order.entry`)

Die Groovy-Scripts im Paket `entry` und `entry.cart`/`entry.catalog` sind View-Preparation-Scripts, die Daten für UI-Screens aufbereiten. Sie laufen ohne eigene fachliche Methoden (nur `run()`-Einstiegspunkt) und werden thematisch gruppiert:

**Checkout-Ablauf:**
- `CheckInits` — Initialisiert Checkout-Seite, prüft Warenkorb-Voraussetzungen
- `CheckoutOptions` — Bereitet allgemeine Checkout-Optionen vor
- `CheckoutShippingAddress` — Stellt Adressdaten für Versandauswahl bereit
- `CheckoutPayment` — Lädt verfügbare Zahlungsmethoden und aktuelle Zahlungsauswahl
- `CheckoutReview` — Sammelt alle Daten für die Checkout-Bestätigungsseite
- `BillSettings` / `ShipSettings` — Rechnungs- und Versandeinstellungen
- `OptionSettings` — Allgemeine Bestelloptionen (Auftragstyp, Kanal)
- `SetCheckOutTabBar` — Steuert die Sichtbarkeit der Checkout-Navigationsleiste
- `SetShoppingCart` — Legt den aktuellen Warenkorb als Screen-Kontextvariable fest

**Auftragserfassung:**
- `AddGiftCertificates` — Bereitet Geschenkgutschein-Hinzufügen vor
- `AdditionalPartyListing` / `SetAdditionalParty` — Verwaltung zusätzlicher Parteien
- `OrderAgreements` / `OrderTerms` — Vertrags- und Zahlungsbedingungen
- `ShowCart` — Hauptanzeige des Warenkorbs
- `ShowPromoText` — Zeigt aktive Promotions-Texte
- `SplitShip` — Aufteilen des Warenkorbs auf mehrere Versandgruppen
- `StorePaymentOptions` / `SetAdditionalParty` — Store-spezifische Zahlungsoptionen
- `ShoppingList` — Einkaufslisten-Anzeige im Auftragskontext

**Katalog-Browsing (`entry.catalog`):**
- `Category` / `CategoryDetail` / `SideDeepCategory` — Kategorien-Anzeige und -Navigation
- `Product` / `ProductDetail` / `ProductSummary` / `InlineProductDetail` — Produkt-Detailseiten
- `AdvancedSearchOptions` / `KeywordSearch` / `KeywordSearchOptions` — Suche
- `CompareProducts` — Produktvergleich
- `PrepareConfigForm` — Konfigurierbare Produkte (Produktkonfigurator)
- `QuickAdd` / `ProductUomDropDownOnly` — Schnellerfassung
- `ChooseCatalog` — Katalogauswahl

**Warenkorb-Extras (`entry.cart`):**
- `LookupBulkAddProducts` / `LookupBulkAddSupplierProducts` — Massenerfassung
- `ShowPromotionDetails` — Detailansicht aktiver Promotionen

---

### Groovy-Scripts: Auftragsmanagement (`org.apache.ofbiz.order.order`)

Scripts für die Auftrags-Detailansicht und -bearbeitung im Back-Office:

| Script | Funktion |
|---|---|
| `OrderView` | Hauptscreen Auftragsanzeige: lädt alle Detaildaten eines Auftrags |
| `OrderViewWebSecure` | Sicherheitsgeprüfte Variante der Auftragsanzeige für Kunden-Self-Service |
| `OrderList` / `FindOrders` / `FilterOrderList` | Auftragssuche und -listansicht |
| `OrderHistory` | Statushistorie eines Auftrags |
| `OrderStats` | Bestellstatistiken (Mengen, Umsätze) |
| `OrderDeliveryScheduleInfo` / `OrderDeliveryServices` | Liefertermin-Informationen |
| `ShipGroups` | Verwaltung der Versandgruppen-Ansicht |
| `NewNote` | Neue Notiz zu einem Auftrag erfassen |
| `CompanyHeader` | Firmen-Kopfzeile für Bestelldrucke |
| `AddOrderAttachments` | Anhänge zu einem Auftrag verwalten |
| `CheckoutServices` | Checkout-Service-Auslösung aus dem Back-Office |
| `ReceivePayment` | Manuelle Zahlungserfassung zu einem Auftrag |
| `SendConfirmationEmail` | Auftragsbestätigungs-E-Mail manuell auslösen |
| `OrderRequirementServicesScript` / `OrderServicesScript` / `OrderReturnServicesScript` | Groovy-Wrapper für Java-Services (delegieren an OrderServices, OrderReturnServices) |
| `ViewImage` | Bilddaten für auftragsgebundene Produkte anzeigen |

---

### Groovy-Scripts: Retouren, Angebote, Anforderungen, weitere Bereiche

**Retouren (`org.apache.ofbiz.order.orderReturn`):**

| Script | Funktion |
|---|---|
| `QuickReturn` | Schnellerfassung einer Rückgabe |
| `ReturnHeader` | Kopfdaten eines Rückgabeantrags anzeigen/bearbeiten |
| `ReturnHistory` | Rückgabehistorie anzeigen |
| `ReturnItems` | Positionen eines Rückgabeantrags verwalten |

**Angebote (`org.apache.ofbiz.order.quote`):**

| Script | Funktion |
|---|---|
| `GetPartyAddress` / `GetPartyEmailAddress` | Kontaktdaten für Angebots-E-Mail ermitteln |
| `ManageQuotePrices` | Angebotspreise und Konditionen bearbeiten |
| `ViewQuoteProfit` | Deckungsbeitragsanzeige für ein Angebot |
| `QuoteServicesScript` | Groovy-Wrapper für QuoteServices |

**Anforderungen (`org.apache.ofbiz.order.requirement`):**

| Script | Funktion |
|---|---|
| `ApprovedProductRequirements` | Genehmigte Produktanforderungen auflisten |
| `ApprovedProductRequirementsByVendor` | Genehmigte Anforderungen gruppiert nach Lieferant |
| `SelectCreatedProposed` | Neu erstellte/vorgeschlagene Anforderungen selektieren |
| `RequirementServicesScript` | Groovy-Wrapper für RequirementServices |

**Weitere Scripts:**

| Script | Paket | Funktion |
|---|---|---|
| `CreateAllocationPlan` / `ListAllocationPlan` / `ViewAllocationPlan` | `allocationplan` | Zuteilungsplanung für Aufträge erstellen, listen, anzeigen |
| `CommunicationServices` | `communications` | Bestellbezogene Kommunikations-Services |
| `LookupAssociatedProducts` | `lookup` | Verwandte Produkte für Auftrags-Positionen suchen |
| `OpenOrderItemsReport` | `reports` | Bericht offener Bestellpositionen |
| `GetNextSequenceNum` / `RequestItemNotes` / `SetRequestQuote` | `request` | Kundenanfragen-Verwaltung |
| `PaymentSetup` | `setup` | Zahlungs-Konfiguration für den Store |
| `OrderBlacklistServices` | `order` (root) | Blacklist-Prüfung für Kunden/Adressen |
| `OrderTaskList` | `task` | Aufgabenliste für auftragsgebundene Workflows |
| `ShoppingListServicesScript` | `shoppinglist` | Groovy-Wrapper für ShoppingListServices |

---

### Tests

#### Testklassen im Paket `org.apache.ofbiz.order.test` (Java)

| Klasse | Beschreibung |
|---|---|
| `OrderTest` | Basistest-Klasse; prüft grundlegende Order-Service-Funktionalitäten |
| `SalesOrderTest` | End-to-end Tests für Verkaufsaufträge (Erstellen, Statusübergänge, Zahlungen) |
| `PurchaseOrderTest` | Tests für Einkaufsbestellungen und Lieferanten-Workflows |
| `FinAccountTest` | Tests für Finanzkonto-Funktionalitäten (Gift Cards, Konten-Validierung) |
| `OrderTestServices` | Hilfsdienste speziell für Testszenarien (Testdaten anlegen/bereinigen) |

#### Testklassen im Paket `org.apache.ofbiz.order.order.test` (Groovy/JUnit)

| Klasse | Beschreibung |
|---|---|
| `OrderTests` | Automatisierte Tests für die Kern-Order-Services |
| `OrderRequirementTests` | Tests für Einkaufsanforderungs-Workflows |
| `OrderReturnTests` | Tests für Retourenverarbeitung |
| `QuoteTests` | Tests für die Angebotserstellung und -konvertierung |
| `ShoppingListTests` | Tests für Einkaufslisten-Services |
| `CustRequestPermissionCheckTests` | Tests für rollenbasierte Zugriffskontrollen auf Kundenanfragen |
