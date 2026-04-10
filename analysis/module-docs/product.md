# Modul: product

## Überblick

Das Modul `product` ist das zentrale Produktmanagement-Modul von Apache OFBiz. Es deckt die vollständige Lebenszyklus-Verwaltung von Produkten ab: von der Produktstammdaten-Pflege über Kategorie- und Kataloghierarchien, Preisfindung, Lagerhaltung und Lieferung bis hin zu Aktionen, Abonnements und Bilddatei-Verwaltung. Das Modul bildet die fachliche Domäne eines klassischen B2B/B2C-Produktkatalogs ab und stellt sowohl Service-APIs als auch HTTP-Servlet- und FreeMarker-Integrationspunkte bereit.

## Submodule

| Paket | Beschreibung |
|---|---|
| `org.apache.ofbiz.product.product` | Kerndatenmodell und Hilfsfunktionen für Produkte (Worker, Services, Events, Suche, Keyword-Index, Content-Wrapper) |
| `org.apache.ofbiz.product.catalog` | Katalogstruktur und -verwaltung; Zugriff auf Kataloglisten und Store-Katalog-Zuordnungen |
| `org.apache.ofbiz.product.category` | Produktkategorien, SEO-URL-Filterung, Kategorie-Navigation und FreeMarker-Transforms für URL-Generierung |
| `org.apache.ofbiz.product.config` | Konfigurierbare Produkte (Aggregated Products): Wrapper für Konfigurationsoptionen und Preisberechnung |
| `org.apache.ofbiz.product.feature` | Produktmerkmale (Features): parametrische Suche und CRUD-Services für Feature-Typen und -Gruppen |
| `org.apache.ofbiz.product.image` | Skalierung von Produktbildern in mehrere Standardgrößen (small, medium, large, detail) |
| `org.apache.ofbiz.product.imagemanagement` | Erweiterte Bildverwaltung: Upload, Zuschneiden, Drehen, Rahmen, Statusworkflow (Genehmigung/Ablehnung) |
| `org.apache.ofbiz.product.inventory` | Lagerhaltung: Bestandsprüfung, Umbuchung, Verbrauchsbuchung und durchschnittliche Einstandspreisermittlung |
| `org.apache.ofbiz.product.migrate` | Migrationsdienste für Datenbankschema-Upgrades |
| `org.apache.ofbiz.product.price` | Preisfindungslogik inklusive Regelauswertung, Mengenstaffeln, Steuerberechnung und Vereinbarungspreise |
| `org.apache.ofbiz.product.promo` | Aktionsverwaltung: Promo-Code-Generierung, Aktionsbedingungen und -aktionen (Rabatt, Gratisartikel, Versandkosten) |
| `org.apache.ofbiz.product.shipment` | Versandabwicklung: Sendungserstellung, Verpackung, Kommissionierung, Wareneingang und Statusübergänge |
| `org.apache.ofbiz.product.spreadsheetimport` | Import von Produktdaten aus Excel-Dateien (Apache POI) |
| `org.apache.ofbiz.product.store` | Produktshop-Konfiguration: Store-Einstellungen, Inventory-Prüfung, Umfragen und Event-Handler |
| `org.apache.ofbiz.product.subscription` | Abonnement-Verwaltung: Laufzeitverlängerung, Berechtigungsprüfung |
| `org.apache.ofbiz.product.supplier` | Lieferanten-Produkt-Zuordnungen: Abfrage von Lieferantenkonditionen |
| `org.apache.ofbiz.product.facility.*` (Groovy-Views) | Lager-/Facility-Verwaltungs-Screens: Inventur, Bestandsübersichten, Versand, Kommissionierlisten |
| `org.apache.ofbiz.product.catalog.*` (Groovy-Views) | Admin-Screens für Katalog, Kategorien, Features, Preisregeln, Aktionen, Bilddatei-Management |
| `org.apache.ofbiz.product.*.test` | Automatisierte Integrationstests (OFBizTestCase-Subklassen) |

---

## Klasse: `ProductWorker`

**Paket:** `org.apache.ofbiz.product.product`
**Typ:** Java-Klasse (Utility, `final`, nicht instantiierbar)
**Zweck:** Zentrale Hilfsbibliothek für produktbezogene Geschäftslogik. Wird von Services, Events und Views überall im Modul verwendet.

| Methode | Beschreibung |
|---|---|
| `shippingApplies(product)` | Prüft, ob für ein Produkt Versandkosten anfallen (Services und digitale Produkte ausgenommen) |
| `isBillableToAddress(product, postalAddress)` | Prüft, ob ein Produkt an eine Rechnungsadresse geliefert werden darf (Geo-Einschränkungen) |
| `isShippableToAddress(product, postalAddress)` | Prüft, ob ein Produkt an eine Lieferadresse verschickt werden darf (Geo-Include/Exclude-Logik) |
| `isSerialized(delegator, productId)` | Gibt an, ob Lagerartikel für dieses Produkt serialisiert verwaltet werden |
| `taxApplies(product)` | Gibt zurück, ob das Produkt steuerpflichtig ist |
| `getInstanceAggregatedId(delegator, instanceProductId)` | Ermittelt die übergeordnete Aggregated-Product-ID für eine konfigurierte Instanz |
| `getAggregatedInstanceId(delegator, aggregatedProductId, configId)` | Findet die konkrete Variante eines konfigurierbaren Produkts anhand der Konfigurations-ID |
| `getVariantVirtualId(variantProduct)` | Liefert die ID des übergeordneten virtuellen Produkts für eine Variante |
| `getVariantDistinguishingFeatures(variantProduct)` | Gibt die Merkmale zurück, die eine Variante von anderen Varianten des gleichen virtuellen Produkts unterscheiden |
| `getProductFeaturesByApplTypeId(product, typeId)` | Liefert alle Merkmale eines Produkts für einen bestimmten Anwendungstyp (z.B. SELECTABLE_FEATURE) |
| `getSelectableProductFeaturesByTypesAndSeq(product)` | Gibt alle wählbaren Merkmale gruppiert nach Merkmaltyp und Reihenfolge zurück (für Variantenauswahl) |
| `getVariantSelectionFeatures(variantProduct)` | Ermittelt die für die Auswahl dieser Variante relevanten Merkmale |
| `getOptionalProductFeatures(delegator, productId)` | Liefert optionale Produktmerkmale, geordnet nach Merkmaltyp |
| `getVariantFromFeatureTree(productId, selectedFeatures, delegator)` | Sucht die passende Variante anhand einer Merkmalauswahl; legt bei Bedarf eine neue Variante an |
| `calcOrderAdjustments(adjustments, subTotal, ...)` | Berechnet die Summe aller Auftragsanpassungen (Steuern, Versand, Sonstiges) |
| `calcOrderAdjustment(orderAdjustment, subTotal)` | Berechnet den Betrag einer einzelnen Auftragsanpassung (Absolutbetrag oder prozentualer Anteil) |
| `filterOrderAdjustments(adjustments, ...)` | Filtert eine Liste von Auftragsanpassungen nach Typen (Steuer, Versand, Sonstiges) |
| `getAverageProductRating(product, reviews, storeId, delegator)` | Berechnet die Durchschnittsbewertung eines Produkts aus Rezensionen, mit Unterstützung für Mindestwert/Maximalwert-Konfiguration |
| `getCurrentProductCategories(product)` | Gibt alle aktiven Kategorien zurück, in denen das Produkt gelistet ist |
| `getParentProduct(productId, delegator)` | Ermittelt das übergeordnete (virtuelle) Produkt über PRODUCT_VARIANT- oder UNIQUE_ITEM-Assoziationen |
| `isDigital(product)` / `isPhysical(product)` | Prüft den Produkttyp auf digitale bzw. physische Natur |
| `isVirtual(delegator, productId)` | Prüft, ob ein Produkt als virtuelles Produkt (Hülle für Varianten) markiert ist |
| `isSellable(product, atTime)` | Prüft, ob das Produkt zum gegebenen Zeitpunkt verkäuflich ist (Einführungs-/Abkündigungsdatum) |
| `isAlternativePacking(delegator, productId, virtualVariantId)` | Stellt fest, ob ein Produkt als alternative Verpackungsvariante zu einem anderen verknüpft ist |
| `findProductsById(delegator, idToFind, typeId, ...)` | Sucht Produkte nach Produkt-ID oder Fremdidentifikator (GoodIdentification) |
| `findProduct(delegator, idToFind)` | Gibt das erste gefundene Produkt für einen Identifikator zurück |
| `getProductWeight(product, desiredUomId, ...)` | Liefert das Produktgewicht, ggf. nach Einheitenumrechnung |
| `filterOutOfStockProducts(products, dispatcher, delegator)` | Filtert nicht lagerhaltige Produkte aus einer Liste heraus (berücksichtigt Marketing-Pakete und virtuelle Produkte) |
| `isDecimalQuantityOrderAllowed(delegator, productId, storeId)` | Prüft, ob Dezimalmengen bei der Bestellung erlaubt sind (Produkt- und Shop-Einstellung) |
| `isAggregateService(delegator, productId)` | Prüft, ob es sich um einen konfigurierbaren Service-Produkttyp handelt |
| `getRefurbishedProductIdSet(productId, delegator)` | Liefert alle aufbereiteten (refurbishten) Varianten-IDs eines Produkts |

---

## Klasse: `ProductServices`

**Paket:** `org.apache.ofbiz.product.product`
**Typ:** Java-Klasse (OFBiz-Service-Implementierung)
**Zweck:** Service-Methoden für Produktvarianten, Merkmalbaum-Aufbau und Bildverwaltung. Wird als OFBiz-Service-Implementierung registriert.

| Methode | Beschreibung |
|---|---|
| `prodFindAllVariants(dctx, context)` | Gibt alle aktiven Varianten eines virtuellen Produkts zurück |
| `prodFindSelectedVariant(dctx, context)` | Sucht die Variante, die zu einer gewählten Merkmalskombination passt |
| `prodFindFeatureTypes(dctx, context)` | Liefert alle distinkten Merkmaltypen eines Produkts für einen Anwendungstyp |
| `prodMakeFeatureTree(dctx, context)` | Baut den hierarchischen Merkmalsbaum für die Variantenauswahl auf, inklusive Lagerprüfung |
| `prodGetFeatures(dctx, context)` | Liest Produktmerkmale nach Typ und Anwendungsart aus |
| `prodFindProduct(dctx, context)` | Gibt ein Produkt zurück; bei Varianten wird automatisch zum übergeordneten virtuellen Produkt navigiert |
| `prodFindAssociatedByType(dctx, context)` | Liefert alle Produktassoziationen eines bestimmten Typs (bidirektional möglich) |
| `quickAddVariant(dctx, context)` | Legt eine neue Variante an und verknüpft sie mit dem virtuellen Produkt sowie den gewählten Merkmalen |
| `quickCreateVirtualWithVariants(dctx, context)` | Erstellt ein neues virtuelles Produkt und ordnet ihm bestehende oder neue Varianten zu |
| `updateProductIfAvailableFromShipment(dctx, context)` | Reaktiviert ein abgekündigtes Produkt, wenn nach einem Wareneingang wieder Bestand vorhanden ist |
| `addAdditionalViewForProduct(dctx, context)` | Lädt ein zusätzliches Produktbild hoch, validiert es, speichert alle Größenvarianten und erstellt Content-Datensätze |
| `addImageForProductPromo(dctx, context)` | Lädt ein Aktionsbild hoch und verknüpft es mit einem ProductPromo-Datensatz |
| `findProductById(dctx, context)` | Sucht ein Produkt über Produkt-ID oder GoodIdentification-Fremdschlüssel |

---

## Klasse: `ProductUtilServices`

**Paket:** `org.apache.ofbiz.product.product`
**Typ:** Java-Klasse (Utility-Services, `final`)
**Zweck:** Hilfsdienste für Datenpflege und -bereinigung im Produktstamm, insbesondere für Massendatenoperationen.

| Methode | Beschreibung |
|---|---|
| `discVirtualsWithDiscVariants(dctx, context)` | Setzt virtuelle Produkte auf abgekündigt, sobald alle ihre Varianten abgekündigt sind |
| `removeCategoryMembersOfDiscProducts(dctx, context)` | Entfernt abgekündigte Produkte aus Kategorien |
| `removeDuplicateOpenEndedCategoryMembers(dctx, context)` | Bereinigt Kategorie-Mitgliedschaften ohne Enddatum, die doppelt vorhanden sind |
| `makeStandAloneFromSingleVariantVirtuals(dctx, context)` | Konvertiert virtuelle Produkte mit nur einer Variante in eigenständige Produkte |
| `mergeVirtualWithSingleVariant(dctx, context)` | Fügt ein virtuelles Produkt mit seiner einzigen Variante zu einem einzelnen Produkt zusammen |
| `setAllProductImageNames(dctx, context)` | Benennt Produktbilder nach einem konfigurierten Schema für alle Produkte |
| `clearAllVirtualProductImageNames(dctx, context)` | Löscht Bildnamen aus allen virtuellen Produktdatensätzen |
| `attachProductFeaturesToCategory(dctx, context)` | Ordnet die Merkmale aller Produkte einer Kategorie auch der Kategorie selbst zu |

---

## Klasse: `ProductSearch`

**Paket:** `org.apache.ofbiz.product.product`
**Typ:** Java-Klasse (Suchanfragen-Framework mit inneren Klassen)
**Zweck:** Implementiert die datenbankbasierte Produktsuche mit austauschbaren Einschränkungen und Sortierungen.

| Methode / Klasse | Beschreibung |
|---|---|
| `parametricKeywordSearch(...)` | Führt eine kombinierte Keyword- und Merkmalssuche durch und gibt eine geordnete Produkt-ID-Liste zurück |
| `searchProducts(constraintList, sortOrder, delegator, visitId)` | Führt eine Suche mit beliebig kombinierbaren Einschränkungsobjekten und einer Sortierungsstrategie aus |
| `getAllSubCategoryIds(categoryId, idSet, ...)` | Sammelt rekursiv alle Unterkategorie-IDs einer Elternkategorie |
| `ProductSearchContext` (innere Klasse) | Verwaltet den Zustand einer laufenden Suche, baut SQL-Anfragen auf und führt sie aus |
| `ProductSearchConstraint` (abstrakt) | Basistyp für alle Sucheinschränkungen; konkrete Implementierungen: `CategoryConstraint`, `KeywordConstraint`, `FeatureConstraint`, `FeatureSetConstraint`, `FeatureGroupConstraint`, `FeatureCategoryConstraint`, `ListPriceRangeConstraint`, `AvailabilityDateConstraint`, `ExcludeVariantsConstraint`, `ProductFieldConstraint`, `GoodIdentificationConstraint`, `CatalogConstraint`, `SupplierConstraint`, `StoreGroupPriceConstraint`, `LastUpdatedRangeConstraint` |
| `ResultSortOrder` / Implementierungen | Sortierstrategien: `SortKeywordRelevancy`, `SortProductField`, `SortProductPrice`, `SortProductFeature` |

---

## Klasse: `ProductSearchSession`

**Paket:** `org.apache.ofbiz.product.product`
**Typ:** Java-Klasse (HTTP-Session-Management für Suche)
**Zweck:** Persistiert Suchzustand (Constraints, Sortierung, Verlauf) in der HTTP-Session und koordiniert die Ausführung einer Suche aus Request-Parametern.

| Methode | Beschreibung |
|---|---|
| `getProductSearchOptions(session)` | Liest die aktuellen Suchoptionen aus der Session oder legt neue an |
| `processSearchParameters(params, request)` | Parst HTTP-Request-Parameter und überträgt sie in Sucheinschränkungsobjekte |
| `searchDo(session, delegator, catalogId)` | Führt die gespeicherte Suche aus und gibt eine Liste von Produkt-IDs zurück |
| `searchClear(session)` | Setzt alle Sucheinschränkungen der Session zurück |
| `searchGetConstraintStrings(detailed, session, delegator)` | Gibt eine lesbare Beschreibung der aktiven Einschränkungen zurück |
| `getProductSearchResult(request, delegator, catalogId)` | Führt Suche aus und bereitet das Suchergebnis (Produkte, Facetten, Seitenzahlen) für die Ansicht auf |
| `listCountByFeatureForType(featureTypeId, session, delegator)` | Zählt, wie viele Suchergebnisse pro Merkmalwert eines Typs existieren (Facettierung) |
| `getCountForListPriceRange(min, max, session, delegator)` | Zählt Suchergebnisse innerhalb eines Preisbereichs |
| `checkSaveSearchOptionsHistory(session)` | Speichert den aktuellen Suchzustand im Session-Verlauf |
| `makeSearchParametersString(session)` | Serialisiert aktive Suchparameter als URL-Query-String |

---

## Klasse: `ProductEvents`

**Paket:** `org.apache.ofbiz.product.product`
**Typ:** Java-Klasse (HTTP-Event-Handler)
**Zweck:** Verarbeitet HTTP-Formulare für Produktdatenpflege und Session-Management für kürzlich angesehene Artikel und Vergleichslisten.

| Methode | Beschreibung |
|---|---|
| `updateAllKeywords(request, response)` | Löst die Neuindizierung aller Produkt-Keywords aus |
| `updateProductAssoc(request, response)` | Speichert eine Produktassoziation aus einem Formular |
| `clearLastViewedCategories/Products/AllLastViewed(...)` | Bereinigt die zuletzt angesehenen Kategorien bzw. Produkte in der Session |
| `updateProductQuickAdminShipping(request, response)` | Aktualisiert Versandeinstellungen eines Produkts über die Schnellbearbeitung |
| `updateProductQuickAdminSelFeat(request, response)` | Aktualisiert wählbare Merkmale eines virtuellen Produkts über die Schnellbearbeitung |
| `addProductToCategories(request, response)` | Fügt ein Produkt zu mehreren Kategorien gleichzeitig hinzu |
| `addProductToComparisonList / removeProductFromComparisonList` | Verwaltet die Session-basierte Produktvergleichsliste |
| `addProductTags(request, response)` | Speichert Tag-Keywords für ein Produkt |
| `tellAFriend(request, response)` | Sendet eine Empfehlungs-E-Mail mit Produktinformationen |

---

## Klasse: `ProductSearchEvents`

**Paket:** `org.apache.ofbiz.product.product`
**Typ:** Java-Klasse (HTTP-Event-Handler für Suchergebnisse)
**Zweck:** Ermöglicht Batch-Operationen auf Suchergebnissen (Kategoriezuordnung, Merkmalzuordnung, Export).

| Methode | Beschreibung |
|---|---|
| `searchAddToCategory / searchRemoveFromCategory / searchExpireFromCategory` | Ordnet alle Suchergebnis-Produkte einer Kategorie zu, entfernt sie oder setzt sie auf abgelaufen |
| `searchAddFeature / searchRemoveFeature` | Ordnet ein Produktmerkmal allen Suchergebnis-Produkten zu oder entfernt es |
| `searchExportProductList(request, response)` | Exportiert die Suchergebnisliste in eine CSV-Datei für den Download |

---

## Klasse: `KeywordIndex`

**Paket:** `org.apache.ofbiz.product.product`
**Typ:** Java-Klasse (Utility)
**Zweck:** Baut den Keyword-Suchindex für ein Produkt auf, indem Texte aus Produktdaten, Merkmalen und Content-Datensätzen extrahiert und gewichtet werden.

| Methode | Beschreibung |
|---|---|
| `indexKeywords(product)` | Aktualisiert den Keyword-Index für ein Produkt, respektiert Konfigurationsflags (autoCreateKeywords, Varianten, abgekündigt) |
| `forceIndexKeywords(product)` | Erzwingt eine vollständige Neuindizierung unabhängig von den Konfigurationsflags |
| `addWeightedDataResourceString(dataResource, weight, strings, ...)` | Extrahiert Text aus einem DataResource-Objekt und fügt ihn gewichtet zum Index hinzu |
| `addWeightedKeywordSourceString(product, string, strings)` | Tokenisiert eine Zeichenkette und fügt ihre Begriffe gewichtet zur Indexliste hinzu |

---

## Klasse: `ProductContentWrapper`

**Paket:** `org.apache.ofbiz.product.product`
**Typ:** Java-Klasse (implementiert `ContentWrapper`)
**Zweck:** Kapselt den Zugriff auf produktbezogene Content-Daten (Namen, Beschreibungen, Bilder) und liefert sie lokalisiert und im gewünschten MIME-Typ.

| Methode | Beschreibung |
|---|---|
| `makeProductContentWrapper(product, request)` | Fabrikmethode: erstellt einen Wrapper aus einem HTTP-Request-Kontext |
| `get(contentTypeId, mimeTypeId)` | Gibt den Inhalt eines bestimmten Content-Typs als StringWrapper zurück |
| `getProductContentAsText(product, contentTypeId, ...)` | Liest Produkt-Content als Text, mit Fallback auf Parent-Produkte; unterstützt mehrere Signaturen für unterschiedliche Aufrufkontexte |

---

## Klasse: `ProductPromoContentWrapper`

**Paket:** `org.apache.ofbiz.product.product`
**Typ:** Java-Klasse (implementiert `ContentWrapper`)
**Zweck:** Analog zu `ProductContentWrapper`, aber für Aktions-Content (Bilder und Texte zu ProductPromo-Datensätzen).

| Methode | Beschreibung |
|---|---|
| `makeProductPromoContentWrapper(productPromo, request)` | Fabrikmethode für Aktions-Content-Wrapper |
| `get(contentTypeId, mimeTypeId)` | Liefert Aktions-Content lokalisiert zurück |
| `getProductPromoContentAsText(productPromo, contentTypeId, ...)` | Liest Aktions-Content als Text mit Caching |

---

## Klasse: `CatalogWorker`

**Paket:** `org.apache.ofbiz.product.catalog`
**Typ:** Java-Klasse (Utility, `final`)
**Zweck:** Zugriffshilfe auf Katalogdaten aus HTTP-Session und Datenbank; verwaltet den aktuell gewählten Katalog im Request.

| Methode | Beschreibung |
|---|---|
| `getAllCatalogIds(request)` | Gibt eine sortierte Liste aller Katalog-IDs aus der Datenbank zurück |
| `getStoreCatalogs(delegator, productStoreId)` | Gibt die dem Shop zugeordneten Kataloge in Anzeigereihenfolge zurück |
| `getCurrentCatalogId(request)` | Ermittelt den aktiven Katalog aus Session oder Request-Parameter |
| `getCatalogName(delegator, prodCatalogId)` | Gibt den Anzeigenamen eines Katalogs zurück |
| `getCatalogTopCategoryId(delegator, prodCatalogId)` | Liefert die Wurzelkategorie des Katalogs |
| `getCatalogViewAllowCategoryId(delegator, prodCatalogId)` | Gibt die Kategorie zurück, auf die der Sichtbarkeitszugriff beschränkt ist |
| `getCatalogQuickaddCategoryId(delegator, prodCatalogId)` | Liefert die Standardkategorie für die Schnellanlage |
| `isProductInCatalog(delegator, product, prodCatalogId, ...)` | Prüft, ob ein Produkt in einem Katalog sichtbar ist |

---

## Klasse: `CategoryWorker`

**Paket:** `org.apache.ofbiz.product.category`
**Typ:** Java-Klasse (Utility, `final`)
**Zweck:** Navigationshilfe für die Kategoriehierarchie: Pfadberechnung, Filterung von Produktlisten und Session-Management für Trail/Breadcrumb.

| Methode | Beschreibung |
|---|---|
| `getCatalogTopCategory(request, defaultTopCategory)` | Liest die Wurzelkategorie des Katalogs aus Session oder Request und speichert sie für Folgeaufrufe |
| `getCategoriesWithNoParent(request, attributeName)` | Gibt alle Kategorien ohne Elternkategorie zurück (Wurzelknoten) |
| `getRelatedCategories(delegator, parentCategoryId, ...)` | Gibt die Unterkategorien einer Elternkategorie zurück |
| `filterProductsInCategory(delegator, productAssocList, productCategoryId, ...)` | Filtert eine Assoziationsliste auf Produkte, die in einer bestimmten Kategorie vorhanden sind |
| `setTrail(request, currentCategory)` | Setzt den Kategoriepfad (Breadcrumb) in der Session |
| `getTrail(request)` | Liest den gespeicherten Kategoriepfad aus der Session |
| `adjustTrail(trail, currentCategory)` | Kürzt oder verlängert den Pfad um die aktuelle Kategorie |
| `checkTrailItem(request, category)` | Prüft, ob eine Kategorie im aktuellen Trail enthalten ist |

---

## Klasse: `CategoryServices`

**Paket:** `org.apache.ofbiz.product.category`
**Typ:** Java-Klasse (OFBiz-Service-Implementierung)
**Zweck:** Service-Methoden für Kategorie-Navigation und -Pflege, insbesondere für die Vor-/Zurück-Navigation innerhalb einer Kategorie.

| Methode | Beschreibung |
|---|---|
| `getCategoryMembers(dctx, context)` | Gibt alle aktiven Mitglieder einer Produktkategorie sortiert nach Reihenfolge zurück |
| `getPreviousNextProducts(dctx, context)` | Ermittelt das vorherige und nächste Produkt innerhalb einer Kategorie für die Detailseitennavigation |
| `getProductCategoryAndLimitedMembers(dctx, context)` | Gibt eine Kategorie mit einer begrenzten Anzahl an Produktmitgliedern zurück (Paginierung) |

---

## Klassen: `CatalogUrlFilter`, `CatalogUrlSeoFilter`, `SeoContentUrlFilter`, `SeoContextFilter`, `SeoControlServlet`, `SeoCatalogUrlServlet`, `CatalogUrlServlet`, `CategoryControlServlet`

**Paket:** `org.apache.ofbiz.product.category`
**Typ:** Servlet / Servlet-Filter
**Zweck:** URL-Routing-Infrastruktur für SEO-freundliche Katalog- und Kategorie-URLs. Die Filter rewrite eingehende SEO-URLs auf interne OFBiz-Pfade; die Servlets bedienen direkte Katalog-Requests. `CategoryControlServlet` erweitert den OFBiz-Standard-ControlServlet für Kategorie-Kontext.

---

## Klassen: FreeMarker-Transforms im Paket `org.apache.ofbiz.product.category.ftl`

**Typ:** Java-Klassen (implementieren `TemplateTransformModel` bzw. `TemplateDirectiveModel`)
**Zweck:** Stellen in FreeMarker-Templates Funktionen zur URL-Generierung bereit.

| Klasse | Beschreibung |
|---|---|
| `OfbizCatalogUrlTransform` | FreeMarker-Transform für Standard-Katalog-URLs |
| `OfbizCatalogAltUrlTransform` | FreeMarker-Transform für alternative (SEO) Katalog-URLs |
| `CatalogUrlSeoTransform` | FreeMarker-Transform für SEO-optimierte Katalog-URLs |
| `CatalogAltUrlSeoTransform` | FreeMarker-Transform für SEO-Alternative-URLs |
| `SeoTransform` | Allgemeiner SEO-URL-Transform |
| `UrlRegexpTransform` | Transform zur regulären Ausdrucks-basierten URL-Manipulation |
| `CatalogUrlDirective` | FreeMarker-Direktive für Katalog-URL-Ausgabe |

---

## Klasse: `CategoryContentWrapper`

**Paket:** `org.apache.ofbiz.product.category`
**Typ:** Java-Klasse (implementiert `ContentWrapper`)
**Zweck:** Liefert lokalisierte Textinhalte (Name, Beschreibung, Bilder) für Produktkategorien, mit Caching-Unterstützung.

---

## Klasse: `ProductConfigWrapper`

**Paket:** `org.apache.ofbiz.product.config`
**Typ:** Java-Klasse (serialisierbar, Session-fähig)
**Zweck:** Kapselung des Konfigurationszustands eines konfigurierbaren Produkts (AGGREGATED). Verwaltet die Konfigurationsfragen (`ConfigItem`), die gewählten Optionen und berechnet den konfigurierten Preis.

| Methode | Beschreibung |
|---|---|
| `init(...)` | Lädt das Produkt und seine Konfigurationsfragen aus der Datenbank |
| `setSelected(index, optionIndex)` | Wählt eine Option für eine Konfigurationsfrage aus |
| `isCompleted()` | Prüft, ob alle Pflichtfragen beantwortet wurden |
| `getTotalPrice()` | Berechnet den Gesamtpreis der aktuellen Konfiguration |
| `getSelectedOptions()` | Gibt die gewählten Konfigurationsoptionen zurück |
| `resetConfig()` | Setzt alle Auswahlen zurück |
| `saveConfig(delegator, configId)` | Speichert die aktuelle Konfiguration unter einer Konfigurations-ID |

**Innere Klassen:**
- `ConfigItem`: Repräsentiert eine Konfigurationsfrage mit ihren Optionen und Pflichtfeld-Status
- `ConfigOption`: Repräsentiert eine auswählbare Konfigurationsoption mit Preis, Komponenten und Verfügbarkeitsstatus

---

## Klasse: `ProductConfigWorker`

**Paket:** `org.apache.ofbiz.product.config`
**Typ:** Java-Klasse (Utility, `final`)
**Zweck:** Fabrik und Verwaltung von `ProductConfigWrapper`-Instanzen mit eingebautem Cache.

| Methode | Beschreibung |
|---|---|
| `getProductConfigWrapper(productId, currencyUomId, request)` | Gibt einen gecachten oder neuen Konfigurations-Wrapper zurück |
| `fillProductConfigWrapper(configWrapper, request)` | Befüllt einen Wrapper mit den Auswahlen aus einem HTTP-Request |
| `createProductConfigWrapper(delegator, dispatcher, productId, ...)` | Erstellt einen neuen Wrapper ohne HTTP-Request-Kontext |

---

## Klasse: `ProductConfigItemContentWrapper`

**Paket:** `org.apache.ofbiz.product.config`
**Typ:** Java-Klasse (implementiert `ContentWrapper`)
**Zweck:** Liefert lokalisierte Inhalte (Name, Beschreibung) für einzelne Konfigurationspositionen (ProductConfigItem).

---

## Klasse: `ProductConfigWrapperException`

**Paket:** `org.apache.ofbiz.product.config`
**Typ:** Java-Exception-Klasse
**Zweck:** Geprüfte Ausnahme für Fehler beim Aufbau oder der Validierung von Produktkonfigurationen.

---

## Klasse: `ProductFeatureServices`

**Paket:** `org.apache.ofbiz.product.feature`
**Typ:** Java-Klasse (OFBiz-Service-Implementierung)
**Zweck:** Service-Methoden zum Abfragen und Verwalten von Produktmerkmalen und Merkmaltypen.

| Methode | Beschreibung |
|---|---|
| `getProductFeaturesByType(dctx, context)` | Gibt Merkmale nach Merkmaltyp, Merkmalsgruppe oder Produkt-ID zurück |
| `applyFeaturesFromCategory(dctx, context)` | Ordnet alle Merkmale einer Kategorie einem Produkt zu |

---

## Klasse: `ParametricSearch`

**Paket:** `org.apache.ofbiz.product.feature`
**Typ:** Java-Klasse
**Zweck:** Führt eine parametrische Produktsuche durch, bei der Produkte anhand einer Kombination aus Merkmalen gefiltert werden.

---

## Klasse: `ScaleImage`

**Paket:** `org.apache.ofbiz.product.image`
**Typ:** Java-Klasse (Utility)
**Zweck:** Skaliert ein hochgeladenes Produktbild auf alle konfigurierten Standardgrößen (small, medium, large, detail) gemäß `ImageProperties.xml` und gibt die URL-Map zurück.

| Methode | Beschreibung |
|---|---|
| `scaleImageInAllSize(context, filenameToUse, viewType, viewNumber)` | Liest die Bildgrößenkonfiguration aus XML, skaliert das Originalbild und speichert alle Größenvarianten |

---

## Klassen im Paket `org.apache.ofbiz.product.imagemanagement`

**Typ:** Java-Klassen (Service-Implementierungen)
**Zweck:** Erweiterte Verwaltung von Produktbildern mit Workflow für Genehmigung und Ablehnung.

| Klasse | Beschreibung |
|---|---|
| `ImageManagementServices` | Kernservices: Bild-Upload, Statuswechsel (genehmigen/ablehnen), Größenanpassung, Sortierung |
| `CropImage` | Schneidet ein Bild auf einen definierten Ausschnitt zu |
| `RotateImage` | Dreht ein Bild um einen definierten Winkel |
| `FrameImage` | Überlagert ein Bild mit einem Rahmen |
| `ReplaceImage` | Ersetzt ein bestehendes Produktbild durch eine neue Datei |
| `ImageManagementHelper` | Hilfsmethoden für die Bildverwaltung (Pfadberechnung, Dateioperationen) |
| `ImageUrlServlet` | Servlet zur direkten Auslieferung von verwalteten Bildwürfen über URL |

---

## Klasse: `InventoryServices`

**Paket:** `org.apache.ofbiz.product.inventory`
**Typ:** Java-Klasse (OFBiz-Service-Implementierung)
**Zweck:** Kernservices für Lagerbestandsverwaltung: Umbuchungen, Reservierungen und Bestandsabfragen.

| Methode | Beschreibung |
|---|---|
| `prepareInventoryTransfer(dctx, context)` | Bereitet einen Lagertransfer vor: teilt bei Bedarf nicht-serialisierte Artikel auf |
| `completeInventoryTransfer(dctx, context)` | Schließt einen Lagertransfer ab und aktualisiert Bestand am Zielort |
| `cancelInventoryTransfer(dctx, context)` | Storniert einen offenen Lagertransfer |
| `getInventoryAvailableByFacility(dctx, context)` | Gibt verfügbaren und reservierten Bestand für ein Produkt an einem Lager zurück |
| `getProductInventoryAvailable(dctx, context)` | Gibt den globalen verfügbaren Bestand eines Produkts über alle Lager zurück |
| `getProductInventorySummaryForItems(dctx, context)` | Liefert Bestandszusammenfassungen für eine Liste von Auftragspositionen |
| `checkInventoryAvailableAndReserve(dctx, context)` | Prüft Verfügbarkeit und legt bei ausreichend Bestand eine Reservierung an |
| `getMktgPackagesAvailable(dctx, context)` | Berechnet die verfügbare Menge fertigstellbarer Marketing-Pakete |
| `updateProductAverageCost(dctx, context)` | Aktualisiert den durchschnittlichen Einstandspreis nach einem Wareneingang |

---

## Klasse: `InventoryWorker`

**Paket:** `org.apache.ofbiz.product.inventory`
**Typ:** Java-Klasse (Utility)
**Zweck:** Statische Hilfsmethoden für Bestandsberechnungen, insbesondere für Marketing-Pakete.

---

## Klasse: `PriceServices`

**Paket:** `org.apache.ofbiz.product.price`
**Typ:** Java-Klasse (OFBiz-Service-Implementierung)
**Zweck:** Berechnet den aktuellen Produktpreis unter Berücksichtigung von Preisregeln, Mengenstaffeln, Vereinbarungspreisen, Kundengruppen und Steuern.

| Methode | Beschreibung |
|---|---|
| `calculateProductPrice(dctx, context)` | Hauptpreisfindungsroutine: wertet alle aktiven Preisregeln aus und gibt Listenpreis, Basispreis und berechneten Preis zurück |
| `calculateProductPrices(dctx, context)` | Berechnet gleichzeitig mehrere Preistypen (DEFAULT, PROMO, MINIMUM) für eine Mengenreihe |
| `getProductPrice(dctx, context)` | Gibt den direkt hinterlegten Produktpreis ohne Regelauswertung zurück |
| `setBasePrice(dctx, context)` | Setzt den Basispreis für eine Produktpreisregel |

---

## Klasse: `PromoServices`

**Paket:** `org.apache.ofbiz.product.promo`
**Typ:** Java-Klasse (OFBiz-Service-Implementierung)
**Zweck:** Verwaltung von Aktionscodes: Massengenerierung, Import aus Dateien und Bereinigung abgelaufener Shop-Aktionen.

| Methode | Beschreibung |
|---|---|
| `createProductPromoCodeSet(dctx, context)` | Generiert eine definierte Menge zufälliger Aktionscodes in konfigurierbaren Layouts (smart/normal) |
| `purgeOldStoreAutoPromos(dctx, context)` | Entfernt abgelaufene automatische Shop-Aktionen |
| `importPromoCodesFromFile(dctx, context)` | Importiert Aktionscodes aus einer hochgeladenen Textdatei |
| `importPromoCodeEmailsFromFile(dctx, context)` | Importiert E-Mail-Adressen für Code-Zuordnungen aus einer Datei |

---

## Klasse: `SubscriptionServices`

**Paket:** `org.apache.ofbiz.product.subscription`
**Typ:** Java-Klasse (OFBiz-Service-Implementierung)
**Zweck:** Verwaltung von Produktabonnements: Laufzeitverlängerung und Ablaufprüfung.

| Methode | Beschreibung |
|---|---|
| `processExtendSubscription(dctx, context)` | Verlängert ein bestehendes Abonnement oder legt bei Erstabschluss ein neues an; berechnet die neue Laufzeit |
| `processExtendSubscriptionByProduct(dctx, context)` | Verlängert Abonnements auf Basis eines Produkts und Lagerartikels |
| `runSubscriptionExpired(dctx, context)` | Batch-Job: Verarbeitet abgelaufene Abonnements und triggert definierte Folgeaktionen |

---

## Klasse: `SupplierProductServices`

**Paket:** `org.apache.ofbiz.product.supplier`
**Typ:** Java-Klasse (OFBiz-Service-Implementierung)
**Zweck:** Abfrage von Lieferanten-Produkt-Kombinationen mit Preis- und Staffelangaben.

| Methode | Beschreibung |
|---|---|
| `getSuppliersForProduct(dctx, context)` | Gibt alle Lieferanten für ein Produkt zurück, gefiltert nach Partei, Währung, Menge und Drop-Ship-Fähigkeit; navigiert bei Varianten automatisch zum virtuellen Produkt |

---

## Klasse: `ProductStoreWorker`

**Paket:** `org.apache.ofbiz.product.store`
**Typ:** Java-Klasse (Utility, `final`)
**Zweck:** Zugriffshilfe auf Shop-Konfigurationsdaten aus HTTP-Session und Datenbank.

| Methode | Beschreibung |
|---|---|
| `getProductStore(productStoreId, delegator)` | Gibt den Shop-Datensatz zurück |
| `getProductStoreId(request)` | Ermittelt die aktive Shop-ID aus Session oder Web-Site |
| `isStoreInventoryRequired(request, product)` | Prüft, ob der Shop Lagerbestand für dieses Produkt erfordert |
| `isStoreInventoryAvailable(request, product, quantity)` | Prüft, ob ausreichend Bestand für die angeforderte Menge vorhanden ist |
| `determineSingleFacilityForStore(productStore)` | Gibt das einzige Lager des Shops zurück, falls vorhanden |
| `getRandomProductStorePromotion(request, productPromoTypeId)` | Wählt eine zufällige aktive Promotion des Shops aus |

---

## Klasse: `ProductStoreEvents`

**Paket:** `org.apache.ofbiz.product.store`
**Typ:** Java-Klasse (HTTP-Event-Handler)
**Zweck:** Event-Handler für Shop-bezogene HTTP-Requests (Zahlungseinrichtung).

---

## Klasse: `ProductStoreSurveyWrapper`

**Paket:** `org.apache.ofbiz.product.store`
**Typ:** Java-Klasse (erweitert `SurveyWrapper`)
**Zweck:** Kapselt produkt- oder kategoriebezogene Umfragen eines Shops und stellt sie für FreeMarker-Templates bereit.

---

## Klassen im Paket `org.apache.ofbiz.product.spreadsheetimport`

| Klasse | Beschreibung |
|---|---|
| `ImportProductServices` | Service `productImportFromSpreadsheet`: liest Excel-Dateien (Apache POI HSSF) und legt Produkte und Lagerartikel an |
| `ImportProductHelper` | Hilfsmethoden: Produkt-Map aufbauen, Lagerartikel-Map aufbauen, Existenzprüfung |

---

## Klasse: `MigrationServices`

**Paket:** `org.apache.ofbiz.product.migrate`
**Typ:** Java-Klasse (OFBiz-Service-Implementierung)
**Zweck:** Datenbankmigrationen zwischen OFBiz-Versionen (z.B. Umschlüsselung von Entitäten).

---

## Groovy-Service-Scripts mit fachlichen Methoden

Die folgenden Groovy-Klassen implementieren OFBiz-Service-Definitionen. Sie werden durch den Service-Container aufgerufen und sind funktional äquivalent zu Java-Service-Klassen.

### `CatalogServices`
**Paket:** `org.apache.ofbiz.product.product.catalog`

| Methode | Beschreibung |
|---|---|
| `getAllCategories()` | Gibt alle Kategorien des aktuellen Katalogs zurück |
| `getRelatedCategories()` | Gibt Unterkategorien einer Kategorie zurück |
| `checkImageUrlForAllCategories()` | Prüft für alle Kategorien und Produkte, ob Bildpfade existieren |
| `checkImageUrlForCategory()` / `checkImageUrlForProduct()` / `checkImageUrl()` | Prüft einzelne Bild-URLs auf Existenz im Dateisystem |
| `catalogPermissionCheck()` / `prodCatalogToPartyPermissionCheck()` | Berechtigungsprüfung für Katalogzugriff |
| `createMissingCategoryAndProductAltUrls()` | Legt fehlende SEO-Alt-URLs für Kategorien und Produkte an |

### `CategoryContentServicesScript`
**Paket:** `org.apache.ofbiz.product.product.category`

| Methode | Beschreibung |
|---|---|
| `createCategoryContent()` / `updateCategoryContent()` | Erstellt/aktualisiert eine Kategorie-Content-Verknüpfung |
| `createSimpleTextContentForCategory()` | Legt einen einfachen Textinhalt (z.B. Name, Beschreibung) für eine Kategorie an |
| `updateContentSEOForCategory()` | Aktualisiert SEO-Metadaten für eine Kategorie |
| `createRelatedUrlContentForCategory()` / `updateRelatedUrlContentForCategory()` | Verwaltet URL-Content-Verknüpfungen für Kategorien |
| `createDownloadContentForCategory()` / `updateDownloadContentForCategory()` | Verwaltet Download-Content für Kategorien |

### `CategoryServicesScript`
**Paket:** `org.apache.ofbiz.product.product.category`

| Methode | Beschreibung |
|---|---|
| `createProductCategory()` / `updateProductCategory()` | Anlage und Pflege von Produktkategorien |
| `addProductToCategories()` / `removeProductFromCategory()` | Verknüpft oder entfernt ein Produkt aus Kategorien |
| `addPartyToCategory()` / `updatePartyToCategory()` / `removePartyFromCategory()` | Verwaltet Parteizuordnungen (z.B. Kategorie-Verantwortliche) |
| `addProductCategoryToCategory()` / `removeProductCategoryFromCategory()` | Verwaltung der Kategoriehierarchie (Eltern-Kind-Beziehungen) |
| `copyCategoryProductMembers()` / `duplicateCategoryEntities()` | Kopiert Kategoriemitgliedschaften und -datensätze |
| `expireAllCategoryProductMembers()` / `removeExpiredCategoryProductMembers()` | Setzt Ablaufdaten oder entfernt abgelaufene Mitgliedschaften |
| `createProductInCategory()` | Legt ein neues Produkt direkt mit Kategoriemitgliedschaft an |
| `duplicateProductCategory()` | Dupliziert eine Kategorie inklusive ihrer Unterstruktur |
| `productCategoryGenericPermission()` / `checkCategoryRelatedPermission(...)` | Berechtigungsprüfung für Kategorie-Operationen |
| `getAssociatedProductsList()` | Gibt Produkte zurück, die mit einer Kategorie assoziiert sind |

### `CostServices`
**Paket:** `org.apache.ofbiz.product.product.cost`

| Methode | Beschreibung |
|---|---|
| `getProductCost()` / `getTaskCost()` | Gibt die Stückkosten eines Produkts oder einer Arbeitsaufgabe zurück |
| `calculateAllProductsCosts()` / `calculateProductCosts()` | Berechnet die Kosten aller bzw. eines bestimmten Produkts auf Basis von Kostenkomponenten |
| `calculateProductAverageCost()` / `getProductAverageCost()` | Berechnet und liest den gewichteten Durchschnittseinstandspreis |
| `updateProductAverageCostOnReceiveInventory()` | Aktualisiert den Einstandspreis nach einem Wareneingang |
| `productCostPercentageFormula()` | Berechnet Kostenaufschläge nach Prozentregel |
| `cancelCostComponents()` / `recreateCostComponent()` | Storniert und erneuert Kostenkomponenten für ein Produkt |

### `ProductFeatureServicesScript`
**Paket:** `org.apache.ofbiz.product.product.feature`

| Methode | Beschreibung |
|---|---|
| `applyFeatureToProductFromTypeAndCode()` | Ordnet ein Merkmal einem Produkt zu, identifiziert über Typ und Code |
| `createProductFeatureType()` | Legt einen neuen Merkmaltyp an |
| `createProductFeatureApplAttr()` | Erstellt ein Attribut für eine Merkmalsanwendung |

### `ImageManagementServicesScript`
**Paket:** `org.apache.ofbiz.product.product.imagemanagement`

| Methode | Beschreibung |
|---|---|
| `uploadProductImages()` | Koordiniert den Upload und die Validierung mehrerer Produktbilder |
| `removeProductContentAndImageFile()` | Löscht Content-Verknüpfung und Bilddatei vom Dateisystem |
| `setImageDetail()` | Setzt Detaileigenschaften eines Produktbildes (Beschriftung, Sortierung) |
| `updateStatusImageManagement()` | Ändert den Genehmigungsstatus eines Bildes im Workflow |
| `addRejectedReasonImageManagement()` | Speichert den Ablehnungsgrund für ein Bild |
| `createImageContentApproval()` / `removeImageContentApproval()` | Verwaltet Genehmigungseinträge für Bildcontent |
| `resizeImages()` / `removeImageBySize()` | Erstellt oder entfernt skalierte Bildversionen |

### `InventoryIssueServices`
**Paket:** `org.apache.ofbiz.product.product.inventory`

| Methode | Beschreibung |
|---|---|
| `issueImmediatelyFulfilledOrder()` / `issueImmediatelyFulfilledOrderItem()` | Bucht Bestand sofort für einen Auftrag oder eine Auftragsposition aus (digitale/sofort erfüllte Artikel) |
| `issueImmediateForInventoryItemInline(inventoryItem)` | Interne Hilfsmethode: führt die Ausbuchtransaktion für einen einzelnen Lagerartikel durch |

### `InventoryServicesScript`
**Paket:** `org.apache.ofbiz.product.product.inventory`

| Methode | Beschreibung |
|---|---|
| `createInventoryItem()` | Legt einen neuen Lagerartikel an |
| `checkFacilityRelatedPermission(...)` / `facilityGenericPermission()` / `checkProductFacilityRelatedPermission()` | Berechtigungsprüfungen für Lager- und Facility-Operationen |

### `PriceServicesScript`
**Paket:** `org.apache.ofbiz.product.product.price`

| Methode | Beschreibung |
|---|---|
| `createProductPrice()` / `updateProductPrice()` / `deleteProductPrice()` | CRUD-Operationen für Produktpreiseinträge |
| `inlineHandlePriceWithTaxIncluded()` | Berechnet Netto- und Bruttopreise für steuerinklusive Preise |
| `createProductPriceCond()` / `updateProductPriceCond()` | Erstellt und pflegt Preisregelbedingungen |
| `getAssociatedPriceRulesConds()` | Gibt alle Bedingungen zurück, die mit Preisregeln eines Produkts verknüpft sind |

### `ProductContentServicesScript`
**Paket:** `org.apache.ofbiz.product.product.product`

| Methode | Beschreibung |
|---|---|
| `createProductContent()` / `updateProductContent()` | Verknüpft und aktualisiert Content-Datensätze für ein Produkt |
| `createSimpleTextContentForProduct()` / `createSimpleTextContentForAlternateLocale()` | Legt einfachen Textinhalt (Name, Beschreibung) für ein Produkt in einer Sprache an |
| `createDownloadContentForProduct()` / `createEmailContentForProduct()` | Erstellt Download- oder E-Mail-Content für ein Produkt |
| `uploadProductAdditionalViewImages()` | Verarbeitet den Upload zusätzlicher Produktansichten |
| `updateContentSEOForProduct()` | Aktualisiert SEO-Metadaten für ein Produkt |

### `ProductServicesScript`
**Paket:** `org.apache.ofbiz.product.product.product`

| Methode | Beschreibung |
|---|---|
| `createProduct()` / `updateProduct()` | Anlage und Pflege von Produktstammdaten |
| `duplicateProduct()` | Kopiert ein Produkt inklusive seiner assoziierten Daten |
| `forceIndexProductKeywords()` / `deleteProductKeywords()` / `indexProductKeywords()` | Steuert den Keyword-Suchindex für ein Produkt |
| `discontinueProductSales()` | Setzt das Verkaufsabkündigungsdatum eines Produkts |
| `countProductView()` | Erhöht den Seitenaufrufzähler eines Produkts |
| `createProductReview()` / `updateProductReview()` / `setProductReviewStatus()` | Verwaltung von Produktrezensionen und ihrem Genehmigungsstatus |
| `copyToProductVariants()` | Überträgt Produktdatenfelder auf alle Varianten des virtuellen Produkts |
| `checkProductRelatedPermission(...)` / `productGenericPermission()` | Berechtigungsprüfung für Produktoperationen |
| `addPartyToProduct()` / `removePartyFromProduct()` | Verwaltet Parteizuordnungen zu Produkten (z.B. Hersteller) |
| `createProductGroupOrder()` / `updateProductGroupOrder()` / `checkOrderItemForProductGroupOrder()` | Verwaltung von Gruppenbestellungen (Sammelbestellungen) |

### `ProductPromoActionServices`
**Paket:** `org.apache.ofbiz.product.product.promo`

Implementiert alle OFBiz-Standard-Promo-Aktionstypen:

| Methode | Beschreibung |
|---|---|
| `productGWP()` | Gratisartikel-Aktion (Gift With Purchase) |
| `productActFreeShip()` | Kostenloser Versand-Aktion |
| `productDISC()` | Prozentualer Rabatt auf Produktpreis |
| `productAMDISC()` | Absoluter Rabatt auf Produktpreis |
| `productPrice()` | Fixpreisrabatt |
| `productOrderPercent()` / `productOrderAmount()` | Rabatt auf den Gesamtauftragswert |
| `productSpecialPrice()` | Sonderpreis für ausgewählte Produkte |
| `productShipCharge()` | Versandkostenrabatt |
| `productTaxPercent()` | Steuerrabatt |

### `ProductPromoCondServices`
**Paket:** `org.apache.ofbiz.product.product.promo`

Implementiert alle OFBiz-Standard-Promo-Bedingungstypen:

| Methode | Beschreibung |
|---|---|
| `productAmount()` / `productTotal()` | Mindestbestellwert-Bedingungen |
| `productQuant()` | Mindestmenge-Bedingung |
| `productPartyID()` / `productPartyGM()` / `productPartyClass()` / `productRoleType()` | Kundenbezogene Bedingungen (Party-ID, Gruppe, Klasse, Rolle) |
| `productGeoID()` | Geografische Bedingung (Land/Region) |
| `productOrderTotal()` / `productOrderHist()` / `productOrderYear()` / `productOrderLastYear()` | Historische Bestellwert-Bedingungen |
| `productPromoRecurrence()` | Bedingung auf Basis der Nutzungshäufigkeit einer Aktion |
| `productShipTotal()` | Bedingung auf Basis der Versandkosten |
| `productListPriceMinAmount()` / `productListPriceMinPercent()` | Listenpreis-Mindestbedingungen |

### `PromoServicesScript`
**Paket:** `org.apache.ofbiz.product.product.promo`

| Methode | Beschreibung |
|---|---|
| `createProductPromoCond()` / `updateProductPromoCond()` | Anlage und Pflege von Aktionsbedingungen |

### `ProductStoreServices`
**Paket:** `org.apache.ofbiz.product.product.store`

| Methode | Beschreibung |
|---|---|
| `createProductStore()` / `updateProductStore()` | Anlage und Pflege von Shop-Konfigurationen |
| `reserveStoreInventory()` | Reserviert Bestand für eine Bestellung im Shop-Kontext |
| `isStoreInventoryRequired()` / `isStoreInventoryAvailable()` / `isStoreInventoryAvailableOrNotRequired()` | Prüft Bestandspflicht und -verfügbarkeit aus Shop-Perspektive |
| `checkProductStoreGroupRollup()` | Prüft hierarchische Shop-Gruppen-Zuordnungen |

### `SubscriptionServicesScript`
**Paket:** `org.apache.ofbiz.product.product.subscription`

| Methode | Beschreibung |
|---|---|
| `createSubscription()` | Legt ein neues Abonnement an |
| `isSubscribed()` | Prüft, ob eine Partei aktiv abonniert ist |
| `getSubscription()` | Gibt das aktive Abonnement einer Partei zurück |
| `updateSubscriptionAttribute()` | Aktualisiert ein Attribut eines Abonnements |
| `subscriptionPermissionCheck()` | Berechtigungsprüfung für Abonnement-Operationen |

### `SupplierProductServicesScript`
**Paket:** `org.apache.ofbiz.product.supplier`

| Methode | Beschreibung |
|---|---|
| `getSupplierProductFeatures()` | Gibt Merkmale zurück, die für Lieferanten-Produkt-Einträge relevant sind |

---

## Groovy-Scripts: Versandmodul (`org.apache.ofbiz.product.shipment`)

Diese Groovy-Scripts bilden die Versandlogik ab und werden als OFBiz-Services aufgerufen.

### `ShipmentServices`

| Methode | Beschreibung |
|---|---|
| `updateShipment()` | Aktualisiert Sendungsstammdaten |
| `createShipmentForReturn()` / `createShipmentAndItemsForReturn()` | Erstellt Rücksendungen |
| `createShipmentAndItemsForVendorReturn()` | Erstellt Lieferantenrücksendungen |
| `setShipmentSettingsFromPrimaryOrder()` / `setShipmentSettingsFromFacilities()` | Übernimmt Einstellungen aus Auftrag oder Lager in die Sendung |
| `createShipmentPackage()` / `updateShipmentPackage()` / `deleteShipmentPackage()` | Verwaltung von Versandpaketen |
| `addShipmentContentToPackage()` | Fügt Sendungsinhalt einem Paket hinzu |
| `checkCanChangeShipmentStatus*(...)` | Prüft, ob ein Statuswechsel der Sendung zulässig ist |
| `quickShipEntireOrder()` / `quickDropShipOrder()` / `quickReceivePurchaseOrder()` | Schnellversand: versendet einen ganzen Auftrag oder empfängt eine Lieferung |
| `createOrderShipmentPlan()` | Plant die Versandaufteilung für einen Auftrag |
| `quickShipOrderByItem()` | Versendet einzelne Auftragspositionen |
| `removeOrderShipmentFromShipment()` / `addOrderShipmentToShipment()` | Verwaltet die Zuordnung von Auftragspositionen zu Sendungen |

### `ShipmentReceiptServices`

| Methode | Beschreibung |
|---|---|
| `createShipmentReceipt()` | Bucht einen Wareneingang und legt Lagerartikel an |
| `receiveInventoryProduct()` | Wareneingang mit vollständiger Bestandsbuchung |
| `quickReceiveReturn()` | Schnelleinbuchung einer Rücksendung |
| `issueOrderItemToShipmentAndReceiveAgainstPO()` | Bucht eine Bestellposition aus und empfängt gegen Bestellung |
| `cancelReceivedItems()` | Storniert eingegangene Warenpositionen |

### `IssuanceServices`

| Methode | Beschreibung |
|---|---|
| `issueImmediatelyFulfilledOrder()` / `issueImmediatelyFulfilledOrderItem()` | Sofortausbuchung für digital oder sofort erfüllte Aufträge |

### `PicklistServices`

| Methode | Beschreibung |
|---|---|
| `migrateOldPicklistStatusHistoryToPickListStatus()` | Datenmigration: überführt Statushistorie in das aktuelle Schema |

---

## Groovy-View-Scripts: Facility-/Versand-Screens (`org.apache.ofbiz.product.facility.*`)

Diese Klassen sind reine View-Scripts ohne eigenständige fachliche Methoden (nur `run()`-Einstiegspunkt). Sie bereiten Daten für FTL-Templates im Facility-Bereich auf.

**Facility-Verwaltung** (`org.apache.ofbiz.product.facility.facility`):
`ComputeProductSellThroughData`, `CountFacilityInventoryByProduct`, `EditContactMech`, `EditFacility`, `EditFacilityLocation`, `FacilityGeoServices`, `FacilityLocationGeoLocation`, `FindFacility`, `FindFacilityLocation`, `FindFacilityTransfers`, `FindInventoryItemsByLabels`, `ViewContactMechs`, `ViewFacilityInventoryByProduct`

**Inventur** (`org.apache.ofbiz.product.facility.inventory`):
`FindFacilityPhysicalInventory`, `InventoryAverageCosts`, `InventoryItemTotals`, `LookupInventoryItems`, `PhysicalInventoryVariance`, `ReceiveInventory`, `TransferInventoryItem`

**Retouren** (`org.apache.ofbiz.product.facility.returns`):
`ReceiveReturn`

**Versand-Screens** (`org.apache.ofbiz.product.facility.shipment`):
`AddItemsFromInventory`, `AddItemsFromOrder`, `EditShipment`, `EditShipmentItems`, `EditShipmentPackages`, `EditShipmentPlan`, `EditShipmentRouteSegments`, `PackingSlip`, `PackOrder`, `PrintPickSheets`, `QuickShipOrder`, `ReceiveInventoryAgainstPurchaseOrder`, `ReviewOrdersNotPickedOrPacked`, `ShipmentManifest`, `VerifyPick`, `ViewShipment`, `WeightPackage`

**Lager** (`org.apache.ofbiz.product.facility.storage`):
`StorageServices`

---

## Groovy-View-Scripts: Katalog-Admin-Screens (`org.apache.ofbiz.product.catalog.*`)

Reine View-Scripts zur Datenvorbereitung für den Katalog-Administrationsbereich, ohne eigenständige Geschäftslogik.

**Kategorie-Screens** (`org.apache.ofbiz.product.catalog.category`):
`CategoryTree`, `CreateProductInCategoryCheckExisting`, `EditCategory`, `EditCategoryContentContent`, `EditCategoryProducts`, `EditCategorySEO`

**Produkt-Screens** (`org.apache.ofbiz.product.catalog.product`):
`ApplyFeaturesFromCategory`, `ApplyFeaturesFromGroup`, `BestProducts`, `EditProductAssoc`, `EditProductContent`, `EditProductContentContent`, `EditProductFeatures`, `EditProductInventoryItems`, `EditProductQuickAdmin`, `EditProductSEO`, `QuickAddVariants`

**Feature-Screens** (`org.apache.ofbiz.product.catalog.feature`):
`EditFeatureCategoryFeatures`, `EditFeatureGroups`, `QuickAddProductFeatures`

**Suchscreens** (`org.apache.ofbiz.product.catalog.find`):
`AdvancedSearchOptions`, `KeywordSearch`, `KeywordSearchBox`, `MiniProductList`, `SideCatalogs`, `SideDeepCategory`

**Bildverwaltungs-Screens** (`org.apache.ofbiz.product.catalog.imagemanagement`):
`CheckAction`, `CheckRejected`, `ImageFrame`, `ImageGallery`, `ImageRecentlyApproved`, `ImageUpload`, `SeoLocales`, `SetDefaultImage`, `SortSequenceNum`

**Sonstige Admin-Screens**:
`ChooseTopCategory`, `FastLoadCache`, `GetSupplierInventories`, `PrepareCreateShipmentTimeEstimate`, `PrepareCreateShipMeth`

**Konfigurations-Screens** (`org.apache.ofbiz.product.catalog.config`):
`EditProductConfigItemContent`, `EditProductConfigItemContentContent`

**Preis-Screens** (`org.apache.ofbiz.product.catalog.price`):
`EditProductPriceRules`

**Aktions-Screens** (`org.apache.ofbiz.product.catalog.promo`):
`EditProductPromoCode`

**Shop-Screens** (`org.apache.ofbiz.product.catalog.store`):
`EditProductStorePaySetup`, `EditProductStoreSurveys`

**Thesaurus** (`org.apache.ofbiz.product.catalog.thesaurus`):
`EditKeywordThesaurus`

**Lookup** (`org.apache.ofbiz.product.catalog.lookup`):
`LookupVariantProduct`

---

## Testklassen

Die folgenden Klassen sind automatisierte Integrationstests, die den OFBiz-Testrahmen (`OFBizTestCase`) verwenden. Sie sind alle als Gruppen zu betrachten und werden nicht im Produktivbetrieb ausgeführt.

**Java-Tests** (`org.apache.ofbiz.product.test`):
- `StockMovesTest`: Tests für Bestandsbewegungen
- `InventoryItemTransferTest`: Tests für Lagertransfers

**Groovy-Tests** (`org.apache.ofbiz.product.product.test`):
- `CategoryTests`, `CostTests`, `InventoryTests`, `ProductConfigTests`, `ProductFeatureTypeTests`, `ProductPriceTests`, `ProductPromoActionTests`, `ProductPromoCondTests`, `ProductTagTest`, `ProductTest`, `ProductTests`, `ShipmentTests`

**Groovy-Tests** (`org.apache.ofbiz.product.shipment.test`):
- `ShipmentCostTests`: Tests für Versandkostenberechnungen (verschiedene Berechnungsmodelle: Pauschal, Prozent, Gewichts-/Mengen-/Preisbreaks)

---

## Klasse: `ProductConfigItemContentServicesScript`

**Paket:** `org.apache.ofbiz.product.product.config`
**Typ:** Groovy-Script

| Methode | Beschreibung |
|---|---|
| `createProductConfigItemContent()` / `updateProductConfigItemContent()` | Verknüpft und aktualisiert Inhalte (Beschreibungen) für Konfigurationspositionen |
| `createSimpleTextContentForProductConfigItem()` | Legt einfachen Textinhalt für eine Konfigurationsposition an |

---

## Klasse: `SeoUrlUtil`

**Paket:** `org.apache.ofbiz.product.category`
**Typ:** Java-Klasse (Utility)
**Zweck:** Hilfsfunktionen für die Verarbeitung und Konvertierung von SEO-freundlichen URLs (Normalisierung, Segment-Extraktion).
