# Öffentliche API-Katalog: Apache OFBiz
Generiert aus `javap -p` Ausgabe aller 1.568 Top-Level-Klassen.
Nur public Methoden gelistet. Groovy-Klassen mit Laufzeit-Artefakten markiert.

## Modul: accounting (114 Klassen, 918 public Methoden)

### `GatewayRequest` — class
Vollständiger Name: `org.apache.ofbiz.accounting.thirdparty.eway.GatewayRequest`
- `public org.apache.ofbiz.accounting.thirdparty.eway.GatewayRequest();`
- `public org.apache.ofbiz.accounting.thirdparty.eway.GatewayRequest(int);`
- `public int getRequestMethod();`
- `public java.lang.String getUrl();`
- `public java.lang.String getCustomerID();`
- `public void setCustomerID(java.lang.String);`
- `public java.lang.String getRefundPassword();`
- `public void setRefundPassword(java.lang.String);`
- `public java.math.BigDecimal getTotalAmount();`
- `public void setTotalAmount(java.math.BigDecimal);`
- `public java.lang.String getCardHoldersName();`
- `public void setCardHoldersName(java.lang.String);`
- `public java.lang.String getCardNumber();`
- `public void setCardNumber(java.lang.String);`
- `public java.lang.String getCardExpiryMonth();`
- *(... 34 weitere Methoden)*

### `PaymentGatewayServices` — class
Vollständiger Name: `org.apache.ofbiz.accounting.payment.PaymentGatewayServices`
- `public org.apache.ofbiz.accounting.payment.PaymentGatewayServices();`
- `public static java.util.Map<java.lang.String, java.lang.Object> authOrderPaymentPreference(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> authOrderPayments(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> releaseOrderPayments(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> processCreditResult(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> releaseOrderPaymentPreference(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> processReleaseResult(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> capturePaymentsByInvoice(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> captureOrderPayments(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> processCaptureSplitPayment(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> captureBillingAccountPayments(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> storePaymentErrorMessage(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> processAuthResult(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> processCaptureResult(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> refundOrderPaymentPreference(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- *(... 32 weitere Methoden)*

### `InvoiceWorker` — class
Vollständiger Name: `org.apache.ofbiz.accounting.invoice.InvoiceWorker`
- `public static java.math.BigDecimal getInvoiceTotal(org.apache.ofbiz.entity.Delegator, java.lang.String);`
- `public static java.math.BigDecimal getInvoiceTotal(org.apache.ofbiz.entity.Delegator, java.lang.String, java.lang.Boolean);`
- `public static java.math.BigDecimal getInvoiceItemTotal(org.apache.ofbiz.entity.GenericValue);`
- `public static java.lang.String getInvoiceItemDescription(org.apache.ofbiz.service.LocalDispatcher, org.apache.ofbiz.entity.GenericValue, java.util.Locale) `
- `public static java.util.List<java.lang.String> getTaxableInvoiceItemTypeIds(org.apache.ofbiz.entity.Delegator) `
- `public static java.math.BigDecimal getInvoiceTaxTotal(org.apache.ofbiz.entity.GenericValue);`
- `public static java.math.BigDecimal getInvoiceNoTaxTotal(org.apache.ofbiz.entity.GenericValue);`
- `public static java.math.BigDecimal getInvoiceTotal(org.apache.ofbiz.entity.GenericValue);`
- `public static java.math.BigDecimal getInvoiceTotal(org.apache.ofbiz.entity.GenericValue, java.lang.Boolean);`
- `public static org.apache.ofbiz.entity.GenericValue getBillToParty(org.apache.ofbiz.entity.GenericValue);`
- `public static org.apache.ofbiz.entity.GenericValue getBillFromParty(org.apache.ofbiz.entity.GenericValue);`
- `public static org.apache.ofbiz.entity.GenericValue getSendFromParty(org.apache.ofbiz.entity.GenericValue);`
- `public static org.apache.ofbiz.entity.GenericValue getShippingAddress(org.apache.ofbiz.entity.GenericValue);`
- `public static org.apache.ofbiz.entity.GenericValue getBillToAddress(org.apache.ofbiz.entity.GenericValue);`
- `public static org.apache.ofbiz.entity.GenericValue getSendFromAddress(org.apache.ofbiz.entity.GenericValue);`
- *(... 20 weitere Methoden)*

### `PaymentServices` [Groovy] — class
Vollständiger Name: `org.apache.ofbiz.accounting.payment.PaymentServices`
- `public org.apache.ofbiz.accounting.payment.PaymentServices();`
- `public org.apache.ofbiz.accounting.payment.PaymentServices(groovy.lang.Binding);`
- `public static void main(java.lang.String...);`
- `public java.lang.Object run();`
- `public java.util.Map createPayment();`
- `public java.util.Map getInvoicePaymentInfoList();`
- `public java.util.Map updatePayment();`
- `public java.util.Map createPaymentAndApplicationForParty();`
- `public java.util.Map checkAndCreateBatchForValidPayments();`
- `public java.util.Map getPaymentRunningTotal();`
- `public java.util.Map createPaymentContent();`
- `public java.util.Map updatePaymentContent();`
- `public java.util.Map massChangePaymentStatus();`
- `public java.util.Map getInvoicePaymentInfoListByDueDateOffset();`
- `public java.util.Map voidPayment();`
- *(... 15 weitere Methoden)*

### `InvoiceServicesScript` [Groovy] — class
Vollständiger Name: `org.apache.ofbiz.accounting.invoice.InvoiceServicesScript`
- `public org.apache.ofbiz.accounting.invoice.InvoiceServicesScript();`
- `public org.apache.ofbiz.accounting.invoice.InvoiceServicesScript(groovy.lang.Binding);`
- `public static void main(java.lang.String...);`
- `public java.lang.Object run();`
- `public java.util.Map getNextInvoiceId();`
- `public java.util.Map invoiceSequenceEnforced();`
- `public java.util.Map invoiceSequenceRestart();`
- `public java.util.Map createInvoice();`
- `public java.util.Map getInvoice();`
- `public java.util.Map updateInvoice();`
- `public java.util.Map copyInvoice();`
- `public java.util.Map copyInvoiceToTemplate();`
- `public java.util.Map setInvoiceStatus();`
- `public java.util.Map checkInvoiceStatusInProgress();`
- `public java.util.Map cancelInvoice();`
- *(... 13 weitere Methoden)*

### `ValueLinkApi` — class
Vollständiger Name: `org.apache.ofbiz.accounting.thirdparty.valuelink.ValueLinkApi`
- `public static org.apache.ofbiz.accounting.thirdparty.valuelink.ValueLinkApi getInstance(org.apache.ofbiz.entity.Delegator, java.util.Properties, boolean);`
- `public static org.apache.ofbiz.accounting.thirdparty.valuelink.ValueLinkApi getInstance(org.apache.ofbiz.entity.Delegator, java.util.Properties);`
- `public java.lang.String encryptPin(java.lang.String);`
- `public java.lang.String decryptPin(java.lang.String);`
- `public java.util.Map<java.lang.String, java.lang.Object> send(java.util.Map<java.lang.String, java.lang.Object>) `
- `public java.util.Map<java.lang.String, java.lang.Object> send(java.lang.String, java.util.Map<java.lang.String, java.lang.Object>) `
- `public java.lang.StringBuffer outputKeyCreation(boolean, java.lang.String);`
- `public java.security.KeyPair createKeys() `
- `public byte[] generateKek(java.security.PrivateKey) `
- `public java.security.PublicKey getValueLinkPublicKey() `
- `public java.security.PrivateKey getPrivateKey() `
- `public byte[] generateMwk();`
- `public byte[] generateMwk(byte[]);`
- `public byte[] generateMwk(javax.crypto.SecretKey);`
- `public byte[] encryptViaKek(byte[]);`
- *(... 11 weitere Methoden)*

### `UtilAccounting` — class
Vollständiger Name: `org.apache.ofbiz.accounting.util.UtilAccounting`
- `public static java.lang.String getProductOrgGlAccountId(java.lang.String, java.lang.String, java.lang.String, org.apache.ofbiz.entity.Delegator) `
- `public static java.lang.String getDefaultAccountId(java.lang.String, java.lang.String, org.apache.ofbiz.entity.Delegator) `
- `public static java.util.List<java.lang.String> getDescendantGlAccountClassIds(org.apache.ofbiz.entity.GenericValue) `
- `public static boolean isPaymentType(org.apache.ofbiz.entity.GenericValue, java.lang.String) `
- `public static boolean isTaxPayment(org.apache.ofbiz.entity.GenericValue) `
- `public static boolean isDisbursement(org.apache.ofbiz.entity.GenericValue) `
- `public static boolean isReceipt(org.apache.ofbiz.entity.GenericValue) `
- `public static boolean isAccountClassClass(org.apache.ofbiz.entity.GenericValue, java.lang.String) `
- `public static boolean isAccountClass(org.apache.ofbiz.entity.GenericValue, java.lang.String) `
- `public static boolean isDebitAccount(org.apache.ofbiz.entity.GenericValue) `
- `public static boolean isCreditAccount(org.apache.ofbiz.entity.GenericValue) `
- `public static boolean isAssetAccount(org.apache.ofbiz.entity.GenericValue) `
- `public static boolean isLiabilityAccount(org.apache.ofbiz.entity.GenericValue) `
- `public static boolean isEquityAccount(org.apache.ofbiz.entity.GenericValue) `
- `public static boolean isIncomeAccount(org.apache.ofbiz.entity.GenericValue) `
- *(... 8 weitere Methoden)*

### `ValueLinkServices` — class
Vollständiger Name: `org.apache.ofbiz.accounting.thirdparty.valuelink.ValueLinkServices`
- `public org.apache.ofbiz.accounting.thirdparty.valuelink.ValueLinkServices();`
- `public static java.util.Map<java.lang.String, java.lang.Object> createKeys(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> testKekEncryption(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> assignWorkingKey(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> activate(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> linkPhysicalCard(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> disablePin(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> redeem(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> reload(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> balanceInquire(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> transactionHistory(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> refund(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> voidRedeem(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> voidRefund(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> voidReload(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, java.lang.Object>);`
- *(... 7 weitere Methoden)*

### `AutoAcctgAdminTests` [Groovy] — class
Vollständiger Name: `org.apache.ofbiz.accounting.accounting.AutoAcctgAdminTests`
- `public org.apache.ofbiz.accounting.accounting.AutoAcctgAdminTests(java.lang.String);`
- `public void testGetFXConversion();`
- `public void testAddPaymentMethodTypeGlAssignment();`
- `public void testRemovePaymentTypeGlAssignment();`
- `public void testCreatePartyAcctgPreference();`
- `public void testUpdatePartyAcctgPreference();`
- `public void testGetPartyAccountingPreferences();`
- `public void testSetAcctgCompany();`
- `public void testUpdateFXConversion();`
- `public void testCreateGlAccountTypeDefault();`
- `public void testRemoveGlAccountTypeDefault();`
- `public void testAddInvoiceItemTypeGlAssignment();`
- `public void testRemoveInvoiceItemTypeGlAssignment();`
- `public void testAddPaymentTypeGlAssignment();`
- `public void testRemovePaymentMethodTypeGlAssignment();`
- *(... 3 weitere Methoden)*

### `InvoiceServices` — class
Vollständiger Name: `org.apache.ofbiz.accounting.invoice.InvoiceServices`
- `public org.apache.ofbiz.accounting.invoice.InvoiceServices();`
- `public static java.util.Map<java.lang.String, java.lang.Object> createInvoiceForOrderAllItems(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> createInvoiceForOrder(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> createCommissionInvoices(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> readyInvoices(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> createInvoicesFromShipment(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> setInvoicesToReadyFromShipment(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> createSalesInvoicesFromDropShipment(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> createInvoicesFromShipments(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> createInvoicesFromReturnShipment(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> createInvoiceFromReturn(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> checkInvoicePaymentApplications(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> updatePaymentApplication(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> updatePaymentApplicationDef(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> updatePaymentApplicationDefBd(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, java.lang.Object>);`
- *(... 3 weitere Methoden)*

### `AutoAcctgInvoiceTests` [Groovy] — class
Vollständiger Name: `org.apache.ofbiz.accounting.accounting.AutoAcctgInvoiceTests`
- `public org.apache.ofbiz.accounting.accounting.AutoAcctgInvoiceTests(java.lang.String);`
- `public void testCreateInvoiceContent();`
- `public void testCreateSimpleTextContentForInvoice();`
- `public void testCopyInvoice();`
- `public void testCreateInvoice();`
- `public void testGetInvoice();`
- `public void testSetInvoiceStatus();`
- `public void testCopyInvoiceToTemplate();`
- `public void testCreateInvoiceItem();`
- `public void testCreateInvoiceStatus();`
- `public void testCreateInvoiceRole();`
- `public void testCreateInvoiceTerm();`
- `public void testCancelInvoice();`
- `public groovy.lang.MetaClass getMetaClass();`
- `public void setMetaClass(groovy.lang.MetaClass);`
- *(... 1 weitere Methoden)*

### `RateServices` [Groovy] — class
Vollständiger Name: `org.apache.ofbiz.accounting.rate.RateServices`
- `public org.apache.ofbiz.accounting.rate.RateServices();`
- `public org.apache.ofbiz.accounting.rate.RateServices(groovy.lang.Binding);`
- `public static void main(java.lang.String...);`
- `public java.lang.Object run();`
- `public java.util.Map updateRateAmount();`
- `public java.util.Map expireRateAmount();`
- `public java.util.Map deleteRateAmount();`
- `public java.util.Map updatePartyRate();`
- `public java.util.Map deletePartyRate();`
- `public java.util.Map expirePartyRate();`
- `public java.util.Map getRateAmount();`
- `public java.util.Map getRatesAmountsFrom(java.lang.String);`
- `public java.util.Map getRatesAmountsFromWorkEffortId();`
- `public java.util.Map getRatesAmountsFromPartyId();`
- `public java.util.Map getRatesAmountsFromEmplPositionTypeId();`
- *(... 1 weitere Methoden)*

### `FixedAssetServices` [Groovy] — class
Vollständiger Name: `org.apache.ofbiz.accounting.fixedasset.FixedAssetServices`
- `public org.apache.ofbiz.accounting.fixedasset.FixedAssetServices();`
- `public org.apache.ofbiz.accounting.fixedasset.FixedAssetServices(groovy.lang.Binding);`
- `public static void main(java.lang.String...);`
- `public java.lang.Object run();`
- `public java.util.Map createFixedAssetMaint();`
- `public java.util.Map updateFixedAssetMaint();`
- `public java.util.Map createMaintsFromMeterReading();`
- `public java.util.Map createMaintsFromTimeInterval();`
- `public java.util.Map createFixedAssetMaintOrder();`
- `public java.util.Map autoAssignFixedAssetPartiesToMaintenance();`
- `public java.util.Map straightLineDepreciation();`
- `public java.util.Map doubleDecliningBalanceDepreciation();`
- `public java.util.Map calculateFixedAssetDepreciation();`
- `public java.util.Map checkUpdateFixedAssetDepreciation();`
- `public static void __$swapInit();`

### `AutoPaymentTests` [Groovy] — class
Vollständiger Name: `org.apache.ofbiz.accounting.accounting.AutoPaymentTests`
- `public org.apache.ofbiz.accounting.accounting.AutoPaymentTests(java.lang.String);`
- `public void testCreatePaymentGroupAndMember();`
- `public void testVoidPayment();`
- `public void testCancelInvoice();`
- `public void testCreatePaymentAndPaymentGroupForInvoices();`
- `public void testCancelCheckRunPayments();`
- `public void testDepositWithdrawPayments();`
- `public void testDepositWithdrawPaymentsInSingleTrans();`
- `public void testSetFinAccountTransStatus();`
- `public void testGlPostingsOnVoidPayment();`
- `public void testGlPostingOnCheckRun();`
- `public groovy.lang.MetaClass getMetaClass();`
- `public void setMetaClass(groovy.lang.MetaClass);`
- `public static void __$swapInit();`

### `PaymentWorker` — class
Vollständiger Name: `org.apache.ofbiz.accounting.payment.PaymentWorker`
- `public static java.util.List<java.util.Map<java.lang.String, org.apache.ofbiz.entity.GenericValue>> getPartyPaymentMethodValueMaps(org.apache.ofbiz.entity.Delegator, java.lang.String);`
- `public static java.util.List<java.util.Map<java.lang.String, org.apache.ofbiz.entity.GenericValue>> getPartyPaymentMethodValueMaps(org.apache.ofbiz.entity.Delegator, java.lang.String, java.lang.Boolean);`
- `public static java.util.Map<java.lang.String, java.lang.Object> getPaymentMethodAndRelated(javax.servlet.ServletRequest, java.lang.String);`
- `public static org.apache.ofbiz.entity.GenericValue getPaymentAddress(org.apache.ofbiz.entity.Delegator, java.lang.String);`
- `public static java.math.BigDecimal getPaymentsTotal(java.util.List<org.apache.ofbiz.entity.GenericValue>);`
- `public static java.math.BigDecimal getPaymentApplied(org.apache.ofbiz.entity.Delegator, java.lang.String);`
- `public static java.math.BigDecimal getPaymentApplied(org.apache.ofbiz.entity.Delegator, java.lang.String, java.lang.Boolean);`
- `public static java.math.BigDecimal getPaymentAppliedAmount(org.apache.ofbiz.entity.Delegator, java.lang.String);`
- `public static java.math.BigDecimal getPaymentApplied(org.apache.ofbiz.entity.GenericValue);`
- `public static java.math.BigDecimal getPaymentApplied(org.apache.ofbiz.entity.GenericValue, java.lang.Boolean);`
- `public static java.math.BigDecimal getPaymentNotApplied(org.apache.ofbiz.entity.GenericValue);`
- `public static java.math.BigDecimal getPaymentNotApplied(org.apache.ofbiz.entity.GenericValue, java.lang.Boolean);`
- `public static java.math.BigDecimal getPaymentNotApplied(org.apache.ofbiz.entity.Delegator, java.lang.String);`
- `public static java.math.BigDecimal getPaymentNotApplied(org.apache.ofbiz.entity.Delegator, java.lang.String, java.lang.Boolean);`

### `AutoAcctgFinAccountTests` [Groovy] — class
Vollständiger Name: `org.apache.ofbiz.accounting.accounting.AutoAcctgFinAccountTests`
- `public org.apache.ofbiz.accounting.accounting.AutoAcctgFinAccountTests(java.lang.String);`
- `public void testCreateFinAccount();`
- `public void testUpdateFinAccount();`
- `public void testDeleteFinAccount();`
- `public void testCreateFinAccountRole();`
- `public void testUpdateFinAccountRole();`
- `public void testDeleteFinAccountRole();`
- `public void testCreateFinAccountTrans();`
- `public void testCreateFinAccountStatus();`
- `public void testCreateFinAccountAuth();`
- `public void testSetFinAccountTransStatus();`
- `public groovy.lang.MetaClass getMetaClass();`
- `public void setMetaClass(groovy.lang.MetaClass);`

### `GiftCertificateServices` — class
Vollständiger Name: `org.apache.ofbiz.accounting.payment.GiftCertificateServices`
- `public org.apache.ofbiz.accounting.payment.GiftCertificateServices();`
- `public static java.util.Map<java.lang.String, java.lang.Object> createGiftCertificate(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> addFundsToGiftCertificate(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> redeemGiftCertificate(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> checkGiftCertificateBalance(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> giftCertificateProcessor(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> giftCertificateAuthorize(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> giftCertificateRefund(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> giftCertificateRelease(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> giftCertificatePurchase(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> giftCertificateReload(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> createFulfillmentRecord(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> refundGcPurchase(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`

### `AccountEntrySum` [Groovy] — class
Vollständiger Name: `org.apache.ofbiz.accounting.reports.AccountEntrySum`
- `public org.apache.ofbiz.accounting.reports.AccountEntrySum();`
- `public groovy.lang.MetaClass getMetaClass();`
- `public void setMetaClass(groovy.lang.MetaClass);`
- `public java.lang.String getGlAccountId();`
- `public void setGlAccountId(java.lang.String);`
- `public java.lang.String getAccountCode();`
- `public void setAccountCode(java.lang.String);`
- `public java.lang.String getAccountName();`
- `public void setAccountName(java.lang.String);`
- `public java.lang.String getDebitCreditFlag();`
- `public void setDebitCreditFlag(java.lang.String);`
- `public java.math.BigDecimal getAmount();`
- `public void setAmount(java.math.BigDecimal);`

### `AuthorizeResponse` — class
Vollständiger Name: `org.apache.ofbiz.accounting.thirdparty.authorizedotnet.AuthorizeResponse`
- `public org.apache.ofbiz.accounting.thirdparty.authorizedotnet.AuthorizeResponse(java.lang.String, int);`
- `public org.apache.ofbiz.accounting.thirdparty.authorizedotnet.AuthorizeResponse(java.lang.String, java.lang.String, int);`
- `public boolean isApproved();`
- `public java.lang.String getTransactionId();`
- `public java.lang.String getAuthorizationCode();`
- `public java.lang.String getResponseCode();`
- `public java.lang.String getReasonCode();`
- `public java.lang.String getReasonText();`
- `public java.lang.String getAvsResult();`
- `public java.lang.String getCvResult();`
- `public java.math.BigDecimal getAmount();`
- `public java.lang.String getRawResponse();`
- `public java.lang.String toString();`

### `GatewayResponse` — class
Vollständiger Name: `org.apache.ofbiz.accounting.thirdparty.eway.GatewayResponse`
- `public java.lang.String getTrxnNumber();`
- `public java.lang.String getTrxnReference();`
- `public java.lang.String getTrxnOption1();`
- `public java.lang.String getTrxnOption2();`
- `public java.lang.String getTrxnOption3();`
- `public java.lang.String getAuthCode();`
- `public java.lang.String getTrxnError();`
- `public int getReturnAmount();`
- `public java.math.BigDecimal getTransactionAmount();`
- `public boolean getTrxnStatus();`
- `public double getBeagleScore();`
- `public org.apache.ofbiz.accounting.thirdparty.eway.GatewayResponse(java.io.InputStream, org.apache.ofbiz.accounting.thirdparty.eway.GatewayRequest) `
- `public java.lang.String toString();`

## Modul: base (155 Klassen, 1608 public Methoden)

### `UtilDateTime` — class
Vollständiger Name: `org.apache.ofbiz.base.util.UtilDateTime`
- `public static int getIntervalInDays(java.sql.Timestamp, java.sql.Timestamp);`
- `public static java.sql.Timestamp addDaysToTimestamp(java.sql.Timestamp, int);`
- `public static java.sql.Timestamp addDaysToTimestamp(java.sql.Timestamp, java.lang.Double);`
- `public static double getInterval(java.sql.Timestamp, java.sql.Timestamp);`
- `public static java.lang.String formatInterval(java.util.Date, java.util.Date, int, java.util.Locale);`
- `public static java.lang.String formatInterval(java.util.Date, java.util.Date, java.util.Locale);`
- `public static java.lang.String formatInterval(java.sql.Timestamp, java.sql.Timestamp, int, java.util.Locale);`
- `public static java.lang.String formatInterval(java.sql.Timestamp, java.sql.Timestamp, java.util.Locale);`
- `public static java.lang.String formatInterval(long, int, java.util.Locale);`
- `public static java.lang.String formatInterval(long, java.util.Locale);`
- `public static java.lang.String formatInterval(double, java.util.Locale);`
- `public static java.lang.String formatInterval(double, int, java.util.Locale);`
- `public static java.sql.Timestamp nowTimestamp();`
- `public static java.sql.Timestamp getTimestamp(long);`
- `public static java.sql.Timestamp getTimestamp(java.lang.String) `
- *(... 90 weitere Methoden)*

### `UtilHttp` — class
Vollständiger Name: `org.apache.ofbiz.base.util.UtilHttp`
- `public static java.util.Map<java.lang.String, java.lang.Object> getCombinedMap(javax.servlet.http.HttpServletRequest);`
- `public static java.util.Map<java.lang.String, java.lang.Object> getCombinedMap(javax.servlet.http.HttpServletRequest, java.util.Set<? extends java.lang.String>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> getParameterMap(javax.servlet.http.HttpServletRequest);`
- `public static java.util.Map<java.lang.String, java.lang.Object> getParameterMap(javax.servlet.http.HttpServletRequest, java.util.function.Predicate<java.lang.String>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> getMultiPartParameterMap(javax.servlet.http.HttpServletRequest);`
- `public static long getMaxUploadSize(org.apache.ofbiz.entity.Delegator);`
- `public static int getSizeThreshold(org.apache.ofbiz.entity.Delegator);`
- `public static java.io.File getTmpUploadRepository(org.apache.ofbiz.entity.Delegator);`
- `public static java.util.Map<java.lang.String, java.lang.Object> getQueryStringOnlyParameterMap(java.lang.String);`
- `public static java.util.Map<java.lang.String, java.lang.Object> getPathInfoOnlyParameterMap(java.lang.String, java.util.function.Predicate<java.lang.String>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> getUrlOnlyParameterMap(javax.servlet.http.HttpServletRequest);`
- `public static java.util.Map<java.lang.String, java.lang.Object> canonicalizeParameterMap(java.util.Map<java.lang.String, java.lang.Object>);`
- `public static java.lang.String canonicalizeParameter(java.lang.String);`
- `public static java.util.Map<java.lang.String, java.lang.Object> getJSONAttributeMap(javax.servlet.http.HttpServletRequest);`
- `public static java.util.Map<java.lang.String, java.lang.Object> getAttributeMap(javax.servlet.http.HttpServletRequest);`
- *(... 69 weitere Methoden)*

### `UtilValidate` — class
Vollständiger Name: `org.apache.ofbiz.base.util.UtilValidate`
- `public static boolean isEmpty(java.lang.Object);`
- `public static boolean isNotEmpty(java.lang.Object);`
- `public static boolean isEmpty(org.apache.ofbiz.base.lang.IsEmpty);`
- `public static boolean isNotEmpty(org.apache.ofbiz.base.lang.IsEmpty);`
- `public static <E> boolean isEmpty(java.util.Collection<E>);`
- `public static <K, E> boolean isEmpty(java.util.Map<K, E>);`
- `public static boolean isEmpty(java.lang.CharSequence);`
- `public static <E> boolean isNotEmpty(java.util.Collection<E>);`
- `public static boolean isNotEmpty(java.lang.CharSequence);`
- `public static boolean isString(java.lang.Object);`
- `public static boolean isWhitespace(java.lang.String);`
- `public static java.lang.String stripCharsInBag(java.lang.String, java.lang.String);`
- `public static boolean isInteger(java.lang.String);`
- `public static boolean isSignedInteger(java.lang.String);`
- `public static boolean isSignedLong(java.lang.String);`
- *(... 62 weitere Methoden)*

### `Debug` — class
Vollständiger Name: `org.apache.ofbiz.base.util.Debug`
- `public org.apache.ofbiz.base.util.Debug();`
- `public static java.lang.Integer getLevelFromString(java.lang.String);`
- `public static void log(int, java.lang.Throwable, java.lang.String, java.lang.String);`
- `public static void log(int, java.lang.Throwable, java.lang.String, java.lang.String, java.lang.Object...);`
- `public static void log(int, java.lang.Throwable, java.lang.String, java.lang.String, java.lang.String);`
- `public static void log(int, java.lang.Throwable, java.lang.String, java.lang.String, java.lang.String, java.lang.Object...);`
- `public static boolean isOn(int);`
- `public static void log(java.lang.String);`
- `public static void log(java.lang.String, java.lang.Object...);`
- `public static void log(java.lang.Throwable);`
- `public static void log(java.lang.String, java.lang.String);`
- `public static void log(java.lang.String, java.lang.String, java.lang.Object...);`
- `public static void log(java.lang.Throwable, java.lang.String);`
- `public static void log(java.lang.Throwable, java.lang.String, java.lang.String);`
- `public static void log(java.lang.Throwable, java.lang.String, java.lang.String, java.lang.Object...);`
- *(... 44 weitere Methoden)*

### `UtilXml` — class
Vollständiger Name: `org.apache.ofbiz.base.util.UtilXml`
- `public static org.w3c.dom.ls.DOMImplementationLS getDomLsImplementation() `
- `public static void writeXmlDocument(java.io.OutputStream, org.w3c.dom.Node, java.lang.String, boolean, boolean) `
- `public static javax.xml.transform.Transformer createOutputTransformer(java.lang.String, boolean, boolean, int) `
- `public static void transformDomDocument(javax.xml.transform.Transformer, org.w3c.dom.Node, java.io.OutputStream) `
- `public static void writeXmlDocument(org.w3c.dom.Node, java.io.OutputStream, java.lang.String, boolean, boolean, int) `
- `public static java.lang.Object fromXml(java.io.InputStream);`
- `public static java.lang.Object fromXml(java.io.Reader);`
- `public static java.lang.Object fromXml(java.lang.String);`
- `public static java.lang.String toXml(java.lang.Object);`
- `public static void toXml(java.lang.Object, java.io.OutputStream);`
- `public static void toXml(java.lang.Object, java.io.Writer);`
- `public static java.lang.String writeXmlDocument(org.w3c.dom.Node) `
- `public static void writeXmlDocument(java.lang.String, org.w3c.dom.Node) `
- `public static void writeXmlDocument(java.io.OutputStream, org.w3c.dom.Node) `
- `public static org.w3c.dom.Document readXmlDocument(java.lang.String) `
- *(... 44 weitere Methoden)*

### `UtilCache` — class
Vollständiger Name: `org.apache.ofbiz.base.util.cache.UtilCache`
- `public java.lang.Object getCacheLineTable();`
- `public boolean isEmpty();`
- `public V put(K, V);`
- `public V putIfAbsent(K, V);`
- `public V putIfAbsentAndGet(K, V);`
- `public V put(K, V, long);`
- `public V putIfAbsent(K, V, long);`
- `public V get(java.lang.Object);`
- `public java.util.Collection<V> values();`
- `public long getSizeInBytes();`
- `public V remove(java.lang.Object);`
- `public synchronized void erase();`
- `public void clear();`
- `public static void clearAllCaches();`
- `public static java.util.Set<java.lang.String> getUtilCacheTableKeySet();`
- *(... 36 weitere Methoden)*

### `HttpClient` — class
Vollständiger Name: `org.apache.ofbiz.base.util.HttpClient`
- `public org.apache.ofbiz.base.util.HttpClient();`
- `public org.apache.ofbiz.base.util.HttpClient(java.net.URL);`
- `public org.apache.ofbiz.base.util.HttpClient(java.lang.String);`
- `public org.apache.ofbiz.base.util.HttpClient(java.lang.String, java.util.Map<java.lang.String, java.lang.Object>);`
- `public org.apache.ofbiz.base.util.HttpClient(java.net.URL, java.util.Map<java.lang.String, java.lang.Object>);`
- `public org.apache.ofbiz.base.util.HttpClient(java.lang.String, java.util.Map<java.lang.String, java.lang.Object>, java.util.Map<java.lang.String, java.lang.String>);`
- `public org.apache.ofbiz.base.util.HttpClient(java.net.URL, java.util.Map<java.lang.String, java.lang.Object>, java.util.Map<java.lang.String, java.lang.String>);`
- `public void setDebug(boolean);`
- `public void setTimeout(int);`
- `public void followRedirects(boolean);`
- `public void setLineFeed(boolean);`
- `public void setRawStream(java.lang.String);`
- `public void setUrl(java.net.URL);`
- `public void setUrl(java.lang.String);`
- `public void setParameters(java.util.Map<java.lang.String, java.lang.Object>);`
- *(... 34 weitere Methoden)*

### `UtilProperties` — class
Vollständiger Name: `org.apache.ofbiz.base.util.UtilProperties`
- `public static boolean propertyValueEquals(java.lang.String, java.lang.String, java.lang.String);`
- `public static boolean propertyValueEqualsIgnoreCase(java.lang.String, java.lang.String, java.lang.String);`
- `public static java.lang.String getPropertyValue(java.lang.String, java.lang.String, java.lang.String);`
- `public static double getPropertyNumber(java.lang.String, java.lang.String, double);`
- `public static double getPropertyNumber(java.lang.String, java.lang.String);`
- `public static java.lang.Boolean getPropertyAsBoolean(java.lang.String, java.lang.String, boolean);`
- `public static java.lang.Integer getPropertyAsInteger(java.lang.String, java.lang.String, int);`
- `public static java.lang.Long getPropertyAsLong(java.lang.String, java.lang.String, long);`
- `public static java.lang.Float getPropertyAsFloat(java.lang.String, java.lang.String, float);`
- `public static java.lang.Double getPropertyAsDouble(java.lang.String, java.lang.String, double);`
- `public static java.math.BigInteger getPropertyAsBigInteger(java.lang.String, java.lang.String, java.math.BigInteger);`
- `public static java.math.BigDecimal getPropertyAsBigDecimal(java.lang.String, java.lang.String, java.math.BigDecimal);`
- `public static java.lang.String getPropertyValue(java.lang.String, java.lang.String);`
- `public static java.util.Properties createProperties(java.lang.String);`
- `public static java.util.Properties getProperties(java.lang.String);`
- *(... 28 weitere Methoden)*

### `UtilMisc` — class
Vollständiger Name: `org.apache.ofbiz.base.util.UtilMisc`
- `public static <T extends java.lang.Throwable> T initCause(T, java.lang.Throwable);`
- `public static <T> int compare(java.lang.Comparable<T>, T);`
- `public static <E> int compare(java.util.List<E>, java.util.List<E>);`
- `public static <T> java.util.Iterator<T> toIterator(java.util.Collection<T>);`
- `public static <K, V> java.util.Map<K, V> toMap(java.lang.Object...);`
- `public static <K, V> java.util.Map<K, V> toMap(java.util.function.Supplier<java.util.Map<K, V>>, java.lang.Object...);`
- `public static <K, V> java.lang.String printMap(java.util.Map<? extends K, ? extends V>);`
- `public static <T> java.util.List<T> makeListWritable(java.util.Collection<? extends T>);`
- `public static <K, V> java.util.Map<K, V> makeMapWritable(java.util.Map<K, ? extends V>);`
- `public static <V> void makeMapSerializable(java.util.Map<java.lang.String, V>);`
- `public static <V> void makeArrayListSerializable(java.util.ArrayList<java.lang.Object>);`
- `public static java.util.List<java.util.Map<java.lang.Object, java.lang.Object>> sortMaps(java.util.List<java.util.Map<java.lang.Object, java.lang.Object>>, java.util.List<? extends java.lang.String>);`
- `public static <K, IK, V> java.util.Map<IK, V> getMapFromMap(java.util.Map<K, java.lang.Object>, K);`
- `public static <K, V> java.util.List<V> getListFromMap(java.util.Map<K, java.lang.Object>, K);`
- `public static <K> java.math.BigDecimal addToBigDecimalInMap(java.util.Map<K, java.lang.Object>, K, java.math.BigDecimal);`
- *(... 26 weitere Methoden)*

### `UtilFormatOut` — class
Vollständiger Name: `org.apache.ofbiz.base.util.UtilFormatOut`
- `public static java.lang.String formatNumber(java.lang.Double, java.lang.String, org.apache.ofbiz.entity.Delegator, java.util.Locale);`
- `public static java.lang.String formatNumber(java.math.BigDecimal, java.lang.String, org.apache.ofbiz.entity.Delegator, java.util.Locale);`
- `public static java.lang.String formatPrice(java.lang.Double);`
- `public static java.lang.String formatPrice(java.math.BigDecimal);`
- `public static java.lang.String formatCurrency(double, java.lang.String, java.util.Locale, int);`
- `public static java.lang.String formatCurrency(java.math.BigDecimal, java.lang.String, java.util.Locale, int);`
- `public static java.lang.String formatDecimalNumber(double, java.lang.String, java.util.Locale);`
- `public static java.lang.String formatCurrency(java.math.BigDecimal, java.lang.String, java.util.Locale);`
- `public static java.lang.String formatSpelledOutAmount(java.lang.Double, java.util.Locale);`
- `public static java.lang.String formatAmount(double, java.util.Locale);`
- `public static java.lang.String formatPercentage(java.lang.Double);`
- `public static java.lang.String formatPercentage(java.math.BigDecimal);`
- `public static java.lang.String formatPercentageRate(java.math.BigDecimal, boolean);`
- `public static java.lang.String formatQuantity(java.lang.Long);`
- `public static java.lang.String formatQuantity(java.lang.Integer);`
- *(... 24 weitere Methoden)*

### `UelFunctions` — class
Vollständiger Name: `org.apache.ofbiz.base.util.string.UelFunctions`
- `public org.apache.ofbiz.base.util.string.UelFunctions();`
- `public static javax.el.FunctionMapper getFunctionMapper();`
- `public static synchronized void setFunction(java.lang.String, java.lang.String, java.lang.reflect.Method);`
- `public static java.lang.String dateString(java.sql.Timestamp, java.util.TimeZone, java.util.Locale);`
- `public static java.lang.String localizedDateString(java.sql.Timestamp, java.util.TimeZone, java.util.Locale);`
- `public static java.lang.String dateTimeString(java.sql.Timestamp, java.util.TimeZone, java.util.Locale);`
- `public static java.lang.String localizedDateTimeString(java.sql.Timestamp, java.util.TimeZone, java.util.Locale);`
- `public static java.lang.String timeString(java.sql.Timestamp, java.util.TimeZone, java.util.Locale);`
- `public static int getSize(java.lang.Object);`
- `public static boolean endsWith(java.lang.String, java.lang.String);`
- `public static int indexOf(java.lang.String, java.lang.String);`
- `public static int lastIndexOf(java.lang.String, java.lang.String);`
- `public static int length(java.lang.String);`
- `public static java.lang.String replace(java.lang.String, java.lang.String, java.lang.String);`
- `public static java.lang.String replaceAll(java.lang.String, java.lang.String, java.lang.String);`
- *(... 17 weitere Methoden)*

### `ComponentConfig` — class
Vollständiger Name: `org.apache.ofbiz.base.component.ComponentConfig`
- `public static java.lang.Boolean componentExists(java.lang.String);`
- `public static java.util.List<org.apache.ofbiz.base.component.ComponentConfig$ClasspathInfo> getAllClasspathInfos();`
- `public static java.util.Collection<org.apache.ofbiz.base.component.ComponentConfig> getAllComponents();`
- `public static void sortDependencies() `
- `public static java.util.stream.Stream<org.apache.ofbiz.base.component.ComponentConfig> components();`
- `public static java.util.List<org.apache.ofbiz.base.container.ContainerConfig$Configuration> getAllConfigurations();`
- `public static java.util.List<org.apache.ofbiz.base.component.ComponentConfig$EntityResourceInfo> getAllEntityResourceInfos(java.lang.String);`
- `public static java.util.List<org.apache.ofbiz.base.component.ComponentConfig$EntityResourceInfo> getAllEntityResourceInfos(java.lang.String, java.lang.String);`
- `public static java.util.List<org.apache.ofbiz.base.component.ComponentConfig$KeystoreInfo> getAllKeystoreInfos();`
- `public static java.util.List<org.apache.ofbiz.base.component.ComponentConfig$ServiceResourceInfo> getAllServiceResourceInfos(java.lang.String);`
- `public static java.util.List<org.apache.ofbiz.base.component.ComponentConfig$TestSuiteInfo> getAllTestSuiteInfos(java.lang.String);`
- `public static java.util.List<org.apache.ofbiz.base.component.ComponentConfig$WebappInfo> getAllWebappResourceInfos();`
- `public static org.apache.ofbiz.base.component.ComponentConfig getComponentConfig(java.lang.String) `
- `public static org.apache.ofbiz.base.component.ComponentConfig getComponentConfig(java.lang.String, java.lang.String) `
- `public static org.apache.ofbiz.base.component.ComponentConfig$KeystoreInfo getKeystoreInfo(java.lang.String, java.lang.String);`
- *(... 15 weitere Methoden)*

### `GenericTestCaseBase` — class
Vollständiger Name: `org.apache.ofbiz.base.test.GenericTestCaseBase`
- `public static void useAllMemory() `
- `public static void assertStaticHelperClass(java.lang.Class<?>) `
- `public static void assertComparison(java.lang.String, int, int);`
- `public static <V, E extends java.lang.Exception> void assertFuture(java.lang.String, java.util.concurrent.Future<V>, V, boolean, java.lang.Class<E>, java.lang.String);`
- `public static void assertNotEquals(java.lang.Object, java.lang.Object);`
- `public static void assertNotEquals(java.lang.String, java.lang.Object, java.lang.Object);`
- `public static <T> void assertEquals(java.util.List<T>, java.lang.Object);`
- `public static <T> void assertEquals(java.lang.String, java.util.List<T>, java.lang.Object);`
- `public static <T> void assertEquals(java.util.Collection<T>, java.lang.Object);`
- `public static <T> void assertEquals(java.lang.String, java.util.Collection<T>, java.lang.Object);`
- `public static <T> void assertEquals(java.util.Set<T>, java.lang.Object);`
- `public static <T> void assertEquals(java.lang.String, java.util.Set<T>, java.lang.Object);`
- `public static <V, I extends java.lang.Iterable<V>> void assertEqualsIterable(java.lang.String, java.util.List<? extends V>, I);`
- `public static <V, I extends java.lang.Iterable<V>> void assertEqualsIterable(java.lang.String, java.util.List<? extends V>, int, I, int);`
- `public static <V, I extends java.lang.Iterable<V>> void assertEqualsIterable(java.lang.String, java.util.List<? extends V>, java.util.List<? extends V>, I, java.util.List<? extends V>);`
- *(... 13 weitere Methoden)*

### `StringUtil` — class
Vollständiger Name: `org.apache.ofbiz.base.util.StringUtil`
- `public static java.lang.String internString(java.lang.String);`
- `public static java.lang.String replaceString(java.lang.String, java.lang.String, java.lang.String);`
- `public static java.lang.String join(java.util.Collection<?>, java.lang.CharSequence);`
- `public static java.util.List<java.lang.String> split(java.lang.String, java.lang.String);`
- `public static java.util.List<java.lang.String> splitWithStringSeparator(java.lang.String, java.lang.String);`
- `public static java.util.Map<java.lang.String, java.lang.String> strToMap(java.lang.String, java.lang.String, boolean);`
- `public static java.util.Map<java.lang.String, java.lang.String> strToMap(java.lang.String, java.lang.String, boolean, java.lang.String);`
- `public static java.util.Map<java.lang.String, java.lang.String> strToMap(java.lang.String, boolean);`
- `public static java.util.Map<java.lang.String, java.lang.String> strToMap(java.lang.String);`
- `public static java.util.List<java.lang.String> toList(java.lang.String);`
- `public static java.util.Set<java.lang.String> toSet(java.lang.String);`
- `public static <K, V> java.util.Map<K, V> createMap(java.util.List<K>, java.util.List<V>);`
- `public static java.lang.String cleanUpPathPrefix(java.lang.String);`
- `public static java.lang.String removeSpaces(java.lang.String);`
- `public static java.lang.String toHexString(byte[]);`
- *(... 10 weitere Methoden)*

### `MessageString` — class
Vollständiger Name: `org.apache.ofbiz.base.util.MessageString`
- `public static java.util.List<java.lang.Object> getMessagesForField(java.lang.String, boolean, java.util.List<java.lang.Object>);`
- `public static java.util.List<java.lang.Object> getMessagesForField(java.lang.String, java.lang.String, java.lang.String, java.lang.String, boolean, java.util.List<java.lang.Object>);`
- `public org.apache.ofbiz.base.util.MessageString(java.lang.String, java.lang.String, java.lang.String, java.lang.String, java.util.Locale, boolean);`
- `public org.apache.ofbiz.base.util.MessageString(java.lang.String, java.lang.String, boolean);`
- `public org.apache.ofbiz.base.util.MessageString(java.lang.String, java.lang.String, java.lang.String, java.lang.Throwable);`
- `public org.apache.ofbiz.base.util.MessageString(java.lang.String, java.lang.Throwable);`
- `public java.lang.String getFieldName();`
- `public void setFieldName(java.lang.String);`
- `public boolean isForField(java.lang.String);`
- `public java.lang.String getMessage();`
- `public void setMessage(java.lang.String);`
- `public java.lang.Throwable getSourceError();`
- `public void setSourceError(java.lang.Throwable);`
- `public java.lang.String getToFieldName();`
- `public void setToFieldName(java.lang.String);`
- *(... 9 weitere Methoden)*

### `ComparableRange` — class
Vollständiger Name: `org.apache.ofbiz.base.lang.ComparableRange`
- `public T getStart();`
- `public T getEnd();`
- `public org.apache.ofbiz.base.lang.ComparableRange(T, T);`
- `public boolean after(org.apache.ofbiz.base.lang.Range<T>);`
- `public boolean after(T);`
- `public boolean before(org.apache.ofbiz.base.lang.Range<T>);`
- `public boolean before(T);`
- `public T end();`
- `public boolean equals(java.lang.Object);`
- `public int hashCode();`
- `public int compareTo(org.apache.ofbiz.base.lang.ComparableRange<T>);`
- `public boolean includes(org.apache.ofbiz.base.lang.Range<T>);`
- `public boolean includes(T);`
- `public boolean isPoint();`
- `public boolean overlaps(org.apache.ofbiz.base.lang.Range<T>);`
- *(... 8 weitere Methoden)*

### `FreeMarkerWorker` — class
Vollständiger Name: `org.apache.ofbiz.base.util.template.FreeMarkerWorker`
- `public static freemarker.ext.beans.BeansWrapper getDefaultOfbizWrapper();`
- `public static freemarker.template.Configuration newConfiguration();`
- `public static freemarker.template.Configuration makeConfiguration(freemarker.ext.beans.BeansWrapper);`
- `public static void renderTemplate(java.lang.String, java.util.Map<java.lang.String, java.lang.Object>, java.lang.Appendable) `
- `public static void renderTemplateFromString(java.lang.String, java.lang.String, java.util.Map<java.lang.String, java.lang.Object>, java.lang.Appendable, long, boolean) `
- `public static void clearTemplateFromCache(java.lang.String);`
- `public static freemarker.core.Environment renderTemplate(freemarker.template.Template, java.util.Map<java.lang.String, java.lang.Object>, java.lang.Appendable) `
- `public static freemarker.template.Configuration getDefaultOfbizConfig();`
- `public static freemarker.template.Template getTemplate(java.lang.String) `
- `public static freemarker.template.Template getTemplate(java.lang.String, org.apache.ofbiz.base.util.cache.UtilCache<java.lang.String, freemarker.template.Template>, freemarker.template.Configuration) `
- `public static java.lang.String getArg(java.util.Map<java.lang.String, ? extends java.lang.Object>, java.lang.String, freemarker.core.Environment);`
- `public static java.lang.String getArg(java.util.Map<java.lang.String, ? extends java.lang.Object>, java.lang.String, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public static <T> T getWrappedObject(java.lang.String, freemarker.core.Environment);`
- `public static java.lang.Object get(freemarker.template.SimpleHash, java.lang.String);`
- `public static <T> T unwrap(java.lang.Object);`
- *(... 8 weitere Methoden)*

### `UtilTimer` — class
Vollständiger Name: `org.apache.ofbiz.base.util.UtilTimer`
- `public static org.apache.ofbiz.base.util.UtilTimer makeTimer();`
- `public org.apache.ofbiz.base.util.UtilTimer();`
- `public org.apache.ofbiz.base.util.UtilTimer(java.lang.String, boolean);`
- `public org.apache.ofbiz.base.util.UtilTimer(java.lang.String, boolean, boolean);`
- `public void startTimer();`
- `public java.lang.String getName();`
- `public boolean isRunning();`
- `public java.lang.String timerString(java.lang.String);`
- `public java.lang.String timerString(java.lang.String, java.lang.String);`
- `public double secondsSinceStart();`
- `public double secondsSinceLast();`
- `public long timeSinceStart();`
- `public long timeSinceLast();`
- `public void setLog(boolean);`
- `public boolean getLog();`
- *(... 7 weitere Methoden)*

### `ResourceBundleMapWrapper` — class
Vollständiger Name: `org.apache.ofbiz.base.util.collections.ResourceBundleMapWrapper`
- `public org.apache.ofbiz.base.util.collections.ResourceBundleMapWrapper(org.apache.ofbiz.base.util.collections.ResourceBundleMapWrapper$InternalRbmWrapper);`
- `public org.apache.ofbiz.base.util.collections.ResourceBundleMapWrapper(java.util.ResourceBundle);`
- `public org.apache.ofbiz.base.util.collections.ResourceBundleMapWrapper(java.util.ResourceBundle, java.util.Map<java.lang.String, java.lang.Object>);`
- `public void addBottomResourceBundle(java.util.ResourceBundle);`
- `public void addBottomResourceBundle(org.apache.ofbiz.base.util.collections.ResourceBundleMapWrapper$InternalRbmWrapper);`
- `public void addBottomResourceBundle(java.lang.String);`
- `public void pushResourceBundle(java.util.ResourceBundle);`
- `public java.util.ResourceBundle getInitialResourceBundle();`
- `public void clear();`
- `public boolean containsKey(java.lang.Object);`
- `public boolean containsValue(java.lang.Object);`
- `public java.util.Set<java.util.Map$Entry<java.lang.String, java.lang.Object>> entrySet();`
- `public java.lang.Object get(java.lang.Object);`
- `public boolean isEmpty();`
- `public java.util.Set<java.lang.String> keySet();`
- *(... 6 weitere Methoden)*

### `TimeDuration` — class
Vollständiger Name: `org.apache.ofbiz.base.util.TimeDuration`
- `public org.apache.ofbiz.base.util.TimeDuration(int, int, int, int, int, int, int);`
- `public org.apache.ofbiz.base.util.TimeDuration(com.ibm.icu.util.Calendar, com.ibm.icu.util.Calendar);`
- `public boolean equals(java.lang.Object);`
- `public java.lang.String toString();`
- `public int compareTo(org.apache.ofbiz.base.util.TimeDuration);`
- `public boolean isNegative();`
- `public boolean isZero();`
- `public int milliseconds();`
- `public int seconds();`
- `public int minutes();`
- `public int hours();`
- `public int days();`
- `public int months();`
- `public int years();`
- `public com.ibm.icu.util.Calendar addToCalendar(com.ibm.icu.util.Calendar);`
- *(... 6 weitere Methoden)*

## Modul: catalina (7 Klassen, 17 public Methoden)

### `CatalinaContainer` — class
Vollständiger Name: `org.apache.ofbiz.catalina.container.CatalinaContainer`
- `public org.apache.ofbiz.catalina.container.CatalinaContainer();`
- `public void init(java.util.List<org.apache.ofbiz.base.start.StartupCommand>, java.lang.String, java.lang.String) `
- `public boolean start() `
- `public void stop();`
- `public java.lang.String getName();`

### `HashedCredentialHandler` — class
Vollständiger Name: `org.apache.ofbiz.catalina.container.HashedCredentialHandler`
- `public org.apache.ofbiz.catalina.container.HashedCredentialHandler();`
- `public boolean matches(java.lang.String, java.lang.String);`
- `public java.lang.String mutate(java.lang.String);`

### `SimpleCredentialHandler` — class
Vollständiger Name: `org.apache.ofbiz.catalina.container.SimpleCredentialHandler`
- `public org.apache.ofbiz.catalina.container.SimpleCredentialHandler();`
- `public boolean matches(java.lang.String, java.lang.String);`
- `public java.lang.String mutate(java.lang.String);`

### `SslAcceleratorValve` — class
Vollständiger Name: `org.apache.ofbiz.catalina.container.SslAcceleratorValve`
- `public org.apache.ofbiz.catalina.container.SslAcceleratorValve();`
- `public java.lang.Integer getSslAcceleratorPort();`
- `public void invoke(org.apache.catalina.connector.Request, org.apache.catalina.connector.Response) `

### `CrossSubdomainSessionValve` — class
Vollständiger Name: `org.apache.ofbiz.catalina.container.CrossSubdomainSessionValve`
- `public void invoke(org.apache.catalina.connector.Request, org.apache.catalina.connector.Response) `

### `FilterJars` — class
Vollständiger Name: `org.apache.ofbiz.catalina.container.FilterJars`
- `public boolean check(org.apache.tomcat.JarScanType, java.lang.String);`

### `OFBizRealm` — class
Vollständiger Name: `org.apache.ofbiz.catalina.container.OFBizRealm`
- `public org.apache.ofbiz.catalina.container.OFBizRealm();`

## Modul: common (54 Klassen, 328 public Methoden)

### `ContextHelper` — class
Vollständiger Name: `org.apache.ofbiz.common.scripting.ContextHelper`
- `public java.lang.Object addBinding(java.lang.String, java.lang.Object);`
- `public java.lang.String expandString(java.lang.String);`
- `public org.apache.ofbiz.entity.Delegator getDelegator();`
- `public org.apache.ofbiz.service.LocalDispatcher getDispatcher();`
- `public <T> T getEnv(java.lang.String);`
- `public java.util.List<java.lang.String> getErrorMessages();`
- `public java.util.Iterator<java.util.Map$Entry<java.lang.String, java.lang.Object>> getEnvEntryIterator();`
- `public java.util.Locale getLocale();`
- `public org.apache.ofbiz.widget.renderer.VisualTheme getVisualTheme();`
- `public java.lang.Object getParameter(java.lang.String);`
- `public java.util.Map<java.lang.String, java.lang.Object> getParameters();`
- `public javax.servlet.http.HttpServletRequest getRequest();`
- `public javax.servlet.http.HttpServletResponse getResponse();`
- `public java.lang.Object getResult(java.lang.String);`
- `public java.util.Map<java.lang.String, java.lang.Object> getResults();`
- *(... 10 weitere Methoden)*

### `CommonServices` — class
Vollständiger Name: `org.apache.ofbiz.common.CommonServices`
- `public org.apache.ofbiz.common.CommonServices();`
- `public static java.util.Map<java.lang.String, java.lang.Object> testService(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ?>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> testSOAPService(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ?>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> blockingTestService(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ?>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> testRollbackListener(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ?>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> testCommitListener(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ?>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> createNote(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ?>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> adjustDebugLevels(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ?>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> forceGc(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ?>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> echoService(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ?>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> returnErrorService(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ?>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> conditionTrueService(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ?>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> conditionFalseService(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ?>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> entityFailTest(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ?>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> entitySortTest(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ?>);`
- *(... 9 weitere Methoden)*

### `CommonServicesScript` [Groovy] — class
Vollständiger Name: `org.apache.ofbiz.common.CommonServicesScript`
- `public org.apache.ofbiz.common.CommonServicesScript();`
- `public org.apache.ofbiz.common.CommonServicesScript(groovy.lang.Binding);`
- `public static void main(java.lang.String...);`
- `public java.lang.Object run();`
- `public java.util.Map commonGenericPermission();`
- `public java.util.Map convertUom();`
- `public java.util.Map convertUomCustom();`
- `public java.util.Map getFileUploadProgressStatus();`
- `public java.util.Map getVisualThemeResources();`
- `public java.util.Map getCountryList();`
- `public java.util.Map getAssociatedStateList();`
- `public java.util.Map linkGeos();`
- `public java.util.Map getRelatedGeos();`
- `public java.util.Map checkUomConversion();`
- `public java.util.Map checkUomConversionDated();`
- *(... 6 weitere Methoden)*

### `ScriptHelperImpl` — class
Vollständiger Name: `org.apache.ofbiz.common.scripting.ScriptHelperImpl`
- `public org.apache.ofbiz.common.scripting.ScriptHelperImpl(javax.script.ScriptContext);`
- `public java.util.Map<java.lang.String, ? extends java.lang.Object> createServiceMap(java.lang.String, java.util.Map<java.lang.String, ? extends java.lang.Object>) `
- `public void error(java.lang.String);`
- `public java.lang.String evalString(java.lang.String);`
- `public void failure(java.lang.String);`
- `public java.util.List<java.util.Map<java.lang.String, java.lang.Object>> findList(java.lang.String, java.util.Map<java.lang.String, ? extends java.lang.Object>) `
- `public java.util.Map<java.lang.String, java.lang.Object> findOne(java.lang.String) `
- `public java.util.Map<java.lang.String, java.lang.Object> findOne(java.lang.String, java.util.Map<java.lang.String, ? extends java.lang.Object>, java.util.Map<java.lang.String, ? extends java.lang.Object>) `
- `public void logError(java.lang.String);`
- `public void logInfo(java.lang.String);`
- `public void logWarning(java.lang.String);`
- `public java.util.Map<java.lang.String, java.lang.Object> makeValue(java.lang.String) `
- `public java.util.Map<java.lang.String, java.lang.Object> makeValue(java.lang.String, java.util.Map<java.lang.String, java.lang.Object>) `
- `public java.util.Map<java.lang.String, ? extends java.lang.Object> runService(java.lang.String, java.util.Map<java.lang.String, ? extends java.lang.Object>) `
- `public java.util.Map<java.lang.String, ? extends java.lang.Object> runService(java.lang.String, java.util.Map<java.lang.String, ? extends java.lang.Object>, java.util.Map<java.lang.String, ? extends java.lang.Object>) `
- *(... 2 weitere Methoden)*

### `PortalPageServices` [Groovy] — class
Vollständiger Name: `org.apache.ofbiz.common.PortalPageServices`
- `public org.apache.ofbiz.common.PortalPageServices();`
- `public org.apache.ofbiz.common.PortalPageServices(groovy.lang.Binding);`
- `public static void main(java.lang.String...);`
- `public java.lang.Object run();`
- `public java.util.Map movePortletToPortalPage();`
- `public java.util.Map addPortalPageColumn();`
- `public java.util.Map deletePortalPageColumn();`
- `public java.util.Map createPortalPagePortlet();`
- `public java.util.Map deletePortalPagePortlet();`
- `public java.util.Map getPortletAttributes();`
- `public java.util.Map createPortalPage();`
- `public java.util.Map deletePortalPage();`
- `public java.util.Map updatePortalPageSeq();`
- `public java.util.Map updatePortletSeqDragDrop();`
- `public java.util.Map duplicatePortalPageDetails();`

### `KeywordSearchUtil` — class
Vollständiger Name: `org.apache.ofbiz.common.KeywordSearchUtil`
- `public static java.lang.String getSeparators();`
- `public static java.lang.String getStopWordBagOr();`
- `public static java.lang.String getStopWordBagAnd();`
- `public static boolean getRemoveStems();`
- `public static java.util.Set<java.lang.String> getStemSet();`
- `public static void processForKeywords(java.lang.String, java.util.Map<java.lang.String, java.lang.Long>, boolean, boolean, boolean, boolean);`
- `public static void processKeywordsForIndex(java.lang.String, java.util.Map<java.lang.String, java.lang.Long>, java.lang.String, java.lang.String, java.lang.String, boolean, java.util.Set<java.lang.String>);`
- `public static void processForKeywords(java.lang.String, java.util.Map<java.lang.String, java.lang.Long>, java.lang.String, java.lang.String, java.lang.String, boolean, java.util.Set<java.lang.String>, boolean, boolean, boolean, boolean);`
- `public static void fixupKeywordSet(java.util.Set<java.lang.String>, java.util.Map<java.lang.String, java.lang.Long>, java.lang.String, java.lang.String, boolean, java.util.Set<java.lang.String>, boolean, boolean, boolean, boolean);`
- `public static java.util.Set<java.lang.String> makeKeywordSet(java.lang.String, java.lang.String, boolean);`
- `public static java.util.Set<java.lang.String> fixKeywordsForSearch(java.util.Set<java.lang.String>, boolean, boolean, boolean, boolean);`
- `public static boolean expandKeywordForSearch(java.lang.String, java.util.Set<java.lang.String>, org.apache.ofbiz.entity.Delegator);`

### `FindServices` — class
Vollständiger Name: `org.apache.ofbiz.common.FindServices`
- `public org.apache.ofbiz.common.FindServices();`
- `public static java.util.Map<java.lang.String, java.util.Map<java.lang.String, java.util.Map<java.lang.String, java.lang.Object>>> prepareField(java.util.Map<java.lang.String, ?>, java.util.Map<java.lang.String, java.lang.Object>, java.util.Map<java.lang.String, java.util.List<java.lang.Object[]>>);`
- `public static java.util.List<org.apache.ofbiz.entity.condition.EntityCondition> createConditionList(java.util.Map<java.lang.String, ? extends java.lang.Object>, java.util.List<org.apache.ofbiz.entity.model.ModelField>, java.util.Map<java.lang.String, java.lang.Object>, org.apache.ofbiz.entity.Delegator, java.util.Map<java.lang.String, ?>);`
- `public static org.apache.ofbiz.entity.condition.EntityCondition createSingleCondition(org.apache.ofbiz.entity.model.ModelField, java.lang.String, java.lang.Object, boolean, org.apache.ofbiz.entity.Delegator, java.util.Map<java.lang.String, ?>);`
- `public static java.util.List<org.apache.ofbiz.entity.condition.EntityCondition> createCondition(org.apache.ofbiz.entity.model.ModelEntity, java.util.Map<java.lang.String, java.util.Map<java.lang.String, java.util.Map<java.lang.String, java.lang.Object>>>, java.util.Map<java.lang.String, java.lang.Object>, java.util.Map<java.lang.String, java.util.List<java.lang.Object[]>>, org.apache.ofbiz.entity.Delegator, java.util.Map<java.lang.String, ?>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> performFindList(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> performFind(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ?>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> prepareFind(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ?>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> executeFind(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ?>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> buildReducedQueryString(java.util.Map<java.lang.String, ?>, java.lang.String, org.apache.ofbiz.entity.Delegator);`
- `public static java.util.Map<java.lang.String, java.lang.Object> performFindItem(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, java.lang.Object>);`

### `LoginServices` — class
Vollständiger Name: `org.apache.ofbiz.common.login.LoginServices`
- `public org.apache.ofbiz.common.login.LoginServices();`
- `public static java.util.Map<java.lang.String, java.lang.Object> userLogin(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ?>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> userImpersonate(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ?>);`
- `public static void createUserLoginPasswordHistory(org.apache.ofbiz.entity.GenericValue) `
- `public static java.util.Map<java.lang.String, java.lang.Object> createUserLogin(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ?>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> updatePassword(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ?>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> updateUserLoginId(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ?>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> updateUserLoginSecurity(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ?>);`
- `public static void checkNewPassword(org.apache.ofbiz.entity.GenericValue, java.lang.String, java.lang.String, java.lang.String, java.lang.String, java.util.List<java.lang.String>, boolean, java.util.Locale);`
- `public static java.lang.String getHashType();`
- `public static boolean checkPassword(java.lang.String, boolean, java.lang.String);`

### `TestFailAuthenticator` — class
Vollständiger Name: `org.apache.ofbiz.common.authentication.example.TestFailAuthenticator`
- `public org.apache.ofbiz.common.authentication.example.TestFailAuthenticator();`
- `public void initialize(org.apache.ofbiz.service.LocalDispatcher);`
- `public boolean authenticate(java.lang.String, java.lang.String, boolean) `
- `public void logout(java.lang.String) `
- `public void syncUser(java.lang.String) `
- `public void updatePassword(java.lang.String, java.lang.String, java.lang.String) `
- `public float getWeight();`
- `public boolean isUserSynchronized();`
- `public boolean isSingleAuthenticator();`
- `public boolean isEnabled();`

### `CommonEvents` — class
Vollständiger Name: `org.apache.ofbiz.common.CommonEvents`
- `public org.apache.ofbiz.common.CommonEvents();`
- `public static java.lang.String setSessionLocale(javax.servlet.http.HttpServletRequest, javax.servlet.http.HttpServletResponse);`
- `public static java.lang.String setSessionTimeZone(javax.servlet.http.HttpServletRequest, javax.servlet.http.HttpServletResponse);`
- `public static java.lang.String setSessionTheme(javax.servlet.http.HttpServletRequest, javax.servlet.http.HttpServletResponse);`
- `public static java.lang.String setSessionCurrencyUom(javax.servlet.http.HttpServletRequest, javax.servlet.http.HttpServletResponse);`
- `public static java.lang.String jsResponseFromRequest(javax.servlet.http.HttpServletRequest, javax.servlet.http.HttpServletResponse);`
- `public static java.lang.String jsonResponseFromRequestAttributes(javax.servlet.http.HttpServletRequest, javax.servlet.http.HttpServletResponse);`
- `public static java.lang.String getCaptcha(javax.servlet.http.HttpServletRequest, javax.servlet.http.HttpServletResponse);`
- `public static java.lang.String loadJWT(javax.servlet.http.HttpServletRequest, javax.servlet.http.HttpServletResponse) `
- `public static java.lang.String openSourceFile(javax.servlet.http.HttpServletRequest, javax.servlet.http.HttpServletResponse);`

### `Authenticator` — interface
Vollständiger Name: `org.apache.ofbiz.common.authentication.api.Authenticator`
- `public abstract void initialize(org.apache.ofbiz.service.LocalDispatcher);`
- `public abstract boolean authenticate(java.lang.String, java.lang.String, boolean) `
- `public abstract void logout(java.lang.String) `
- `public abstract void syncUser(java.lang.String) `
- `public abstract void updatePassword(java.lang.String, java.lang.String, java.lang.String) `
- `public abstract float getWeight();`
- `public abstract boolean isUserSynchronized();`
- `public abstract boolean isSingleAuthenticator();`
- `public abstract boolean isEnabled();`

### `AuthenticatorException` — class
Vollständiger Name: `org.apache.ofbiz.common.authentication.api.AuthenticatorException`
- `public org.apache.ofbiz.common.authentication.api.AuthenticatorException();`
- `public org.apache.ofbiz.common.authentication.api.AuthenticatorException(java.lang.String);`
- `public org.apache.ofbiz.common.authentication.api.AuthenticatorException(java.lang.String, java.lang.Throwable);`
- `public org.apache.ofbiz.common.authentication.api.AuthenticatorException(java.lang.Throwable);`
- `public org.apache.ofbiz.common.authentication.api.AuthenticatorException(java.lang.String, java.util.List<java.lang.String>);`
- `public org.apache.ofbiz.common.authentication.api.AuthenticatorException(java.lang.String, java.util.List<java.lang.String>, java.lang.Throwable);`
- `public org.apache.ofbiz.common.authentication.api.AuthenticatorException(java.util.List<java.lang.String>, java.lang.Throwable);`
- `public org.apache.ofbiz.common.authentication.api.AuthenticatorException(java.util.List<java.lang.String>);`

### `CommonPermissionServices` [Groovy] — class
Vollständiger Name: `org.apache.ofbiz.common.permission.CommonPermissionServices`
- `public org.apache.ofbiz.common.permission.CommonPermissionServices();`
- `public org.apache.ofbiz.common.permission.CommonPermissionServices(groovy.lang.Binding);`
- `public static void main(java.lang.String...);`
- `public java.lang.Object run();`
- `public java.util.Map genericBasePermissionCheck();`
- `public java.util.Map getAllCrudPermissions();`
- `public java.util.Map hasCrudPermission(java.lang.String, java.util.Map);`
- `public java.util.Map visualThemePermissionCheck();`

### `GeoWorker` — class
Vollständiger Name: `org.apache.ofbiz.common.geo.GeoWorker`
- `public static java.util.List<org.apache.ofbiz.entity.GenericValue> expandGeoGroup(java.lang.String, org.apache.ofbiz.entity.Delegator);`
- `public static java.util.List<org.apache.ofbiz.entity.GenericValue> expandGeoGroup(org.apache.ofbiz.entity.GenericValue);`
- `public static java.util.Map<java.lang.String, java.lang.String> expandGeoRegionDeep(java.util.Map<java.lang.String, java.lang.String>, org.apache.ofbiz.entity.Delegator) `
- `public static boolean containsGeo(java.util.List<org.apache.ofbiz.entity.GenericValue>, java.lang.String, org.apache.ofbiz.entity.Delegator);`
- `public static boolean containsGeo(java.util.List<org.apache.ofbiz.entity.GenericValue>, org.apache.ofbiz.entity.GenericValue);`
- `public static org.apache.ofbiz.entity.GenericValue findLatestGeoPoint(org.apache.ofbiz.entity.Delegator, java.lang.String, java.lang.String, java.lang.String, java.lang.String, java.lang.String);`
- `public static java.lang.String getMeasurementSystem(java.util.Locale);`

### `PortalPageMethods` [Groovy] — class
Vollständiger Name: `org.apache.ofbiz.common.PortalPageMethods`
- `public org.apache.ofbiz.common.PortalPageMethods();`
- `public org.apache.ofbiz.common.PortalPageMethods(groovy.lang.Binding);`
- `public static void main(java.lang.String...);`
- `public java.lang.Object run();`
- `public java.lang.String duplicatePortalPage();`
- `public java.lang.String setPortalPortletAttributes();`
- `public java.lang.String copyIfRequiredSystemPage();`

### `PreferenceServices` — class
Vollständiger Name: `org.apache.ofbiz.common.preferences.PreferenceServices`
- `public org.apache.ofbiz.common.preferences.PreferenceServices();`
- `public static java.util.Map<java.lang.String, java.lang.Object> getUserPreference(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ?>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> getUserPreferenceGroup(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ?>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> setUserPreference(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ?>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> removeUserPreference(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ?>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> setUserPreferenceGroup(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ?>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> copyUserPreferenceGroup(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ?>);`

### `AuthHelper` — class
Vollständiger Name: `org.apache.ofbiz.common.authentication.AuthHelper`
- `public static boolean authenticate(java.lang.String, java.lang.String, boolean) `
- `public static void logout(java.lang.String) `
- `public static void syncUser(java.lang.String) `
- `public static void updatePassword(java.lang.String, java.lang.String, java.lang.String) `
- `public static boolean authenticatorsLoaded();`
- `public static void loadAuthenticators(org.apache.ofbiz.service.LocalDispatcher);`

### `EmailServices` — class
Vollständiger Name: `org.apache.ofbiz.common.email.EmailServices`
- `public org.apache.ofbiz.common.email.EmailServices();`
- `public static java.util.Map<java.lang.String, java.lang.Object> sendMail(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> sendMailFromUrl(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> sendMailFromScreen(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> sendMailHiddenInLogFromScreen(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public static void sendFailureNotification(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>, javax.mail.internet.MimeMessage, java.util.List<com.sun.mail.smtp.SMTPAddressFailedException>);`

### `ImageTransform` — class
Vollständiger Name: `org.apache.ofbiz.common.image.ImageTransform`
- `public org.apache.ofbiz.common.image.ImageTransform();`
- `public static java.util.Map<java.lang.String, java.lang.Object> getBufferedImage(java.lang.String, java.util.Locale) `
- `public static java.util.Map<java.lang.String, java.lang.Object> scaleImage(java.awt.image.BufferedImage, double, double, java.util.Map<java.lang.String, java.util.Map<java.lang.String, java.lang.String>>, java.lang.String, java.util.Locale);`
- `public static java.util.Map<java.lang.String, java.lang.Object> getXMLValue(java.lang.String, java.util.Locale) `
- `public static java.awt.image.BufferedImage toBufferedImage(java.awt.Image);`
- `public static java.awt.image.BufferedImage toBufferedImage(java.awt.Image, int);`

### `EmailServicesScript` [Groovy] — class
Vollständiger Name: `org.apache.ofbiz.common.email.EmailServicesScript`
- `public org.apache.ofbiz.common.email.EmailServicesScript();`
- `public org.apache.ofbiz.common.email.EmailServicesScript(groovy.lang.Binding);`
- `public static void main(java.lang.String...);`
- `public java.lang.Object run();`
- `public java.util.Map sendMailFromTemplateSetting();`

## Modul: commonext (7 Klassen, 36 public Methoden)

### `SystemInfoServices` [Groovy] — class
Vollständiger Name: `org.apache.ofbiz.commonext.ofbizsetup.SystemInfoServices`
- `public org.apache.ofbiz.commonext.ofbizsetup.SystemInfoServices();`
- `public org.apache.ofbiz.commonext.ofbizsetup.SystemInfoServices(groovy.lang.Binding);`
- `public static void main(java.lang.String...);`
- `public java.lang.Object run();`
- `public java.util.Map createSystemInfoNote();`
- `public java.util.Map deleteSystemInfoNote();`
- `public java.util.Map deleteAllSystemNotes();`
- `public java.util.Map getSystemInfoNotes();`
- `public java.util.Map getLastSystemInfoNote();`
- `public java.util.Map getSystemInfoStatus();`

### `DocTypeTemplate` [Groovy] — class
Vollständiger Name: `org.apache.ofbiz.commonext.template.DocTypeTemplate`
- `public org.apache.ofbiz.commonext.template.DocTypeTemplate();`
- `public org.apache.ofbiz.commonext.template.DocTypeTemplate(groovy.lang.Binding);`
- `public static void main(java.lang.String...);`
- `public java.lang.Object run();`
- `public java.lang.String getFieldTypeName(java.lang.String);`
- `public java.util.Map getCustomScreenTemplate(java.lang.String, java.lang.String);`

### `ChangeOrgPartyId` [Groovy] — class
Vollständiger Name: `org.apache.ofbiz.commonext.ofbizsetup.ChangeOrgPartyId`
- `public org.apache.ofbiz.commonext.ofbizsetup.ChangeOrgPartyId();`
- `public org.apache.ofbiz.commonext.ofbizsetup.ChangeOrgPartyId(groovy.lang.Binding);`
- `public static void main(java.lang.String...);`
- `public java.lang.Object run();`

### `FindFacility` [Groovy] — class
Vollständiger Name: `org.apache.ofbiz.commonext.ofbizsetup.FindFacility`
- `public org.apache.ofbiz.commonext.ofbizsetup.FindFacility();`
- `public org.apache.ofbiz.commonext.ofbizsetup.FindFacility(groovy.lang.Binding);`
- `public static void main(java.lang.String...);`
- `public java.lang.Object run();`

### `GetProdCatalog` [Groovy] — class
Vollständiger Name: `org.apache.ofbiz.commonext.ofbizsetup.GetProdCatalog`
- `public org.apache.ofbiz.commonext.ofbizsetup.GetProdCatalog();`
- `public org.apache.ofbiz.commonext.ofbizsetup.GetProdCatalog(groovy.lang.Binding);`
- `public static void main(java.lang.String...);`
- `public java.lang.Object run();`

### `GetProductStoreAndWebSite` [Groovy] — class
Vollständiger Name: `org.apache.ofbiz.commonext.ofbizsetup.GetProductStoreAndWebSite`
- `public org.apache.ofbiz.commonext.ofbizsetup.GetProductStoreAndWebSite();`
- `public org.apache.ofbiz.commonext.ofbizsetup.GetProductStoreAndWebSite(groovy.lang.Binding);`
- `public static void main(java.lang.String...);`
- `public java.lang.Object run();`

### `SystemInfoNote` [Groovy] — class
Vollständiger Name: `org.apache.ofbiz.commonext.ofbizsetup.SystemInfoNote`
- `public org.apache.ofbiz.commonext.ofbizsetup.SystemInfoNote();`
- `public org.apache.ofbiz.commonext.ofbizsetup.SystemInfoNote(groovy.lang.Binding);`
- `public static void main(java.lang.String...);`
- `public java.lang.Object run();`

## Modul: content (77 Klassen, 611 public Methoden)

### `ContentWorker` — class
Vollständiger Name: `org.apache.ofbiz.content.content.ContentWorker`
- `public org.apache.ofbiz.content.content.ContentWorker();`
- `public org.apache.ofbiz.entity.GenericValue getWebSitePublishPointExt(org.apache.ofbiz.entity.Delegator, java.lang.String, boolean) `
- `public org.apache.ofbiz.entity.GenericValue getCurrentContentExt(org.apache.ofbiz.entity.Delegator, java.util.List<java.util.Map<java.lang.String, ? extends java.lang.Object>>, org.apache.ofbiz.entity.GenericValue, java.util.Map<java.lang.String, java.lang.Object>, java.lang.Boolean, java.lang.String) `
- `public java.lang.String getMimeTypeIdExt(org.apache.ofbiz.entity.Delegator, org.apache.ofbiz.entity.GenericValue, java.util.Map<java.lang.String, java.lang.Object>);`
- `public void renderContentAsTextExt(org.apache.ofbiz.service.LocalDispatcher, java.lang.String, java.lang.Appendable, java.util.Map<java.lang.String, java.lang.Object>, java.util.Locale, java.lang.String, boolean) `
- `public void renderSubContentAsTextExt(org.apache.ofbiz.service.LocalDispatcher, java.lang.String, java.lang.Appendable, java.lang.String, java.util.Map<java.lang.String, java.lang.Object>, java.util.Locale, java.lang.String, boolean) `
- `public java.lang.String renderSubContentAsTextExt(org.apache.ofbiz.service.LocalDispatcher, java.lang.String, java.lang.String, java.util.Map<java.lang.String, java.lang.Object>, java.util.Locale, java.lang.String, boolean) `
- `public java.lang.String renderContentAsTextExt(org.apache.ofbiz.service.LocalDispatcher, java.lang.String, java.util.Map<java.lang.String, java.lang.Object>, java.util.Locale, java.lang.String, boolean) `
- `public static org.apache.ofbiz.entity.GenericValue findContentForRendering(org.apache.ofbiz.entity.Delegator, java.lang.String, java.util.Locale, java.lang.String, java.lang.String, boolean) `
- `public static void renderContentAsText(org.apache.ofbiz.service.LocalDispatcher, org.apache.ofbiz.entity.GenericValue, java.lang.Appendable, java.util.Map<java.lang.String, java.lang.Object>, java.util.Locale, java.lang.String, boolean, java.util.List<org.apache.ofbiz.entity.GenericValue>) `
- `public static java.lang.String renderContentAsText(org.apache.ofbiz.service.LocalDispatcher, java.lang.String, java.util.Map<java.lang.String, java.lang.Object>, java.util.Locale, java.lang.String, boolean) `
- `public static java.lang.String renderContentAsText(org.apache.ofbiz.service.LocalDispatcher, java.lang.String, java.lang.Appendable, java.util.Map<java.lang.String, java.lang.Object>, java.util.Locale, java.lang.String, java.lang.String, java.lang.String, boolean, java.util.List<org.apache.ofbiz.entity.GenericValue>) `
- `public static void renderContentAsText(org.apache.ofbiz.service.LocalDispatcher, java.lang.String, java.lang.Appendable, java.util.Map<java.lang.String, java.lang.Object>, java.util.Locale, java.lang.String, java.lang.String, java.lang.String, boolean) `
- `public static java.lang.String renderSubContentAsText(org.apache.ofbiz.service.LocalDispatcher, java.lang.String, java.lang.String, java.util.Map<java.lang.String, java.lang.Object>, java.util.Locale, java.lang.String, boolean) `
- `public static void renderSubContentAsText(org.apache.ofbiz.service.LocalDispatcher, java.lang.String, java.lang.Appendable, java.lang.String, java.util.Map<java.lang.String, java.lang.Object>, java.util.Locale, java.lang.String, boolean) `
- *(... 50 weitere Methoden)*

### `DataResourceWorker` — class
Vollständiger Name: `org.apache.ofbiz.content.data.DataResourceWorker`
- `public org.apache.ofbiz.content.data.DataResourceWorker();`
- `public static java.lang.String getDataCategoryMap(org.apache.ofbiz.entity.Delegator, int, java.util.Map<java.lang.String, java.lang.Object>, java.util.List<java.lang.String>, boolean) `
- `public static void getDataCategoryAncestry(org.apache.ofbiz.entity.Delegator, java.lang.String, java.util.List<java.lang.String>) `
- `public static void buildList(java.util.Map<java.lang.String, java.lang.Object>, java.util.List<java.util.Map<java.lang.String, java.lang.Object>>, int);`
- `public static java.lang.String uploadAndStoreImage(javax.servlet.http.HttpServletRequest, java.lang.String, java.lang.String);`
- `public static java.lang.String getMimeTypeFromImageFileName(java.lang.String);`
- `public static java.lang.String callDataResourcePermissionCheck(org.apache.ofbiz.entity.Delegator, org.apache.ofbiz.service.LocalDispatcher, java.util.Map<java.lang.String, java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> callDataResourcePermissionCheckResult(org.apache.ofbiz.entity.Delegator, org.apache.ofbiz.service.LocalDispatcher, java.util.Map<java.lang.String, java.lang.Object>);`
- `public static byte[] acquireImage(org.apache.ofbiz.entity.Delegator, java.lang.String) `
- `public static byte[] acquireImage(org.apache.ofbiz.entity.Delegator, org.apache.ofbiz.entity.GenericValue) `
- `public static java.lang.String getMimeType(org.apache.ofbiz.entity.GenericValue);`
- `public static java.lang.String getMimeType(org.apache.ofbiz.entity.GenericValue, java.lang.String);`
- `public static java.lang.String getMimeType(org.apache.ofbiz.entity.Delegator, java.lang.String, java.lang.String);`
- `public static java.lang.String getMimeTypeWithByteBuffer(java.nio.ByteBuffer) `
- `public static java.lang.String buildRequestPrefix(org.apache.ofbiz.entity.Delegator, java.util.Locale, java.lang.String, java.lang.String);`
- *(... 19 weitere Methoden)*

### `ContentServicesScript` [Groovy] — class
Vollständiger Name: `org.apache.ofbiz.content.content.ContentServicesScript`
- `public org.apache.ofbiz.content.content.ContentServicesScript();`
- `public org.apache.ofbiz.content.content.ContentServicesScript(groovy.lang.Binding);`
- `public static void main(java.lang.String...);`
- `public java.lang.Object run();`
- `public java.util.Map createTextAndUploadedContent();`
- `public java.util.Map findAssocContent();`
- `public java.util.Map updateSingleContentPurpose();`
- `public java.util.Map createEmailContent();`
- `public java.util.Map deactivateAllContentRoles();`
- `public java.util.Map createContentAlternativeUrl();`
- `public java.util.Map updateEmailContent();`
- `public java.util.Map createArticleContent();`
- `public java.util.Map setContentStatus();`
- `public java.util.Map createDownloadContent();`
- `public java.util.Map updateDownloadContent();`
- *(... 16 weitere Methoden)*

### `ContentManagementServices` — class
Vollständiger Name: `org.apache.ofbiz.content.ContentManagementServices`
- `public org.apache.ofbiz.content.ContentManagementServices();`
- `public static java.util.Map<java.lang.String, java.lang.Object> getSubContent(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> getContent(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> persistContentAndAssoc(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>) `
- `public static java.util.Map<java.lang.String, java.lang.Object> updateSiteRoles(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> persistDataResourceAndData(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> persistDataResourceAndDataMethod(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>) `
- `public static void addRoleToUser(org.apache.ofbiz.entity.Delegator, org.apache.ofbiz.service.LocalDispatcher, java.util.Map<java.lang.String, java.lang.Object>) `
- `public static java.util.Map<java.lang.String, java.lang.Object> updateSiteRolesDyn(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> updateOrRemove(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> resequence(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>) `
- `public static java.util.Map<java.lang.String, java.lang.Object> changeLeafToNode(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>) `
- `public static java.util.Map<java.lang.String, java.lang.Object> updateLeafCount(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>) `
- `public static java.util.Map<java.lang.String, java.lang.Object> updatePageType(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>) `
- `public static java.util.Map<java.lang.String, java.lang.Object> resetToOutlineMode(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>) `
- *(... 15 weitere Methoden)*

### `ContentManagementWorker` — class
Vollständiger Name: `org.apache.ofbiz.content.ContentManagementWorker`
- `public static void mruAdd(javax.servlet.http.HttpServletRequest, org.apache.ofbiz.entity.GenericEntity, java.lang.String);`
- `public static void mruAdd(javax.servlet.http.HttpServletRequest, org.apache.ofbiz.entity.GenericEntity);`
- `public static void mruAdd(javax.servlet.http.HttpSession, org.apache.ofbiz.entity.GenericEntity);`
- `public static void mruAddByEntityName(java.lang.String, org.apache.ofbiz.entity.GenericEntity, java.util.Map<java.lang.String, org.apache.ofbiz.base.util.collections.LifoSet<java.lang.Object>>);`
- `public static java.util.Iterator<java.lang.Object> mostRecentlyViewedIterator(java.lang.String, java.util.Map<java.lang.String, org.apache.ofbiz.base.util.collections.LifoSet<java.lang.Object>>);`
- `public static java.lang.String buildPKSig(org.apache.ofbiz.entity.GenericEntity, java.lang.String);`
- `public static void setCurrentEntityMap(javax.servlet.http.HttpServletRequest, org.apache.ofbiz.entity.GenericEntity);`
- `public static void setCurrentEntityMap(javax.servlet.http.HttpServletRequest, java.lang.String, org.apache.ofbiz.entity.GenericEntity);`
- `public static java.lang.String getFromSomewhere(java.lang.String, java.util.Map<java.lang.String, java.lang.Object>, javax.servlet.http.HttpServletRequest, java.util.Map<java.lang.String, java.lang.Object>);`
- `public static void getCurrentValue(javax.servlet.http.HttpServletRequest, org.apache.ofbiz.entity.Delegator);`
- `public static void getCurrentValueWithCachedPK(javax.servlet.http.HttpServletRequest, org.apache.ofbiz.entity.Delegator, org.apache.ofbiz.entity.GenericPK, java.lang.String);`
- `public static java.util.List<java.lang.String[]> getPermittedPublishPoints(org.apache.ofbiz.entity.Delegator, java.util.List<org.apache.ofbiz.entity.GenericValue>, org.apache.ofbiz.entity.GenericValue, org.apache.ofbiz.security.Security, java.lang.String, java.lang.String, java.lang.String) `
- `public static java.util.List<org.apache.ofbiz.entity.GenericValue> getAllPublishPoints(org.apache.ofbiz.entity.Delegator, java.lang.String) `
- `public static java.util.Map<java.lang.String, org.apache.ofbiz.entity.GenericValue> getPublishPointMap(org.apache.ofbiz.entity.Delegator, java.lang.String) `
- `public static void getAllPublishPointMap(org.apache.ofbiz.entity.Delegator, java.lang.String, java.util.Map<java.lang.String, org.apache.ofbiz.entity.GenericValue>) `
- *(... 15 weitere Methoden)*

### `PermissionRecorder` — class
Vollständiger Name: `org.apache.ofbiz.content.content.PermissionRecorder`
- `public org.apache.ofbiz.content.content.PermissionRecorder();`
- `public int getCheckMode();`
- `public void setCheckMode(int);`
- `public boolean isOn();`
- `public void setOn(boolean);`
- `public org.apache.ofbiz.entity.GenericValue getUserLogin();`
- `public void setUserLogin(org.apache.ofbiz.entity.GenericValue);`
- `public boolean getEntityPermCheckResult();`
- `public void setEntityPermCheckResult(boolean);`
- `public org.apache.ofbiz.entity.GenericValue[] getContentPurposeOperations();`
- `public void setContentPurposeOperations(java.util.List<org.apache.ofbiz.entity.GenericValue>);`
- `public java.lang.String getPrivilegeEnumId();`
- `public void setPrivilegeEnumId(java.lang.String);`
- `public java.lang.String[] getStatusTargets();`
- `public void setStatusTargets(java.util.List<java.lang.String>);`
- *(... 11 weitere Methoden)*

### `DataServices` — class
Vollständiger Name: `org.apache.ofbiz.content.data.DataServices`
- `public org.apache.ofbiz.content.data.DataServices();`
- `public static java.util.Map<java.lang.String, java.lang.Object> clearAssociatedRenderCache(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> createDataResourceAndText(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> createDataResource(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> createDataResourceMethod(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> createElectronicText(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> createElectronicTextMethod(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> createFile(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> createFileNoPerm(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>) `
- `public static java.util.Map<java.lang.String, java.lang.Object> createFileMethod(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> updateDataResourceAndText(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> updateDataResource(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> updateDataResourceMethod(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> updateElectronicText(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> updateElectronicTextMethod(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- *(... 11 weitere Methoden)*

### `SurveyWrapper` — class
Vollständiger Name: `org.apache.ofbiz.content.survey.SurveyWrapper`
- `public void setDelegator(org.apache.ofbiz.entity.Delegator);`
- `public void setPartyId(java.lang.String);`
- `public void setSurveyId(java.lang.String);`
- `public org.apache.ofbiz.content.survey.SurveyWrapper(org.apache.ofbiz.entity.Delegator, java.lang.String, java.lang.String, java.lang.String, java.util.Map<java.lang.String, java.lang.Object>, java.util.Map<java.lang.String, java.lang.Object>);`
- `public org.apache.ofbiz.content.survey.SurveyWrapper(org.apache.ofbiz.entity.Delegator, java.lang.String, java.lang.String, java.lang.String, java.util.Map<java.lang.String, java.lang.Object>);`
- `public org.apache.ofbiz.content.survey.SurveyWrapper(org.apache.ofbiz.entity.Delegator, java.lang.String);`
- `public void setPassThru(java.util.Map<java.lang.String, java.lang.Object>);`
- `public void setDefaultValues(java.util.Map<java.lang.String, java.lang.Object>);`
- `public void addToTemplateContext(java.lang.String, java.lang.Object);`
- `public void removeFromTemplateContext(java.lang.String);`
- `public java.io.Writer render(java.lang.String) `
- `public void render(java.net.URL, java.io.Writer) `
- `public void setEdit(boolean);`
- `public org.apache.ofbiz.entity.GenericValue getSurvey();`
- `public java.lang.String getSurveyName();`
- *(... 9 weitere Methoden)*

### `ContentMapFacade` — class
Vollständiger Name: `org.apache.ofbiz.content.content.ContentMapFacade`
- `public org.apache.ofbiz.content.content.ContentMapFacade(org.apache.ofbiz.service.LocalDispatcher, org.apache.ofbiz.entity.GenericValue, java.util.Map<java.lang.String, java.lang.Object>, java.util.Locale, java.lang.String, boolean);`
- `public void setRenderFlag(boolean);`
- `public void setIsDecorated(boolean);`
- `public int size();`
- `public boolean isEmpty();`
- `public boolean containsKey(java.lang.Object);`
- `public boolean containsValue(java.lang.Object);`
- `public java.lang.Object put(java.lang.Object, java.lang.Object);`
- `public java.lang.Object remove(java.lang.Object);`
- `public void putAll(java.util.Map<?, ?>);`
- `public void clear();`
- `public java.util.Set<java.lang.Object> keySet();`
- `public java.util.Collection<java.lang.Object> values();`
- `public java.util.Set<java.util.Map$Entry<java.lang.Object, java.lang.Object>> entrySet();`
- `public void setSortOrder(java.lang.Object);`
- *(... 5 weitere Methoden)*

### `ContentPermissionServices` [Groovy] — class
Vollständiger Name: `org.apache.ofbiz.content.permission.ContentPermissionServices`
- `public org.apache.ofbiz.content.permission.ContentPermissionServices();`
- `public org.apache.ofbiz.content.permission.ContentPermissionServices(groovy.lang.Binding);`
- `public static void main(java.lang.String...);`
- `public java.lang.Object run();`
- `public java.util.Map contentManagerPermission();`
- `public java.util.Map contentManagerRolePermission();`
- `public java.util.Map genericContentPermission();`
- `public java.util.Map viewContentPermission(java.lang.Boolean, java.lang.String, java.lang.String, java.lang.String, java.lang.String, java.lang.String);`
- `public java.util.Map createContentPermission(java.lang.Boolean, java.lang.String, java.lang.String, java.lang.String, java.lang.String, java.lang.String, java.lang.String);`
- `public java.util.Map updateContentPermission(java.lang.Boolean, java.lang.String, java.lang.String, java.lang.String, java.lang.String, java.lang.String, java.lang.String);`
- `public java.util.Map checkContentOperationSecurity(java.lang.String, java.lang.String, java.lang.String, java.lang.String, java.lang.String);`
- `public java.util.Map checkOwnership();`
- `public java.util.Map checkRoleSecurity(java.lang.String, java.lang.String, java.lang.String, java.lang.String, java.lang.String);`
- `public java.util.Map findAllContentPurposes(java.lang.String);`
- `public java.util.Map findAllAssociatedPartyIds();`
- *(... 1 weitere Methoden)*

### `ContentServices` — class
Vollständiger Name: `org.apache.ofbiz.content.content.ContentServices`
- `public org.apache.ofbiz.content.content.ContentServices();`
- `public static java.util.Map<java.lang.String, java.lang.Object> findRelatedContent(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> findContentParents(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> traverseContent(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> deactivateContentAssoc(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> deactivateContentAssocMethod(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> deactivateAssocs(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> renderSubContentAsText(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> renderContentAsText(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> linkContentToPubPt(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> publishContent(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>) `
- `public static java.util.Map<java.lang.String, java.lang.Object> getPrefixedMembers(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>) `
- `public static java.util.Map<java.lang.String, java.lang.Object> splitString(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>) `
- `public static java.util.Map<java.lang.String, java.lang.Object> joinString(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>) `
- `public static java.util.Map<java.lang.String, java.lang.Object> urlEncodeArgs(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>) `

### `ContentSearchSession` — class
Vollständiger Name: `org.apache.ofbiz.content.content.ContentSearchSession`
- `public org.apache.ofbiz.content.content.ContentSearchSession();`
- `public static org.apache.ofbiz.content.content.ContentSearchSession$ContentSearchOptions getContentSearchOptions(javax.servlet.http.HttpSession);`
- `public static void processSearchParameters(java.util.Map<java.lang.String, java.lang.Object>, javax.servlet.http.HttpServletRequest);`
- `public static void searchAddConstraint(org.apache.ofbiz.content.content.ContentSearch$ContentSearchConstraint, javax.servlet.http.HttpSession);`
- `public static void searchSetSortOrder(org.apache.ofbiz.content.content.ContentSearch$ResultSortOrder, javax.servlet.http.HttpSession);`
- `public static java.util.List<org.apache.ofbiz.content.content.ContentSearchSession$ContentSearchOptions> getSearchOptionsHistoryList(javax.servlet.http.HttpSession);`
- `public static java.util.List<java.lang.String> searchGetConstraintStrings(boolean, javax.servlet.http.HttpSession, org.apache.ofbiz.entity.Delegator);`
- `public static java.lang.String searchGetSortOrderString(boolean, javax.servlet.http.HttpServletRequest);`
- `public static void checkSaveSearchOptionsHistory(javax.servlet.http.HttpSession);`
- `public static void searchRemoveConstraint(int, javax.servlet.http.HttpSession);`
- `public static void searchClear(javax.servlet.http.HttpSession);`

### `ContentTests` [Groovy] — class
Vollständiger Name: `org.apache.ofbiz.content.content.ContentTests`
- `public org.apache.ofbiz.content.content.ContentTests(java.lang.String);`
- `public void testGetDataResource();`
- `public void testCreateDataCategory();`
- `public void testUpdateDataCategory();`
- `public void testDeleteDataCategory();`
- `public void testCreateDataResourceRole();`
- `public void testUpdateDataResourceRole();`
- `public void testRemoveDataResourceRole();`
- `public void testGetContent();`
- `public groovy.lang.MetaClass getMetaClass();`
- `public void setMetaClass(groovy.lang.MetaClass);`

### `DataServicesScript` [Groovy] — class
Vollständiger Name: `org.apache.ofbiz.content.data.DataServicesScript`
- `public org.apache.ofbiz.content.data.DataServicesScript();`
- `public org.apache.ofbiz.content.data.DataServicesScript(groovy.lang.Binding);`
- `public static void main(java.lang.String...);`
- `public java.lang.Object run();`
- `public java.util.Map createDataResource();`
- `public java.util.Map createDataResourceAndAssocToContent();`
- `public java.util.Map getElectronicText();`
- `public java.util.Map attachUploadToDataResource();`
- `public java.util.Map saveLocalFileDataResource(java.lang.String);`
- `public java.util.Map saveExtFileDataResource(boolean, java.lang.String);`
- `public java.util.Map prepareServiceContext(org.apache.ofbiz.entity.GenericValue, java.lang.String);`

### `PdfSurveyServices` — class
Vollständiger Name: `org.apache.ofbiz.content.survey.PdfSurveyServices`
- `public org.apache.ofbiz.content.survey.PdfSurveyServices();`
- `public static java.util.Map<java.lang.String, java.lang.Object> buildSurveyFromPdf(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> buildSurveyResponseFromPdf(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> getAcroFieldsFromPdf(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> setAcroFields(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> buildPdfFromSurveyResponse(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> buildSurveyQuestionsAndAnswers(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> setAcroFieldsFromSurveyResponse(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public static java.nio.ByteBuffer getInputByteBuffer(java.util.Map<java.lang.String, ? extends java.lang.Object>, org.apache.ofbiz.entity.Delegator) `

### `BlogServices` [Groovy] — class
Vollständiger Name: `org.apache.ofbiz.content.BlogServices`
- `public org.apache.ofbiz.content.BlogServices();`
- `public org.apache.ofbiz.content.BlogServices(groovy.lang.Binding);`
- `public static void main(java.lang.String...);`
- `public java.lang.Object run();`
- `public java.util.Map createBlogEntry();`
- `public java.util.Map getBlogEntry();`
- `public java.util.Map updateBlogEntry();`
- `public java.util.Map getOwnedOrPublishedBlogEntries();`

### `LayoutEvents` — class
Vollständiger Name: `org.apache.ofbiz.content.layout.LayoutEvents`
- `public org.apache.ofbiz.content.layout.LayoutEvents();`
- `public static java.lang.String createLayoutImage(javax.servlet.http.HttpServletRequest, javax.servlet.http.HttpServletResponse);`
- `public static java.lang.String updateLayoutImage(javax.servlet.http.HttpServletRequest, javax.servlet.http.HttpServletResponse);`
- `public static java.lang.String replaceSubContent(javax.servlet.http.HttpServletRequest, javax.servlet.http.HttpServletResponse);`
- `public static java.lang.String cloneLayout(javax.servlet.http.HttpServletRequest, javax.servlet.http.HttpServletResponse);`
- `public static java.lang.String createLayoutSubContent(javax.servlet.http.HttpServletRequest, javax.servlet.http.HttpServletResponse);`
- `public static java.lang.String updateLayoutSubContent(javax.servlet.http.HttpServletRequest, javax.servlet.http.HttpServletResponse);`
- `public static java.lang.String copyToClip(javax.servlet.http.HttpServletRequest, javax.servlet.http.HttpServletResponse);`

### `SecureFtpClient` — class
Vollständiger Name: `org.apache.ofbiz.content.ftp.SecureFtpClient`
- `public org.apache.ofbiz.content.ftp.SecureFtpClient();`
- `public void connect(java.lang.String, java.lang.String, java.lang.String, java.lang.Long, java.lang.Long) `
- `public void copy(java.lang.String, java.lang.String, java.io.InputStream) `
- `public java.util.List<java.lang.String> list(java.lang.String) `
- `public void setBinaryTransfer(boolean) `
- `public void setPassiveMode(boolean) `
- `public void closeConnection();`

### `SimpleFtpClient` — class
Vollständiger Name: `org.apache.ofbiz.content.ftp.SimpleFtpClient`
- `public org.apache.ofbiz.content.ftp.SimpleFtpClient();`
- `public void connect(java.lang.String, java.lang.String, java.lang.String, java.lang.Long, java.lang.Long) `
- `public java.util.List<java.lang.String> list(java.lang.String) `
- `public void setBinaryTransfer(boolean) `
- `public void setPassiveMode(boolean);`
- `public void copy(java.lang.String, java.lang.String, java.io.InputStream) `
- `public void closeConnection() `

### `SshFtpClient` — class
Vollständiger Name: `org.apache.ofbiz.content.ftp.SshFtpClient`
- `public org.apache.ofbiz.content.ftp.SshFtpClient();`
- `public void connect(java.lang.String, java.lang.String, java.lang.String, java.lang.Long, java.lang.Long) `
- `public void copy(java.lang.String, java.lang.String, java.io.InputStream) `
- `public java.util.List<java.lang.String> list(java.lang.String) `
- `public void setBinaryTransfer(boolean) `
- `public void setPassiveMode(boolean) `
- `public void closeConnection() `

## Modul: datafile (9 Klassen, 121 public Methoden)

### `ModelRecord` — class
Vollständiger Name: `org.apache.ofbiz.datafile.ModelRecord`
- `public org.apache.ofbiz.datafile.ModelRecord();`
- `public java.lang.String getName();`
- `public void setName(java.lang.String);`
- `public java.lang.String getDescription();`
- `public void setDescription(java.lang.String);`
- `public java.lang.String getParentName();`
- `public void setParentName(java.lang.String);`
- `public java.util.List<org.apache.ofbiz.datafile.ModelField> getFields();`
- `public void setFields(java.util.List<org.apache.ofbiz.datafile.ModelField>);`
- `public java.lang.String getTypeCode();`
- `public int getTcPosition();`
- `public void setTypeCode(java.lang.String);`
- `public void setTcMin(java.lang.String);`
- `public void setTcMax(java.lang.String);`
- `public void setTcIsNum(boolean);`
- *(... 14 weitere Methoden)*

### `ModelDataFile` — class
Vollständiger Name: `org.apache.ofbiz.datafile.ModelDataFile`
- `public org.apache.ofbiz.datafile.ModelDataFile();`
- `public java.lang.String getTextDelimiter();`
- `public void setTextDelimiter(java.lang.String);`
- `public java.lang.String getName();`
- `public void setName(java.lang.String);`
- `public java.lang.String getTypeCode();`
- `public void setTypeCode(java.lang.String);`
- `public java.lang.String getSender();`
- `public void setSender(java.lang.String);`
- `public java.lang.String getReceiver();`
- `public void setReceiver(java.lang.String);`
- `public int getRecordLength();`
- `public void setRecordLength(int);`
- `public char getDelimiter();`
- `public void setDelimiter(char);`
- *(... 12 weitere Methoden)*

### `ModelField` — class
Vollständiger Name: `org.apache.ofbiz.datafile.ModelField`
- `public org.apache.ofbiz.datafile.ModelField();`
- `public java.lang.String getName();`
- `public void setName(java.lang.String);`
- `public int getPosition();`
- `public int getLength();`
- `public void setPosition(int);`
- `public void setLength(int);`
- `public void setType(java.lang.String);`
- `public java.lang.String getType();`
- `public void setFormat(java.lang.String);`
- `public java.lang.String getFormat();`
- `public void setValidExp(java.lang.String);`
- `public void setDescription(java.lang.String);`
- `public void setDefaultValue(java.lang.Object);`
- `public void setPk(boolean);`
- *(... 7 weitere Methoden)*

### `Record` — class
Vollständiger Name: `org.apache.ofbiz.datafile.Record`
- `public java.lang.String getRecordName();`
- `public org.apache.ofbiz.datafile.ModelRecord getModelRecord();`
- `public synchronized java.lang.Object get(java.lang.String);`
- `public java.lang.String getString(java.lang.String);`
- `public java.lang.String getStringAndEmpty(java.lang.String);`
- `public java.sql.Timestamp getTimestamp(java.lang.String);`
- `public java.sql.Time getTime(java.lang.String);`
- `public java.sql.Date getDate(java.lang.String);`
- `public java.lang.Integer getInteger(java.lang.String);`
- `public java.lang.Long getLong(java.lang.String);`
- `public java.lang.Float getFloat(java.lang.String);`
- `public java.lang.Double getDouble(java.lang.String);`
- `public void set(java.lang.String, java.lang.Object);`
- `public synchronized void set(java.lang.String, java.lang.Object, boolean);`
- `public void setString(java.lang.String, java.lang.String) `
- *(... 6 weitere Methoden)*

### `DataFile` — class
Vollständiger Name: `org.apache.ofbiz.datafile.DataFile`
- `public static org.apache.ofbiz.datafile.DataFile makeDataFile(java.net.URL, java.lang.String) `
- `public org.apache.ofbiz.datafile.DataFile(org.apache.ofbiz.datafile.ModelDataFile);`
- `public java.util.List<org.apache.ofbiz.datafile.Record> getRecords();`
- `public void addRecord(org.apache.ofbiz.datafile.Record);`
- `public org.apache.ofbiz.datafile.Record makeRecord(java.lang.String);`
- `public void readDataFile(java.lang.String) `
- `public org.apache.ofbiz.datafile.RecordIterator makeRecordIterator(java.net.URL) `
- `public void writeDataFile(java.lang.String) `
- `public java.lang.String writeDataFile() `
- `public void writeDataFile(java.io.OutputStream) `

### `RecordIterator` — class
Vollständiger Name: `org.apache.ofbiz.datafile.RecordIterator`
- `public org.apache.ofbiz.datafile.RecordIterator(java.net.URL, org.apache.ofbiz.datafile.ModelDataFile) `
- `public org.apache.ofbiz.datafile.RecordIterator(java.io.InputStream, org.apache.ofbiz.datafile.ModelDataFile, java.lang.String) `
- `public boolean hasNext();`
- `public org.apache.ofbiz.datafile.Record next() `
- `public void close() `

### `DataFile2EntityXml` — class
Vollständiger Name: `org.apache.ofbiz.datafile.DataFile2EntityXml`
- `public org.apache.ofbiz.datafile.DataFile2EntityXml();`
- `public static void writeToEntityXml(java.lang.String, org.apache.ofbiz.datafile.DataFile) `
- `public static void main(java.lang.String[]) `

### `ModelDataFileReader` — class
Vollständiger Name: `org.apache.ofbiz.datafile.ModelDataFileReader`
- `public java.util.Collection<java.lang.String> getDataFileNames();`
- `public java.util.Iterator<java.lang.String> getDataFileNamesIterator();`
- `public java.util.Map<java.lang.String, org.apache.ofbiz.datafile.ModelDataFile> getModelDataFiles();`

### `DataFileException` — class
Vollständiger Name: `org.apache.ofbiz.datafile.DataFileException`
- `public org.apache.ofbiz.datafile.DataFileException();`

## Modul: entity (146 Klassen, 1861 public Methoden)

### `ModelEntity` — class
Vollständiger Name: `org.apache.ofbiz.entity.model.ModelEntity`
- `public org.apache.ofbiz.entity.model.ModelEntity();`
- `public org.apache.ofbiz.entity.model.ModelEntity(org.apache.ofbiz.entity.model.ModelReader, org.w3c.dom.Element, org.apache.ofbiz.base.util.UtilTimer, org.apache.ofbiz.entity.model.ModelInfo);`
- `public org.apache.ofbiz.entity.model.ModelEntity(java.lang.String, java.util.Map<java.lang.String, org.apache.ofbiz.entity.jdbc.DatabaseUtil$ColumnCheckInfo>, org.apache.ofbiz.entity.model.ModelFieldTypeReader, boolean);`
- `public org.apache.ofbiz.entity.model.ModelEntity(java.lang.String, java.util.Map<java.lang.String, org.apache.ofbiz.entity.jdbc.DatabaseUtil$ColumnCheckInfo>, java.util.Map<java.lang.String, org.apache.ofbiz.entity.jdbc.DatabaseUtil$ReferenceCheckInfo>, org.apache.ofbiz.entity.model.ModelFieldTypeReader, boolean);`
- `public boolean containsAllPkFieldNames(java.util.Set<java.lang.String>);`
- `public void addExtendEntity(org.apache.ofbiz.entity.model.ModelReader, org.w3c.dom.Element);`
- `public org.apache.ofbiz.entity.model.ModelReader getModelReader();`
- `public java.lang.String getEntityName();`
- `public void setEntityName(java.lang.String);`
- `public java.lang.String getPlainTableName();`
- `public java.lang.String getTableName(java.lang.String);`
- `public java.lang.String getTableName(org.apache.ofbiz.entity.config.model.Datasource);`
- `public void setTableName(java.lang.String);`
- `public java.lang.String getPackageName();`
- `public void setPackageName(java.lang.String);`
- *(... 130 weitere Methoden)*

### `GenericDelegator` — class
Vollständiger Name: `org.apache.ofbiz.entity.GenericDelegator`
- `public static void pushUserIdentifier(java.lang.String);`
- `public static java.lang.String popUserIdentifier();`
- `public static void clearUserIdentifierStack();`
- `public static void pushSessionIdentifier(java.lang.String);`
- `public static java.lang.String popSessionIdentifier();`
- `public static void clearSessionIdentifierStack();`
- `public synchronized void initEntityEcaHandler();`
- `public java.lang.String getDelegatorName();`
- `public java.lang.String getDelegatorBaseName();`
- `public java.lang.String getDelegatorTenantId();`
- `public java.lang.String getOriginalDelegatorName();`
- `public org.apache.ofbiz.entity.model.ModelReader getModelReader();`
- `public org.apache.ofbiz.entity.model.ModelGroupReader getModelGroupReader();`
- `public org.apache.ofbiz.entity.model.ModelEntity getModelEntity(java.lang.String);`
- `public java.lang.String getEntityGroupName(java.lang.String);`
- *(... 99 weitere Methoden)*

### `Delegator` — interface
Vollständiger Name: `org.apache.ofbiz.entity.Delegator`
- `public abstract void clearAllCacheLinesByDummyPK(java.util.Collection<org.apache.ofbiz.entity.GenericPK>);`
- `public abstract void clearAllCacheLinesByValue(java.util.Collection<org.apache.ofbiz.entity.GenericValue>);`
- `public abstract void clearAllCaches();`
- `public abstract void clearAllCaches(boolean);`
- `public abstract void clearCacheLine(org.apache.ofbiz.entity.GenericPK);`
- `public abstract void clearCacheLine(org.apache.ofbiz.entity.GenericPK, boolean);`
- `public abstract void clearCacheLine(org.apache.ofbiz.entity.GenericValue);`
- `public abstract void clearCacheLine(org.apache.ofbiz.entity.GenericValue, boolean);`
- `public abstract void clearCacheLine(java.lang.String);`
- `public abstract void clearCacheLine(java.lang.String, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public abstract void clearCacheLine(java.lang.String, java.lang.Object...);`
- `public abstract void clearCacheLineByCondition(java.lang.String, org.apache.ofbiz.entity.condition.EntityCondition);`
- `public abstract void clearCacheLineByCondition(java.lang.String, org.apache.ofbiz.entity.condition.EntityCondition, boolean);`
- `public abstract void clearCacheLineFlexible(org.apache.ofbiz.entity.GenericEntity);`
- `public abstract void clearCacheLineFlexible(org.apache.ofbiz.entity.GenericEntity, boolean);`
- *(... 93 weitere Methoden)*

### `GenericEntity` — class
Vollständiger Name: `org.apache.ofbiz.entity.GenericEntity`
- `public static org.apache.ofbiz.entity.GenericEntity createGenericEntity(org.apache.ofbiz.entity.model.ModelEntity);`
- `public static org.apache.ofbiz.entity.GenericEntity createGenericEntity(org.apache.ofbiz.entity.Delegator, org.apache.ofbiz.entity.model.ModelEntity, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public static org.apache.ofbiz.entity.GenericEntity createGenericEntity(org.apache.ofbiz.entity.GenericEntity);`
- `public void reset();`
- `public void refreshFromValue(org.apache.ofbiz.entity.GenericEntity) `
- `public boolean isModified();`
- `public void synchronizedWithDatasource();`
- `public void removedFromDatasource();`
- `public boolean isMutable();`
- `public void setImmutable();`
- `public boolean getIsFromEntitySync();`
- `public void setIsFromEntitySync(boolean);`
- `public java.lang.String getEntityName();`
- `public org.apache.ofbiz.entity.model.ModelEntity getModelEntity();`
- `public org.apache.ofbiz.entity.Delegator getDelegator();`
- *(... 78 weitere Methoden)*

### `DatabaseUtil` — class
Vollständiger Name: `org.apache.ofbiz.entity.jdbc.DatabaseUtil`
- `public org.apache.ofbiz.entity.jdbc.DatabaseUtil(org.apache.ofbiz.entity.datasource.GenericHelperInfo);`
- `public org.apache.ofbiz.entity.config.model.Datasource getDatasource();`
- `public void checkDb(java.util.Map<java.lang.String, org.apache.ofbiz.entity.model.ModelEntity>, java.util.List<java.lang.String>, boolean);`
- `public void checkDb(java.util.Map<java.lang.String, org.apache.ofbiz.entity.model.ModelEntity>, java.util.List<java.lang.String>, java.util.List<java.lang.String>, boolean, boolean, boolean, boolean);`
- `public java.util.List<org.apache.ofbiz.entity.model.ModelEntity> induceModelFromDb(java.util.Collection<java.lang.String>);`
- `public java.sql.DatabaseMetaData getDatabaseMetaData(java.sql.Connection, java.util.Collection<java.lang.String>);`
- `public void printDbMiscData(java.sql.DatabaseMetaData, java.sql.Connection);`
- `public java.util.TreeSet<java.lang.String> getTableNames(java.util.Collection<java.lang.String>);`
- `public int checkPrimaryKeyInfo(java.sql.ResultSet, java.lang.String, boolean, java.util.Map<java.lang.String, java.util.Map<java.lang.String, org.apache.ofbiz.entity.jdbc.DatabaseUtil$ColumnCheckInfo>>, java.util.Collection<java.lang.String>) `
- `public java.util.Map<java.lang.String, java.util.Map<java.lang.String, org.apache.ofbiz.entity.jdbc.DatabaseUtil$ReferenceCheckInfo>> getReferenceInfo(java.util.Set<java.lang.String>, java.util.Collection<java.lang.String>);`
- `public java.util.Map<java.lang.String, java.util.Set<java.lang.String>> getIndexInfo(java.util.Set<java.lang.String>, java.util.Collection<java.lang.String>, boolean[]);`
- `public java.lang.String createTable(org.apache.ofbiz.entity.model.ModelEntity, java.util.Map<java.lang.String, org.apache.ofbiz.entity.model.ModelEntity>, boolean);`
- `public void deleteTable(org.apache.ofbiz.entity.model.ModelEntity, java.util.List<java.lang.String>);`
- `public java.lang.String addColumn(org.apache.ofbiz.entity.model.ModelEntity, org.apache.ofbiz.entity.model.ModelField);`
- `public java.lang.String renameColumn(org.apache.ofbiz.entity.model.ModelEntity, org.apache.ofbiz.entity.model.ModelField, java.lang.String);`
- *(... 35 weitere Methoden)*

### `EntityUtilProperties` — class
Vollständiger Name: `org.apache.ofbiz.entity.util.EntityUtilProperties`
- `public static boolean propertyValueEquals(java.lang.String, java.lang.String, java.lang.String);`
- `public static boolean propertyValueEqualsIgnoreCase(java.lang.String, java.lang.String, java.lang.String, org.apache.ofbiz.entity.Delegator);`
- `public static java.lang.String getPropertyValue(java.lang.String, java.lang.String, java.lang.String, org.apache.ofbiz.entity.Delegator);`
- `public static java.lang.String getPropertyValueFromDelegatorName(java.lang.String, java.lang.String, java.lang.String, java.lang.String);`
- `public static double getPropertyNumber(java.lang.String, java.lang.String, double);`
- `public static double getPropertyNumber(java.lang.String, java.lang.String);`
- `public static java.lang.Boolean getPropertyAsBoolean(java.lang.String, java.lang.String, boolean);`
- `public static java.lang.Integer getPropertyAsInteger(java.lang.String, java.lang.String, int);`
- `public static java.lang.Long getPropertyAsLong(java.lang.String, java.lang.String, long);`
- `public static java.lang.Float getPropertyAsFloat(java.lang.String, java.lang.String, float);`
- `public static java.lang.Double getPropertyAsDouble(java.lang.String, java.lang.String, double);`
- `public static java.math.BigInteger getPropertyAsBigInteger(java.lang.String, java.lang.String, java.math.BigInteger);`
- `public static java.math.BigDecimal getPropertyAsBigDecimal(java.lang.String, java.lang.String, java.math.BigDecimal);`
- `public static java.lang.String getPropertyValue(java.lang.String, java.lang.String, org.apache.ofbiz.entity.Delegator);`
- `public static java.lang.String getPropertyValueFromDelegatorName(java.lang.String, java.lang.String, java.lang.String);`
- *(... 30 weitere Methoden)*

### `EntityUtil` — class
Vollständiger Name: `org.apache.ofbiz.entity.util.EntityUtil`
- `public static <V> java.util.Map<java.lang.String, V> makeFields(V...);`
- `public static org.apache.ofbiz.entity.GenericValue getFirst(java.util.Collection<org.apache.ofbiz.entity.GenericValue>);`
- `public static org.apache.ofbiz.entity.GenericValue getFirst(java.util.List<org.apache.ofbiz.entity.GenericValue>);`
- `public static org.apache.ofbiz.entity.GenericValue getOnly(java.util.Collection<org.apache.ofbiz.entity.GenericValue>);`
- `public static org.apache.ofbiz.entity.GenericValue getOnly(java.util.List<org.apache.ofbiz.entity.GenericValue>);`
- `public static org.apache.ofbiz.entity.condition.EntityCondition getFilterByDateExpr();`
- `public static org.apache.ofbiz.entity.condition.EntityCondition getFilterByDateExpr(java.lang.String, java.lang.String);`
- `public static org.apache.ofbiz.entity.condition.EntityCondition getFilterByDateExpr(java.util.Date);`
- `public static org.apache.ofbiz.entity.condition.EntityCondition getFilterByDateExpr(java.sql.Timestamp);`
- `public static org.apache.ofbiz.entity.condition.EntityCondition getFilterByDateExpr(java.sql.Timestamp, java.lang.String, java.lang.String);`
- `public static <T extends org.apache.ofbiz.entity.GenericEntity> java.util.List<T> filterByDate(java.util.List<T>);`
- `public static <T extends org.apache.ofbiz.entity.GenericEntity> java.util.List<T> filterByDate(java.util.List<T>, boolean);`
- `public static <T extends org.apache.ofbiz.entity.GenericEntity> java.util.List<T> filterByDate(java.util.List<T>, java.util.Date);`
- `public static <T extends org.apache.ofbiz.entity.GenericEntity> java.util.List<T> filterByDate(java.util.List<T>, java.sql.Timestamp);`
- `public static <T extends org.apache.ofbiz.entity.GenericEntity> java.util.List<T> filterByDate(java.util.List<T>, java.sql.Timestamp, java.lang.String, java.lang.String, boolean);`
- *(... 26 weitere Methoden)*

### `EntityQuery` — class
Vollständiger Name: `org.apache.ofbiz.entity.util.EntityQuery`
- `public static org.apache.ofbiz.entity.util.EntityQuery use(org.apache.ofbiz.entity.Delegator);`
- `public org.apache.ofbiz.entity.util.EntityQuery(org.apache.ofbiz.entity.Delegator);`
- `public org.apache.ofbiz.entity.util.EntityQuery select(java.util.Set<java.lang.String>);`
- `public org.apache.ofbiz.entity.util.EntityQuery select(java.lang.String...);`
- `public org.apache.ofbiz.entity.util.EntityQuery from(java.lang.String);`
- `public org.apache.ofbiz.entity.util.EntityQuery from(org.apache.ofbiz.entity.model.DynamicViewEntity);`
- `public org.apache.ofbiz.entity.util.EntityQuery where(org.apache.ofbiz.entity.condition.EntityCondition);`
- `public org.apache.ofbiz.entity.util.EntityQuery where(java.util.Map<java.lang.String, java.lang.Object>);`
- `public org.apache.ofbiz.entity.util.EntityQuery where(java.lang.Object...);`
- `public org.apache.ofbiz.entity.util.EntityQuery where(org.apache.ofbiz.entity.condition.EntityCondition...);`
- `public <T extends org.apache.ofbiz.entity.condition.EntityCondition> org.apache.ofbiz.entity.util.EntityQuery where(java.util.List<T>);`
- `public org.apache.ofbiz.entity.util.EntityQuery having(org.apache.ofbiz.entity.condition.EntityCondition);`
- `public org.apache.ofbiz.entity.util.EntityQuery orderBy(java.util.List<java.lang.String>);`
- `public org.apache.ofbiz.entity.util.EntityQuery orderBy(java.lang.String...);`
- `public org.apache.ofbiz.entity.util.EntityQuery cursorForwardOnly();`
- *(... 25 weitere Methoden)*

### `Datasource` — class
Vollständiger Name: `org.apache.ofbiz.entity.config.model.Datasource`
- `public java.lang.String getName();`
- `public java.lang.String getHelperClass();`
- `public java.lang.String getFieldTypeName();`
- `public boolean getUseSchemas();`
- `public java.lang.String getSchemaName();`
- `public boolean getCheckOnStart();`
- `public boolean getAddMissingOnStart();`
- `public boolean getUsePkConstraintNames();`
- `public boolean getCheckPksOnStart();`
- `public int getConstraintNameClipLength();`
- `public boolean getUseProxyCursor();`
- `public java.lang.String getProxyCursorName();`
- `public int getResultFetchSize();`
- `public boolean getUseForeignKeys();`
- `public boolean getUseForeignKeyIndices();`
- *(... 23 weitere Methoden)*

### `TransactionUtil` — class
Vollständiger Name: `org.apache.ofbiz.entity.transaction.TransactionUtil`
- `public static <V> V doNewTransaction(java.util.concurrent.Callable<V>, java.lang.String, int, boolean) `
- `public static <V> V doTransaction(java.util.concurrent.Callable<V>, java.lang.String, int, boolean) `
- `public static <V> org.apache.ofbiz.entity.transaction.TransactionUtil$NoTransaction<V> noTransaction(java.util.concurrent.Callable<V>);`
- `public static <V> org.apache.ofbiz.entity.transaction.TransactionUtil$InTransaction<V> inTransaction(java.util.concurrent.Callable<V>, java.lang.String, int, boolean);`
- `public static boolean begin() `
- `public static boolean begin(int) `
- `public static int getStatus() `
- `public static java.lang.String getStatusString() `
- `public static boolean isTransactionInPlace() `
- `public static void commit(boolean) `
- `public static void commit() `
- `public static void rollback(boolean, java.lang.String, java.lang.Throwable) `
- `public static void rollback() `
- `public static void rollback(java.lang.Throwable) `
- `public static void setRollbackOnly(java.lang.String, java.lang.Throwable) `
- *(... 22 weitere Methoden)*

### `ModelViewEntity` — class
Vollständiger Name: `org.apache.ofbiz.entity.model.ModelViewEntity`
- `public org.apache.ofbiz.entity.model.ModelViewEntity(org.apache.ofbiz.entity.model.ModelReader, org.w3c.dom.Element, org.apache.ofbiz.base.util.UtilTimer, org.apache.ofbiz.entity.model.ModelInfo);`
- `public org.apache.ofbiz.entity.model.ModelViewEntity(org.apache.ofbiz.entity.model.DynamicViewEntity, org.apache.ofbiz.entity.model.ModelReader);`
- `public java.util.Map<java.lang.String, org.apache.ofbiz.entity.model.ModelViewEntity$ModelMemberEntity> getMemberModelMemberEntities();`
- `public java.util.List<org.apache.ofbiz.entity.model.ModelViewEntity$ModelMemberEntity> getAllModelMemberEntities();`
- `public org.apache.ofbiz.entity.model.ModelViewEntity$ModelMemberEntity getMemberModelMemberEntity(java.lang.String);`
- `public org.apache.ofbiz.entity.model.ModelEntity getMemberModelEntity(java.lang.String);`
- `public void addMemberModelMemberEntity(org.apache.ofbiz.entity.model.ModelViewEntity$ModelMemberEntity);`
- `public void removeMemberModelMemberEntity(java.lang.String);`
- `public java.lang.String getColNameOrAlias(java.lang.String);`
- `public org.apache.ofbiz.entity.model.ModelViewEntity$ModelAlias getAlias(int);`
- `public org.apache.ofbiz.entity.model.ModelViewEntity$ModelAlias getAlias(java.lang.String);`
- `public int getAliasesSize();`
- `public java.util.Iterator<org.apache.ofbiz.entity.model.ModelViewEntity$ModelAlias> getAliasesIterator();`
- `public java.util.List<org.apache.ofbiz.entity.model.ModelViewEntity$ModelAlias> getAliasesCopy();`
- `public int getGroupBysSize();`
- *(... 20 weitere Methoden)*

### `SQLProcessor` — class
Vollständiger Name: `org.apache.ofbiz.entity.jdbc.SQLProcessor`
- `public org.apache.ofbiz.entity.jdbc.SQLProcessor(org.apache.ofbiz.entity.Delegator, org.apache.ofbiz.entity.datasource.GenericHelperInfo);`
- `public org.apache.ofbiz.entity.jdbc.SQLProcessor(org.apache.ofbiz.entity.Delegator, org.apache.ofbiz.entity.datasource.GenericHelperInfo, java.sql.Connection);`
- `public org.apache.ofbiz.entity.Delegator getDelegator();`
- `public void commit() `
- `public void rollback() `
- `public void close() `
- `public java.sql.Connection getConnection() `
- `public void prepareStatement(java.lang.String) `
- `public void prepareStatement(java.lang.String, boolean, int, int) `
- `public void prepareStatement(java.lang.String, boolean, int, int, int, int) `
- `public java.sql.ResultSet executeQuery() `
- `public java.sql.ResultSet executeQuery(java.lang.String) `
- `public int executeUpdate() `
- `public int executeUpdate(java.lang.String) `
- `public boolean next() `
- *(... 19 weitere Methoden)*

### `DynamicViewEntity` — class
Vollständiger Name: `org.apache.ofbiz.entity.model.DynamicViewEntity`
- `public org.apache.ofbiz.entity.model.DynamicViewEntity();`
- `public org.apache.ofbiz.entity.model.ModelViewEntity makeModelViewEntity(org.apache.ofbiz.entity.Delegator);`
- `public java.lang.String getViewXml(java.lang.String) `
- `public org.w3c.dom.Element getViewElement(org.w3c.dom.Document, java.lang.String);`
- `public java.lang.String getOneRealEntityName();`
- `public java.lang.String getEntityName();`
- `public void setEntityName(java.lang.String);`
- `public java.lang.String getPackageName();`
- `public void setPackageName(java.lang.String);`
- `public java.lang.String getDefaultResourceName();`
- `public void setDefaultResourceName(java.lang.String);`
- `public java.lang.String getTitle();`
- `public void setTitle(java.lang.String);`
- `public void addMemberEntity(java.lang.String, java.lang.String);`
- `public java.util.Iterator<java.util.Map$Entry<java.lang.String, org.apache.ofbiz.entity.model.ModelViewEntity$ModelMemberEntity>> getModelMemberEntitiesEntryIter();`
- *(... 19 weitere Methoden)*

### `EntityTestSuite` — class
Vollständiger Name: `org.apache.ofbiz.entity.test.EntityTestSuite`
- `public org.apache.ofbiz.entity.test.EntityTestSuite(java.lang.String);`
- `public void testModels() `
- `public void testMakeValue() `
- `public void testUpdateValue() `
- `public void testRemoveValue() `
- `public void testEntityCache() `
- `public void testXmlSerialization() `
- `public void testCreateTree() `
- `public void testAddMembersToTree() `
- `public void testCountViews() `
- `public void testFindDistinct() `
- `public void testNotLike() `
- `public void testForeignKeyCreate();`
- `public void testForeignKeyRemove() `
- `public void testRemoveNodeMemberAndTesting() `
- *(... 19 weitere Methoden)*

### `EntityListIterator` — class
Vollständiger Name: `org.apache.ofbiz.entity.util.EntityListIterator`
- `public org.apache.ofbiz.entity.util.EntityListIterator(org.apache.ofbiz.entity.jdbc.SQLProcessor, org.apache.ofbiz.entity.model.ModelEntity, java.util.List<org.apache.ofbiz.entity.model.ModelField>, org.apache.ofbiz.entity.model.ModelFieldTypeReader);`
- `public org.apache.ofbiz.entity.util.EntityListIterator(org.apache.ofbiz.entity.jdbc.SQLProcessor, org.apache.ofbiz.entity.model.ModelEntity, java.util.List<org.apache.ofbiz.entity.model.ModelField>, org.apache.ofbiz.entity.model.ModelFieldTypeReader, org.apache.ofbiz.entity.datasource.GenericDAO, org.apache.ofbiz.entity.condition.EntityCondition, org.apache.ofbiz.entity.condition.EntityCondition, boolean);`
- `public org.apache.ofbiz.entity.util.EntityListIterator(java.sql.ResultSet, org.apache.ofbiz.entity.model.ModelEntity, java.util.List<org.apache.ofbiz.entity.model.ModelField>, org.apache.ofbiz.entity.model.ModelFieldTypeReader);`
- `public void setDelegator(org.apache.ofbiz.entity.Delegator);`
- `public void afterLast() `
- `public void beforeFirst() `
- `public boolean last() `
- `public boolean first() `
- `public void close() `
- `public org.apache.ofbiz.entity.GenericValue currentGenericValue() `
- `public int currentIndex() `
- `public boolean absolute(int) `
- `public boolean relative(int) `
- `public boolean hasNext();`
- `public boolean hasPrevious();`
- *(... 15 weitere Methoden)*

### `GenericValue` — class
Vollständiger Name: `org.apache.ofbiz.entity.GenericValue`
- `public org.apache.ofbiz.entity.GenericValue();`
- `public static org.apache.ofbiz.entity.GenericValue create(org.apache.ofbiz.entity.model.ModelEntity);`
- `public static org.apache.ofbiz.entity.GenericValue create(org.apache.ofbiz.entity.Delegator, org.apache.ofbiz.entity.model.ModelEntity, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public static org.apache.ofbiz.entity.GenericValue create(org.apache.ofbiz.entity.Delegator, org.apache.ofbiz.entity.model.ModelEntity, java.lang.Object);`
- `public static org.apache.ofbiz.entity.GenericValue create(org.apache.ofbiz.entity.GenericValue);`
- `public static org.apache.ofbiz.entity.GenericValue create(org.apache.ofbiz.entity.GenericPK);`
- `public org.apache.ofbiz.entity.GenericValue create() `
- `public void store() `
- `public void remove() `
- `public void refresh() `
- `public void refreshFromCache() `
- `public java.util.List<org.apache.ofbiz.entity.GenericValue> getRelated(java.lang.String) `
- `public java.util.List<org.apache.ofbiz.entity.GenericValue> getRelated(java.lang.String, java.util.List<java.lang.String>) `
- `public java.util.List<org.apache.ofbiz.entity.GenericValue> getRelated(java.lang.String, java.util.Map<java.lang.String, ? extends java.lang.Object>, java.util.List<java.lang.String>) `
- `public java.util.List<org.apache.ofbiz.entity.GenericValue> getRelated(java.lang.String, java.util.Map<java.lang.String, ? extends java.lang.Object>, java.util.List<java.lang.String>, boolean) `
- *(... 11 weitere Methoden)*

### `EntityConfig` — class
Vollständiger Name: `org.apache.ofbiz.entity.config.model.EntityConfig`
- `public static org.apache.ofbiz.entity.config.model.EntityConfig getInstance() `
- `public static java.lang.String createConfigFileLineNumberText(org.w3c.dom.Element);`
- `public org.apache.ofbiz.entity.config.model.ResourceLoader getResourceLoader(java.lang.String);`
- `public java.util.List<org.apache.ofbiz.entity.config.model.ResourceLoader> getResourceLoaderList();`
- `public org.apache.ofbiz.entity.config.model.TransactionFactory getTransactionFactory();`
- `public org.apache.ofbiz.entity.config.model.ConnectionFactory getConnectionFactory();`
- `public org.apache.ofbiz.entity.config.model.DebugXaResources getDebugXaResources();`
- `public org.apache.ofbiz.entity.config.model.DelegatorElement getDelegator(java.lang.String);`
- `public java.util.List<org.apache.ofbiz.entity.config.model.DelegatorElement> getDelegatorList();`
- `public org.apache.ofbiz.entity.config.model.EntityModelReader getEntityModelReader(java.lang.String);`
- `public java.util.List<org.apache.ofbiz.entity.config.model.EntityModelReader> getEntityModelReaderList();`
- `public org.apache.ofbiz.entity.config.model.EntityGroupReader getEntityGroupReader(java.lang.String);`
- `public java.util.List<org.apache.ofbiz.entity.config.model.EntityGroupReader> getEntityGroupReaderList();`
- `public org.apache.ofbiz.entity.config.model.EntityEcaReader getEntityEcaReader(java.lang.String);`
- `public java.util.List<org.apache.ofbiz.entity.config.model.EntityEcaReader> getEntityEcaReaderList();`
- *(... 8 weitere Methoden)*

### `EntityCondition` — interface
Vollständiger Name: `org.apache.ofbiz.entity.condition.EntityCondition`
- `public static <L, R, LL, RR> org.apache.ofbiz.entity.condition.EntityExpr makeCondition(L, org.apache.ofbiz.entity.condition.EntityComparisonOperator<LL, RR>, R);`
- `public static <R> org.apache.ofbiz.entity.condition.EntityExpr makeCondition(java.lang.String, R);`
- `public static org.apache.ofbiz.entity.condition.EntityExpr makeCondition(org.apache.ofbiz.entity.condition.EntityCondition, org.apache.ofbiz.entity.condition.EntityJoinOperator, org.apache.ofbiz.entity.condition.EntityCondition);`
- `public static <R extends org.apache.ofbiz.entity.condition.EntityCondition, T extends R> org.apache.ofbiz.entity.condition.EntityConditionList<R> makeCondition(org.apache.ofbiz.entity.condition.EntityJoinOperator, T...);`
- `public static <R extends org.apache.ofbiz.entity.condition.EntityCondition, T extends R> org.apache.ofbiz.entity.condition.EntityConditionList<R> makeCondition(T...);`
- `public static <T extends org.apache.ofbiz.entity.condition.EntityCondition> org.apache.ofbiz.entity.condition.EntityConditionList<T> makeCondition(java.util.List<? extends T>, org.apache.ofbiz.entity.condition.EntityJoinOperator);`
- `public static <T extends org.apache.ofbiz.entity.condition.EntityCondition> org.apache.ofbiz.entity.condition.EntityConditionList<T> makeCondition(java.util.List<? extends T>);`
- `public static <L, R> org.apache.ofbiz.entity.condition.EntityFieldMap makeCondition(java.util.Map<java.lang.String, ? extends java.lang.Object>, org.apache.ofbiz.entity.condition.EntityComparisonOperator<L, R>, org.apache.ofbiz.entity.condition.EntityJoinOperator);`
- `public static org.apache.ofbiz.entity.condition.EntityFieldMap makeCondition(java.util.Map<java.lang.String, ? extends java.lang.Object>, org.apache.ofbiz.entity.condition.EntityJoinOperator);`
- `public static org.apache.ofbiz.entity.condition.EntityFieldMap makeCondition(java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public static <L, R> org.apache.ofbiz.entity.condition.EntityFieldMap makeCondition(org.apache.ofbiz.entity.condition.EntityComparisonOperator<L, R>, org.apache.ofbiz.entity.condition.EntityJoinOperator, java.lang.Object...);`
- `public static org.apache.ofbiz.entity.condition.EntityFieldMap makeCondition(org.apache.ofbiz.entity.condition.EntityJoinOperator, java.lang.Object...);`
- `public static org.apache.ofbiz.entity.condition.EntityFieldMap makeConditionMap(java.lang.Object...);`
- `public static org.apache.ofbiz.entity.condition.EntityDateFilterCondition makeConditionDate(java.lang.String, java.lang.String);`
- `public static org.apache.ofbiz.entity.condition.EntityWhereString makeConditionWhere(java.lang.String);`
- *(... 7 weitere Methoden)*

### `SqlJdbcUtil` — class
Vollständiger Name: `org.apache.ofbiz.entity.jdbc.SqlJdbcUtil`
- `public static java.lang.String makeFromClause(org.apache.ofbiz.entity.model.ModelEntity, org.apache.ofbiz.entity.model.ModelFieldTypeReader, org.apache.ofbiz.entity.config.model.Datasource) `
- `public static java.lang.String makeWhereStringFromFields(java.util.List<org.apache.ofbiz.entity.model.ModelField>, java.util.Map<java.lang.String, java.lang.Object>, java.lang.String);`
- `public static java.lang.StringBuilder makeWhereStringFromFields(java.lang.StringBuilder, java.util.List<org.apache.ofbiz.entity.model.ModelField>, java.util.Map<java.lang.String, java.lang.Object>, java.lang.String);`
- `public static java.lang.String makeWhereStringFromFields(java.util.List<org.apache.ofbiz.entity.model.ModelField>, java.util.Map<java.lang.String, java.lang.Object>, java.lang.String, java.util.List<org.apache.ofbiz.entity.condition.EntityConditionParam>);`
- `public static java.lang.StringBuilder makeWhereStringFromFields(java.lang.StringBuilder, java.util.List<org.apache.ofbiz.entity.model.ModelField>, java.util.Map<java.lang.String, java.lang.Object>, java.lang.String, java.util.List<org.apache.ofbiz.entity.condition.EntityConditionParam>);`
- `public static java.lang.String makeWhereClause(org.apache.ofbiz.entity.model.ModelEntity, java.util.List<org.apache.ofbiz.entity.model.ModelField>, java.util.Map<java.lang.String, java.lang.Object>, java.lang.String, java.lang.String) `
- `public static java.lang.String makeViewWhereClause(org.apache.ofbiz.entity.model.ModelEntity, java.lang.String) `
- `public static java.lang.String makeOrderByClause(org.apache.ofbiz.entity.model.ModelEntity, java.util.List<java.lang.String>, org.apache.ofbiz.entity.config.model.Datasource) `
- `public static java.lang.String makeOrderByClause(org.apache.ofbiz.entity.model.ModelEntity, java.util.List<java.lang.String>, boolean, org.apache.ofbiz.entity.config.model.Datasource) `
- `public static java.lang.String makeViewTable(org.apache.ofbiz.entity.model.ModelEntity, org.apache.ofbiz.entity.model.ModelFieldTypeReader, org.apache.ofbiz.entity.config.model.Datasource) `
- `public static java.lang.String filterColName(java.lang.String);`
- `public static void setValues(org.apache.ofbiz.entity.jdbc.SQLProcessor, java.util.List<org.apache.ofbiz.entity.model.ModelField>, org.apache.ofbiz.entity.GenericEntity, org.apache.ofbiz.entity.model.ModelFieldTypeReader) `
- `public static void setValuesWhereClause(org.apache.ofbiz.entity.jdbc.SQLProcessor, java.util.List<org.apache.ofbiz.entity.model.ModelField>, org.apache.ofbiz.entity.GenericValue, org.apache.ofbiz.entity.model.ModelFieldTypeReader) `
- `public static void setPkValues(org.apache.ofbiz.entity.jdbc.SQLProcessor, org.apache.ofbiz.entity.model.ModelEntity, org.apache.ofbiz.entity.GenericEntity, org.apache.ofbiz.entity.model.ModelFieldTypeReader) `
- `public static void getValue(java.sql.ResultSet, int, org.apache.ofbiz.entity.model.ModelField, org.apache.ofbiz.entity.GenericEntity, org.apache.ofbiz.entity.model.ModelFieldTypeReader) `
- *(... 7 weitere Methoden)*

### `EntityJoinOperator` — class
Vollständiger Name: `org.apache.ofbiz.entity.condition.EntityJoinOperator`
- `public void addSqlValue(java.lang.StringBuilder, org.apache.ofbiz.entity.model.ModelEntity, java.util.List<org.apache.ofbiz.entity.condition.EntityConditionParam>, boolean, org.apache.ofbiz.entity.condition.EntityCondition, org.apache.ofbiz.entity.condition.EntityCondition, org.apache.ofbiz.entity.config.model.Datasource);`
- `public void addSqlValue(java.lang.StringBuilder, org.apache.ofbiz.entity.model.ModelEntity, java.util.List<org.apache.ofbiz.entity.condition.EntityConditionParam>, java.util.List<? extends org.apache.ofbiz.entity.condition.EntityCondition>, org.apache.ofbiz.entity.config.model.Datasource);`
- `public org.apache.ofbiz.entity.condition.EntityCondition freeze(org.apache.ofbiz.entity.condition.EntityCondition, org.apache.ofbiz.entity.condition.EntityCondition);`
- `public org.apache.ofbiz.entity.condition.EntityCondition freeze(java.util.List<? extends org.apache.ofbiz.entity.condition.EntityCondition>);`
- `public java.lang.Boolean eval(org.apache.ofbiz.entity.GenericEntity, org.apache.ofbiz.entity.condition.EntityCondition, org.apache.ofbiz.entity.condition.EntityCondition);`
- `public boolean isEmpty(org.apache.ofbiz.entity.condition.EntityCondition, org.apache.ofbiz.entity.condition.EntityCondition);`
- `public boolean isEmpty(java.util.List<? extends org.apache.ofbiz.entity.condition.EntityCondition>);`
- `public boolean entityMatches(org.apache.ofbiz.entity.GenericEntity, org.apache.ofbiz.entity.condition.EntityCondition, org.apache.ofbiz.entity.condition.EntityCondition);`
- `public boolean entityMatches(org.apache.ofbiz.entity.GenericEntity, java.util.List<? extends org.apache.ofbiz.entity.condition.EntityCondition>);`
- `public java.lang.Boolean eval(org.apache.ofbiz.entity.Delegator, java.util.Map<java.lang.String, ? extends java.lang.Object>, org.apache.ofbiz.entity.condition.EntityCondition, org.apache.ofbiz.entity.condition.EntityCondition);`
- `public boolean mapMatches(org.apache.ofbiz.entity.Delegator, java.util.Map<java.lang.String, ? extends java.lang.Object>, org.apache.ofbiz.entity.condition.EntityCondition, org.apache.ofbiz.entity.condition.EntityCondition);`
- `public java.lang.Boolean eval(org.apache.ofbiz.entity.Delegator, java.util.Map<java.lang.String, ? extends java.lang.Object>, java.util.List<? extends org.apache.ofbiz.entity.condition.EntityCondition>);`
- `public boolean mapMatches(org.apache.ofbiz.entity.Delegator, java.util.Map<java.lang.String, ? extends java.lang.Object>, java.util.List<? extends org.apache.ofbiz.entity.condition.EntityCondition>);`
- `public void validateSql(org.apache.ofbiz.entity.model.ModelEntity, org.apache.ofbiz.entity.condition.EntityCondition, org.apache.ofbiz.entity.condition.EntityCondition) `
- `public void validateSql(org.apache.ofbiz.entity.model.ModelEntity, java.util.List<? extends org.apache.ofbiz.entity.condition.EntityCondition>) `
- *(... 6 weitere Methoden)*

## Modul: entityext (18 Klassen, 135 public Methoden)

### `EntitySyncContext` — class
Vollständiger Name: `org.apache.ofbiz.entityext.synchronization.EntitySyncContext`
- `public java.sql.Timestamp getCurrentRunEndTime();`
- `public java.sql.Timestamp getStartDate();`
- `public long getTotalRowsPerSplit();`
- `public java.sql.Timestamp getCurrentRunStartTime();`
- `public java.lang.String getEntitySyncId();`
- `public void setTotalSplits(long);`
- `public org.apache.ofbiz.entity.GenericValue getEntitySync();`
- `public long getTotalSplits();`
- `public org.apache.ofbiz.entityext.synchronization.EntitySyncContext(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>) `
- `public boolean isEntitySyncRunning();`
- `public boolean hasMoreTimeToSync();`
- `public void advanceRunTimes();`
- `public void setSplitStartTime();`
- `public void createInitialHistory() `
- `public java.util.ArrayList<org.apache.ofbiz.entity.GenericValue> assembleValuesToCreate() `
- *(... 13 weitere Methoden)*

### `EntityPermissionChecker` — class
Vollständiger Name: `org.apache.ofbiz.entityext.permission.EntityPermissionChecker`
- `public org.apache.ofbiz.entityext.permission.EntityPermissionChecker(org.w3c.dom.Element);`
- `public boolean runPermissionCheck(java.util.Map<java.lang.String, ?>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> checkPermission(org.apache.ofbiz.entity.GenericValue, java.lang.String, org.apache.ofbiz.entity.GenericValue, java.util.List<java.lang.String>, java.util.List<java.lang.String>, java.util.List<java.lang.String>, org.apache.ofbiz.entity.Delegator, org.apache.ofbiz.security.Security, java.lang.String);`
- `public static java.util.Map<java.lang.String, java.lang.Object> checkPermission(org.apache.ofbiz.entity.GenericValue, java.lang.String, org.apache.ofbiz.entity.GenericValue, java.util.List<java.lang.String>, java.util.List<java.lang.String>, java.util.List<java.lang.String>, org.apache.ofbiz.entity.Delegator, org.apache.ofbiz.security.Security, java.lang.String, java.lang.String, java.lang.String);`
- `public static java.util.Map<java.lang.String, java.lang.Object> checkPermission(org.apache.ofbiz.entity.GenericValue, java.util.List<java.lang.String>, org.apache.ofbiz.entity.GenericValue, java.util.List<java.lang.String>, java.util.List<java.lang.String>, java.util.List<java.lang.String>, org.apache.ofbiz.entity.Delegator, org.apache.ofbiz.security.Security, java.lang.String, java.lang.String);`
- `public static java.util.Map<java.lang.String, java.lang.Object> checkPermission(org.apache.ofbiz.entity.GenericValue, java.util.List<java.lang.String>, org.apache.ofbiz.entity.GenericValue, java.util.List<java.lang.String>, java.util.List<java.lang.String>, java.util.List<java.lang.String>, org.apache.ofbiz.entity.Delegator, org.apache.ofbiz.security.Security, java.lang.String, java.lang.String, java.lang.String);`
- `public static boolean checkPermissionMethod(org.apache.ofbiz.entity.Delegator, org.apache.ofbiz.entity.GenericValue, java.util.List<java.lang.String>, java.lang.String, java.util.List<? extends java.lang.Object>, java.util.List<java.lang.String>, java.util.List<java.lang.String>, java.lang.String) `
- `public static boolean checkPermissionMethod(org.apache.ofbiz.entity.Delegator, java.lang.String, java.lang.String, java.util.List<? extends java.lang.Object>, org.apache.ofbiz.entityext.permission.EntityPermissionChecker$AuxiliaryValueGetter, org.apache.ofbiz.entityext.permission.EntityPermissionChecker$RelatedRoleGetter, org.apache.ofbiz.entityext.permission.EntityPermissionChecker$PermissionConditionGetter) `
- `public static org.apache.ofbiz.entity.GenericValue getNextEntity(org.apache.ofbiz.entity.Delegator, java.lang.String, java.lang.String, java.lang.Object, java.util.Map<java.lang.String, org.apache.ofbiz.entity.GenericValue>) `
- `public static boolean checkHasRoleOperations(java.lang.String, org.apache.ofbiz.entityext.permission.EntityPermissionChecker$PermissionConditionGetter, org.apache.ofbiz.entity.Delegator);`
- `public static boolean checkHasRoleOperations(java.lang.String, java.util.List<java.lang.String>, org.apache.ofbiz.entity.Delegator);`
- `public static boolean hasMatch(java.lang.String, java.util.List<org.apache.ofbiz.entity.GenericValue>, java.util.List<java.lang.String>, boolean, java.util.List<java.lang.String>, boolean, java.lang.String);`
- `public static boolean hasMatch(org.apache.ofbiz.entity.GenericValue, org.apache.ofbiz.entityext.permission.EntityPermissionChecker$PermissionConditionGetter, org.apache.ofbiz.entityext.permission.EntityPermissionChecker$RelatedRoleGetter, org.apache.ofbiz.entityext.permission.EntityPermissionChecker$AuxiliaryValueGetter, java.lang.String, boolean) `
- `public static java.util.List<java.lang.String> getRelatedPurposes(org.apache.ofbiz.entity.GenericValue, java.util.List<java.lang.String>);`
- `public static java.util.List<java.lang.String> getUserRoles(org.apache.ofbiz.entity.GenericValue, org.apache.ofbiz.entity.GenericValue, org.apache.ofbiz.entity.Delegator) `
- *(... 4 weitere Methoden)*

### `EntityEcaRule` — class
Vollständiger Name: `org.apache.ofbiz.entityext.eca.EntityEcaRule`
- `public org.apache.ofbiz.entityext.eca.EntityEcaRule(org.w3c.dom.Element);`
- `public java.lang.String getEntityName();`
- `public java.lang.String getOperationName();`
- `public java.lang.String getEventName();`
- `public boolean getRunOnError();`
- `public java.util.List<java.lang.Object> getActionsAndSets();`
- `public java.util.List<org.apache.ofbiz.entityext.eca.EntityEcaCondition> getConditions();`
- `public void eval(java.lang.String, org.apache.ofbiz.service.DispatchContext, org.apache.ofbiz.entity.GenericEntity, boolean, java.util.Set<java.lang.String>) `
- `public void setEnabled(boolean);`
- `public boolean isEnabled();`
- `public int hashCode();`
- `public boolean equals(java.lang.Object);`
- `public java.lang.String toString();`

### `EntityCacheServices` — class
Vollständiger Name: `org.apache.ofbiz.entityext.cache.EntityCacheServices`
- `public org.apache.ofbiz.entityext.cache.EntityCacheServices();`
- `public void setDelegator(org.apache.ofbiz.entity.Delegator, java.lang.String);`
- `public org.apache.ofbiz.entity.GenericValue getAuthUserLogin();`
- `public void distributedClearCacheLine(org.apache.ofbiz.entity.GenericValue);`
- `public void distributedClearCacheLineFlexible(org.apache.ofbiz.entity.GenericEntity);`
- `public void distributedClearCacheLineByCondition(java.lang.String, org.apache.ofbiz.entity.condition.EntityCondition);`
- `public void distributedClearCacheLine(org.apache.ofbiz.entity.GenericPK);`
- `public void clearAllCaches();`
- `public static java.util.Map<java.lang.String, java.lang.Object> clearAllEntityCaches(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> clearCacheLine(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`

### `EntitySyncServices` — class
Vollständiger Name: `org.apache.ofbiz.entityext.synchronization.EntitySyncServices`
- `public org.apache.ofbiz.entityext.synchronization.EntitySyncServices();`
- `public static java.util.Map<java.lang.String, java.lang.Object> runEntitySync(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> storeEntitySyncData(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> runPullEntitySync(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> pullAndReportEntitySyncData(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> runOfflineEntitySync(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> loadOfflineSyncData(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> updateOfflineEntitySync(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> cleanSyncRemoveInfo(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`

### `EntityDataServices` — class
Vollständiger Name: `org.apache.ofbiz.entityext.data.EntityDataServices`
- `public org.apache.ofbiz.entityext.data.EntityDataServices();`
- `public static java.util.Map<java.lang.String, java.lang.Object> exportDelimitedToDirectory(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> importDelimitedFromDirectory(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> importDelimitedFile(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> rebuildAllIndexesAndKeys(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> unwrapByteWrappers(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> reencryptPrivateKeys(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> reencryptFields(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, java.lang.Object>);`

### `EntityEcaCondition` — class
Vollständiger Name: `org.apache.ofbiz.entityext.eca.EntityEcaCondition`
- `public org.apache.ofbiz.entityext.eca.EntityEcaCondition(org.w3c.dom.Element, boolean, boolean);`
- `public boolean eval(org.apache.ofbiz.service.DispatchContext, org.apache.ofbiz.entity.GenericEntity, java.util.Map<java.lang.String, java.lang.Object>) `
- `public java.lang.String getLValue();`
- `public java.lang.String getRValue();`
- `public java.lang.String getOperator();`
- `public java.lang.String toString();`
- `public int hashCode();`
- `public boolean equals(java.lang.Object);`

### `EntityEcaAction` — class
Vollständiger Name: `org.apache.ofbiz.entityext.eca.EntityEcaAction`
- `public org.apache.ofbiz.entityext.eca.EntityEcaAction(org.w3c.dom.Element);`
- `public java.lang.String getServiceName();`
- `public void runAction(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>, org.apache.ofbiz.entity.GenericEntity) `
- `public java.lang.String toString();`
- `public int hashCode();`
- `public boolean equals(java.lang.Object);`

### `EntitySyncServices` [Groovy] — class
Vollständiger Name: `org.apache.ofbiz.entityext.EntitySyncServices`
- `public org.apache.ofbiz.entityext.EntitySyncServices();`
- `public org.apache.ofbiz.entityext.EntitySyncServices(groovy.lang.Binding);`
- `public static void main(java.lang.String...);`
- `public java.lang.Object run();`
- `public java.util.Map entitySyncPermissionCheck();`
- `public java.util.Map resetEntitySyncStatus();`

### `EntityDataLoadContainer` — class
Vollständiger Name: `org.apache.ofbiz.entityext.data.EntityDataLoadContainer`
- `public org.apache.ofbiz.entityext.data.EntityDataLoadContainer();`
- `public void init(java.util.List<org.apache.ofbiz.base.start.StartupCommand>, java.lang.String, java.lang.String) `
- `public boolean start();`
- `public void stop();`
- `public java.lang.String getName();`

### `DelegatorEcaHandler` — class
Vollständiger Name: `org.apache.ofbiz.entityext.eca.DelegatorEcaHandler`
- `public org.apache.ofbiz.entityext.eca.DelegatorEcaHandler();`
- `public void setDelegator(org.apache.ofbiz.entity.Delegator);`
- `public java.util.Map<java.lang.String, java.util.List<org.apache.ofbiz.entityext.eca.EntityEcaRule>> getEntityEventMap(java.lang.String);`
- `public void evalRules(java.lang.String, java.util.Map<java.lang.String, java.util.List<org.apache.ofbiz.entityext.eca.EntityEcaRule>>, java.lang.String, org.apache.ofbiz.entity.GenericEntity, boolean) `

### `EntityEcaSetField` — class
Vollständiger Name: `org.apache.ofbiz.entityext.eca.EntityEcaSetField`
- `public org.apache.ofbiz.entityext.eca.EntityEcaSetField(org.w3c.dom.Element);`
- `public void eval(java.util.Map<java.lang.String, java.lang.Object>);`
- `public java.lang.String getFieldName();`
- `public java.lang.String getRValue();`

### `EntityEcaException` — class
Vollständiger Name: `org.apache.ofbiz.entityext.eca.EntityEcaException`
- `public org.apache.ofbiz.entityext.eca.EntityEcaException();`
- `public org.apache.ofbiz.entityext.eca.EntityEcaException(java.lang.String);`
- `public org.apache.ofbiz.entityext.eca.EntityEcaException(java.lang.String, java.lang.Throwable);`

### `EntityEcaUtil` — class
Vollständiger Name: `org.apache.ofbiz.entityext.eca.EntityEcaUtil`
- `public static java.util.Map<java.lang.String, java.util.Map<java.lang.String, java.util.List<org.apache.ofbiz.entityext.eca.EntityEcaRule>>> getEntityEcaCache(java.lang.String);`
- `public static java.lang.String getEntityEcaReaderName(java.lang.String);`
- `public static java.util.Collection<org.apache.ofbiz.entityext.eca.EntityEcaRule> getEntityEcaRules(org.apache.ofbiz.entity.Delegator, java.lang.String, java.lang.String);`

### `EntityServiceFactory` — class
Vollständiger Name: `org.apache.ofbiz.entityext.EntityServiceFactory`
- `public org.apache.ofbiz.entityext.EntityServiceFactory();`
- `public static org.apache.ofbiz.service.LocalDispatcher getLocalDispatcher(org.apache.ofbiz.entity.Delegator);`
- `public static org.apache.ofbiz.service.DispatchContext getDispatchContext(org.apache.ofbiz.entity.Delegator);`

### `UpgradeServices` — class
Vollständiger Name: `org.apache.ofbiz.entityext.data.UpgradeServices`
- `public org.apache.ofbiz.entityext.data.UpgradeServices();`
- `public static java.util.Map<java.lang.String, java.lang.Object> generateMySqlFileWithAlterTableForTimestamps(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, java.lang.Object>);`

### `EntityGroupUtil` — class
Vollständiger Name: `org.apache.ofbiz.entityext.EntityGroupUtil`
- `public static java.util.Set<java.lang.String> getEntityNamesByGroup(java.lang.String, org.apache.ofbiz.entity.Delegator, boolean) `
- `public static java.util.List<org.apache.ofbiz.entity.model.ModelEntity> getModelEntitiesFromRecords(java.util.List<org.apache.ofbiz.entity.GenericValue>, org.apache.ofbiz.entity.Delegator, boolean) `

### `EntityWatchServices` — class
Vollständiger Name: `org.apache.ofbiz.entityext.EntityWatchServices`
- `public org.apache.ofbiz.entityext.EntityWatchServices();`
- `public static java.util.Map<java.lang.String, java.lang.Object> watchEntity(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`

## Modul: humanres (2 Klassen, 6 public Methoden)

### `CategoryTree` [Groovy] — class
Vollständiger Name: `org.apache.ofbiz.humanres.category.CategoryTree`
- `public org.apache.ofbiz.humanres.category.CategoryTree();`
- `public org.apache.ofbiz.humanres.category.CategoryTree(groovy.lang.Binding);`
- `public static void main(java.lang.String...);`
- `public java.lang.Object run();`

### `HumanResEvents` — class
Vollständiger Name: `org.apache.ofbiz.humanres.HumanResEvents`
- `public org.apache.ofbiz.humanres.HumanResEvents();`
- `public static java.lang.String getChildHRCategoryTree(javax.servlet.http.HttpServletRequest, javax.servlet.http.HttpServletResponse);`

## Modul: manufacturing (44 Klassen, 302 public Methoden)

### `BOMNode` — class
Vollständiger Name: `org.apache.ofbiz.manufacturing.bom.BOMNode`
- `public org.apache.ofbiz.manufacturing.bom.BOMNode(org.apache.ofbiz.entity.GenericValue, org.apache.ofbiz.service.LocalDispatcher, org.apache.ofbiz.entity.GenericValue);`
- `public org.apache.ofbiz.manufacturing.bom.BOMNode(java.lang.String, org.apache.ofbiz.entity.Delegator, org.apache.ofbiz.service.LocalDispatcher, org.apache.ofbiz.entity.GenericValue) `
- `public org.apache.ofbiz.manufacturing.bom.BOMNode getParentNode();`
- `public org.apache.ofbiz.manufacturing.bom.BOMNode getRootNode();`
- `public void setParentNode(org.apache.ofbiz.manufacturing.bom.BOMNode);`
- `public void print(java.lang.StringBuffer, java.math.BigDecimal, int);`
- `public void print(java.util.List<org.apache.ofbiz.manufacturing.bom.BOMNode>, java.math.BigDecimal, int, boolean);`
- `public void getProductsInPackages(java.util.List<org.apache.ofbiz.manufacturing.bom.BOMNode>, java.math.BigDecimal, int, boolean);`
- `public void sumQuantity(java.util.Map<java.lang.String, org.apache.ofbiz.manufacturing.bom.BOMNode>);`
- `public java.util.Map<java.lang.String, java.lang.Object> createManufacturingOrder(java.lang.String, java.util.Date, java.lang.String, java.lang.String, java.lang.String, java.lang.String, java.lang.String, java.lang.String, java.lang.String, boolean, boolean) `
- `public java.sql.Timestamp getStartDate(java.lang.String, java.sql.Timestamp, boolean);`
- `public boolean isWarehouseManaged(java.lang.String);`
- `public boolean isManufactured(boolean);`
- `public boolean isManufactured();`
- `public boolean isVirtual();`
- *(... 23 weitere Methoden)*

### `ProductionRunServices` — class
Vollständiger Name: `org.apache.ofbiz.manufacturing.jobshopmgt.ProductionRunServices`
- `public org.apache.ofbiz.manufacturing.jobshopmgt.ProductionRunServices();`
- `public static java.util.Map<java.lang.String, java.lang.Object> cancelProductionRun(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> createProductionRun(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> updateProductionRun(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> changeProductionRunStatus(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> changeProductionRunTaskStatus(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> getWorkEffortCosts(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> getProductionRunCost(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> createProductionRunTaskCosts(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> checkUpdatePrunRoutingTask(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> addProductionRunComponent(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> updateProductionRunComponent(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> addProductionRunRoutingTask(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> productionRunProduce(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> productionRunDeclareAndProduce(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- *(... 17 weitere Methoden)*

### `ProductionRun` — class
Vollständiger Name: `org.apache.ofbiz.manufacturing.jobshopmgt.ProductionRun`
- `public org.apache.ofbiz.manufacturing.jobshopmgt.ProductionRun(java.lang.String, org.apache.ofbiz.entity.Delegator, org.apache.ofbiz.service.LocalDispatcher);`
- `public boolean exist();`
- `public org.apache.ofbiz.entity.GenericValue getGenericValue();`
- `public boolean store();`
- `public org.apache.ofbiz.entity.GenericValue getProductProduced();`
- `public java.math.BigDecimal getQuantity();`
- `public void setQuantity(java.math.BigDecimal);`
- `public java.sql.Timestamp getEstimatedStartDate();`
- `public void setEstimatedStartDate(java.sql.Timestamp);`
- `public java.sql.Timestamp getEstimatedCompletionDate();`
- `public void setEstimatedCompletionDate(java.sql.Timestamp);`
- `public java.sql.Timestamp recalculateEstimatedCompletionDate(java.lang.Long, java.sql.Timestamp);`
- `public java.sql.Timestamp recalculateEstimatedCompletionDate();`
- `public java.lang.String getProductionRunName();`
- `public void setProductionRunName(java.lang.String);`
- *(... 10 weitere Methoden)*

### `BOMTree` — class
Vollständiger Name: `org.apache.ofbiz.manufacturing.bom.BOMTree`
- `public org.apache.ofbiz.manufacturing.bom.BOMTree(java.lang.String, java.lang.String, java.util.Date, org.apache.ofbiz.entity.Delegator, org.apache.ofbiz.service.LocalDispatcher, org.apache.ofbiz.entity.GenericValue) `
- `public org.apache.ofbiz.manufacturing.bom.BOMTree(java.lang.String, java.lang.String, java.util.Date, int, org.apache.ofbiz.entity.Delegator, org.apache.ofbiz.service.LocalDispatcher, org.apache.ofbiz.entity.GenericValue) `
- `public org.apache.ofbiz.entity.GenericValue getInputProduct();`
- `public boolean isConfigured();`
- `public java.math.BigDecimal getRootQuantity();`
- `public void setRootQuantity(java.math.BigDecimal);`
- `public java.math.BigDecimal getRootAmount();`
- `public void setRootAmount(java.math.BigDecimal);`
- `public org.apache.ofbiz.manufacturing.bom.BOMNode getRoot();`
- `public java.util.Date getInDate();`
- `public java.lang.String getBomTypeId();`
- `public void print(java.lang.StringBuffer);`
- `public void print(java.util.List<org.apache.ofbiz.manufacturing.bom.BOMNode>, int);`
- `public void print(java.util.List<org.apache.ofbiz.manufacturing.bom.BOMNode>, int, boolean);`
- `public void print(java.util.List<org.apache.ofbiz.manufacturing.bom.BOMNode>);`
- *(... 5 weitere Methoden)*

### `TechDataServices` — class
Vollständiger Name: `org.apache.ofbiz.manufacturing.techdata.TechDataServices`
- `public org.apache.ofbiz.manufacturing.techdata.TechDataServices();`
- `public static java.util.Map<java.lang.String, java.lang.Object> lookupRoutingTask(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> checkRoutingTaskAssoc(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public static org.apache.ofbiz.entity.GenericValue getTechDataCalendar(org.apache.ofbiz.entity.GenericValue);`
- `public static java.util.Map<java.lang.String, java.lang.Object> dayStartCapacityAvailable(org.apache.ofbiz.entity.GenericValue, int);`
- `public static long capacityRemaining(org.apache.ofbiz.entity.GenericValue, java.sql.Timestamp);`
- `public static java.util.Map<java.lang.String, java.lang.Object> startNextDay(org.apache.ofbiz.entity.GenericValue, java.sql.Timestamp);`
- `public static java.sql.Timestamp addForward(org.apache.ofbiz.entity.GenericValue, java.sql.Timestamp, long);`
- `public static java.util.Map<java.lang.String, java.lang.Object> dayEndCapacityAvailable(org.apache.ofbiz.entity.GenericValue, int);`
- `public static long capacityRemainingBackward(org.apache.ofbiz.entity.GenericValue, java.sql.Timestamp);`
- `public static java.util.Map<java.lang.String, java.lang.Object> endPreviousDay(org.apache.ofbiz.entity.GenericValue, java.sql.Timestamp);`
- `public static java.sql.Timestamp addBackward(org.apache.ofbiz.entity.GenericValue, java.sql.Timestamp, long);`

### `ProductionRunServicesScript` [Groovy] — class
Vollständiger Name: `org.apache.ofbiz.manufacturing.jobshopmgt.ProductionRunServicesScript`
- `public org.apache.ofbiz.manufacturing.jobshopmgt.ProductionRunServicesScript();`
- `public org.apache.ofbiz.manufacturing.jobshopmgt.ProductionRunServicesScript(groovy.lang.Binding);`
- `public static void main(java.lang.String...);`
- `public java.lang.Object run();`
- `public java.util.Map createProductionRunPartyAssign();`
- `public java.util.Map createProductionRunAssoc();`
- `public java.util.Map issueProductionRunTask();`
- `public java.util.Map issueProductionRunTaskComponent();`
- `public java.util.Map issueProductionRunTaskComponentInline(java.util.Map, org.apache.ofbiz.entity.GenericValue, org.apache.ofbiz.entity.GenericValue);`
- `public java.util.Map issueInventoryItemToWorkEffort();`
- `public static void __$swapInit();`

### `BOMServices` — class
Vollständiger Name: `org.apache.ofbiz.manufacturing.bom.BOMServices`
- `public org.apache.ofbiz.manufacturing.bom.BOMServices();`
- `public static java.util.Map<java.lang.String, java.lang.Object> getMaxDepth(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> updateLowLevelCode(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> initLowLevelCode(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> searchDuplicatedAncestor(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> getBOMTree(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> getManufacturingComponents(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> getNotAssembledComponents(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> createShipmentPackages(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> getProductsInPackages(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`

### `MrpServices` — class
Vollständiger Name: `org.apache.ofbiz.manufacturing.mrp.MrpServices`
- `public org.apache.ofbiz.manufacturing.mrp.MrpServices();`
- `public static java.util.Map<java.lang.String, java.lang.Object> initMrpEvents(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public static java.math.BigDecimal findProductMrpQoh(java.lang.String, org.apache.ofbiz.entity.GenericValue, java.lang.String, org.apache.ofbiz.service.LocalDispatcher, org.apache.ofbiz.entity.Delegator);`
- `public static java.math.BigDecimal findProductMrpQoh(java.lang.String, java.lang.String, java.lang.String, org.apache.ofbiz.service.LocalDispatcher, org.apache.ofbiz.entity.Delegator);`
- `public static void logMrpError(java.lang.String, java.lang.String, java.lang.String, org.apache.ofbiz.entity.Delegator);`
- `public static void logMrpError(java.lang.String, java.lang.String, java.sql.Timestamp, java.lang.String, org.apache.ofbiz.entity.Delegator);`
- `public static void processBomComponent(java.lang.String, org.apache.ofbiz.entity.GenericValue, java.math.BigDecimal, java.sql.Timestamp, java.util.Map<java.lang.String, java.lang.Object>, java.util.List<org.apache.ofbiz.manufacturing.bom.BOMNode>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> executeMrp(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`

### `ProposedOrder` — class
Vollständiger Name: `org.apache.ofbiz.manufacturing.mrp.ProposedOrder`
- `public org.apache.ofbiz.manufacturing.mrp.ProposedOrder(org.apache.ofbiz.entity.GenericValue, java.lang.String, java.lang.String, boolean, java.sql.Timestamp, java.math.BigDecimal);`
- `public java.math.BigDecimal getQuantity();`
- `public java.sql.Timestamp getRequirementStartDate();`
- `public java.util.Map<java.lang.String, java.lang.Object> calculateStartDate(int, org.apache.ofbiz.entity.GenericValue, org.apache.ofbiz.entity.Delegator, org.apache.ofbiz.service.LocalDispatcher, org.apache.ofbiz.entity.GenericValue);`
- `public void calculateQuantityToSupply(java.math.BigDecimal, java.math.BigDecimal, java.util.ListIterator<org.apache.ofbiz.entity.GenericValue>);`
- `public java.lang.String create(org.apache.ofbiz.service.DispatchContext, org.apache.ofbiz.entity.GenericValue);`
- `public void setMrpName(java.lang.String);`

### `RoutingServicesScript` [Groovy] — class
Vollständiger Name: `org.apache.ofbiz.manufacturing.routing.RoutingServicesScript`
- `public org.apache.ofbiz.manufacturing.routing.RoutingServicesScript();`
- `public org.apache.ofbiz.manufacturing.routing.RoutingServicesScript(groovy.lang.Binding);`
- `public static void main(java.lang.String...);`
- `public java.lang.Object run();`
- `public java.util.Map getProductRouting();`
- `public java.util.Map getRoutingTaskAssocs();`

### `BomSimulation` [Groovy] — class
Vollständiger Name: `org.apache.ofbiz.manufacturing.bom.BomSimulation`
- `public org.apache.ofbiz.manufacturing.bom.BomSimulation();`
- `public org.apache.ofbiz.manufacturing.bom.BomSimulation(groovy.lang.Binding);`
- `public static void main(java.lang.String...);`
- `public java.lang.Object run();`
- `public static void __$swapInit();`

### `ProductionRunDeclaration` [Groovy] — class
Vollständiger Name: `org.apache.ofbiz.manufacturing.jobshopmgt.ProductionRunDeclaration`
- `public org.apache.ofbiz.manufacturing.jobshopmgt.ProductionRunDeclaration();`
- `public org.apache.ofbiz.manufacturing.jobshopmgt.ProductionRunDeclaration(groovy.lang.Binding);`
- `public static void main(java.lang.String...);`
- `public java.lang.Object run();`
- `public static void __$swapInit();`

### `PRunsComponentsByFeature` [Groovy] — class
Vollständiger Name: `org.apache.ofbiz.manufacturing.reports.PRunsComponentsByFeature`
- `public org.apache.ofbiz.manufacturing.reports.PRunsComponentsByFeature();`
- `public org.apache.ofbiz.manufacturing.reports.PRunsComponentsByFeature(groovy.lang.Binding);`
- `public static void main(java.lang.String...);`
- `public java.lang.Object run();`
- `public static void __$swapInit();`

### `EditProductBom` [Groovy] — class
Vollständiger Name: `org.apache.ofbiz.manufacturing.bom.EditProductBom`
- `public org.apache.ofbiz.manufacturing.bom.EditProductBom();`
- `public org.apache.ofbiz.manufacturing.bom.EditProductBom(groovy.lang.Binding);`
- `public static void main(java.lang.String...);`
- `public java.lang.Object run();`

### `FindProductBom` [Groovy] — class
Vollständiger Name: `org.apache.ofbiz.manufacturing.bom.FindProductBom`
- `public org.apache.ofbiz.manufacturing.bom.FindProductBom();`
- `public org.apache.ofbiz.manufacturing.bom.FindProductBom(groovy.lang.Binding);`
- `public static void main(java.lang.String...);`
- `public java.lang.Object run();`

### `ProductionRunActualComponents` [Groovy] — class
Vollständiger Name: `org.apache.ofbiz.manufacturing.jobshopmgt.ProductionRunActualComponents`
- `public org.apache.ofbiz.manufacturing.jobshopmgt.ProductionRunActualComponents();`
- `public org.apache.ofbiz.manufacturing.jobshopmgt.ProductionRunActualComponents(groovy.lang.Binding);`
- `public static void main(java.lang.String...);`
- `public java.lang.Object run();`

### `ProductionRunAllFixedAssets` [Groovy] — class
Vollständiger Name: `org.apache.ofbiz.manufacturing.jobshopmgt.ProductionRunAllFixedAssets`
- `public org.apache.ofbiz.manufacturing.jobshopmgt.ProductionRunAllFixedAssets();`
- `public org.apache.ofbiz.manufacturing.jobshopmgt.ProductionRunAllFixedAssets(groovy.lang.Binding);`
- `public static void main(java.lang.String...);`
- `public java.lang.Object run();`

### `ProductionRunComponents` [Groovy] — class
Vollständiger Name: `org.apache.ofbiz.manufacturing.jobshopmgt.ProductionRunComponents`
- `public org.apache.ofbiz.manufacturing.jobshopmgt.ProductionRunComponents();`
- `public org.apache.ofbiz.manufacturing.jobshopmgt.ProductionRunComponents(groovy.lang.Binding);`
- `public static void main(java.lang.String...);`
- `public java.lang.Object run();`

### `ProductionRunContent` [Groovy] — class
Vollständiger Name: `org.apache.ofbiz.manufacturing.jobshopmgt.ProductionRunContent`
- `public org.apache.ofbiz.manufacturing.jobshopmgt.ProductionRunContent();`
- `public org.apache.ofbiz.manufacturing.jobshopmgt.ProductionRunContent(groovy.lang.Binding);`
- `public static void main(java.lang.String...);`
- `public java.lang.Object run();`

### `ProductionRunCosts` [Groovy] — class
Vollständiger Name: `org.apache.ofbiz.manufacturing.jobshopmgt.ProductionRunCosts`
- `public org.apache.ofbiz.manufacturing.jobshopmgt.ProductionRunCosts();`
- `public org.apache.ofbiz.manufacturing.jobshopmgt.ProductionRunCosts(groovy.lang.Binding);`
- `public static void main(java.lang.String...);`
- `public java.lang.Object run();`

## Modul: marketing (13 Klassen, 56 public Methoden)

### `TrackingCodeEvents` — class
Vollständiger Name: `org.apache.ofbiz.marketing.tracking.TrackingCodeEvents`
- `public org.apache.ofbiz.marketing.tracking.TrackingCodeEvents();`
- `public static java.lang.String checkTrackingCodeUrlParam(javax.servlet.http.HttpServletRequest, javax.servlet.http.HttpServletResponse);`
- `public static java.lang.String checkPartnerTrackingCodeUrlParam(javax.servlet.http.HttpServletRequest, javax.servlet.http.HttpServletResponse);`
- `public static java.lang.String processTrackingCode(org.apache.ofbiz.entity.GenericValue, javax.servlet.http.HttpServletRequest, javax.servlet.http.HttpServletResponse, java.lang.String);`
- `public static java.lang.String checkTrackingCodeCookies(javax.servlet.http.HttpServletRequest, javax.servlet.http.HttpServletResponse);`
- `public static java.lang.String checkAccessTrackingCode(javax.servlet.http.HttpServletRequest, javax.servlet.http.HttpServletResponse);`
- `public static java.lang.String removeAccesTrackingCodeCookie(javax.servlet.http.HttpServletRequest, javax.servlet.http.HttpServletResponse);`
- `public static java.util.List<org.apache.ofbiz.entity.GenericValue> makeTrackingCodeOrders(javax.servlet.http.HttpServletRequest);`

### `LeadServices` [Groovy] — class
Vollständiger Name: `org.apache.ofbiz.marketing.sfa.lead.LeadServices`
- `public org.apache.ofbiz.marketing.sfa.lead.LeadServices();`
- `public org.apache.ofbiz.marketing.sfa.lead.LeadServices(groovy.lang.Binding);`
- `public static void main(java.lang.String...);`
- `public java.lang.Object run();`
- `public java.util.Map createLead();`
- `public java.util.Map convertLeadToContact();`
- `public java.util.Map resolvePartyProcessMap();`

### `AccountServices` [Groovy] — class
Vollständiger Name: `org.apache.ofbiz.marketing.sfa.account.AccountServices`
- `public org.apache.ofbiz.marketing.sfa.account.AccountServices();`
- `public org.apache.ofbiz.marketing.sfa.account.AccountServices(groovy.lang.Binding);`
- `public static void main(java.lang.String...);`
- `public java.lang.Object run();`
- `public java.util.Map createAccount();`

### `GetContactListMarketingEmail` [Groovy] — class
Vollständiger Name: `org.apache.ofbiz.marketing.marketing.contact.GetContactListMarketingEmail`
- `public org.apache.ofbiz.marketing.marketing.contact.GetContactListMarketingEmail();`
- `public org.apache.ofbiz.marketing.marketing.contact.GetContactListMarketingEmail(groovy.lang.Binding);`
- `public static void main(java.lang.String...);`
- `public java.lang.Object run();`

### `EmailStatusReport` [Groovy] — class
Vollständiger Name: `org.apache.ofbiz.marketing.marketing.reports.EmailStatusReport`
- `public org.apache.ofbiz.marketing.marketing.reports.EmailStatusReport();`
- `public org.apache.ofbiz.marketing.marketing.reports.EmailStatusReport(groovy.lang.Binding);`
- `public static void main(java.lang.String...);`
- `public java.lang.Object run();`

### `MarketingCampaignReport` [Groovy] — class
Vollständiger Name: `org.apache.ofbiz.marketing.marketing.reports.MarketingCampaignReport`
- `public org.apache.ofbiz.marketing.marketing.reports.MarketingCampaignReport();`
- `public org.apache.ofbiz.marketing.marketing.reports.MarketingCampaignReport(groovy.lang.Binding);`
- `public static void main(java.lang.String...);`
- `public java.lang.Object run();`

### `PartyStatusReport` [Groovy] — class
Vollständiger Name: `org.apache.ofbiz.marketing.marketing.reports.PartyStatusReport`
- `public org.apache.ofbiz.marketing.marketing.reports.PartyStatusReport();`
- `public org.apache.ofbiz.marketing.marketing.reports.PartyStatusReport(groovy.lang.Binding);`
- `public static void main(java.lang.String...);`
- `public java.lang.Object run();`

### `TrackingCodeReport` [Groovy] — class
Vollständiger Name: `org.apache.ofbiz.marketing.marketing.reports.TrackingCodeReport`
- `public org.apache.ofbiz.marketing.marketing.reports.TrackingCodeReport();`
- `public org.apache.ofbiz.marketing.marketing.reports.TrackingCodeReport(groovy.lang.Binding);`
- `public static void main(java.lang.String...);`
- `public java.lang.Object run();`

### `MarketingTests` [Groovy] — class
Vollständiger Name: `org.apache.ofbiz.marketing.marketing.test.MarketingTests`
- `public org.apache.ofbiz.marketing.marketing.test.MarketingTests(java.lang.String);`
- `public void testCreateAndUpdateContactList();`
- `public groovy.lang.MetaClass getMetaClass();`
- `public void setMetaClass(groovy.lang.MetaClass);`

### `CloneLead` [Groovy] — class
Vollständiger Name: `org.apache.ofbiz.marketing.sfa.CloneLead`
- `public org.apache.ofbiz.marketing.sfa.CloneLead();`
- `public org.apache.ofbiz.marketing.sfa.CloneLead(groovy.lang.Binding);`
- `public static void main(java.lang.String...);`
- `public java.lang.Object run();`

### `MergeContacts` [Groovy] — class
Vollständiger Name: `org.apache.ofbiz.marketing.sfa.MergeContacts`
- `public org.apache.ofbiz.marketing.sfa.MergeContacts();`
- `public org.apache.ofbiz.marketing.sfa.MergeContacts(groovy.lang.Binding);`
- `public static void main(java.lang.String...);`
- `public java.lang.Object run();`

### `MarketingServices` — class
Vollständiger Name: `org.apache.ofbiz.marketing.marketing.MarketingServices`
- `public org.apache.ofbiz.marketing.marketing.MarketingServices();`
- `public static java.util.Map<java.lang.String, java.lang.Object> signUpForContactList(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> deleteContactListParty(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`

### `ReportHelper` — class
Vollständiger Name: `org.apache.ofbiz.marketing.report.ReportHelper`
- `public static java.util.List<java.util.Map<java.lang.String, java.lang.Object>> calcConversionRates(java.util.List<org.apache.ofbiz.entity.GenericValue>, java.util.List<org.apache.ofbiz.entity.GenericValue>, java.lang.String);`

## Modul: minilang (125 Klassen, 512 public Methoden)

### `SimpleMethod` — class
Vollständiger Name: `org.apache.ofbiz.minilang.SimpleMethod`
- `public org.apache.ofbiz.minilang.SimpleMethod(org.w3c.dom.Element, java.lang.String) `
- `public static java.util.Map<java.lang.String, org.apache.ofbiz.minilang.SimpleMethod> getDirectSimpleMethods(java.lang.String, java.lang.String, java.lang.String) `
- `public static org.apache.ofbiz.minilang.SimpleMethod getSimpleMethod(java.lang.String, java.lang.String, java.lang.ClassLoader) `
- `public static org.apache.ofbiz.minilang.SimpleMethod getSimpleMethod(java.net.URL, java.lang.String) `
- `public static java.util.List<org.apache.ofbiz.minilang.SimpleMethod> getSimpleMethodsList(java.lang.String, java.lang.ClassLoader) `
- `public static java.util.List<org.apache.ofbiz.minilang.method.MethodOperation> readOperations(org.w3c.dom.Element, org.apache.ofbiz.minilang.SimpleMethod) `
- `public static java.lang.String runSimpleEvent(java.lang.String, java.lang.String, javax.servlet.http.HttpServletRequest, javax.servlet.http.HttpServletResponse) `
- `public static java.lang.String runSimpleEvent(java.lang.String, java.lang.String, javax.servlet.http.HttpServletRequest, javax.servlet.http.HttpServletResponse, java.lang.ClassLoader) `
- `public static java.lang.String runSimpleEvent(java.net.URL, java.lang.String, javax.servlet.http.HttpServletRequest, javax.servlet.http.HttpServletResponse, java.lang.ClassLoader) `
- `public static java.lang.String runSimpleMethod(java.lang.String, java.lang.String, org.apache.ofbiz.minilang.method.MethodContext) `
- `public static java.lang.String runSimpleMethod(java.net.URL, java.lang.String, org.apache.ofbiz.minilang.method.MethodContext) `
- `public static java.util.Map<java.lang.String, java.lang.Object> runSimpleService(java.lang.String, java.lang.String, org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>) `
- `public static java.util.Map<java.lang.String, java.lang.Object> runSimpleService(java.lang.String, java.lang.String, org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>, java.lang.ClassLoader) `
- `public static java.util.Map<java.lang.String, java.lang.Object> runSimpleService(java.net.URL, java.lang.String, org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>, java.lang.ClassLoader) `
- `public static boolean runSubOps(java.util.List<org.apache.ofbiz.minilang.method.MethodOperation>, org.apache.ofbiz.minilang.method.MethodContext) `
- *(... 31 weitere Methoden)*

### `MethodContext` — class
Vollständiger Name: `org.apache.ofbiz.minilang.method.MethodContext`
- `public org.apache.ofbiz.minilang.method.MethodContext(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>, java.lang.ClassLoader);`
- `public org.apache.ofbiz.minilang.method.MethodContext(javax.servlet.http.HttpServletRequest, javax.servlet.http.HttpServletResponse, java.lang.ClassLoader);`
- `public org.apache.ofbiz.minilang.method.MethodContext(java.util.Map<java.lang.String, ? extends java.lang.Object>, java.lang.ClassLoader, int);`
- `public org.apache.ofbiz.entity.Delegator getDelegator();`
- `public org.apache.ofbiz.service.LocalDispatcher getDispatcher();`
- `public <T> T getEnv(org.apache.ofbiz.base.util.collections.FlexibleMapAccessor<T>);`
- `public <T> T getEnv(java.lang.String);`
- `public java.util.Map<java.lang.String, java.lang.Object> getEnvMap();`
- `public java.lang.ClassLoader getLoader();`
- `public java.util.Locale getLocale();`
- `public int getMethodType();`
- `public java.lang.Object getParameter(java.lang.String);`
- `public java.util.Map<java.lang.String, java.lang.Object> getParameters();`
- `public javax.servlet.http.HttpServletRequest getRequest();`
- `public javax.servlet.http.HttpServletResponse getResponse();`
- *(... 17 weitere Methoden)*

### `MiniLangValidate` — class
Vollständiger Name: `org.apache.ofbiz.minilang.MiniLangValidate`
- `public static void attributeNames(org.apache.ofbiz.minilang.SimpleMethod, org.w3c.dom.Element, java.lang.String...) `
- `public static java.lang.String checkAttribute(java.lang.String, java.lang.String);`
- `public static void childElements(org.apache.ofbiz.minilang.SimpleMethod, org.w3c.dom.Element, java.lang.String...) `
- `public static void constantAttributes(org.apache.ofbiz.minilang.SimpleMethod, org.w3c.dom.Element, java.lang.String...) `
- `public static void constantPlusExpressionAttributes(org.apache.ofbiz.minilang.SimpleMethod, org.w3c.dom.Element, java.lang.String...) `
- `public static void deprecatedAttribute(org.apache.ofbiz.minilang.SimpleMethod, org.w3c.dom.Element, java.lang.String, java.lang.String) `
- `public static void expressionAttributes(org.apache.ofbiz.minilang.SimpleMethod, org.w3c.dom.Element, java.lang.String...) `
- `public static void handleError(java.lang.String, org.apache.ofbiz.minilang.SimpleMethod, org.w3c.dom.Element) `
- `public static boolean lenientOn();`
- `public static void noChildElements(org.apache.ofbiz.minilang.SimpleMethod, org.w3c.dom.Element) `
- `public static void requireAnyAttribute(org.apache.ofbiz.minilang.SimpleMethod, org.w3c.dom.Element, java.lang.String...) `
- `public static void requireAnyChildElement(org.apache.ofbiz.minilang.SimpleMethod, org.w3c.dom.Element, java.lang.String...) `
- `public static void requiredAttributes(org.apache.ofbiz.minilang.SimpleMethod, org.w3c.dom.Element, java.lang.String...) `
- `public static void requiredChildElements(org.apache.ofbiz.minilang.SimpleMethod, org.w3c.dom.Element, java.lang.String...) `
- `public static void scriptAttributes(org.apache.ofbiz.minilang.SimpleMethod, org.w3c.dom.Element, java.lang.String...) `
- *(... 2 weitere Methoden)*

### `MiniLangUtil` — class
Vollständiger Name: `org.apache.ofbiz.minilang.MiniLangUtil`
- `public static boolean containsScript(java.lang.String);`
- `public static boolean autoCorrectOn();`
- `public static void callMethod(org.apache.ofbiz.minilang.method.MethodOperation, org.apache.ofbiz.minilang.method.MethodContext, java.util.List<org.apache.ofbiz.minilang.method.MethodObject<?>>, java.lang.Class<?>, java.lang.Object, java.lang.String, org.apache.ofbiz.base.util.collections.FlexibleMapAccessor<java.lang.Object>) `
- `public static java.lang.Object convertType(java.lang.Object, java.lang.Class<?>, java.util.Locale, java.util.TimeZone, java.lang.String) `
- `public static void flagDocumentAsCorrected(org.w3c.dom.Element);`
- `public static java.lang.Class<?> getObjectClassForConversion(java.lang.Object);`
- `public static boolean isConstantAttribute(java.lang.String);`
- `public static boolean isConstantPlusExpressionAttribute(java.lang.String);`
- `public static boolean isDocumentAutoCorrected(org.w3c.dom.Document);`
- `public static void writeMiniLangDocument(java.net.URL, org.w3c.dom.Document);`

### `ArtifactInfoContext` — class
Vollständiger Name: `org.apache.ofbiz.minilang.artifact.ArtifactInfoContext`
- `public org.apache.ofbiz.minilang.artifact.ArtifactInfoContext();`
- `public void addEntityName(java.lang.String);`
- `public void addServiceName(java.lang.String);`
- `public void addSimpleMethod(org.apache.ofbiz.minilang.SimpleMethod);`
- `public java.util.Set<java.lang.String> getEntityNames();`
- `public java.util.Set<java.lang.String> getServiceNames();`
- `public boolean hasVisited(org.apache.ofbiz.minilang.SimpleMethod);`

### `MiniLangElement` — class
Vollständiger Name: `org.apache.ofbiz.minilang.MiniLangElement`
- `public org.apache.ofbiz.minilang.MiniLangElement(org.w3c.dom.Element, org.apache.ofbiz.minilang.SimpleMethod);`
- `public void gatherArtifactInfo(org.apache.ofbiz.minilang.artifact.ArtifactInfoContext);`
- `public java.lang.String getLineNumber();`
- `public org.apache.ofbiz.minilang.SimpleMethod getSimpleMethod();`
- `public java.lang.String getTagName();`
- `public void outputTraceMessage(org.apache.ofbiz.minilang.method.MethodContext, java.lang.String...);`
- `public java.lang.String toString();`

### `CallSimpleMethod` — class
Vollständiger Name: `org.apache.ofbiz.minilang.method.callops.CallSimpleMethod`
- `public org.apache.ofbiz.minilang.method.callops.CallSimpleMethod(org.w3c.dom.Element, org.apache.ofbiz.minilang.SimpleMethod) `
- `public boolean exec(org.apache.ofbiz.minilang.method.MethodContext) `
- `public void gatherArtifactInfo(org.apache.ofbiz.minilang.artifact.ArtifactInfoContext);`
- `public java.lang.String getMethodName();`
- `public java.lang.String getXmlResource();`
- `public java.lang.String toString();`

### `CompareCondition` — class
Vollständiger Name: `org.apache.ofbiz.minilang.method.conditional.CompareCondition`
- `public org.apache.ofbiz.minilang.method.conditional.CompareCondition(org.w3c.dom.Element, org.apache.ofbiz.minilang.SimpleMethod) `
- `public boolean checkCondition(org.apache.ofbiz.minilang.method.MethodContext) `
- `public boolean exec(org.apache.ofbiz.minilang.method.MethodContext) `
- `public void gatherArtifactInfo(org.apache.ofbiz.minilang.artifact.ArtifactInfoContext);`
- `public void prettyPrint(java.lang.StringBuilder, org.apache.ofbiz.minilang.method.MethodContext);`
- `public java.lang.String toString();`

### `CompareFieldCondition` — class
Vollständiger Name: `org.apache.ofbiz.minilang.method.conditional.CompareFieldCondition`
- `public org.apache.ofbiz.minilang.method.conditional.CompareFieldCondition(org.w3c.dom.Element, org.apache.ofbiz.minilang.SimpleMethod) `
- `public boolean checkCondition(org.apache.ofbiz.minilang.method.MethodContext) `
- `public boolean exec(org.apache.ofbiz.minilang.method.MethodContext) `
- `public void gatherArtifactInfo(org.apache.ofbiz.minilang.artifact.ArtifactInfoContext);`
- `public void prettyPrint(java.lang.StringBuilder, org.apache.ofbiz.minilang.method.MethodContext);`
- `public java.lang.String toString();`

### `EmptyCondition` — class
Vollständiger Name: `org.apache.ofbiz.minilang.method.conditional.EmptyCondition`
- `public org.apache.ofbiz.minilang.method.conditional.EmptyCondition(org.w3c.dom.Element, org.apache.ofbiz.minilang.SimpleMethod) `
- `public boolean checkCondition(org.apache.ofbiz.minilang.method.MethodContext) `
- `public boolean exec(org.apache.ofbiz.minilang.method.MethodContext) `
- `public void gatherArtifactInfo(org.apache.ofbiz.minilang.artifact.ArtifactInfoContext);`
- `public void prettyPrint(java.lang.StringBuilder, org.apache.ofbiz.minilang.method.MethodContext);`
- `public java.lang.String toString();`

### `HasPermissionCondition` — class
Vollständiger Name: `org.apache.ofbiz.minilang.method.conditional.HasPermissionCondition`
- `public org.apache.ofbiz.minilang.method.conditional.HasPermissionCondition(org.w3c.dom.Element, org.apache.ofbiz.minilang.SimpleMethod) `
- `public boolean checkCondition(org.apache.ofbiz.minilang.method.MethodContext) `
- `public boolean exec(org.apache.ofbiz.minilang.method.MethodContext) `
- `public void gatherArtifactInfo(org.apache.ofbiz.minilang.artifact.ArtifactInfoContext);`
- `public void prettyPrint(java.lang.StringBuilder, org.apache.ofbiz.minilang.method.MethodContext);`
- `public java.lang.String toString();`

### `RegexpCondition` — class
Vollständiger Name: `org.apache.ofbiz.minilang.method.conditional.RegexpCondition`
- `public org.apache.ofbiz.minilang.method.conditional.RegexpCondition(org.w3c.dom.Element, org.apache.ofbiz.minilang.SimpleMethod) `
- `public boolean checkCondition(org.apache.ofbiz.minilang.method.MethodContext) `
- `public boolean exec(org.apache.ofbiz.minilang.method.MethodContext) `
- `public void gatherArtifactInfo(org.apache.ofbiz.minilang.artifact.ArtifactInfoContext);`
- `public void prettyPrint(java.lang.StringBuilder, org.apache.ofbiz.minilang.method.MethodContext);`
- `public java.lang.String toString();`

### `ValidateMethodCondition` — class
Vollständiger Name: `org.apache.ofbiz.minilang.method.conditional.ValidateMethodCondition`
- `public org.apache.ofbiz.minilang.method.conditional.ValidateMethodCondition(org.w3c.dom.Element, org.apache.ofbiz.minilang.SimpleMethod) `
- `public boolean checkCondition(org.apache.ofbiz.minilang.method.MethodContext) `
- `public boolean exec(org.apache.ofbiz.minilang.method.MethodContext) `
- `public void gatherArtifactInfo(org.apache.ofbiz.minilang.artifact.ArtifactInfoContext);`
- `public void prettyPrint(java.lang.StringBuilder, org.apache.ofbiz.minilang.method.MethodContext);`
- `public java.lang.String toString();`

### `ElseIf` — class
Vollständiger Name: `org.apache.ofbiz.minilang.method.conditional.ElseIf`
- `public org.apache.ofbiz.minilang.method.conditional.ElseIf(org.w3c.dom.Element, org.apache.ofbiz.minilang.SimpleMethod) `
- `public boolean checkCondition(org.apache.ofbiz.minilang.method.MethodContext) `
- `public void gatherArtifactInfo(org.apache.ofbiz.minilang.artifact.ArtifactInfoContext);`
- `public java.util.List<org.apache.ofbiz.minilang.method.MethodOperation> getThenSubOps();`
- `public boolean runSubOps(org.apache.ofbiz.minilang.method.MethodContext) `

### `StringObject` — class
Vollständiger Name: `org.apache.ofbiz.minilang.method.StringObject`
- `public org.apache.ofbiz.minilang.method.StringObject(org.w3c.dom.Element, org.apache.ofbiz.minilang.SimpleMethod);`
- `public java.lang.String getObject(org.apache.ofbiz.minilang.method.MethodContext);`
- `public java.lang.Class<java.lang.String> getTypeClass(org.apache.ofbiz.minilang.method.MethodContext) `
- `public java.lang.String getTypeName();`
- `public java.lang.Object getObject(org.apache.ofbiz.minilang.method.MethodContext);`

### `CallService` — class
Vollständiger Name: `org.apache.ofbiz.minilang.method.callops.CallService`
- `public org.apache.ofbiz.minilang.method.callops.CallService(org.w3c.dom.Element, org.apache.ofbiz.minilang.SimpleMethod) `
- `public boolean exec(org.apache.ofbiz.minilang.method.MethodContext) `
- `public void gatherArtifactInfo(org.apache.ofbiz.minilang.artifact.ArtifactInfoContext);`
- `public java.lang.String toString();`

### `CallServiceAsynch` — class
Vollständiger Name: `org.apache.ofbiz.minilang.method.callops.CallServiceAsynch`
- `public org.apache.ofbiz.minilang.method.callops.CallServiceAsynch(org.w3c.dom.Element, org.apache.ofbiz.minilang.SimpleMethod) `
- `public boolean exec(org.apache.ofbiz.minilang.method.MethodContext) `
- `public void gatherArtifactInfo(org.apache.ofbiz.minilang.artifact.ArtifactInfoContext);`
- `public java.lang.String toString();`

### `SetServiceFields` — class
Vollständiger Name: `org.apache.ofbiz.minilang.method.callops.SetServiceFields`
- `public org.apache.ofbiz.minilang.method.callops.SetServiceFields(org.w3c.dom.Element, org.apache.ofbiz.minilang.SimpleMethod) `
- `public boolean exec(org.apache.ofbiz.minilang.method.MethodContext) `
- `public void gatherArtifactInfo(org.apache.ofbiz.minilang.artifact.ArtifactInfoContext);`
- `public java.lang.String toString();`

### `ConditionalFactory` — class
Vollständiger Name: `org.apache.ofbiz.minilang.method.conditional.ConditionalFactory`
- `public org.apache.ofbiz.minilang.method.conditional.ConditionalFactory();`
- `public static org.apache.ofbiz.minilang.method.conditional.Conditional makeConditional(org.w3c.dom.Element, org.apache.ofbiz.minilang.SimpleMethod) `
- `public abstract C createCondition(org.w3c.dom.Element, org.apache.ofbiz.minilang.SimpleMethod) `
- `public abstract java.lang.String getName();`

### `MasterIf` — class
Vollständiger Name: `org.apache.ofbiz.minilang.method.conditional.MasterIf`
- `public org.apache.ofbiz.minilang.method.conditional.MasterIf(org.w3c.dom.Element, org.apache.ofbiz.minilang.SimpleMethod) `
- `public boolean exec(org.apache.ofbiz.minilang.method.MethodContext) `
- `public void gatherArtifactInfo(org.apache.ofbiz.minilang.artifact.ArtifactInfoContext);`
- `public java.lang.String toString();`

## Modul: order (147 Klassen, 2041 public Methoden)

### `ShoppingCart` — class
Vollständiger Name: `org.apache.ofbiz.order.shoppingcart.ShoppingCart`
- `public org.apache.ofbiz.order.shoppingcart.ShoppingCart(org.apache.ofbiz.order.shoppingcart.ShoppingCart);`
- `public org.apache.ofbiz.order.shoppingcart.ShoppingCart(org.apache.ofbiz.entity.Delegator, java.lang.String, java.lang.String, java.util.Locale, java.lang.String, java.lang.String, java.lang.String);`
- `public org.apache.ofbiz.order.shoppingcart.ShoppingCart(org.apache.ofbiz.entity.Delegator, java.lang.String, java.lang.String, java.util.Locale, java.lang.String);`
- `public org.apache.ofbiz.order.shoppingcart.ShoppingCart(org.apache.ofbiz.entity.Delegator, java.lang.String, java.util.Locale, java.lang.String);`
- `public org.apache.ofbiz.entity.Delegator getDelegator();`
- `public java.lang.String getProductStoreId();`
- `public boolean getDoPromotions();`
- `public void setDoPromotions(boolean);`
- `public void setProductStoreId(java.lang.String);`
- `public java.lang.String getTransactionId();`
- `public void setTransactionId(java.lang.String);`
- `public java.lang.String getTerminalId();`
- `public void setTerminalId(java.lang.String);`
- `public java.lang.String getAutoOrderShoppingListId();`
- `public void setAutoOrderShoppingListId(java.lang.String);`
- *(... 373 weitere Methoden)*

### `OrderReadHelper` — class
Vollständiger Name: `org.apache.ofbiz.order.order.OrderReadHelper`
- `public org.apache.ofbiz.order.order.OrderReadHelper(org.apache.ofbiz.entity.GenericValue, java.util.List<org.apache.ofbiz.entity.GenericValue>, java.util.List<org.apache.ofbiz.entity.GenericValue>);`
- `public org.apache.ofbiz.order.order.OrderReadHelper(org.apache.ofbiz.entity.GenericValue);`
- `public org.apache.ofbiz.order.order.OrderReadHelper(java.util.List<org.apache.ofbiz.entity.GenericValue>, java.util.List<org.apache.ofbiz.entity.GenericValue>);`
- `public org.apache.ofbiz.order.order.OrderReadHelper(org.apache.ofbiz.entity.Delegator, java.lang.String);`
- `public java.lang.String getOrderId();`
- `public java.lang.String getWebSiteId();`
- `public java.lang.String getProductStoreId();`
- `public org.apache.ofbiz.entity.GenericValue getProductStore();`
- `public java.lang.String getOrderTypeId();`
- `public java.lang.String getCurrency();`
- `public java.lang.String getOrderName();`
- `public java.util.List<org.apache.ofbiz.entity.GenericValue> getAdjustments();`
- `public java.util.List<org.apache.ofbiz.entity.GenericValue> getPaymentPreferences();`
- `public java.util.Map<java.lang.String, java.math.BigDecimal> getReceivedPaymentTotalsByPaymentMethod();`
- `public java.util.Map<java.lang.String, java.math.BigDecimal> getReturnedTotalsByPaymentMethod();`
- *(... 177 weitere Methoden)*

### `ShoppingCartItem` — class
Vollständiger Name: `org.apache.ofbiz.order.shoppingcart.ShoppingCartItem`
- `public org.apache.ofbiz.order.shoppingcart.ShoppingCartItem(org.apache.ofbiz.order.shoppingcart.ShoppingCartItem);`
- `public static org.apache.ofbiz.order.shoppingcart.ShoppingCartItem makePurchaseOrderItem(java.lang.Integer, java.lang.String, java.math.BigDecimal, java.math.BigDecimal, java.util.Map<java.lang.String, org.apache.ofbiz.entity.GenericValue>, java.util.Map<java.lang.String, java.lang.Object>, java.lang.String, org.apache.ofbiz.product.config.ProductConfigWrapper, java.lang.String, org.apache.ofbiz.order.shoppingcart.ShoppingCart$ShoppingCartItemGroup, org.apache.ofbiz.service.LocalDispatcher, org.apache.ofbiz.order.shoppingcart.ShoppingCart, org.apache.ofbiz.entity.GenericValue, java.sql.Timestamp, java.sql.Timestamp, java.sql.Timestamp) `
- `public static org.apache.ofbiz.order.shoppingcart.ShoppingCartItem makeItem(java.lang.Integer, java.lang.String, java.math.BigDecimal, java.math.BigDecimal, java.math.BigDecimal, java.sql.Timestamp, java.math.BigDecimal, java.math.BigDecimal, java.sql.Timestamp, java.sql.Timestamp, java.util.Map<java.lang.String, org.apache.ofbiz.entity.GenericValue>, java.util.Map<java.lang.String, java.lang.Object>, java.lang.String, org.apache.ofbiz.product.config.ProductConfigWrapper, java.lang.String, org.apache.ofbiz.order.shoppingcart.ShoppingCart$ShoppingCartItemGroup, org.apache.ofbiz.service.LocalDispatcher, org.apache.ofbiz.order.shoppingcart.ShoppingCart, java.lang.Boolean, java.lang.Boolean, java.lang.String, java.lang.Boolean, java.lang.Boolean) `
- `public static org.apache.ofbiz.order.shoppingcart.ShoppingCartItem makeItem(java.lang.Integer, java.lang.String, java.math.BigDecimal, java.math.BigDecimal, java.math.BigDecimal, java.sql.Timestamp, java.math.BigDecimal, java.math.BigDecimal, java.lang.String, java.lang.String, java.sql.Timestamp, java.sql.Timestamp, java.util.Map<java.lang.String, org.apache.ofbiz.entity.GenericValue>, java.util.Map<java.lang.String, java.lang.Object>, java.lang.String, org.apache.ofbiz.product.config.ProductConfigWrapper, java.lang.String, org.apache.ofbiz.order.shoppingcart.ShoppingCart$ShoppingCartItemGroup, org.apache.ofbiz.service.LocalDispatcher, org.apache.ofbiz.order.shoppingcart.ShoppingCart, java.lang.Boolean, java.lang.Boolean, java.lang.String, java.lang.Boolean, java.lang.Boolean) `
- `public static org.apache.ofbiz.order.shoppingcart.ShoppingCartItem makeItem(java.lang.Integer, java.lang.String, java.math.BigDecimal, java.math.BigDecimal, java.math.BigDecimal, java.sql.Timestamp, java.math.BigDecimal, java.math.BigDecimal, java.lang.String, java.lang.String, java.sql.Timestamp, java.sql.Timestamp, java.sql.Timestamp, java.util.Map<java.lang.String, org.apache.ofbiz.entity.GenericValue>, java.util.Map<java.lang.String, java.lang.Object>, java.lang.String, org.apache.ofbiz.product.config.ProductConfigWrapper, java.lang.String, org.apache.ofbiz.order.shoppingcart.ShoppingCart$ShoppingCartItemGroup, org.apache.ofbiz.service.LocalDispatcher, org.apache.ofbiz.order.shoppingcart.ShoppingCart, java.lang.Boolean, java.lang.Boolean, java.lang.String, java.lang.Boolean, java.lang.Boolean) `
- `public static org.apache.ofbiz.order.shoppingcart.ShoppingCartItem makeItem(java.lang.Integer, java.lang.String, java.math.BigDecimal, java.math.BigDecimal, java.math.BigDecimal, java.sql.Timestamp, java.math.BigDecimal, java.math.BigDecimal, java.lang.String, java.lang.String, java.sql.Timestamp, java.sql.Timestamp, java.sql.Timestamp, java.util.Map<java.lang.String, org.apache.ofbiz.entity.GenericValue>, java.util.Map<java.lang.String, java.lang.Object>, java.util.Map<java.lang.String, java.lang.String>, java.lang.String, org.apache.ofbiz.product.config.ProductConfigWrapper, java.lang.String, org.apache.ofbiz.order.shoppingcart.ShoppingCart$ShoppingCartItemGroup, org.apache.ofbiz.service.LocalDispatcher, org.apache.ofbiz.order.shoppingcart.ShoppingCart, java.lang.Boolean, java.lang.Boolean, java.lang.String, java.lang.Boolean, java.lang.Boolean) `
- `public static org.apache.ofbiz.order.shoppingcart.ShoppingCartItem makeItem(java.lang.Integer, org.apache.ofbiz.entity.GenericValue, java.math.BigDecimal, java.math.BigDecimal, java.math.BigDecimal, java.sql.Timestamp, java.math.BigDecimal, java.math.BigDecimal, java.sql.Timestamp, java.sql.Timestamp, java.util.Map<java.lang.String, org.apache.ofbiz.entity.GenericValue>, java.util.Map<java.lang.String, java.lang.Object>, java.lang.String, org.apache.ofbiz.product.config.ProductConfigWrapper, java.lang.String, org.apache.ofbiz.order.shoppingcart.ShoppingCart$ShoppingCartItemGroup, org.apache.ofbiz.service.LocalDispatcher, org.apache.ofbiz.order.shoppingcart.ShoppingCart, java.lang.Boolean, java.lang.Boolean, org.apache.ofbiz.entity.GenericValue, java.lang.Boolean, java.lang.Boolean) `
- `public static org.apache.ofbiz.order.shoppingcart.ShoppingCartItem makeItem(java.lang.Integer, org.apache.ofbiz.entity.GenericValue, java.math.BigDecimal, java.math.BigDecimal, java.math.BigDecimal, java.sql.Timestamp, java.math.BigDecimal, java.math.BigDecimal, java.lang.String, java.lang.String, java.sql.Timestamp, java.sql.Timestamp, java.sql.Timestamp, java.util.Map<java.lang.String, org.apache.ofbiz.entity.GenericValue>, java.util.Map<java.lang.String, java.lang.Object>, java.lang.String, org.apache.ofbiz.product.config.ProductConfigWrapper, java.lang.String, org.apache.ofbiz.order.shoppingcart.ShoppingCart$ShoppingCartItemGroup, org.apache.ofbiz.service.LocalDispatcher, org.apache.ofbiz.order.shoppingcart.ShoppingCart, java.lang.Boolean, java.lang.Boolean, org.apache.ofbiz.entity.GenericValue, java.lang.Boolean, java.lang.Boolean) `
- `public static org.apache.ofbiz.order.shoppingcart.ShoppingCartItem makeItem(java.lang.Integer, org.apache.ofbiz.entity.GenericValue, java.math.BigDecimal, java.math.BigDecimal, java.math.BigDecimal, java.sql.Timestamp, java.math.BigDecimal, java.math.BigDecimal, java.lang.String, java.lang.String, java.sql.Timestamp, java.sql.Timestamp, java.sql.Timestamp, java.util.Map<java.lang.String, org.apache.ofbiz.entity.GenericValue>, java.util.Map<java.lang.String, java.lang.Object>, java.util.Map<java.lang.String, java.lang.String>, java.lang.String, org.apache.ofbiz.product.config.ProductConfigWrapper, java.lang.String, org.apache.ofbiz.order.shoppingcart.ShoppingCart$ShoppingCartItemGroup, org.apache.ofbiz.service.LocalDispatcher, org.apache.ofbiz.order.shoppingcart.ShoppingCart, java.lang.Boolean, java.lang.Boolean, org.apache.ofbiz.entity.GenericValue, java.lang.Boolean, java.lang.Boolean) `
- `public static org.apache.ofbiz.entity.GenericValue findProduct(org.apache.ofbiz.entity.Delegator, boolean, java.lang.String, java.lang.String, java.util.Locale) `
- `public static void isValidCartProduct(org.apache.ofbiz.product.config.ProductConfigWrapper, org.apache.ofbiz.entity.GenericValue, java.sql.Timestamp, java.util.Locale) `
- `public static org.apache.ofbiz.order.shoppingcart.ShoppingCartItem makeItem(java.lang.Integer, java.lang.String, java.lang.String, java.lang.String, java.math.BigDecimal, java.math.BigDecimal, java.math.BigDecimal, java.util.Map<java.lang.String, java.lang.Object>, java.lang.String, org.apache.ofbiz.order.shoppingcart.ShoppingCart$ShoppingCartItemGroup, org.apache.ofbiz.service.LocalDispatcher, org.apache.ofbiz.order.shoppingcart.ShoppingCart, java.lang.Boolean) `
- `public static java.lang.String checkAvailability(java.lang.String, java.math.BigDecimal, java.sql.Timestamp, java.math.BigDecimal, org.apache.ofbiz.order.shoppingcart.ShoppingCart);`
- `public static java.lang.String getPurchaseOrderItemDescription(org.apache.ofbiz.entity.GenericValue, org.apache.ofbiz.entity.GenericValue, java.util.Locale, org.apache.ofbiz.service.LocalDispatcher);`
- `public java.lang.String getProdCatalogId();`
- *(... 165 weitere Methoden)*

### `OrderServices` — class
Vollständiger Name: `org.apache.ofbiz.order.order.OrderServices`
- `public org.apache.ofbiz.order.order.OrderServices();`
- `public static java.util.Map<java.lang.String, java.lang.Object> createOrder(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> countProductQuantityOrdered(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, java.lang.Object>);`
- `public static void reserveInventory(org.apache.ofbiz.entity.Delegator, org.apache.ofbiz.service.LocalDispatcher, org.apache.ofbiz.entity.GenericValue, java.util.Locale, java.util.List<org.apache.ofbiz.entity.GenericValue>, java.util.List<java.lang.String>, java.util.Map<java.lang.String, org.apache.ofbiz.entity.GenericValue>, java.lang.String, java.lang.String, java.util.List<java.lang.String>) `
- `public static java.lang.String getProductName(org.apache.ofbiz.entity.GenericValue, org.apache.ofbiz.entity.GenericValue);`
- `public static java.lang.String getProductName(org.apache.ofbiz.entity.GenericValue, java.lang.String);`
- `public static java.lang.String determineSingleFacilityFromOrder(org.apache.ofbiz.entity.GenericValue);`
- `public static java.util.Map<java.lang.String, java.lang.Object> resetGrandTotal(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> setEmptyGrandTotals(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> recalcOrderTax(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> recalcOrderShipping(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> checkItemStatus(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> cancelOrderItem(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> setItemStatus(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> setOrderStatus(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- *(... 69 weitere Methoden)*

### `ShoppingCartPersistence` — class
Vollständiger Name: `org.apache.ofbiz.order.shoppingcart.components.ShoppingCartPersistence`
- `public org.apache.ofbiz.order.shoppingcart.components.ShoppingCartPersistence();`
- `public java.util.List<org.apache.ofbiz.entity.GenericValue> getOrderItems();`
- `public void setOrderItems(java.util.List<org.apache.ofbiz.entity.GenericValue>);`
- `public void addOrderItem(org.apache.ofbiz.entity.GenericValue);`
- `public java.util.List<org.apache.ofbiz.entity.GenericValue> getOrderAdjustments();`
- `public void setOrderAdjustments(java.util.List<org.apache.ofbiz.entity.GenericValue>);`
- `public void addOrderAdjustment(org.apache.ofbiz.entity.GenericValue);`
- `public java.util.List<org.apache.ofbiz.entity.GenericValue> getOrderPaymentInfos();`
- `public void setOrderPaymentInfos(java.util.List<org.apache.ofbiz.entity.GenericValue>);`
- `public void addOrderPaymentInfo(org.apache.ofbiz.entity.GenericValue);`
- `public java.util.List<org.apache.ofbiz.entity.GenericValue> getOrderShipGroupInfos();`
- `public void setOrderShipGroupInfos(java.util.List<org.apache.ofbiz.entity.GenericValue>);`
- `public void addOrderShipGroupInfo(org.apache.ofbiz.entity.GenericValue);`
- `public java.util.List<org.apache.ofbiz.entity.GenericValue> getOrderItemPriceInfos();`
- `public void setOrderItemPriceInfos(java.util.List<org.apache.ofbiz.entity.GenericValue>);`
- *(... 43 weitere Methoden)*

### `ShoppingCartShipping` — class
Vollständiger Name: `org.apache.ofbiz.order.shoppingcart.components.ShoppingCartShipping`
- `public org.apache.ofbiz.order.shoppingcart.components.ShoppingCartShipping();`
- `public int addShipInfo();`
- `public org.apache.ofbiz.order.shoppingcart.components.ShoppingCartShipping$ShipInfo getShipInfo(int);`
- `public java.util.List<org.apache.ofbiz.order.shoppingcart.components.ShoppingCartShipping$ShipInfo> getShipGroups();`
- `public int getShipGroupSize();`
- `public void setShipmentMethodTypeId(int, java.lang.String);`
- `public java.lang.String getShipmentMethodTypeId(int);`
- `public void setShippingContactMechId(int, java.lang.String);`
- `public java.lang.String getShippingContactMechId(int);`
- `public void setCarrierPartyId(int, java.lang.String);`
- `public java.lang.String getCarrierPartyId(int);`
- `public void setSupplierPartyId(int, java.lang.String);`
- `public java.lang.String getSupplierPartyId(int);`
- `public void setSupplierAgreementId(int, java.lang.String);`
- `public java.lang.String getSupplierAgreementId(int);`
- *(... 34 weitere Methoden)*

### `ShoppingCartEvents` — class
Vollständiger Name: `org.apache.ofbiz.order.shoppingcart.ShoppingCartEvents`
- `public org.apache.ofbiz.order.shoppingcart.ShoppingCartEvents();`
- `public static java.lang.String addProductPromoCode(javax.servlet.http.HttpServletRequest, javax.servlet.http.HttpServletResponse);`
- `public static java.lang.String removePromotion(javax.servlet.http.HttpServletRequest, javax.servlet.http.HttpServletResponse);`
- `public static java.lang.String addItemGroup(javax.servlet.http.HttpServletRequest, javax.servlet.http.HttpServletResponse);`
- `public static java.lang.String addCartItemToGroup(javax.servlet.http.HttpServletRequest, javax.servlet.http.HttpServletResponse);`
- `public static java.lang.String addToCart(javax.servlet.http.HttpServletRequest, javax.servlet.http.HttpServletResponse);`
- `public static java.lang.String addToCartFromOrder(javax.servlet.http.HttpServletRequest, javax.servlet.http.HttpServletResponse);`
- `public static java.lang.String addToCartBulk(javax.servlet.http.HttpServletRequest, javax.servlet.http.HttpServletResponse);`
- `public static java.lang.String quickInitPurchaseOrder(javax.servlet.http.HttpServletRequest, javax.servlet.http.HttpServletResponse);`
- `public static java.lang.String quickCheckoutOrderWithDefaultOptions(javax.servlet.http.HttpServletRequest, javax.servlet.http.HttpServletResponse);`
- `public static java.lang.String addToCartBulkRequirements(javax.servlet.http.HttpServletRequest, javax.servlet.http.HttpServletResponse);`
- `public static java.lang.String addCategoryDefaults(javax.servlet.http.HttpServletRequest, javax.servlet.http.HttpServletResponse);`
- `public static java.lang.String deleteFromCart(javax.servlet.http.HttpServletRequest, javax.servlet.http.HttpServletResponse);`
- `public static java.lang.String modifyCart(javax.servlet.http.HttpServletRequest, javax.servlet.http.HttpServletResponse);`
- `public static java.lang.String clearCart(javax.servlet.http.HttpServletRequest, javax.servlet.http.HttpServletResponse);`
- *(... 27 weitere Methoden)*

### `CheckOutHelper` — class
Vollständiger Name: `org.apache.ofbiz.order.shoppingcart.CheckOutHelper`
- `public org.apache.ofbiz.order.shoppingcart.CheckOutHelper(org.apache.ofbiz.service.LocalDispatcher, org.apache.ofbiz.entity.Delegator, org.apache.ofbiz.order.shoppingcart.ShoppingCart);`
- `public java.util.Map<java.lang.String, java.lang.Object> setCheckOutShippingAddress(java.lang.String);`
- `public java.util.Map<java.lang.String, java.lang.Object> setCheckOutShippingOptions(java.lang.String, java.lang.String, java.lang.String, java.lang.String, java.lang.String, java.lang.String, java.lang.String, java.lang.String, java.lang.String);`
- `public java.util.Map<java.lang.String, java.lang.Object> setCheckOutPayment(java.util.Map<java.lang.String, java.util.Map<java.lang.String, java.lang.Object>>, java.util.List<java.lang.String>, java.lang.String);`
- `public java.util.List<java.lang.String> setCheckOutPaymentInternal(java.util.Map<java.lang.String, java.util.Map<java.lang.String, java.lang.Object>>, java.util.List<java.lang.String>, java.lang.String);`
- `public java.util.Map<java.lang.String, java.lang.Object> setCheckOutDates(java.sql.Timestamp, java.sql.Timestamp);`
- `public java.util.Map<java.lang.String, java.lang.Object> setCheckOutOptions(java.lang.String, java.lang.String, java.util.Map<java.lang.String, java.util.Map<java.lang.String, java.lang.Object>>, java.util.List<java.lang.String>, java.lang.String, java.lang.String, java.lang.String, java.lang.String, java.lang.String, java.lang.String, java.lang.String, java.lang.String, java.lang.String);`
- `public java.util.Map<java.lang.String, java.lang.Object> checkGiftCard(java.util.Map<java.lang.String, java.lang.Object>, java.util.Map<java.lang.String, java.util.Map<java.lang.String, java.lang.Object>>);`
- `public java.util.Map<java.lang.String, java.lang.Object> createOrder(org.apache.ofbiz.entity.GenericValue);`
- `public java.util.Map<java.lang.String, java.lang.Object> createOrder(org.apache.ofbiz.entity.GenericValue, java.lang.String, java.lang.String, java.util.List<org.apache.ofbiz.entity.GenericValue>, boolean, java.lang.String, java.lang.String);`
- `public void calcAndAddTax() `
- `public void calcAndAddTax(boolean) `
- `public void calcAndAddTax(org.apache.ofbiz.entity.GenericValue) `
- `public void calcAndAddTax(org.apache.ofbiz.entity.GenericValue, boolean) `
- `public java.util.Map<java.lang.String, java.lang.Object> processPayment(org.apache.ofbiz.entity.GenericValue, org.apache.ofbiz.entity.GenericValue) `
- *(... 18 weitere Methoden)*

### `ShoppingCartPromotion` — class
Vollständiger Name: `org.apache.ofbiz.order.shoppingcart.components.ShoppingCartPromotion`
- `public org.apache.ofbiz.order.shoppingcart.components.ShoppingCartPromotion();`
- `public java.util.List<org.apache.ofbiz.order.shoppingcart.components.ShoppingCartPromotion$ProductPromoUseInfo> getProductPromoUseInfoList();`
- `public void addProductPromoUse(java.lang.String, java.lang.String, java.math.BigDecimal, java.math.BigDecimal, java.util.Map<java.lang.Object, java.math.BigDecimal>);`
- `public void removeProductPromoUse(java.lang.String);`
- `public void clearProductPromoUseInfo();`
- `public java.util.Iterator<org.apache.ofbiz.order.shoppingcart.components.ShoppingCartPromotion$ProductPromoUseInfo> getProductPromoUseInfoIter();`
- `public int getProductPromoUseCount();`
- `public int getProductPromoUseCount(java.lang.String);`
- `public java.math.BigDecimal getProductPromoUseTotalDiscount(java.lang.String);`
- `public boolean hasProductPromoCode(java.lang.String);`
- `public int getProductPromoCodeCount();`
- `public void clearProductPromoCodes();`
- `public int getProductPromoCodeUse(java.lang.String);`
- `public void addFreeShippingProductPromoAction(java.lang.Object);`
- `public void removeFreeShippingProductPromoAction(java.lang.Object);`
- *(... 16 weitere Methoden)*

### `OrderReturnServices` — class
Vollständiger Name: `org.apache.ofbiz.order.order.OrderReturnServices`
- `public org.apache.ofbiz.order.order.OrderReturnServices();`
- `public static java.util.Map<java.lang.String, java.lang.Object> getReturnItemInitialCost(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> getOrderAvailableReturnedTotal(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public static java.math.BigDecimal getReturnItemInitialCost(org.apache.ofbiz.entity.Delegator, java.lang.String, java.lang.String);`
- `public static java.util.Map<java.lang.String, java.lang.Object> sendReturnAcceptNotification(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> sendReturnCompleteNotification(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> sendReturnCancelNotification(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> autoCancelReplacementOrders(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> getReturnableQuantity(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> getReturnableItems(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> checkReturnComplete(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> processCreditReturn(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> processRefundReturnForReplacement(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> processRefundReturn(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> refundBillingAccountPayment(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- *(... 14 weitere Methoden)*

### `OrderReturnServicesScript` [Groovy] — class
Vollständiger Name: `org.apache.ofbiz.order.order.OrderReturnServicesScript`
- `public org.apache.ofbiz.order.order.OrderReturnServicesScript();`
- `public org.apache.ofbiz.order.order.OrderReturnServicesScript(groovy.lang.Binding);`
- `public static void main(java.lang.String...);`
- `public java.lang.Object run();`
- `public java.util.Map createReturnHeader();`
- `public java.util.Map updateReturnHeader();`
- `public java.util.Map createReturnItem();`
- `public java.util.Map updateReturnItem();`
- `public java.util.Map updateReturnItemsStatus();`
- `public java.util.Map removeReturnItem();`
- `public java.util.Map updateReturnStatusFromReceipt();`
- `public java.util.Map quickReturnFromOrder();`
- `public java.util.Map createReturnAndItemOrAdjustment();`
- `public java.util.Map cancelReturnItems();`
- `public java.util.Map cancelReplacementOrderItems();`
- *(... 14 weitere Methoden)*

### `QuoteTests` [Groovy] — class
Vollständiger Name: `org.apache.ofbiz.order.order.test.QuoteTests`
- `public org.apache.ofbiz.order.order.test.QuoteTests(java.lang.String);`
- `public void testCreateQuoteWorkEffort();`
- `public void testCreateQuoteWorkEffortFail();`
- `public void testCheckUpdateQuotestatus();`
- `public void testCreateWorkEffortAndQuoteWorkEffort();`
- `public void testCreateQuote();`
- `public void testUpdateQuote();`
- `public void testCopyQuote();`
- `public void testCreateQuoteItem();`
- `public void testUpdateQuoteItem();`
- `public void testRemoveQuoteItem();`
- `public void testCreateQuoteTerm();`
- `public void testUpdateQuoteTerm();`
- `public void testDeleteQuoteTerm();`
- `public void testCreateQuoteAttribute();`
- *(... 14 weitere Methoden)*

### `ShoppingCartValidator` — class
Vollständiger Name: `org.apache.ofbiz.order.shoppingcart.components.ShoppingCartValidator`
- `public org.apache.ofbiz.order.shoppingcart.components.ShoppingCartValidator();`
- `public boolean isCartEmpty(int);`
- `public boolean isValidQuantity(java.math.BigDecimal);`
- `public boolean isValidPrice(java.math.BigDecimal);`
- `public boolean hasShippingAddress(java.lang.String);`
- `public boolean hasShippingMethod(java.lang.String);`
- `public boolean hasPaymentMethod(int);`
- `public boolean isValidGrandTotal(java.math.BigDecimal);`
- `public boolean isPaymentTotalValid(java.math.BigDecimal, java.math.BigDecimal);`
- `public boolean isValidShippingTotal(java.math.BigDecimal);`
- `public boolean isValidTaxTotal(java.math.BigDecimal);`
- `public boolean isValidProductId(java.lang.String);`
- `public boolean isValidShipGroup(int, int);`
- `public void addValidationError(java.lang.String, java.lang.String);`
- `public void addValidationWarning(java.lang.String, java.lang.String);`
- *(... 14 weitere Methoden)*

### `OrderReturnTests` [Groovy] — class
Vollständiger Name: `org.apache.ofbiz.order.order.test.OrderReturnTests`
- `public org.apache.ofbiz.order.order.test.OrderReturnTests(java.lang.String);`
- `public void testQuickReturnOrder();`
- `public void testProcessCreditReturn();`
- `public void testProcessCrossShipReplacementReturn();`
- `public void testProcessRefundImmediatelyReturn();`
- `public void testGetReturnItemInitialCost();`
- `public void testProcessRefundReturn();`
- `public void testProcessReplacementReturn();`
- `public void testProcessReplaceImmediatelyReturn();`
- `public void testProcessRefundOnlyReturn();`
- `public void testProcessWaitReplacementReturn();`
- `public void testProcessWaitReplacementReservedReturn();`
- `public void testProcessSubscriptionReturn();`
- `public void testCreateReturnAndItemOrAdjustment();`
- `public void testCreateReturnAdjustment();`
- *(... 11 weitere Methoden)*

### `ProductPromoWorker` — class
Vollständiger Name: `org.apache.ofbiz.order.shoppingcart.product.ProductPromoWorker`
- `public static java.util.List<org.apache.ofbiz.entity.GenericValue> getStoreProductPromos(org.apache.ofbiz.entity.Delegator, org.apache.ofbiz.service.LocalDispatcher, javax.servlet.ServletRequest);`
- `public static java.util.Set<java.lang.String> getStoreProductPromoCodes(org.apache.ofbiz.order.shoppingcart.ShoppingCart);`
- `public static java.util.List<org.apache.ofbiz.entity.GenericValue> getProductStorePromotions(org.apache.ofbiz.order.shoppingcart.ShoppingCart, java.sql.Timestamp, org.apache.ofbiz.service.LocalDispatcher);`
- `public static java.util.List<org.apache.ofbiz.entity.GenericValue> getAgreementPromotions(org.apache.ofbiz.order.shoppingcart.ShoppingCart, java.sql.Timestamp, org.apache.ofbiz.service.LocalDispatcher);`
- `public static void doPromotions(org.apache.ofbiz.order.shoppingcart.ShoppingCart, org.apache.ofbiz.service.LocalDispatcher);`
- `public static void doPromotions(org.apache.ofbiz.order.shoppingcart.ShoppingCart, java.util.List<org.apache.ofbiz.entity.GenericValue>, org.apache.ofbiz.service.LocalDispatcher);`
- `public static java.lang.Long getProductPromoUseLimit(org.apache.ofbiz.entity.GenericValue, java.lang.String, org.apache.ofbiz.entity.Delegator) `
- `public static java.lang.Long getProductPromoCodeUseLimit(org.apache.ofbiz.entity.GenericValue, java.lang.String, org.apache.ofbiz.entity.Delegator) `
- `public static java.lang.String checkCanUsePromoCode(java.lang.String, java.lang.String, org.apache.ofbiz.entity.Delegator, java.util.Locale);`
- `public static java.lang.String checkCanUsePromoCode(java.lang.String, java.lang.String, org.apache.ofbiz.entity.Delegator, org.apache.ofbiz.order.shoppingcart.ShoppingCart, java.util.Locale);`
- `public static java.lang.String makeAutoDescription(org.apache.ofbiz.entity.GenericValue, org.apache.ofbiz.entity.Delegator, java.util.Locale, org.apache.ofbiz.service.LocalDispatcher) `
- `public static boolean checkConditionsForItem(org.apache.ofbiz.entity.GenericValue, org.apache.ofbiz.order.shoppingcart.ShoppingCart, org.apache.ofbiz.order.shoppingcart.ShoppingCartItem, org.apache.ofbiz.entity.Delegator, org.apache.ofbiz.service.LocalDispatcher, java.sql.Timestamp) `
- `public static boolean checkConditionForItem(org.apache.ofbiz.entity.GenericValue, org.apache.ofbiz.order.shoppingcart.ShoppingCart, org.apache.ofbiz.order.shoppingcart.ShoppingCartItem, org.apache.ofbiz.entity.Delegator, org.apache.ofbiz.service.LocalDispatcher, java.sql.Timestamp) `
- `public static int checkConditionPartyHierarchy(org.apache.ofbiz.entity.Delegator, java.sql.Timestamp, java.lang.String, java.lang.String) `
- `public static void performAction(org.apache.ofbiz.order.shoppingcart.product.ProductPromoWorker$ActionResultInfo, org.apache.ofbiz.entity.GenericValue, org.apache.ofbiz.order.shoppingcart.ShoppingCart, org.apache.ofbiz.entity.Delegator, org.apache.ofbiz.service.LocalDispatcher, java.sql.Timestamp) `
- *(... 11 weitere Methoden)*

### `CheckOutEvents` — class
Vollständiger Name: `org.apache.ofbiz.order.shoppingcart.CheckOutEvents`
- `public org.apache.ofbiz.order.shoppingcart.CheckOutEvents();`
- `public static java.lang.String cartNotEmpty(javax.servlet.http.HttpServletRequest, javax.servlet.http.HttpServletResponse);`
- `public static java.lang.String setCheckOutPages(javax.servlet.http.HttpServletRequest, javax.servlet.http.HttpServletResponse);`
- `public static java.lang.String determineInitialCheckOutPage(org.apache.ofbiz.order.shoppingcart.ShoppingCart);`
- `public static java.lang.String setCheckOutError(javax.servlet.http.HttpServletRequest, javax.servlet.http.HttpServletResponse);`
- `public static java.lang.String setQuickCheckOutOptions(javax.servlet.http.HttpServletRequest, javax.servlet.http.HttpServletResponse);`
- `public static java.lang.String setPartialCheckOutOptions(javax.servlet.http.HttpServletRequest, javax.servlet.http.HttpServletResponse);`
- `public static java.lang.String setCartShipToCustomerParty(javax.servlet.http.HttpServletRequest, javax.servlet.http.HttpServletResponse);`
- `public static java.lang.String checkPaymentMethods(javax.servlet.http.HttpServletRequest, javax.servlet.http.HttpServletResponse);`
- `public static java.util.Map<java.lang.String, java.util.Map<java.lang.String, java.lang.Object>> getSelectedPaymentMethods(javax.servlet.http.HttpServletRequest);`
- `public static java.lang.String setCheckOutOptions(javax.servlet.http.HttpServletRequest, javax.servlet.http.HttpServletResponse);`
- `public static java.lang.String checkoutValidation(javax.servlet.http.HttpServletRequest, javax.servlet.http.HttpServletResponse);`
- `public static java.lang.String createOrder(javax.servlet.http.HttpServletRequest, javax.servlet.http.HttpServletResponse);`
- `public static java.lang.String calcTax(javax.servlet.http.HttpServletRequest, javax.servlet.http.HttpServletResponse);`
- `public static boolean explodeOrderItems(org.apache.ofbiz.entity.Delegator, org.apache.ofbiz.order.shoppingcart.ShoppingCart);`
- *(... 10 weitere Methoden)*

### `ShoppingCartItemManager` — class
Vollständiger Name: `org.apache.ofbiz.order.shoppingcart.components.ShoppingCartItemManager`
- `public org.apache.ofbiz.order.shoppingcart.components.ShoppingCartItemManager();`
- `public int addOrIncreaseItem(java.lang.String, double);`
- `public int size();`
- `public java.util.List<org.apache.ofbiz.order.shoppingcart.ShoppingCartItem> getItems();`
- `public java.util.List<org.apache.ofbiz.order.shoppingcart.ShoppingCartItem> items();`
- `public java.util.Iterator<org.apache.ofbiz.order.shoppingcart.ShoppingCartItem> iterator();`
- `public org.apache.ofbiz.order.shoppingcart.ShoppingCartItem getCartItem(int);`
- `public org.apache.ofbiz.order.shoppingcart.ShoppingCartItem findCartItem(int);`
- `public org.apache.ofbiz.order.shoppingcart.ShoppingCartItem findCartItem(java.lang.String);`
- `public java.util.List<org.apache.ofbiz.order.shoppingcart.ShoppingCartItem> findAllCartItems(java.lang.String);`
- `public int getItemIndex(org.apache.ofbiz.order.shoppingcart.ShoppingCartItem);`
- `public void addItem(int, org.apache.ofbiz.order.shoppingcart.ShoppingCartItem);`
- `public void removeCartItem(int);`
- `public void removeCartItem(int, org.apache.ofbiz.service.LocalDispatcher);`
- `public void removeCartItem(org.apache.ofbiz.order.shoppingcart.ShoppingCartItem, org.apache.ofbiz.service.LocalDispatcher);`
- *(... 10 weitere Methoden)*

### `QuoteServicesScript` [Groovy] — class
Vollständiger Name: `org.apache.ofbiz.order.quote.QuoteServicesScript`
- `public org.apache.ofbiz.order.quote.QuoteServicesScript();`
- `public org.apache.ofbiz.order.quote.QuoteServicesScript(groovy.lang.Binding);`
- `public static void main(java.lang.String...);`
- `public java.lang.Object run();`
- `public java.util.Map checkUpdateQuoteStatus();`
- `public java.util.Map getNextQuoteId();`
- `public java.util.Map quoteSequenceEnforced();`
- `public java.util.Map createQuote();`
- `public java.util.Map updateQuote();`
- `public java.util.Map copyQuote();`
- `public java.util.Map ensureWorkEffortAndCreateQuoteWorkEffort();`
- `public java.util.Map createQuoteItem();`
- `public java.util.Map updateQuoteItem();`
- `public java.util.Map removeQuoteItem();`
- `public java.util.Map copyQuoteItem();`
- *(... 8 weitere Methoden)*

### `ShoppingCartBuilder` — class
Vollständiger Name: `org.apache.ofbiz.order.shoppingcart.ShoppingCartBuilder`
- `public org.apache.ofbiz.order.shoppingcart.ShoppingCartBuilder();`
- `public org.apache.ofbiz.order.shoppingcart.ShoppingCartBuilder withDelegator(org.apache.ofbiz.entity.Delegator);`
- `public org.apache.ofbiz.order.shoppingcart.ShoppingCartBuilder withProductStoreId(java.lang.String);`
- `public org.apache.ofbiz.order.shoppingcart.ShoppingCartBuilder withWebSiteId(java.lang.String);`
- `public org.apache.ofbiz.order.shoppingcart.ShoppingCartBuilder withLocale(java.util.Locale);`
- `public org.apache.ofbiz.order.shoppingcart.ShoppingCartBuilder withCurrency(java.lang.String);`
- `public org.apache.ofbiz.order.shoppingcart.ShoppingCartBuilder withBillToCustomerPartyId(java.lang.String);`
- `public org.apache.ofbiz.order.shoppingcart.ShoppingCartBuilder withBillFromVendorPartyId(java.lang.String);`
- `public org.apache.ofbiz.order.shoppingcart.ShoppingCartBuilder withOrderType(java.lang.String);`
- `public org.apache.ofbiz.order.shoppingcart.ShoppingCartBuilder asSalesOrder();`
- `public org.apache.ofbiz.order.shoppingcart.ShoppingCartBuilder asPurchaseOrder();`
- `public org.apache.ofbiz.order.shoppingcart.ShoppingCartBuilder withItemsComponent(org.apache.ofbiz.order.shoppingcart.component.IShoppingCartItems);`
- `public org.apache.ofbiz.order.shoppingcart.ShoppingCartBuilder withPricingComponent(org.apache.ofbiz.order.shoppingcart.component.IShoppingCartPricing);`
- `public org.apache.ofbiz.order.shoppingcart.ShoppingCartBuilder withTaxesComponent(org.apache.ofbiz.order.shoppingcart.component.IShoppingCartTaxes);`
- `public org.apache.ofbiz.order.shoppingcart.ShoppingCartBuilder withShippingComponent(org.apache.ofbiz.order.shoppingcart.component.IShoppingCartShipping);`
- *(... 8 weitere Methoden)*

### `ShoppingCartPricing` — class
Vollständiger Name: `org.apache.ofbiz.order.shoppingcart.components.ShoppingCartPricing`
- `public org.apache.ofbiz.order.shoppingcart.components.ShoppingCartPricing(java.util.List<org.apache.ofbiz.order.shoppingcart.ShoppingCartItem>, java.util.List<org.apache.ofbiz.entity.GenericValue>);`
- `public java.math.BigDecimal getItemTotal();`
- `public java.math.BigDecimal getSubTotal();`
- `public java.math.BigDecimal getDisplaySubTotal();`
- `public java.math.BigDecimal getDisplayGrandTotal(java.math.BigDecimal, java.math.BigDecimal);`
- `public java.math.BigDecimal getGrandTotal(java.math.BigDecimal, java.math.BigDecimal);`
- `public java.math.BigDecimal getOrderOtherAdjustmentTotal();`
- `public java.math.BigDecimal getOrderGlobalAdjustments();`
- `public java.math.BigDecimal getSubTotalForPromotions();`
- `public java.math.BigDecimal getSubTotalForPromotions(java.util.Set<java.lang.String>);`
- `public java.math.BigDecimal getDisplayTaxIncluded();`
- `public java.math.BigDecimal getDisplayRecurringSubTotal();`
- `public java.math.BigDecimal getProductPromoTotal();`
- `public java.math.BigDecimal getGrandTotal();`
- `public java.math.BigDecimal getDisplayGrandTotal();`
- *(... 4 weitere Methoden)*

## Modul: party (52 Klassen, 372 public Methoden)

### `PartyServicesScript` [Groovy] — class
Vollständiger Name: `org.apache.ofbiz.party.party.PartyServicesScript`
- `public org.apache.ofbiz.party.party.PartyServicesScript();`
- `public org.apache.ofbiz.party.party.PartyServicesScript(groovy.lang.Binding);`
- `public static void main(java.lang.String...);`
- `public java.lang.Object run();`
- `public java.util.Map savePartyNameChange();`
- `public java.util.Map getPartyNameForDate();`
- `public java.util.Map getPostalAddressBoundary();`
- `public java.util.Map createPartyIdentifications();`
- `public java.util.Map setPartyProfileDefaults();`
- `public java.util.Map getPartiesByRelationship();`
- `public java.util.Map getParentOrganizations();`
- `public java.util.Map getRelatedParties();`
- `public java.util.Map getChildRoleTypes();`
- `public java.util.Map getPartyEmail();`
- `public java.util.Map getPartyTelephone();`
- *(... 16 weitere Methoden)*

### `PartyWorker` — class
Vollständiger Name: `org.apache.ofbiz.party.party.PartyWorker`
- `public static java.util.Map<java.lang.String, org.apache.ofbiz.entity.GenericValue> getPartyOtherValues(javax.servlet.ServletRequest, java.lang.String, java.lang.String, java.lang.String, java.lang.String);`
- `public static java.lang.String createClubId(org.apache.ofbiz.entity.Delegator, java.lang.String, int);`
- `public static org.apache.ofbiz.entity.GenericValue findPartyLatestContactMech(java.lang.String, java.lang.String, org.apache.ofbiz.entity.Delegator);`
- `public static org.apache.ofbiz.entity.GenericValue findPartyLatestPostalAddress(java.lang.String, org.apache.ofbiz.entity.Delegator);`
- `public static org.apache.ofbiz.entity.GenericValue findPartyLatestPostalAddressGeoPoint(java.lang.String, org.apache.ofbiz.entity.Delegator);`
- `public static org.apache.ofbiz.entity.GenericValue findPartyLatestTelecomNumber(java.lang.String, org.apache.ofbiz.entity.Delegator);`
- `public static org.apache.ofbiz.entity.GenericValue findPartyLatestUserLogin(java.lang.String, org.apache.ofbiz.entity.Delegator);`
- `public static java.sql.Timestamp findPartyLastLoginTime(java.lang.String, org.apache.ofbiz.entity.Delegator);`
- `public static java.util.Locale findPartyLastLocale(java.lang.String, org.apache.ofbiz.entity.Delegator);`
- `public static java.lang.String findFirstMatchingPartyId(org.apache.ofbiz.entity.Delegator, java.lang.String, java.lang.String, java.lang.String, java.lang.String, java.lang.String, java.lang.String, java.lang.String, java.lang.String, java.lang.String, java.lang.String) `
- `public static java.lang.String[] findFirstMatchingPartyAndContactMechId(org.apache.ofbiz.entity.Delegator, java.lang.String, java.lang.String, java.lang.String, java.lang.String, java.lang.String, java.lang.String, java.lang.String, java.lang.String, java.lang.String, java.lang.String) `
- `public static java.util.List<org.apache.ofbiz.entity.GenericValue> findMatchingPersonPostalAddresses(org.apache.ofbiz.entity.Delegator, java.lang.String, java.lang.String, java.lang.String, java.lang.String, java.lang.String, java.lang.String, java.lang.String, java.lang.String, java.lang.String, java.lang.String) `
- `public static java.util.List<org.apache.ofbiz.entity.GenericValue> findMatchingPartyAndPostalAddress(org.apache.ofbiz.entity.Delegator, java.lang.String, java.lang.String, java.lang.String, java.lang.String, java.lang.String, java.lang.String, java.lang.String, java.lang.String, java.lang.String, java.lang.String) `
- `public static java.util.List<org.apache.ofbiz.entity.GenericValue> findMatchingPartyPostalAddress(org.apache.ofbiz.entity.Delegator, java.lang.String, java.lang.String, java.lang.String, java.lang.String, java.lang.String, java.lang.String, java.lang.String, java.lang.String) `
- `public static java.lang.String makeMatchingString(org.apache.ofbiz.entity.Delegator, java.lang.String);`
- *(... 9 weitere Methoden)*

### `PartyServices` — class
Vollständiger Name: `org.apache.ofbiz.party.party.PartyServices`
- `public org.apache.ofbiz.party.party.PartyServices();`
- `public static java.util.Map<java.lang.String, java.lang.Object> createPerson(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> setPartyStatus(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> updatePerson(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> createPartyGroup(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> updatePartyGroup(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> createAffiliate(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> updateAffiliate(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> createPartyNote(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> getPartiesFromExactEmail(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> getPartiesFromPartOfEmail(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> getPartiesFromPartOfUserloginId(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> getPartiesFromPerson(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> getPartiesFromPartyGroup(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> getPartiesFromExternalId(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- *(... 8 weitere Methoden)*

### `ContactMechServicesScript` [Groovy] — class
Vollständiger Name: `org.apache.ofbiz.party.contact.ContactMechServicesScript`
- `public org.apache.ofbiz.party.contact.ContactMechServicesScript();`
- `public org.apache.ofbiz.party.contact.ContactMechServicesScript(groovy.lang.Binding);`
- `public static void main(java.lang.String...);`
- `public java.lang.Object run();`
- `public java.util.Map updateContactMech();`
- `public java.util.Map hasValidStateProvince(java.lang.String, java.lang.String);`
- `public java.util.Map createPostalAddress();`
- `public java.util.Map updatePostalAddress();`
- `public java.util.Map createTelecomNumber();`
- `public java.util.Map updateTelecomNumber();`
- `public java.util.Map createEmailAddress();`
- `public java.util.Map updateEmailAddress();`
- `public java.util.Map createFtpAddress();`
- `public java.util.Map updateFtpAddressWithHistory();`
- `public java.util.Map createPartyFtpAddress();`
- *(... 3 weitere Methoden)*

### `ContactMechWorker` — class
Vollständiger Name: `org.apache.ofbiz.party.contact.ContactMechWorker`
- `public static java.util.List<java.util.Map<java.lang.String, java.lang.Object>> getPartyContactMechValueMaps(org.apache.ofbiz.entity.Delegator, java.lang.String, boolean);`
- `public static java.util.List<java.util.Map<java.lang.String, java.lang.Object>> getPartyContactMechValueMaps(org.apache.ofbiz.entity.Delegator, java.lang.String, boolean, java.lang.String);`
- `public static java.util.List<java.util.Map<java.lang.String, java.lang.Object>> getPartyContactMechValueMaps(org.apache.ofbiz.entity.Delegator, java.lang.String, java.sql.Timestamp, java.lang.String);`
- `public static java.util.List<java.util.Map<java.lang.String, java.lang.Object>> getFacilityContactMechValueMaps(org.apache.ofbiz.entity.Delegator, java.lang.String, boolean);`
- `public static java.util.List<java.util.Map<java.lang.String, java.lang.Object>> getFacilityContactMechValueMaps(org.apache.ofbiz.entity.Delegator, java.lang.String, boolean, java.lang.String);`
- `public static java.util.List<java.util.Map<java.lang.String, java.lang.Object>> getFacilityContactMechValueMaps(org.apache.ofbiz.entity.Delegator, java.lang.String, java.sql.Timestamp, java.lang.String);`
- `public static java.util.List<java.util.Map<java.lang.String, org.apache.ofbiz.entity.GenericValue>> getOrderContactMechValueMaps(org.apache.ofbiz.entity.Delegator, java.lang.String);`
- `public static java.util.Collection<java.util.Map<java.lang.String, org.apache.ofbiz.entity.GenericValue>> getWorkEffortContactMechValueMaps(org.apache.ofbiz.entity.Delegator, java.lang.String);`
- `public static void getContactMechAndRelated(javax.servlet.ServletRequest, java.lang.String, java.util.Map<java.lang.String, java.lang.Object>);`
- `public static org.apache.ofbiz.entity.GenericValue getFacilityContactMechByPurpose(org.apache.ofbiz.entity.Delegator, java.lang.String, java.util.List<java.lang.String>);`
- `public static void getFacilityContactMechAndRelated(javax.servlet.ServletRequest, java.lang.String, java.util.Map<java.lang.String, java.lang.Object>);`
- `public static java.util.List<java.util.Map<java.lang.String, java.lang.Object>> getPartyPostalAddresses(javax.servlet.ServletRequest, java.lang.String, java.lang.String);`
- `public static java.util.Map<java.lang.String, java.lang.Object> getCurrentPostalAddress(javax.servlet.ServletRequest, java.lang.String, java.lang.String);`
- `public static boolean isUspsAddress(org.apache.ofbiz.entity.GenericValue);`
- `public static boolean isCompanyAddress(org.apache.ofbiz.entity.GenericValue, java.lang.String);`
- *(... 3 weitere Methoden)*

### `PartyContentWrapper` — class
Vollständiger Name: `org.apache.ofbiz.party.content.PartyContentWrapper`
- `public org.apache.ofbiz.party.content.PartyContentWrapper(org.apache.ofbiz.service.LocalDispatcher, org.apache.ofbiz.entity.GenericValue, java.util.Locale, java.lang.String);`
- `public org.apache.ofbiz.party.content.PartyContentWrapper(org.apache.ofbiz.entity.GenericValue, javax.servlet.http.HttpServletRequest);`
- `public java.lang.String get(java.lang.String, boolean, java.lang.String);`
- `public org.apache.ofbiz.base.util.StringUtil$StringWrapper get(java.lang.String, java.lang.String);`
- `public java.lang.String getId(java.lang.String);`
- `public java.util.List<java.lang.String> getList(java.lang.String);`
- `public java.lang.String getContent(java.lang.String, boolean, java.lang.String);`
- `public java.lang.String getContent(java.lang.String, java.lang.String);`
- `public static java.lang.String getPartyContentAsText(org.apache.ofbiz.entity.GenericValue, java.lang.String, javax.servlet.http.HttpServletRequest, java.lang.String);`
- `public static java.lang.String getPartyContentAsText(org.apache.ofbiz.entity.GenericValue, java.lang.String, java.util.Locale, org.apache.ofbiz.service.LocalDispatcher, java.lang.String);`
- `public static java.lang.String getPartyContentAsText(org.apache.ofbiz.entity.GenericValue, java.lang.String, java.util.Locale, java.lang.String, org.apache.ofbiz.entity.Delegator, org.apache.ofbiz.service.LocalDispatcher, boolean, java.lang.String);`
- `public static java.lang.String getPartyContentAsText(org.apache.ofbiz.entity.GenericValue, java.lang.String, java.lang.String, java.util.Locale, java.lang.String, org.apache.ofbiz.entity.Delegator, org.apache.ofbiz.service.LocalDispatcher, boolean, java.lang.String);`
- `public static void getPartyContentAsText(java.lang.String, java.lang.String, org.apache.ofbiz.entity.GenericValue, java.lang.String, java.util.Locale, java.lang.String, org.apache.ofbiz.entity.Delegator, org.apache.ofbiz.service.LocalDispatcher, java.io.Writer) `
- `public static void getPartyContentAsText(java.lang.String, java.lang.String, org.apache.ofbiz.entity.GenericValue, java.lang.String, java.util.Locale, java.lang.String, org.apache.ofbiz.entity.Delegator, org.apache.ofbiz.service.LocalDispatcher, java.io.Writer, boolean) `
- `public static java.util.List<java.lang.String> getPartyContentTextList(org.apache.ofbiz.entity.GenericValue, java.lang.String, java.util.Locale, java.lang.String, org.apache.ofbiz.entity.Delegator, org.apache.ofbiz.service.LocalDispatcher) `
- *(... 2 weitere Methoden)*

### `CommunicationEventServicesScript` [Groovy] — class
Vollständiger Name: `org.apache.ofbiz.party.communication.CommunicationEventServicesScript`
- `public org.apache.ofbiz.party.communication.CommunicationEventServicesScript();`
- `public org.apache.ofbiz.party.communication.CommunicationEventServicesScript(groovy.lang.Binding);`
- `public static void main(java.lang.String...);`
- `public java.lang.Object run();`
- `public java.util.Map createCommunicationEvent();`
- `public java.util.Map createCommunicationEventWithoutPermission();`
- `public java.util.Map updateCommunicationEvent();`
- `public java.util.Map deleteCommunicationEvent();`
- `public java.util.Map deleteCommunicationEventWorkEffort();`
- `public java.util.Map createCommunicationEventRole();`
- `public java.util.Map removeCommunicationEventRole();`
- `public java.util.Map sendEmailDated();`
- `public java.util.Map setCommunicationEventStatus();`
- `public java.util.Map setCommEventRoleToRead();`
- `public java.util.Map setCommunicationEventRoleStatus();`
- *(... 1 weitere Methoden)*

### `PartyPermissionServices` [Groovy] — class
Vollständiger Name: `org.apache.ofbiz.party.party.PartyPermissionServices`
- `public org.apache.ofbiz.party.party.PartyPermissionServices();`
- `public org.apache.ofbiz.party.party.PartyPermissionServices(groovy.lang.Binding);`
- `public static void main(java.lang.String...);`
- `public java.lang.Object run();`
- `public java.util.Map basePermissionCheck();`
- `public java.util.Map partyIdPermissionCheck(java.util.Map);`
- `public java.util.Map basePlusPartyIdPermissionCheck();`
- `public java.util.Map partyStatusPermissionCheck();`
- `public java.util.Map partyGroupPermissionCheck();`
- `public java.util.Map partyDatasourcePermissionCheck();`
- `public java.util.Map partyRolePermissionCheck();`
- `public java.util.Map partyRelationshipPermissionCheck();`
- `public java.util.Map partyContactMechPermissionCheck();`
- `public java.util.Map accAndDecPartyInvitationPermissionCheck();`
- `public java.util.Map cancelPartyInvitationPermissionCheck();`
- *(... 1 weitere Methoden)*

### `ContactMechServices` — class
Vollständiger Name: `org.apache.ofbiz.party.contact.ContactMechServices`
- `public org.apache.ofbiz.party.contact.ContactMechServices();`
- `public static java.util.Map<java.lang.String, java.lang.Object> createContactMech(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> updateContactMech(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> deleteContactMech(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> createPostalAddress(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> updatePostalAddress(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> createTelecomNumber(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> updateTelecomNumber(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> createEmailAddress(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> updateEmailAddress(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> createPartyContactMechPurpose(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> getPartyContactMechValueMaps(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> copyPartyContactMechs(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> createEmailAddressVerification(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`

### `CommunicationEventServices` — class
Vollständiger Name: `org.apache.ofbiz.party.communication.CommunicationEventServices`
- `public org.apache.ofbiz.party.communication.CommunicationEventServices();`
- `public static java.util.Map<java.lang.String, java.lang.Object> sendCommEventAsEmail(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> sendCommEventAsFtp(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ?>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> sendEmailToContactList(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> setCommEventComplete(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> createCommEventFromFtpTransfer(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> createCommEventFromEmail(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> updateCommEventAfterEmail(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> storeIncomingEmail(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> processBouncedMessage(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> logIncomingMessage(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public static java.lang.String markCommunicationAsRead(javax.servlet.http.HttpServletRequest, javax.servlet.http.HttpServletResponse);`

### `PartyContactMechTests` [Groovy] — class
Vollständiger Name: `org.apache.ofbiz.party.party.test.PartyContactMechTests`
- `public org.apache.ofbiz.party.party.test.PartyContactMechTests(java.lang.String);`
- `public void testUpdatePartyEmailAddress();`
- `public void testUpdatePartyTelecomNumber();`
- `public void testUpdatePartyPostalAddress();`
- `public void testCreatePartyEmailAddress();`
- `public void testCreatePartyTelecomNumber();`
- `public void testCreateUpdatePartyTelecomNumberWithCreate();`
- `public void testCreateUpdatePartyTelecomNumberWithUpdate();`
- `public void testCreateUpdatePartyEmailAddressWithCreate();`
- `public void testCreateUpdatePartyEmailAddressWithUpdate();`
- `public groovy.lang.MetaClass getMetaClass();`
- `public void setMetaClass(groovy.lang.MetaClass);`

### `PartySimpleMethods` [Groovy] — class
Vollständiger Name: `org.apache.ofbiz.party.party.PartySimpleMethods`
- `public org.apache.ofbiz.party.party.PartySimpleMethods();`
- `public org.apache.ofbiz.party.party.PartySimpleMethods(groovy.lang.Binding);`
- `public static void main(java.lang.String...);`
- `public java.lang.Object run();`
- `public java.util.Map createPartyGroupRoleAndContactMechs();`
- `public java.util.Map resolvePartyGroupMap();`
- `public java.util.Map resolvePostalAddressMap();`
- `public java.util.Map resolveTelecomNumberMap();`
- `public java.util.Map resolveEmailAddressMap();`
- `public java.util.Map resolvePartyProcessMap(java.lang.String, java.lang.String);`

### `PartyInvitationServices` [Groovy] — class
Vollständiger Name: `org.apache.ofbiz.party.party.PartyInvitationServices`
- `public org.apache.ofbiz.party.party.PartyInvitationServices();`
- `public org.apache.ofbiz.party.party.PartyInvitationServices(groovy.lang.Binding);`
- `public static void main(java.lang.String...);`
- `public java.lang.Object run();`
- `public java.util.Map createPartyInvitation();`
- `public java.util.Map updatePartyInvitation();`
- `public java.util.Map acceptPartyInvitation();`

### `ContactMechWorkerTests` [Groovy] — class
Vollständiger Name: `org.apache.ofbiz.party.party.test.ContactMechWorkerTests`
- `public org.apache.ofbiz.party.party.test.ContactMechWorkerTests(java.lang.String);`
- `public void testPartyContactMechResolution();`
- `public void testOrderContactMechResolution();`
- `public void testWorkEffortContactMechResolution();`
- `public groovy.lang.MetaClass getMetaClass();`
- `public void setMetaClass(groovy.lang.MetaClass);`

### `ContactHelper` — class
Vollständiger Name: `org.apache.ofbiz.party.contact.ContactHelper`
- `public static java.util.Collection<org.apache.ofbiz.entity.GenericValue> getContactMech(org.apache.ofbiz.entity.GenericValue, boolean);`
- `public static java.util.Collection<org.apache.ofbiz.entity.GenericValue> getContactMechByType(org.apache.ofbiz.entity.GenericValue, java.lang.String, boolean);`
- `public static java.util.Collection<org.apache.ofbiz.entity.GenericValue> getContactMechByPurpose(org.apache.ofbiz.entity.GenericValue, java.lang.String, boolean);`
- `public static java.util.Collection<org.apache.ofbiz.entity.GenericValue> getContactMech(org.apache.ofbiz.entity.GenericValue, java.lang.String, java.lang.String, boolean);`
- `public static java.lang.String formatCreditCard(org.apache.ofbiz.entity.GenericValue);`

### `EditShoppingList` [Groovy] — class
Vollständiger Name: `org.apache.ofbiz.party.party.EditShoppingList`
- `public org.apache.ofbiz.party.party.EditShoppingList();`
- `public org.apache.ofbiz.party.party.EditShoppingList(groovy.lang.Binding);`
- `public static void main(java.lang.String...);`
- `public java.lang.Object run();`
- `public static void __$swapInit();`

### `LookupServices` [Groovy] — class
Vollständiger Name: `org.apache.ofbiz.party.party.LookupServices`
- `public org.apache.ofbiz.party.party.LookupServices();`
- `public org.apache.ofbiz.party.party.LookupServices(groovy.lang.Binding);`
- `public static void main(java.lang.String...);`
- `public java.lang.Object run();`
- `public java.util.Map lookupParty();`

### `PartyStatusChangeTests` [Groovy] — class
Vollständiger Name: `org.apache.ofbiz.party.party.test.PartyStatusChangeTests`
- `public org.apache.ofbiz.party.party.test.PartyStatusChangeTests(java.lang.String);`
- `public void testSetPartyStatusToDisabled();`
- `public void testSetPartyStatusToEnabled();`
- `public groovy.lang.MetaClass getMetaClass();`
- `public void setMetaClass(groovy.lang.MetaClass);`

### `FindCommEventContactMechs` [Groovy] — class
Vollständiger Name: `org.apache.ofbiz.party.communication.FindCommEventContactMechs`
- `public org.apache.ofbiz.party.communication.FindCommEventContactMechs();`
- `public org.apache.ofbiz.party.communication.FindCommEventContactMechs(groovy.lang.Binding);`
- `public static void main(java.lang.String...);`
- `public java.lang.Object run();`

### `GetMyCommunicationEventRole` [Groovy] — class
Vollständiger Name: `org.apache.ofbiz.party.communication.GetMyCommunicationEventRole`
- `public org.apache.ofbiz.party.communication.GetMyCommunicationEventRole();`
- `public org.apache.ofbiz.party.communication.GetMyCommunicationEventRole(groovy.lang.Binding);`
- `public static void main(java.lang.String...);`
- `public java.lang.Object run();`

## Modul: product (181 Klassen, 1256 public Methoden)

### `ProductWorker` — class
Vollständiger Name: `org.apache.ofbiz.product.product.ProductWorker`
- `public static boolean shippingApplies(org.apache.ofbiz.entity.GenericValue);`
- `public static boolean isBillableToAddress(org.apache.ofbiz.entity.GenericValue, org.apache.ofbiz.entity.GenericValue);`
- `public static boolean isShippableToAddress(org.apache.ofbiz.entity.GenericValue, org.apache.ofbiz.entity.GenericValue);`
- `public static boolean isSerialized(org.apache.ofbiz.entity.Delegator, java.lang.String);`
- `public static boolean taxApplies(org.apache.ofbiz.entity.GenericValue);`
- `public static java.lang.String getInstanceAggregatedId(org.apache.ofbiz.entity.Delegator, java.lang.String) `
- `public static java.lang.String getAggregatedInstanceId(org.apache.ofbiz.entity.Delegator, java.lang.String, java.lang.String) `
- `public static java.util.List<org.apache.ofbiz.entity.GenericValue> getAggregatedAssocs(org.apache.ofbiz.entity.Delegator, java.lang.String) `
- `public static java.lang.String getVariantVirtualId(org.apache.ofbiz.entity.GenericValue) `
- `public static java.util.List<org.apache.ofbiz.entity.GenericValue> getVariantVirtualAssocs(org.apache.ofbiz.entity.GenericValue) `
- `public static boolean isProductInventoryAvailableByFacility(org.apache.ofbiz.product.config.ProductConfigWrapper, java.lang.String, java.math.BigDecimal, org.apache.ofbiz.service.LocalDispatcher);`
- `public static java.util.Set<org.apache.ofbiz.entity.GenericValue> getVariantDistinguishingFeatures(org.apache.ofbiz.entity.GenericValue) `
- `public static java.lang.String getGwpAlternativeOptionName(org.apache.ofbiz.service.LocalDispatcher, org.apache.ofbiz.entity.Delegator, java.lang.String, java.util.Locale);`
- `public static java.util.List<org.apache.ofbiz.entity.GenericValue> getProductFeaturesByApplTypeId(org.apache.ofbiz.entity.Delegator, java.lang.String, java.lang.String);`
- `public static java.util.List<org.apache.ofbiz.entity.GenericValue> getProductFeaturesByApplTypeId(org.apache.ofbiz.entity.GenericValue, java.lang.String);`
- *(... 40 weitere Methoden)*

### `CatalogWorker` — class
Vollständiger Name: `org.apache.ofbiz.product.catalog.CatalogWorker`
- `public static java.lang.String getWebSiteId(javax.servlet.ServletRequest);`
- `public static org.apache.ofbiz.entity.GenericValue getWebSite(javax.servlet.ServletRequest);`
- `public static java.util.List<java.lang.String> getAllCatalogIds(javax.servlet.ServletRequest);`
- `public static java.util.List<org.apache.ofbiz.entity.GenericValue> getStoreCatalogs(javax.servlet.ServletRequest);`
- `public static java.util.List<org.apache.ofbiz.entity.GenericValue> getStoreCatalogs(org.apache.ofbiz.entity.Delegator, java.lang.String);`
- `public static java.util.List<org.apache.ofbiz.entity.GenericValue> getPartyCatalogs(javax.servlet.ServletRequest);`
- `public static java.util.List<org.apache.ofbiz.entity.GenericValue> getPartyCatalogs(org.apache.ofbiz.entity.Delegator, java.lang.String);`
- `public static java.util.List<org.apache.ofbiz.entity.GenericValue> getProdCatalogCategories(javax.servlet.ServletRequest, java.lang.String, java.lang.String);`
- `public static java.util.List<org.apache.ofbiz.entity.GenericValue> getProdCatalogCategories(org.apache.ofbiz.entity.Delegator, java.lang.String, java.lang.String);`
- `public static java.lang.String getCurrentCatalogId(javax.servlet.ServletRequest);`
- `public static java.util.List<java.lang.String> getCatalogIdsAvailable(javax.servlet.ServletRequest);`
- `public static java.util.List<java.lang.String> getCatalogIdsAvailable(org.apache.ofbiz.entity.Delegator, java.lang.String, java.lang.String);`
- `public static java.util.List<java.lang.String> getCatalogIdsAvailable(java.util.List<org.apache.ofbiz.entity.GenericValue>, java.util.List<org.apache.ofbiz.entity.GenericValue>);`
- `public static java.lang.String getCatalogName(javax.servlet.ServletRequest);`
- `public static java.lang.String getCatalogName(javax.servlet.ServletRequest, java.lang.String);`
- *(... 23 weitere Methoden)*

### `ProductServicesScript` [Groovy] — class
Vollständiger Name: `org.apache.ofbiz.product.product.product.ProductServicesScript`
- `public org.apache.ofbiz.product.product.product.ProductServicesScript();`
- `public org.apache.ofbiz.product.product.product.ProductServicesScript(groovy.lang.Binding);`
- `public static void main(java.lang.String...);`
- `public java.lang.Object run();`
- `public java.util.Map createProduct();`
- `public java.util.Map updateProduct();`
- `public java.util.Map updateProductQuickAdminName();`
- `public java.util.Map duplicateProduct();`
- `public java.util.Map forceIndexProductKeywords();`
- `public java.util.Map deleteProductKeywords();`
- `public java.util.Map indexProductKeywords();`
- `public java.util.Map discontinueProductSales();`
- `public java.util.Map countProductView();`
- `public java.util.Map createProductReview();`
- `public java.util.Map updateProductReview();`
- *(... 21 weitere Methoden)*

### `ShipmentServices` [Groovy] — class
Vollständiger Name: `org.apache.ofbiz.product.shipment.ShipmentServices`
- `public org.apache.ofbiz.product.shipment.ShipmentServices();`
- `public org.apache.ofbiz.product.shipment.ShipmentServices(groovy.lang.Binding);`
- `public static void main(java.lang.String...);`
- `public java.lang.Object run();`
- `public java.util.Map updateShipment();`
- `public java.util.Map createShipmentForReturn();`
- `public java.util.Map createShipmentAndItemsForReturn();`
- `public java.util.Map createShipmentAndItemsForVendorReturn();`
- `public java.util.Map setShipmentSettingsFromPrimaryOrder();`
- `public java.util.Map setShipmentSettingsFromFacilities();`
- `public java.util.Map sendShipmentScheduledNotification();`
- `public java.util.Map balanceItemIssuancesForShipment();`
- `public java.util.Map splitShipmentItemByQuantity();`
- `public java.util.Map createShipmentPackage();`
- `public java.util.Map updateShipmentPackage();`
- *(... 21 weitere Methoden)*

### `CategoryServicesScript` [Groovy] — class
Vollständiger Name: `org.apache.ofbiz.product.product.category.CategoryServicesScript`
- `public org.apache.ofbiz.product.product.category.CategoryServicesScript();`
- `public org.apache.ofbiz.product.product.category.CategoryServicesScript(groovy.lang.Binding);`
- `public static void main(java.lang.String...);`
- `public java.lang.Object run();`
- `public java.util.Map createProductCategory();`
- `public java.util.Map updateProductCategory();`
- `public java.util.Map addProductToCategories();`
- `public java.util.Map removeProductFromCategory();`
- `public java.util.Map addPartyToCategory();`
- `public java.util.Map updatePartyToCategory();`
- `public java.util.Map removePartyFromCategory();`
- `public java.util.Map addProductCategoryToCategory();`
- `public java.util.Map addProductCategoryToCategories();`
- `public java.util.Map updateProductCategoryToCategory();`
- `public java.util.Map removeProductCategoryFromCategory();`
- *(... 15 weitere Methoden)*

### `ProductStoreWorker` — class
Vollständiger Name: `org.apache.ofbiz.product.store.ProductStoreWorker`
- `public static org.apache.ofbiz.entity.GenericValue getProductStore(java.lang.String, org.apache.ofbiz.entity.Delegator);`
- `public static org.apache.ofbiz.entity.GenericValue getProductStore(javax.servlet.ServletRequest);`
- `public static java.lang.String getProductStoreId(javax.servlet.ServletRequest);`
- `public static java.lang.String getStoreCurrencyUomId(javax.servlet.http.HttpServletRequest);`
- `public static java.util.Locale getStoreLocale(javax.servlet.http.HttpServletRequest);`
- `public static java.util.TimeZone getStoreTimeZone(javax.servlet.http.HttpServletRequest);`
- `public static java.lang.String determineSingleFacilityForStore(org.apache.ofbiz.entity.Delegator, java.lang.String);`
- `public static boolean autoSaveCart(org.apache.ofbiz.entity.Delegator, java.lang.String);`
- `public static boolean autoSaveCart(org.apache.ofbiz.entity.GenericValue);`
- `public static java.lang.String getProductStorePayToPartyId(java.lang.String, org.apache.ofbiz.entity.Delegator);`
- `public static java.lang.String getProductStorePayToPartyId(org.apache.ofbiz.entity.GenericValue);`
- `public static java.lang.String getProductStorePaymentProperties(javax.servlet.ServletRequest, java.lang.String, java.lang.String, boolean);`
- `public static java.lang.String getProductStorePaymentProperties(org.apache.ofbiz.entity.Delegator, java.lang.String, java.lang.String, java.lang.String, boolean);`
- `public static org.apache.ofbiz.entity.GenericValue getProductStorePaymentSetting(org.apache.ofbiz.entity.Delegator, java.lang.String, java.lang.String, java.lang.String, boolean);`
- `public static java.util.List<org.apache.ofbiz.entity.GenericValue> getProductStoreShipmentMethods(org.apache.ofbiz.entity.Delegator, java.lang.String, java.lang.String, java.lang.String, java.lang.String);`
- *(... 14 weitere Methoden)*

### `ProductConfigWrapper` — class
Vollständiger Name: `org.apache.ofbiz.product.config.ProductConfigWrapper`
- `public org.apache.ofbiz.product.config.ProductConfigWrapper();`
- `public void setConfigId(java.lang.String);`
- `public org.apache.ofbiz.product.config.ProductConfigWrapper(org.apache.ofbiz.entity.Delegator, org.apache.ofbiz.service.LocalDispatcher, java.lang.String, java.lang.String, java.lang.String, java.lang.String, java.lang.String, java.util.Locale, org.apache.ofbiz.entity.GenericValue) `
- `public org.apache.ofbiz.product.config.ProductConfigWrapper(org.apache.ofbiz.product.config.ProductConfigWrapper);`
- `public void loadConfig(org.apache.ofbiz.entity.Delegator, java.lang.String) `
- `public void setSelected(java.lang.String, java.lang.Long, java.lang.String, java.lang.String) `
- `public void resetConfig();`
- `public void setDefaultConfig();`
- `public java.lang.String getConfigId();`
- `public org.apache.ofbiz.entity.Delegator getDelegator();`
- `public org.apache.ofbiz.service.LocalDispatcher getDispatcher();`
- `public int hashCode();`
- `public boolean equals(java.lang.Object);`
- `public java.lang.String toString();`
- `public java.util.List<org.apache.ofbiz.product.config.ProductConfigWrapper$ConfigItem> getQuestions();`
- *(... 10 weitere Methoden)*

### `ProductSearchSession` — class
Vollständiger Name: `org.apache.ofbiz.product.product.ProductSearchSession`
- `public org.apache.ofbiz.product.product.ProductSearchSession();`
- `public static org.apache.ofbiz.product.product.ProductSearchSession$ProductSearchOptions getProductSearchOptions(javax.servlet.http.HttpSession);`
- `public static void checkSaveSearchOptionsHistory(javax.servlet.http.HttpSession);`
- `public static java.util.List<org.apache.ofbiz.product.product.ProductSearchSession$ProductSearchOptions> getSearchOptionsHistoryList(javax.servlet.http.HttpSession);`
- `public static void clearSearchOptionsHistoryList(javax.servlet.http.HttpSession);`
- `public static void setCurrentSearchFromHistory(int, boolean, javax.servlet.http.HttpSession);`
- `public static java.lang.String clearSearchOptionsHistoryList(javax.servlet.http.HttpServletRequest, javax.servlet.http.HttpServletResponse);`
- `public static java.lang.String setCurrentSearchFromHistory(javax.servlet.http.HttpServletRequest, javax.servlet.http.HttpServletResponse);`
- `public static final java.lang.String checkDoKeywordOverride(javax.servlet.http.HttpServletRequest, javax.servlet.http.HttpServletResponse);`
- `public static java.util.ArrayList<java.lang.String> searchDo(javax.servlet.http.HttpSession, org.apache.ofbiz.entity.Delegator, java.lang.String);`
- `public static void searchClear(javax.servlet.http.HttpSession);`
- `public static java.util.List<java.lang.String> searchGetConstraintStrings(boolean, javax.servlet.http.HttpSession, org.apache.ofbiz.entity.Delegator);`
- `public static java.lang.String searchGetSortOrderString(boolean, javax.servlet.http.HttpServletRequest);`
- `public static void searchSetSortOrder(org.apache.ofbiz.product.product.ProductSearch$ResultSortOrder, javax.servlet.http.HttpSession);`
- `public static void searchAddFeatureIdConstraints(java.util.Collection<java.lang.String>, java.lang.Boolean, javax.servlet.http.HttpServletRequest);`
- *(... 10 weitere Methoden)*

### `CategoryWorker` — class
Vollständiger Name: `org.apache.ofbiz.product.category.CategoryWorker`
- `public static java.lang.String getCatalogTopCategory(javax.servlet.ServletRequest, java.lang.String);`
- `public static void getCategoriesWithNoParent(javax.servlet.ServletRequest, java.lang.String);`
- `public static void getRelatedCategories(javax.servlet.ServletRequest, java.lang.String, boolean);`
- `public static void getRelatedCategories(javax.servlet.ServletRequest, java.lang.String, java.lang.String, boolean);`
- `public static void getRelatedCategories(javax.servlet.ServletRequest, java.lang.String, java.lang.String, boolean, boolean);`
- `public static java.util.List<org.apache.ofbiz.entity.GenericValue> getRelatedCategoriesRet(javax.servlet.ServletRequest, java.lang.String, java.lang.String, boolean);`
- `public static java.util.List<org.apache.ofbiz.entity.GenericValue> getRelatedCategoriesRet(javax.servlet.ServletRequest, java.lang.String, java.lang.String, boolean, boolean);`
- `public static java.util.List<org.apache.ofbiz.entity.GenericValue> getRelatedCategoriesRet(javax.servlet.ServletRequest, java.lang.String, java.lang.String, boolean, boolean, boolean);`
- `public static java.util.List<org.apache.ofbiz.entity.GenericValue> getRelatedCategoriesRet(org.apache.ofbiz.entity.Delegator, java.lang.String, java.lang.String, boolean, boolean, boolean);`
- `public static boolean isCategoryEmpty(org.apache.ofbiz.entity.GenericValue);`
- `public static long categoryMemberCount(org.apache.ofbiz.entity.GenericValue);`
- `public static long categoryRollupCount(org.apache.ofbiz.entity.GenericValue);`
- `public static void setTrail(javax.servlet.ServletRequest, java.lang.String);`
- `public static void setTrail(javax.servlet.ServletRequest, java.lang.String, java.lang.String);`
- `public static java.util.List<java.lang.String> adjustTrail(java.util.List<java.lang.String>, java.lang.String, java.lang.String);`
- *(... 9 weitere Methoden)*

### `ProductEvents` — class
Vollständiger Name: `org.apache.ofbiz.product.product.ProductEvents`
- `public org.apache.ofbiz.product.product.ProductEvents();`
- `public static java.lang.String updateAllKeywords(javax.servlet.http.HttpServletRequest, javax.servlet.http.HttpServletResponse);`
- `public static java.lang.String updateProductAssoc(javax.servlet.http.HttpServletRequest, javax.servlet.http.HttpServletResponse);`
- `public static java.lang.String clearLastViewedCategories(javax.servlet.http.HttpServletRequest, javax.servlet.http.HttpServletResponse);`
- `public static java.lang.String clearLastViewedProducts(javax.servlet.http.HttpServletRequest, javax.servlet.http.HttpServletResponse);`
- `public static java.lang.String clearAllLastViewed(javax.servlet.http.HttpServletRequest, javax.servlet.http.HttpServletResponse);`
- `public static java.lang.String updateProductQuickAdminShipping(javax.servlet.http.HttpServletRequest, javax.servlet.http.HttpServletResponse);`
- `public static java.lang.String updateProductQuickAdminSelFeat(javax.servlet.http.HttpServletRequest, javax.servlet.http.HttpServletResponse);`
- `public static java.lang.String removeFeatureApplsByFeatureTypeId(javax.servlet.http.HttpServletRequest, javax.servlet.http.HttpServletResponse);`
- `public static java.lang.String removeProductFeatureAppl(javax.servlet.http.HttpServletRequest, javax.servlet.http.HttpServletResponse);`
- `public static java.lang.String addProductToCategories(javax.servlet.http.HttpServletRequest, javax.servlet.http.HttpServletResponse);`
- `public static java.lang.String updateProductCategoryMember(javax.servlet.http.HttpServletRequest, javax.servlet.http.HttpServletResponse);`
- `public static java.lang.String addProductFeatures(javax.servlet.http.HttpServletRequest, javax.servlet.http.HttpServletResponse);`
- `public static java.lang.String setDefaultStoreSettings(javax.servlet.http.HttpServletRequest, javax.servlet.http.HttpServletResponse);`
- `public static java.lang.String checkStoreCustomerRole(javax.servlet.http.HttpServletRequest, javax.servlet.http.HttpServletResponse);`
- *(... 7 weitere Methoden)*

### `ProductPromoCondServices` [Groovy] — class
Vollständiger Name: `org.apache.ofbiz.product.product.promo.ProductPromoCondServices`
- `public org.apache.ofbiz.product.product.promo.ProductPromoCondServices();`
- `public org.apache.ofbiz.product.product.promo.ProductPromoCondServices(groovy.lang.Binding);`
- `public static void main(java.lang.String...);`
- `public java.lang.Object run();`
- `public java.util.Map productAmount();`
- `public java.util.Map productTotal();`
- `public java.util.Map productQuant();`
- `public java.util.Map productNewACCT();`
- `public java.util.Map productPartyID();`
- `public java.util.Map productPartyGM();`
- `public java.util.Map productPartyClass();`
- `public java.util.Map productRoleType();`
- `public java.util.Map productGeoID();`
- `public java.util.Map productOrderTotal();`
- `public java.util.Map productOrderHist();`
- *(... 6 weitere Methoden)*

### `CatalogUrlSeoTransform` — class
Vollständiger Name: `org.apache.ofbiz.product.category.ftl.CatalogUrlSeoTransform`
- `public org.apache.ofbiz.product.category.ftl.CatalogUrlSeoTransform();`
- `public java.lang.String getStringArg(java.util.Map<?, ?>, java.lang.String);`
- `public java.io.Writer getWriter(java.io.Writer, java.util.Map) `
- `public static boolean isCategoryMapInitialed();`
- `public static java.util.Map<java.lang.String, java.lang.String> getCategoryNameIdMap();`
- `public static java.util.Map<java.lang.String, java.lang.String> getCategoryIdNameMap();`
- `public static synchronized void initCategoryMap(javax.servlet.http.HttpServletRequest);`
- `public static synchronized void initCategoryMap(javax.servlet.http.HttpServletRequest, org.apache.ofbiz.entity.Delegator);`
- `public static java.lang.String makeProductUrl(javax.servlet.http.HttpServletRequest, java.lang.String, java.lang.String, java.lang.String);`
- `public static java.lang.String makeCategoryUrl(javax.servlet.http.HttpServletRequest, java.lang.String, java.lang.String, java.lang.String, java.lang.String, java.lang.String, java.lang.String);`
- `public static java.lang.String makeProductUrl(java.lang.String, java.util.List<java.lang.String>, java.lang.String, java.lang.String, java.lang.String, java.lang.String);`
- `public static boolean forwardProductUri(javax.servlet.http.HttpServletRequest, javax.servlet.http.HttpServletResponse, org.apache.ofbiz.entity.Delegator) `
- `public static boolean forwardProductUri(javax.servlet.http.HttpServletRequest, javax.servlet.http.HttpServletResponse, org.apache.ofbiz.entity.Delegator, java.lang.String) `
- `public static boolean forwardUri(javax.servlet.http.HttpServletRequest, javax.servlet.http.HttpServletResponse, org.apache.ofbiz.entity.Delegator, java.lang.String) `
- `public static boolean forwardCategoryUri(javax.servlet.http.HttpServletRequest, javax.servlet.http.HttpServletResponse, org.apache.ofbiz.entity.Delegator, java.lang.String) `
- *(... 2 weitere Methoden)*

### `CatalogServices` [Groovy] — class
Vollständiger Name: `org.apache.ofbiz.product.product.catalog.CatalogServices`
- `public org.apache.ofbiz.product.product.catalog.CatalogServices();`
- `public org.apache.ofbiz.product.product.catalog.CatalogServices(groovy.lang.Binding);`
- `public static void main(java.lang.String...);`
- `public java.lang.Object run();`
- `public java.util.Map getAllCategories();`
- `public java.util.Map getRelatedCategories();`
- `public java.util.Map checkImageUrlForAllCategories();`
- `public java.util.Map checkImageUrlForCategoryAndProduct();`
- `public void fileImageExists(java.lang.String, java.lang.String, java.util.Map<?, ?>, java.util.List<?>, java.util.List<?>);`
- `public java.util.Map checkImageUrlForCategory();`
- `public java.util.Map checkImageUrlForProduct();`
- `public java.util.Map imageUrlCheck(org.apache.ofbiz.entity.GenericValue, java.lang.String, java.util.Map<java.lang.Object, java.lang.Object>);`
- `public java.util.Map checkImageUrl();`
- `public java.util.Map catalogPermissionCheck();`
- `public java.util.Map prodCatalogToPartyPermissionCheck();`
- *(... 2 weitere Methoden)*

### `ProductTest` [Groovy] — class
Vollständiger Name: `org.apache.ofbiz.product.product.test.ProductTest`
- `public org.apache.ofbiz.product.product.test.ProductTest(java.lang.String);`
- `public void testCreateProduct();`
- `public void testUpdateProduct();`
- `public void testDuplicateProduct();`
- `public void testQuickAddVariant();`
- `public void testDeleteProductKeywords();`
- `public void testDiscontinueProductSales();`
- `public void testCreateProductReview();`
- `public void testUpdateProductReview();`
- `public void testFindProductById();`
- `public void testCreateProductPrice();`
- `public void testUpdateProductPrice();`
- `public void testDeleteProductPrice();`
- `public void testCreateProductCategory();`
- `public groovy.lang.MetaClass getMetaClass();`
- *(... 1 weitere Methoden)*

### `ProductPromoCondTests` [Groovy] — class
Vollständiger Name: `org.apache.ofbiz.product.product.test.ProductPromoCondTests`
- `public org.apache.ofbiz.product.product.test.ProductPromoCondTests(java.lang.String);`
- `public void testPartyIdPromo();`
- `public void testNewACCTPromo();`
- `public void testPartyClassPromo();`
- `public void testPartyGMPromo();`
- `public void testRoleTypePromo();`
- `public void testCondGeoIdPromo();`
- `public void testCondOrderTotalPromo();`
- `public void testRecurrencePromo();`
- `public void testShipTotalPromo();`
- `public void testProductAmountPromo();`
- `public void testProductTotalPromo();`
- `public groovy.lang.MetaClass getMetaClass();`
- `public void setMetaClass(groovy.lang.MetaClass);`
- `public static void __$swapInit();`

### `CostServices` [Groovy] — class
Vollständiger Name: `org.apache.ofbiz.product.product.cost.CostServices`
- `public org.apache.ofbiz.product.product.cost.CostServices();`
- `public org.apache.ofbiz.product.product.cost.CostServices(groovy.lang.Binding);`
- `public static void main(java.lang.String...);`
- `public java.lang.Object run();`
- `public java.util.Map cancelCostComponents();`
- `public java.util.Map recreateCostComponent();`
- `public java.util.Map getProductCost();`
- `public java.util.Map getTaskCost();`
- `public java.util.Map calculateAllProductsCosts();`
- `public java.util.Map calculateProductCosts();`
- `public java.util.Map calculateProductAverageCost();`
- `public java.util.Map updateProductAverageCostOnReceiveInventory();`
- `public java.util.Map getProductAverageCost();`
- `public java.util.Map productCostPercentageFormula();`

### `ImageManagementServicesScript` [Groovy] — class
Vollständiger Name: `org.apache.ofbiz.product.product.imagemanagement.ImageManagementServicesScript`
- `public org.apache.ofbiz.product.product.imagemanagement.ImageManagementServicesScript();`
- `public org.apache.ofbiz.product.product.imagemanagement.ImageManagementServicesScript(groovy.lang.Binding);`
- `public static void main(java.lang.String...);`
- `public java.lang.Object run();`
- `public java.util.Map uploadProductImages();`
- `public java.util.Map removeProductContentAndImageFile();`
- `public java.util.Map removeProductContentForImageManagement();`
- `public java.util.Map setImageDetail();`
- `public java.util.Map updateStatusImageManagement();`
- `public java.util.Map addRejectedReasonImageManagement();`
- `public java.util.Map createImageContentApproval();`
- `public java.util.Map removeImageContentApproval();`
- `public java.util.Map resizeImages();`
- `public java.util.Map removeImageBySize();`

### `ProductServices` — class
Vollständiger Name: `org.apache.ofbiz.product.product.ProductServices`
- `public org.apache.ofbiz.product.product.ProductServices();`
- `public static java.util.Map<java.lang.String, java.lang.Object> prodFindAllVariants(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> prodFindSelectedVariant(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> prodFindFeatureTypes(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> prodMakeFeatureTree(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> prodGetFeatures(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> prodFindProduct(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> prodFindAssociatedByType(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> quickAddVariant(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> quickCreateVirtualWithVariants(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> updateProductIfAvailableFromShipment(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> addAdditionalViewForProduct(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>) `
- `public static java.util.Map<java.lang.String, java.lang.Object> findProductById(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> addImageForProductPromo(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`

### `ProductPromoActionServices` [Groovy] — class
Vollständiger Name: `org.apache.ofbiz.product.product.promo.ProductPromoActionServices`
- `public org.apache.ofbiz.product.product.promo.ProductPromoActionServices();`
- `public org.apache.ofbiz.product.product.promo.ProductPromoActionServices(groovy.lang.Binding);`
- `public static void main(java.lang.String...);`
- `public java.lang.Object run();`
- `public java.util.Map productGWP();`
- `public java.util.Map productActFreeShip();`
- `public java.util.Map productDISC();`
- `public java.util.Map productAMDISC();`
- `public java.util.Map productPrice();`
- `public java.util.Map productOrderPercent();`
- `public java.util.Map productOrderAmount();`
- `public java.util.Map productSpecialPrice();`
- `public java.util.Map productShipCharge();`
- `public java.util.Map productTaxPercent();`

### `ProductStoreServices` [Groovy] — class
Vollständiger Name: `org.apache.ofbiz.product.product.store.ProductStoreServices`
- `public org.apache.ofbiz.product.product.store.ProductStoreServices();`
- `public org.apache.ofbiz.product.product.store.ProductStoreServices(groovy.lang.Binding);`
- `public static void main(java.lang.String...);`
- `public java.lang.Object run();`
- `public java.util.Map createProductStore();`
- `public java.util.Map updateProductStore();`
- `public java.util.Map reserveStoreInventory();`
- `public java.util.Map isStoreInventoryRequired();`
- `public java.lang.String isStoreInventoryRequiredInline(org.apache.ofbiz.entity.GenericValue, org.apache.ofbiz.entity.GenericValue);`
- `public java.util.Map isStoreInventoryAvailable();`
- `public java.util.Map isStoreInventoryAvailableOrNotRequired();`
- `public java.util.Map checkProductStoreRelatedPermission(java.util.Map);`
- `public java.util.Map productStoreGenericPermission();`
- `public java.util.Map checkProductStoreGroupRollup();`

## Modul: security (10 Klassen, 61 public Methoden)

### `Security` — interface
Vollständiger Name: `org.apache.ofbiz.security.Security`
- `public abstract org.apache.ofbiz.entity.Delegator getDelegator();`
- `public abstract void setDelegator(org.apache.ofbiz.entity.Delegator);`
- `public abstract java.util.Iterator<org.apache.ofbiz.entity.GenericValue> findUserLoginSecurityGroupByUserLoginId(java.lang.String);`
- `public abstract boolean securityGroupPermissionExists(java.lang.String, java.lang.String);`
- `public abstract boolean hasPermission(java.lang.String, javax.servlet.http.HttpSession);`
- `public abstract boolean hasPermission(java.lang.String, org.apache.ofbiz.entity.GenericValue);`
- `public abstract boolean hasEntityPermission(java.lang.String, java.lang.String, javax.servlet.http.HttpSession);`
- `public abstract boolean hasEntityPermission(java.lang.String, java.lang.String, org.apache.ofbiz.entity.GenericValue);`
- `public abstract boolean hasRolePermission(java.lang.String, java.lang.String, java.lang.String, java.lang.String, javax.servlet.http.HttpSession);`
- `public abstract boolean hasRolePermission(java.lang.String, java.lang.String, java.lang.String, java.lang.String, org.apache.ofbiz.entity.GenericValue);`
- `public abstract boolean hasRolePermission(java.lang.String, java.lang.String, java.lang.String, java.util.List<java.lang.String>, org.apache.ofbiz.entity.GenericValue);`
- `public abstract boolean hasRolePermission(java.lang.String, java.lang.String, java.lang.String, java.util.List<java.lang.String>, javax.servlet.http.HttpSession);`
- `public abstract void clearUserData(org.apache.ofbiz.entity.GenericValue);`

### `CsrfUtil` — class
Vollständiger Name: `org.apache.ofbiz.security.CsrfUtil`
- `public static java.util.Map<java.lang.String, java.lang.String> getTokenMap(javax.servlet.http.HttpServletRequest, java.lang.String);`
- `public static java.lang.String generateTokenForNonAjax(javax.servlet.http.HttpServletRequest, java.lang.String);`
- `public static java.lang.String generateTokenForAjax(javax.servlet.http.HttpServletRequest);`
- `public static java.lang.String getTokenForAjax(javax.servlet.http.HttpSession);`
- `public static java.lang.String addOrUpdateTokenInUrl(java.lang.String, java.lang.String);`
- `public static java.lang.String addOrUpdateTokenInQueryString(java.lang.String, java.lang.String);`
- `public static void checkToken(javax.servlet.http.HttpServletRequest, java.lang.String) `
- `public static void cleanupTokenMap(javax.servlet.http.HttpSession);`
- `public static java.lang.String getTokenNameNonAjax();`
- `public static void setTokenNameNonAjax(java.lang.String);`
- `public static org.apache.ofbiz.security.ICsrfDefenseStrategy getStrategy();`
- `public static void setStrategy(org.apache.ofbiz.security.ICsrfDefenseStrategy);`

### `CsrfDefenseStrategy` — class
Vollständiger Name: `org.apache.ofbiz.security.CsrfDefenseStrategy`
- `public org.apache.ofbiz.security.CsrfDefenseStrategy();`
- `public java.lang.String generateToken();`
- `public int maxSubFolderInRequestUrlForTokenMapLookup(java.lang.String);`
- `public boolean modifySecurityCsrfToken(java.lang.String, java.lang.String, java.lang.String);`
- `public boolean keepTokenAfterUse(java.lang.String, java.lang.String);`
- `public void invalidTokenResponse(java.lang.String, javax.servlet.http.HttpServletRequest) `

### `NoCsrfDefenseStrategy` — class
Vollständiger Name: `org.apache.ofbiz.security.NoCsrfDefenseStrategy`
- `public org.apache.ofbiz.security.NoCsrfDefenseStrategy();`
- `public java.lang.String generateToken();`
- `public int maxSubFolderInRequestUrlForTokenMapLookup(java.lang.String);`
- `public boolean modifySecurityCsrfToken(java.lang.String, java.lang.String, java.lang.String);`
- `public boolean keepTokenAfterUse(java.lang.String, java.lang.String);`
- `public void invalidTokenResponse(java.lang.String, javax.servlet.http.HttpServletRequest);`

### `ICsrfDefenseStrategy` — interface
Vollständiger Name: `org.apache.ofbiz.security.ICsrfDefenseStrategy`
- `public abstract java.lang.String generateToken();`
- `public abstract int maxSubFolderInRequestUrlForTokenMapLookup(java.lang.String);`
- `public abstract boolean modifySecurityCsrfToken(java.lang.String, java.lang.String, java.lang.String);`
- `public abstract boolean keepTokenAfterUse(java.lang.String, java.lang.String);`
- `public abstract void invalidTokenResponse(java.lang.String, javax.servlet.http.HttpServletRequest) `

### `SecuredFreemarker` — class
Vollständiger Name: `org.apache.ofbiz.security.SecuredFreemarker`
- `public org.apache.ofbiz.security.SecuredFreemarker();`
- `public static boolean containsFreemarkerInterpolation(javax.servlet.http.HttpServletRequest, javax.servlet.http.HttpServletResponse, java.lang.String) `
- `public static boolean containsFreemarkerInterpolation(javax.servlet.http.HttpServletResponse, java.lang.String) `
- `public static boolean containsFreemarkerInterpolation(java.lang.String);`
- `public static java.util.Map<java.lang.String, java.lang.Object> sanitizeParameterMap(java.util.Map<java.lang.String, java.lang.Object>);`

### `SecuredUpload` — class
Vollständiger Name: `org.apache.ofbiz.security.SecuredUpload`
- `public org.apache.ofbiz.security.SecuredUpload();`
- `public static boolean isValidText(java.lang.String, java.util.List<java.lang.String>) `
- `public static boolean isValidText(java.lang.String, java.util.List<java.lang.String>, boolean) `
- `public static boolean isValidFileName(java.lang.String, org.apache.ofbiz.entity.Delegator) `
- `public static boolean isValidFile(java.lang.String, java.lang.String, org.apache.ofbiz.entity.Delegator) `

### `SecurityUtil` — class
Vollständiger Name: `org.apache.ofbiz.security.SecurityUtil`
- `public org.apache.ofbiz.security.SecurityUtil();`
- `public static boolean hasUserLoginAdminPermission(org.apache.ofbiz.entity.Delegator, java.lang.String);`
- `public static java.util.List<java.lang.String> hasUserLoginMorePermissionThan(org.apache.ofbiz.entity.Delegator, java.lang.String, java.lang.String);`
- `public static java.lang.String generateJwtToAuthenticateUserLogin(org.apache.ofbiz.entity.Delegator, java.lang.String) `
- `public static boolean authenticateUserLoginByJWT(org.apache.ofbiz.entity.Delegator, java.lang.String, java.lang.String);`

### `SecurityConfigurationException` — class
Vollständiger Name: `org.apache.ofbiz.security.SecurityConfigurationException`
- `public org.apache.ofbiz.security.SecurityConfigurationException(java.lang.String, java.lang.Throwable);`
- `public org.apache.ofbiz.security.SecurityConfigurationException(java.lang.String);`
- `public org.apache.ofbiz.security.SecurityConfigurationException();`

### `SecurityFactory` — class
Vollständiger Name: `org.apache.ofbiz.security.SecurityFactory`
- `public static org.apache.ofbiz.security.Security getInstance(org.apache.ofbiz.entity.Delegator) `

## Modul: securityext (2 Klassen, 9 public Methoden)

### `LoginEvents` — class
Vollständiger Name: `org.apache.ofbiz.securityext.login.LoginEvents`
- `public org.apache.ofbiz.securityext.login.LoginEvents();`
- `public static java.lang.String saveEntryParams(javax.servlet.http.HttpServletRequest, javax.servlet.http.HttpServletResponse);`
- `public static java.lang.String forgotPassword(javax.servlet.http.HttpServletRequest, javax.servlet.http.HttpServletResponse);`
- `public static java.lang.String showPasswordHint(javax.servlet.http.HttpServletRequest, javax.servlet.http.HttpServletResponse);`
- `public static java.lang.String emailPasswordRequest(javax.servlet.http.HttpServletRequest, javax.servlet.http.HttpServletResponse);`
- `public static java.lang.String storeCheckLogin(javax.servlet.http.HttpServletRequest, javax.servlet.http.HttpServletResponse);`
- `public static java.lang.String storeLogin(javax.servlet.http.HttpServletRequest, javax.servlet.http.HttpServletResponse) `

### `CertificateServices` — class
Vollständiger Name: `org.apache.ofbiz.securityext.cert.CertificateServices`
- `public org.apache.ofbiz.securityext.cert.CertificateServices();`
- `public static java.util.Map<java.lang.String, java.lang.Object> importIssuerCertificate(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`

## Modul: service (126 Klassen, 1040 public Methoden)

### `ModelService` — class
Vollständiger Name: `org.apache.ofbiz.service.ModelService`
- `public void setName(java.lang.String);`
- `public void setDefinitionLocation(java.lang.String);`
- `public void setDescription(java.lang.String);`
- `public void setEngineName(java.lang.String);`
- `public void setNameSpace(java.lang.String);`
- `public void setAction(java.lang.String);`
- `public void setLocation(java.lang.String);`
- `public void setInvoke(java.lang.String);`
- `public void setDefaultEntityName(java.lang.String);`
- `public void setFromLoader(java.lang.String);`
- `public void setAuth(boolean);`
- `public void setExport(boolean);`
- `public void setDebug(boolean);`
- `public void setValidate(boolean);`
- `public void setUseTransaction(boolean);`
- *(... 99 weitere Methoden)*

### `ModelParam` — class
Vollständiger Name: `org.apache.ofbiz.service.ModelParam`
- `public org.apache.ofbiz.service.ModelParam();`
- `public org.apache.ofbiz.service.ModelParam(org.apache.ofbiz.service.ModelParam);`
- `public void addValidator(java.lang.String, java.lang.String, java.lang.String);`
- `public void addValidator(java.lang.String, java.lang.String, java.lang.String, java.lang.String);`
- `public java.lang.String getPrimaryFailMessage(java.util.Locale);`
- `public java.lang.String getFailMessage(java.util.Locale);`
- `public java.lang.String getShortDisplayDescription();`
- `public java.lang.String getName();`
- `public void setMode(java.lang.String);`
- `public java.util.List<org.apache.ofbiz.service.ModelParam$ModelParamValidator> getValidators();`
- `public void setFormDisplay(boolean);`
- `public void setDescription(java.lang.String);`
- `public void setOverrideOptional(boolean);`
- `public void setOverrideFormDisplay(boolean);`
- `public void setValidators(java.util.List<org.apache.ofbiz.service.ModelParam$ModelParamValidator>);`
- *(... 40 weitere Methoden)*

### `LocalDispatcher` — interface
Vollständiger Name: `org.apache.ofbiz.service.LocalDispatcher`
- `public abstract void disableEcas();`
- `public abstract void enableEcas();`
- `public abstract boolean isEcasDisabled();`
- `public abstract java.util.Map<java.lang.String, java.lang.Object> runSync(java.lang.String, java.util.Map<java.lang.String, ? extends java.lang.Object>) `
- `public abstract java.util.Map<java.lang.String, java.lang.Object> runSync(java.lang.String, java.util.Map<java.lang.String, ? extends java.lang.Object>, int, boolean) `
- `public abstract java.util.Map<java.lang.String, java.lang.Object> runSync(java.lang.String, int, boolean, java.lang.Object...) `
- `public abstract void runSyncIgnore(java.lang.String, java.util.Map<java.lang.String, ? extends java.lang.Object>) `
- `public abstract void runSyncIgnore(java.lang.String, java.util.Map<java.lang.String, ? extends java.lang.Object>, int, boolean) `
- `public abstract void runSyncIgnore(java.lang.String, int, boolean, java.lang.Object...) `
- `public abstract void runAsync(java.lang.String, java.util.Map<java.lang.String, ? extends java.lang.Object>, org.apache.ofbiz.service.GenericRequester, boolean, int, boolean) `
- `public abstract void runAsync(java.lang.String, org.apache.ofbiz.service.GenericRequester, boolean, int, boolean, java.lang.Object...) `
- `public abstract void runAsync(java.lang.String, java.util.Map<java.lang.String, ? extends java.lang.Object>, org.apache.ofbiz.service.GenericRequester, boolean) `
- `public abstract void runAsync(java.lang.String, org.apache.ofbiz.service.GenericRequester, boolean, java.lang.Object...) `
- `public abstract void runAsync(java.lang.String, java.util.Map<java.lang.String, ? extends java.lang.Object>, org.apache.ofbiz.service.GenericRequester) `
- `public abstract void runAsync(java.lang.String, org.apache.ofbiz.service.GenericRequester, java.lang.Object...) `
- *(... 30 weitere Methoden)*

### `MimeMessageWrapper` — class
Vollständiger Name: `org.apache.ofbiz.service.mail.MimeMessageWrapper`
- `public org.apache.ofbiz.service.mail.MimeMessageWrapper(javax.mail.Session, javax.mail.internet.MimeMessage);`
- `public org.apache.ofbiz.service.mail.MimeMessageWrapper(javax.mail.Session);`
- `public synchronized void setSession(javax.mail.Session);`
- `public synchronized javax.mail.Session getSession();`
- `public synchronized void setMessage(javax.mail.internet.MimeMessage);`
- `public synchronized javax.mail.internet.MimeMessage getMessage();`
- `public java.lang.String getFirstHeader(java.lang.String);`
- `public java.lang.String[] getHeader(java.lang.String);`
- `public javax.mail.Address[] getFrom();`
- `public javax.mail.Address[] getTo();`
- `public javax.mail.Address[] getCc();`
- `public javax.mail.Address[] getBcc();`
- `public java.lang.String getSubject();`
- `public java.lang.String getMessageId();`
- `public java.sql.Timestamp getSentDate();`
- *(... 16 weitere Methoden)*

### `ServiceUtil` — class
Vollständiger Name: `org.apache.ofbiz.service.ServiceUtil`
- `public static boolean isError(java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public static boolean isFailure(java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public static boolean isSuccess(java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> returnError(java.lang.String);`
- `public static java.util.Map<java.lang.String, java.lang.Object> returnError(java.lang.String, java.util.List<? extends java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> returnError(java.util.List<? extends java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> returnFailure(java.lang.String);`
- `public static java.util.Map<java.lang.String, java.lang.Object> returnFailure(java.util.List<? extends java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> returnFailure();`
- `public static java.util.Map<java.lang.String, java.lang.Object> returnError(java.lang.String, java.util.List<? extends java.lang.Object>, java.util.Map<java.lang.String, ? extends java.lang.Object>, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> returnProblem(java.lang.String, java.lang.String, java.util.List<? extends java.lang.Object>, java.util.Map<java.lang.String, ? extends java.lang.Object>, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> returnSuccess(java.lang.String);`
- `public static java.util.Map<java.lang.String, java.lang.Object> returnSuccess();`
- `public static java.util.Map<java.lang.String, java.lang.Object> returnSuccess(java.util.List<java.lang.String>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> returnMessage(java.lang.String, java.lang.String);`
- *(... 16 weitere Methoden)*

### `GenericAbstractDispatcher` — class
Vollständiger Name: `org.apache.ofbiz.service.GenericAbstractDispatcher`
- `public org.apache.ofbiz.service.DispatchContext getCtx();`
- `public void setCtx(org.apache.ofbiz.service.DispatchContext);`
- `public org.apache.ofbiz.service.ServiceDispatcher getDispatcher();`
- `public void setDispatcher(org.apache.ofbiz.service.ServiceDispatcher);`
- `public void setName(java.lang.String);`
- `public org.apache.ofbiz.service.GenericAbstractDispatcher();`
- `public void schedule(java.lang.String, java.lang.String, java.util.Map<java.lang.String, ? extends java.lang.Object>, long, int, int, int, long, int) `
- `public void schedule(java.lang.String, java.lang.String, long, int, int, int, long, int, java.lang.Object...) `
- `public void schedule(java.lang.String, java.lang.String, java.lang.String, java.util.Map<java.lang.String, ? extends java.lang.Object>, long, int, int, int, long, int) `
- `public void schedule(java.lang.String, java.lang.String, java.lang.String, long, int, int, int, long, int, java.lang.Object...) `
- `public void addRollbackService(java.lang.String, java.util.Map<java.lang.String, ? extends java.lang.Object>, boolean) `
- `public void addRollbackService(java.lang.String, boolean, java.lang.Object...) `
- `public void addCommitService(java.lang.String, java.util.Map<java.lang.String, ? extends java.lang.Object>, boolean) `
- `public void addCommitService(java.lang.String, boolean, java.lang.Object...) `
- `public void schedule(java.lang.String, java.util.Map<java.lang.String, ? extends java.lang.Object>, long, int, int, int, long) `
- *(... 15 weitere Methoden)*

### `GroovyBaseScript` [Groovy] — class
Vollständiger Name: `org.apache.ofbiz.service.engine.GroovyBaseScript`
- `public org.apache.ofbiz.service.engine.GroovyBaseScript();`
- `public java.lang.String getModule();`
- `public java.util.Map runService(java.lang.String, java.util.Map) `
- `public java.util.Map run(java.util.Map) `
- `public java.util.Map makeValue(java.lang.String) `
- `public java.util.Map makeValue(java.lang.String, java.util.Map) `
- `public org.apache.ofbiz.entity.util.EntityQuery from(java.lang.String);`
- `public org.apache.ofbiz.entity.util.EntityQuery from(org.apache.ofbiz.entity.model.DynamicViewEntity);`
- `public org.apache.ofbiz.entity.util.EntityQuery select(java.lang.String...);`
- `public org.apache.ofbiz.entity.util.EntityQuery select(java.util.Set<java.lang.String>);`
- `public org.apache.ofbiz.entity.GenericValue findOne(java.lang.String, java.util.Map<java.lang.String, ? extends java.lang.Object>, boolean);`
- `public java.lang.Object success();`
- `public java.lang.Object success(java.lang.String);`
- `public java.lang.Object success(java.util.Map);`
- `public java.lang.Object success(java.lang.String, java.util.Map);`
- *(... 11 weitere Methoden)*

### `RecurrenceInfo` — class
Vollständiger Name: `org.apache.ofbiz.service.calendar.RecurrenceInfo`
- `public org.apache.ofbiz.service.calendar.RecurrenceInfo(org.apache.ofbiz.entity.GenericValue) `
- `public void init() `
- `public java.lang.String getID();`
- `public java.util.Date getStartDate();`
- `public long getStartTime();`
- `public java.util.Iterator<org.apache.ofbiz.service.calendar.RecurrenceRule> getRecurrenceRuleIterator();`
- `public java.util.Iterator<java.util.Date> getRecurrenceDateIterator();`
- `public java.util.Iterator<org.apache.ofbiz.service.calendar.RecurrenceRule> getExceptionRuleIterator();`
- `public java.util.Iterator<java.util.Date> getExceptionDateIterator();`
- `public long getCurrentCount();`
- `public void incrementCurrentCount() `
- `public void incrementCurrentCount(boolean) `
- `public void remove() `
- `public long first();`
- `public long last();`
- *(... 9 weitere Methoden)*

### `ServiceDispatcher` — class
Vollständiger Name: `org.apache.ofbiz.service.ServiceDispatcher`
- `public static org.apache.ofbiz.service.LocalDispatcher getLocalDispatcher(java.lang.String, org.apache.ofbiz.entity.Delegator);`
- `public static org.apache.ofbiz.service.ServiceDispatcher getInstance(org.apache.ofbiz.entity.Delegator);`
- `public void register(org.apache.ofbiz.service.DispatchContext);`
- `public void deregister(org.apache.ofbiz.service.LocalDispatcher);`
- `public synchronized void registerCallback(java.lang.String, org.apache.ofbiz.service.GenericServiceCallback);`
- `public java.util.List<org.apache.ofbiz.service.GenericServiceCallback> getCallbacks(java.lang.String);`
- `public java.util.Map<java.lang.String, java.lang.Object> runSync(java.lang.String, org.apache.ofbiz.service.ModelService, java.util.Map<java.lang.String, ? extends java.lang.Object>) `
- `public void runSyncIgnore(java.lang.String, org.apache.ofbiz.service.ModelService, java.util.Map<java.lang.String, ? extends java.lang.Object>) `
- `public java.util.Map<java.lang.String, java.lang.Object> runSync(java.lang.String, org.apache.ofbiz.service.ModelService, java.util.Map<java.lang.String, ? extends java.lang.Object>, boolean) `
- `public void runAsync(java.lang.String, org.apache.ofbiz.service.ModelService, java.util.Map<java.lang.String, ? extends java.lang.Object>, org.apache.ofbiz.service.GenericRequester, boolean) `
- `public void runAsync(java.lang.String, org.apache.ofbiz.service.ModelService, java.util.Map<java.lang.String, ? extends java.lang.Object>, boolean) `
- `public org.apache.ofbiz.service.engine.GenericEngine getGenericEngine(java.lang.String) `
- `public org.apache.ofbiz.service.job.JobManager getJobManager();`
- `public org.apache.ofbiz.service.jms.JmsListenerFactory getJMSListenerFactory();`
- `public org.apache.ofbiz.entity.Delegator getDelegator();`
- *(... 8 weitere Methoden)*

### `RecurrenceRule` — class
Vollständiger Name: `org.apache.ofbiz.service.calendar.RecurrenceRule`
- `public org.apache.ofbiz.service.calendar.RecurrenceRule(org.apache.ofbiz.entity.GenericValue) `
- `public void init() `
- `public long getEndTime();`
- `public long getCount();`
- `public java.lang.String getFrequencyName();`
- `public int getFrequency();`
- `public long getInterval();`
- `public int getIntervalInt();`
- `public long next(long, long, long);`
- `public long validCurrent(long, long, long);`
- `public boolean isValid(java.util.Date, java.util.Date);`
- `public boolean isValid(long, long);`
- `public void remove() `
- `public java.lang.String primaryKey();`
- `public static org.apache.ofbiz.service.calendar.RecurrenceRule makeRule(org.apache.ofbiz.entity.Delegator, int, int, int) `
- *(... 2 weitere Methoden)*

### `ModelNotification` — class
Vollständiger Name: `org.apache.ofbiz.service.ModelNotification`
- `public org.apache.ofbiz.service.ModelNotification();`
- `public java.lang.String getNotificationGroupName();`
- `public void setNotificationGroupName(java.lang.String);`
- `public java.lang.String getNotificationEvent();`
- `public void setNotificationEvent(java.lang.String);`
- `public java.lang.String getNotificationMode();`
- `public void setNotificationMode(java.lang.String);`
- `public void callNotify(org.apache.ofbiz.service.DispatchContext, org.apache.ofbiz.service.ModelService, java.util.Map<java.lang.String, ? extends java.lang.Object>, java.util.Map<java.lang.String, java.lang.Object>);`
- `public java.util.Map<java.lang.String, java.lang.Object> buildContext(java.util.Map<java.lang.String, ? extends java.lang.Object>, java.util.Map<java.lang.String, java.lang.Object>, org.apache.ofbiz.service.ModelService) `
- `public java.lang.String buildTo();`
- `public java.lang.String buildCc();`
- `public java.lang.String buildBcc();`
- `public java.lang.String buildFrom();`
- `public java.lang.String getSubject();`
- `public java.lang.String getScreen();`
- *(... 2 weitere Methoden)*

### `ModelPermission` — class
Vollständiger Name: `org.apache.ofbiz.service.ModelPermission`
- `public org.apache.ofbiz.service.ModelPermission();`
- `public java.lang.String toString();`
- `public java.util.Map<java.lang.String, java.lang.Object> evalPermission(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public void setPermissionServiceName(java.lang.String);`
- `public void setPermissionType(int);`
- `public void setPermissionMainAction(java.lang.String);`
- `public void setPermissionResourceDesc(java.lang.String);`
- `public void setPermissionRequireNewTransaction(boolean);`
- `public void setPermissionReturnErrorOnFailure(boolean);`
- `public void setNameOrRole(java.lang.String);`
- `public void setAction(java.lang.String);`
- `public static int getPERMISSION();`
- `public static int getEntityPermission();`
- `public java.lang.String getAction();`
- `public void setAuth(java.lang.Boolean);`
- *(... 2 weitere Methoden)*

### `RemoteDispatcherImpl` — class
Vollständiger Name: `org.apache.ofbiz.service.rmi.RemoteDispatcherImpl`
- `public org.apache.ofbiz.service.rmi.RemoteDispatcherImpl(org.apache.ofbiz.service.LocalDispatcher, java.rmi.server.RMIClientSocketFactory, java.rmi.server.RMIServerSocketFactory) `
- `public java.util.Map<java.lang.String, java.lang.Object> runSync(java.lang.String, java.util.Map<java.lang.String, ? extends java.lang.Object>) `
- `public java.util.Map<java.lang.String, java.lang.Object> runSync(java.lang.String, java.util.Map<java.lang.String, ? extends java.lang.Object>, int, boolean) `
- `public void runSyncIgnore(java.lang.String, java.util.Map<java.lang.String, ? extends java.lang.Object>) `
- `public void runSyncIgnore(java.lang.String, java.util.Map<java.lang.String, ? extends java.lang.Object>, int, boolean) `
- `public void runAsync(java.lang.String, java.util.Map<java.lang.String, ? extends java.lang.Object>, org.apache.ofbiz.service.GenericRequester, boolean, int, boolean) `
- `public void runAsync(java.lang.String, java.util.Map<java.lang.String, ? extends java.lang.Object>, org.apache.ofbiz.service.GenericRequester, boolean) `
- `public void runAsync(java.lang.String, java.util.Map<java.lang.String, ? extends java.lang.Object>, org.apache.ofbiz.service.GenericRequester) `
- `public void runAsync(java.lang.String, java.util.Map<java.lang.String, ? extends java.lang.Object>, boolean) `
- `public void runAsync(java.lang.String, java.util.Map<java.lang.String, ? extends java.lang.Object>) `
- `public org.apache.ofbiz.service.GenericResultWaiter runAsyncWait(java.lang.String, java.util.Map<java.lang.String, ? extends java.lang.Object>, boolean) `
- `public org.apache.ofbiz.service.GenericResultWaiter runAsyncWait(java.lang.String, java.util.Map<java.lang.String, ? extends java.lang.Object>) `
- `public void schedule(java.lang.String, java.util.Map<java.lang.String, ? extends java.lang.Object>, long, int, int, int, long) `
- `public void schedule(java.lang.String, java.util.Map<java.lang.String, ? extends java.lang.Object>, long, int, int, int) `
- `public void schedule(java.lang.String, java.util.Map<java.lang.String, ? extends java.lang.Object>, long, int, int, long) `
- *(... 2 weitere Methoden)*

### `TemporalExpressionPrinter` — class
Vollständiger Name: `org.apache.ofbiz.service.calendar.TemporalExpressionPrinter`
- `public org.apache.ofbiz.service.calendar.TemporalExpressionPrinter(org.apache.ofbiz.service.calendar.TemporalExpression);`
- `public org.apache.ofbiz.service.calendar.TemporalExpressionPrinter(org.apache.ofbiz.service.calendar.TemporalExpression, int);`
- `public java.lang.String toString();`
- `public void visit(org.apache.ofbiz.service.calendar.TemporalExpressions$DateRange);`
- `public void visit(org.apache.ofbiz.service.calendar.TemporalExpressions$DayInMonth);`
- `public void visit(org.apache.ofbiz.service.calendar.TemporalExpressions$DayOfMonthRange);`
- `public void visit(org.apache.ofbiz.service.calendar.TemporalExpressions$DayOfWeekRange);`
- `public void visit(org.apache.ofbiz.service.calendar.TemporalExpressions$Difference);`
- `public void visit(org.apache.ofbiz.service.calendar.TemporalExpressions$Frequency);`
- `public void visit(org.apache.ofbiz.service.calendar.TemporalExpressions$HourRange);`
- `public void visit(org.apache.ofbiz.service.calendar.TemporalExpressions$Intersection);`
- `public void visit(org.apache.ofbiz.service.calendar.TemporalExpressions$MinuteRange);`
- `public void visit(org.apache.ofbiz.service.calendar.TemporalExpressions$MonthRange);`
- `public void visit(org.apache.ofbiz.service.calendar.TemporalExpressions$Null);`
- `public void visit(org.apache.ofbiz.service.calendar.TemporalExpressions$Substitution);`
- *(... 1 weitere Methoden)*

### `JobManager` — class
Vollständiger Name: `org.apache.ofbiz.service.job.JobManager`
- `public static org.apache.ofbiz.service.job.JobManager getInstance(org.apache.ofbiz.entity.Delegator, boolean);`
- `public static void shutDown();`
- `public org.apache.ofbiz.entity.Delegator getDelegator();`
- `public org.apache.ofbiz.service.LocalDispatcher getDispatcher();`
- `public java.util.Map<java.lang.String, java.lang.Object> getPoolState();`
- `public boolean isAvailable();`
- `public static java.util.List<org.apache.ofbiz.entity.GenericValue> getJobsToPurge(org.apache.ofbiz.entity.Delegator, java.lang.String, java.lang.String, int, java.sql.Timestamp) `
- `public synchronized void reloadCrashedJobs();`
- `public void runJob(org.apache.ofbiz.service.job.Job) `
- `public void schedule(java.lang.String, java.util.Map<java.lang.String, ? extends java.lang.Object>, long, int, int, int) `
- `public void schedule(java.lang.String, java.util.Map<java.lang.String, ? extends java.lang.Object>, long, int, int, int, long) `
- `public void schedule(java.lang.String, java.util.Map<java.lang.String, ? extends java.lang.Object>, long, int, int, long) `
- `public void schedule(java.lang.String, java.lang.String, java.util.Map<java.lang.String, ? extends java.lang.Object>, long, int, int, int, long) `
- `public void schedule(java.lang.String, java.lang.String, java.lang.String, long) `
- `public void schedule(java.lang.String, java.lang.String, java.lang.String, java.util.Map<java.lang.String, ? extends java.lang.Object>, long, int, int, int, long, int) `
- *(... 1 weitere Methoden)*

### `ServiceEngineTestServices` — class
Vollständiger Name: `org.apache.ofbiz.service.test.ServiceEngineTestServices`
- `public org.apache.ofbiz.service.test.ServiceEngineTestServices();`
- `public static java.util.Map<java.lang.String, java.lang.Object> testServiceDeadLockRetry(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> testServiceDeadLockRetryThreadA(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> testServiceDeadLockRetryThreadB(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> testServiceLockWaitTimeoutRetry(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> testServiceLockWaitTimeoutRetryGrabber(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> testServiceLockWaitTimeoutRetryWaiter(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> testServiceLockWaitTimeoutRetryCantRecover(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> testServiceLockWaitTimeoutRetryCantRecoverWaiter(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> testServiceOwnTxSubServiceAfterSetRollbackOnlyInParentErrorCatchWrapper(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> testServiceOwnTxSubServiceAfterSetRollbackOnlyInParent(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> testServiceOwnTxSubServiceAfterSetRollbackOnlyInParentSubService(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> testServiceEcaGlobalEventExec(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> testServiceEcaGlobalEventExecOnCommit(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> testServiceEcaGlobalEventExecToRollback(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- *(... 1 weitere Methoden)*

### `TemporalExpression` — class
Vollständiger Name: `org.apache.ofbiz.service.calendar.TemporalExpression`
- `public int getSequence();`
- `public void setSequence(int);`
- `public abstract void accept(org.apache.ofbiz.service.calendar.TemporalExpressionVisitor);`
- `public int compareTo(org.apache.ofbiz.service.calendar.TemporalExpression);`
- `public boolean equals(java.lang.Object);`
- `public int hashCode();`
- `public abstract com.ibm.icu.util.Calendar first(com.ibm.icu.util.Calendar);`
- `public java.lang.String getId();`
- `public java.util.Set<java.util.Date> getRange(org.apache.ofbiz.base.util.DateRange, com.ibm.icu.util.Calendar);`
- `public abstract boolean includesDate(com.ibm.icu.util.Calendar);`
- `public abstract boolean isSubstitutionCandidate(com.ibm.icu.util.Calendar, org.apache.ofbiz.service.calendar.TemporalExpression);`
- `public com.ibm.icu.util.Calendar next(com.ibm.icu.util.Calendar);`
- `public void setId(java.lang.String);`
- `public java.lang.String toString();`
- `public int compareTo(java.lang.Object);`

### `RemoteDispatcher` — interface
Vollständiger Name: `org.apache.ofbiz.service.rmi.RemoteDispatcher`
- `public abstract java.util.Map<java.lang.String, java.lang.Object> runSync(java.lang.String, java.util.Map<java.lang.String, ? extends java.lang.Object>) `
- `public abstract java.util.Map<java.lang.String, java.lang.Object> runSync(java.lang.String, java.util.Map<java.lang.String, ? extends java.lang.Object>, int, boolean) `
- `public abstract void runSyncIgnore(java.lang.String, java.util.Map<java.lang.String, ? extends java.lang.Object>) `
- `public abstract void runSyncIgnore(java.lang.String, java.util.Map<java.lang.String, ? extends java.lang.Object>, int, boolean) `
- `public abstract void runAsync(java.lang.String, java.util.Map<java.lang.String, ? extends java.lang.Object>, org.apache.ofbiz.service.GenericRequester, boolean, int, boolean) `
- `public abstract void runAsync(java.lang.String, java.util.Map<java.lang.String, ? extends java.lang.Object>, org.apache.ofbiz.service.GenericRequester, boolean) `
- `public abstract void runAsync(java.lang.String, java.util.Map<java.lang.String, ? extends java.lang.Object>, org.apache.ofbiz.service.GenericRequester) `
- `public abstract void runAsync(java.lang.String, java.util.Map<java.lang.String, ? extends java.lang.Object>, boolean) `
- `public abstract void runAsync(java.lang.String, java.util.Map<java.lang.String, ? extends java.lang.Object>) `
- `public abstract org.apache.ofbiz.service.GenericResultWaiter runAsyncWait(java.lang.String, java.util.Map<java.lang.String, ? extends java.lang.Object>, boolean) `
- `public abstract org.apache.ofbiz.service.GenericResultWaiter runAsyncWait(java.lang.String, java.util.Map<java.lang.String, ? extends java.lang.Object>) `
- `public abstract void schedule(java.lang.String, java.util.Map<java.lang.String, ? extends java.lang.Object>, long, int, int, int, long) `
- `public abstract void schedule(java.lang.String, java.util.Map<java.lang.String, ? extends java.lang.Object>, long, int, int, int) `
- `public abstract void schedule(java.lang.String, java.util.Map<java.lang.String, ? extends java.lang.Object>, long, int, int, long) `
- `public abstract void schedule(java.lang.String, java.util.Map<java.lang.String, ? extends java.lang.Object>, long) `

### `ServiceXaWrapper` — class
Vollständiger Name: `org.apache.ofbiz.service.ServiceXaWrapper`
- `public org.apache.ofbiz.service.ServiceXaWrapper(org.apache.ofbiz.service.DispatchContext);`
- `public void setCommitService(java.lang.String, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public void setCommitService(java.lang.String, java.util.Map<java.lang.String, ? extends java.lang.Object>, boolean, boolean);`
- `public void setCommitService(java.lang.String, java.lang.String, java.util.Map<java.lang.String, ? extends java.lang.Object>, boolean, boolean);`
- `public java.lang.String getCommitService();`
- `public java.util.Map<java.lang.String, ? extends java.lang.Object> getCommitContext();`
- `public void setRollbackService(java.lang.String, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public void setRollbackService(java.lang.String, java.util.Map<java.lang.String, ? extends java.lang.Object>, boolean, boolean);`
- `public void setRollbackService(java.lang.String, java.lang.String, java.util.Map<java.lang.String, ? extends java.lang.Object>, boolean, boolean);`
- `public java.lang.String getRollbackService();`
- `public java.util.Map<java.lang.String, ? extends java.lang.Object> getRollbackContext();`
- `public void enlist() `
- `public void commit(javax.transaction.xa.Xid, boolean) `
- `public void rollback(javax.transaction.xa.Xid) `
- `public int prepare(javax.transaction.xa.Xid) `

### `ServiceEngine` — class
Vollständiger Name: `org.apache.ofbiz.service.config.model.ServiceEngine`
- `public org.apache.ofbiz.service.config.model.Authorization getAuthorization();`
- `public org.apache.ofbiz.service.config.model.Engine getEngine(java.lang.String);`
- `public java.util.List<org.apache.ofbiz.service.config.model.Engine> getEngines();`
- `public java.util.List<org.apache.ofbiz.service.config.model.GlobalServices> getGlobalServices();`
- `public org.apache.ofbiz.service.config.model.JmsService getJmsServiceByName(java.lang.String);`
- `public java.util.List<org.apache.ofbiz.service.config.model.JmsService> getJmsServices();`
- `public java.lang.String getName();`
- `public java.util.List<org.apache.ofbiz.service.config.model.NotificationGroup> getNotificationGroups();`
- `public java.util.List<org.apache.ofbiz.service.config.model.ResourceLoader> getResourceLoaders();`
- `public java.util.List<org.apache.ofbiz.service.config.model.ServiceEcas> getServiceEcas();`
- `public java.util.List<org.apache.ofbiz.service.config.model.ServiceGroups> getServiceGroups();`
- `public java.util.List<org.apache.ofbiz.service.config.model.ServiceLocation> getServiceLocations();`
- `public java.util.List<org.apache.ofbiz.service.config.model.StartupService> getStartupServices();`
- `public org.apache.ofbiz.service.config.model.ThreadPool getThreadPool();`

## Modul: sfa (1 Klassen, 3 public Methoden)

### `VCard` — class
Vollständiger Name: `org.apache.ofbiz.sfa.vcard.VCard`
- `public org.apache.ofbiz.sfa.vcard.VCard();`
- `public static java.util.Map<java.lang.String, java.lang.Object> importVCard(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>) `
- `public static java.util.Map<java.lang.String, java.lang.Object> exportVCard(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`

## Modul: shipment (25 Klassen, 295 public Methoden)

### `PackingSession` — class
Vollständiger Name: `org.apache.ofbiz.shipment.packing.PackingSession`
- `public org.apache.ofbiz.shipment.packing.PackingSession(org.apache.ofbiz.service.LocalDispatcher, org.apache.ofbiz.entity.GenericValue, java.lang.String, java.lang.String, java.lang.String, java.lang.String);`
- `public org.apache.ofbiz.shipment.packing.PackingSession(org.apache.ofbiz.service.LocalDispatcher, org.apache.ofbiz.entity.GenericValue, java.lang.String);`
- `public org.apache.ofbiz.shipment.packing.PackingSession(org.apache.ofbiz.service.LocalDispatcher, org.apache.ofbiz.entity.GenericValue);`
- `public void addOrIncreaseLine(java.lang.String, java.lang.String, java.lang.String, java.lang.String, java.math.BigDecimal, int, java.math.BigDecimal, boolean) `
- `public void addOrIncreaseLine(java.lang.String, java.lang.String, java.lang.String, java.math.BigDecimal, int) `
- `public void addOrIncreaseLine(java.lang.String, java.math.BigDecimal, int) `
- `public org.apache.ofbiz.shipment.packing.PackingSessionLine findLine(java.lang.String, java.lang.String, java.lang.String, java.lang.String, java.lang.String, int);`
- `public void addItemInfo(java.util.List<org.apache.ofbiz.entity.GenericValue>);`
- `public java.util.List<org.apache.ofbiz.shipment.packing.PackingSession$ItemDisplay> getItemInfos();`
- `public java.util.Map<java.lang.Object, java.lang.Object> getPackingSessionLinesByPackage();`
- `public void clearItemInfos();`
- `public java.lang.String getShipmentId();`
- `public java.util.List<org.apache.ofbiz.shipment.packing.PackingSessionLine> getLines();`
- `public int nextPackageSeq();`
- `public int getCurrentPackageSeq();`
- *(... 46 weitere Methoden)*

### `WeightPackageSession` — class
Vollständiger Name: `org.apache.ofbiz.shipment.weightPackage.WeightPackageSession`
- `public org.apache.ofbiz.shipment.weightPackage.WeightPackageSession();`
- `public org.apache.ofbiz.shipment.weightPackage.WeightPackageSession(org.apache.ofbiz.service.LocalDispatcher, org.apache.ofbiz.entity.GenericValue, java.lang.String, java.lang.String, java.lang.String, java.lang.String);`
- `public org.apache.ofbiz.shipment.weightPackage.WeightPackageSession(org.apache.ofbiz.service.LocalDispatcher, org.apache.ofbiz.entity.GenericValue, java.lang.String);`
- `public org.apache.ofbiz.shipment.weightPackage.WeightPackageSession(org.apache.ofbiz.service.LocalDispatcher, org.apache.ofbiz.entity.GenericValue);`
- `public org.apache.ofbiz.service.LocalDispatcher getDispatcher();`
- `public org.apache.ofbiz.entity.Delegator getDelegator();`
- `public void createWeightPackageLine(java.lang.String, java.math.BigDecimal, java.math.BigDecimal, java.math.BigDecimal, java.math.BigDecimal, java.lang.String) `
- `public int getWeightPackageSeqId();`
- `public java.lang.String getFacilityId();`
- `public void setFacilityId(java.lang.String);`
- `public java.lang.String getPrimaryOrderId();`
- `public void setPrimaryOrderId(java.lang.String);`
- `public java.lang.String getPrimaryShipGroupSeqId();`
- `public void setPrimaryShipGroupSeqId(java.lang.String);`
- `public void setPicklistBinId(java.lang.String);`
- *(... 30 weitere Methoden)*

### `PackingSessionLine` — class
Vollständiger Name: `org.apache.ofbiz.shipment.packing.PackingSessionLine`
- `public org.apache.ofbiz.shipment.packing.PackingSessionLine(java.lang.String, java.lang.String, java.lang.String, java.lang.String, java.lang.String, java.math.BigDecimal, java.math.BigDecimal, int);`
- `public java.lang.String getOrderId();`
- `public java.lang.String getOrderItemSeqId();`
- `public java.lang.String getShipGroupSeqId();`
- `public java.lang.String getInventoryItemId();`
- `public java.lang.String getProductId();`
- `public java.lang.String getShipmentItemSeqId();`
- `public void setShipmentItemSeqId(java.lang.String);`
- `public java.math.BigDecimal getQuantity();`
- `public void setQuantity(java.math.BigDecimal);`
- `public void addQuantity(java.math.BigDecimal);`
- `public java.math.BigDecimal getWeight();`
- `public void setWeight(java.math.BigDecimal);`
- `public void addWeight(java.math.BigDecimal);`
- `public int getPackageSeq();`
- *(... 11 weitere Methoden)*

### `UpsServices` — class
Vollständiger Name: `org.apache.ofbiz.shipment.thirdparty.ups.UpsServices`
- `public org.apache.ofbiz.shipment.thirdparty.ups.UpsServices();`
- `public static java.util.Map<java.lang.String, java.lang.Object> upsShipmentConfirm(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> handleUpsShipmentConfirmResponse(org.w3c.dom.Document, org.apache.ofbiz.entity.GenericValue, java.util.Locale) `
- `public static java.util.Map<java.lang.String, java.lang.Object> upsShipmentAccept(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> handleUpsShipmentAcceptResponse(org.w3c.dom.Document, org.apache.ofbiz.entity.GenericValue, java.util.List<org.apache.ofbiz.entity.GenericValue>, org.apache.ofbiz.entity.Delegator, java.lang.String, java.lang.String, java.util.Map<java.lang.String, ? extends java.lang.Object>, java.util.Locale) `
- `public static java.util.Map<java.lang.String, java.lang.Object> upsVoidShipment(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> handleUpsVoidShipmentResponse(org.w3c.dom.Document, org.apache.ofbiz.entity.GenericValue, java.util.Locale) `
- `public static java.util.Map<java.lang.String, java.lang.Object> upsTrackShipment(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> handleUpsTrackShipmentResponse(org.w3c.dom.Document, org.apache.ofbiz.entity.GenericValue, java.util.List<org.apache.ofbiz.entity.GenericValue>, java.util.Locale) `
- `public static java.util.Map<java.lang.String, java.lang.Object> upsRateInquire(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> handleUpsRateInquireResponse(org.w3c.dom.Document, java.util.Locale);`
- `public static org.w3c.dom.Document createAccessRequestDocument(org.apache.ofbiz.entity.Delegator, java.lang.String, java.lang.String);`
- `public static void handleErrors(org.w3c.dom.Element, java.util.List<java.lang.Object>, java.util.Locale);`
- `public static java.lang.String sendUpsRequest(java.lang.String, java.lang.String, java.lang.String, java.lang.String, org.apache.ofbiz.entity.Delegator, java.util.Locale) `
- `public static java.util.Map<java.lang.String, java.lang.Object> upsRateInquireByPostalCode(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- *(... 5 weitere Methoden)*

### `VerifyPickSession` — class
Vollständiger Name: `org.apache.ofbiz.shipment.verify.VerifyPickSession`
- `public org.apache.ofbiz.shipment.verify.VerifyPickSession();`
- `public org.apache.ofbiz.shipment.verify.VerifyPickSession(org.apache.ofbiz.service.LocalDispatcher, org.apache.ofbiz.entity.GenericValue);`
- `public org.apache.ofbiz.service.LocalDispatcher getDispatcher();`
- `public org.apache.ofbiz.entity.Delegator getDelegator();`
- `public void createRow(java.lang.String, java.lang.String, java.lang.String, java.lang.String, java.lang.String, java.math.BigDecimal, java.util.Locale) `
- `public org.apache.ofbiz.entity.GenericValue getUserLogin();`
- `public void setFacilityId(java.lang.String);`
- `public java.lang.String getFacilityId();`
- `public void setPicklistBinId(java.lang.String);`
- `public java.lang.String getPicklistBinId();`
- `public java.util.List<org.apache.ofbiz.shipment.verify.VerifyPickSessionRow> getPickRows();`
- `public java.util.List<org.apache.ofbiz.shipment.verify.VerifyPickSessionRow> getPickRows(java.lang.String);`
- `public java.math.BigDecimal getReadyToVerifyQuantity(java.lang.String, java.lang.String) `
- `public org.apache.ofbiz.shipment.verify.VerifyPickSessionRow getPickRow(java.lang.String, java.lang.String, java.lang.String, java.lang.String, java.lang.String);`
- `public java.math.BigDecimal getVerifiedQuantity(java.lang.String, java.lang.String, java.lang.String, java.lang.String, java.lang.String);`
- *(... 3 weitere Methoden)*

### `WeightPackageSessionLine` — class
Vollständiger Name: `org.apache.ofbiz.shipment.weightPackage.WeightPackageSessionLine`
- `public org.apache.ofbiz.shipment.weightPackage.WeightPackageSessionLine(java.lang.String, java.math.BigDecimal, java.math.BigDecimal, java.math.BigDecimal, java.math.BigDecimal, java.lang.String, int) `
- `public java.lang.String getOrderId();`
- `public void setOrderId(java.lang.String);`
- `public java.math.BigDecimal getPackageWeight();`
- `public void setPackageWeight(java.math.BigDecimal);`
- `public java.math.BigDecimal getPackageLength();`
- `public void setPackageLength(java.math.BigDecimal);`
- `public java.math.BigDecimal getPackageWidth();`
- `public void setPackageWidth(java.math.BigDecimal);`
- `public java.math.BigDecimal getPackageHeight();`
- `public void setPackageHeight(java.math.BigDecimal);`
- `public java.lang.String getShipmentBoxTypeId();`
- `public void setShipmentBoxTypeId(java.lang.String);`
- `public int getWeightPackageSeqId();`
- `public void setWeightPackageSeqId(int);`
- *(... 2 weitere Methoden)*

### `VerifyPickSessionRow` — class
Vollständiger Name: `org.apache.ofbiz.shipment.verify.VerifyPickSessionRow`
- `public org.apache.ofbiz.shipment.verify.VerifyPickSessionRow();`
- `public org.apache.ofbiz.shipment.verify.VerifyPickSessionRow(java.lang.String, java.lang.String, java.lang.String, java.lang.String, java.lang.String, java.lang.String, java.math.BigDecimal);`
- `public java.lang.String getOrderId();`
- `public java.lang.String getOrderItemSeqId();`
- `public java.lang.String getShipGroupSeqId();`
- `public java.lang.String getProductId();`
- `public java.lang.String getOriginGeoId();`
- `public java.lang.String getInventoryItemId();`
- `public java.math.BigDecimal getReadyToVerifyQty();`
- `public void setReadyToVerifyQty(java.math.BigDecimal);`
- `public void setShipmentItemSeqId(java.lang.String);`
- `public java.lang.String getShipmentItemSeqId();`
- `public void setInvoiceItemSeqId(java.lang.String);`
- `public java.lang.String getInvoiceItemSeqId();`
- `public org.apache.ofbiz.entity.GenericValue getOrderItem();`
- *(... 1 weitere Methoden)*

### `UspsServices` — class
Vollständiger Name: `org.apache.ofbiz.shipment.thirdparty.usps.UspsServices`
- `public org.apache.ofbiz.shipment.thirdparty.usps.UspsServices();`
- `public static java.util.Map<java.lang.String, java.lang.Object> uspsRateInquire(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> uspsInternationalRateInquire(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> uspsTrackConfirm(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> uspsAddressValidation(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> uspsCityStateLookup(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> uspsPriorityMailStandard(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> uspsPackageServicesStandard(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> uspsDomesticRate(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> uspsUpdateShipmentRateInfo(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> uspsDeliveryConfirmation(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> uspsDumpShipmentLabelImages(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> uspsPriorityMailInternationalLabel(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public static java.lang.Integer[] convertPoundsToPoundsOunces(java.math.BigDecimal);`

### `ShipmentServices` — class
Vollständiger Name: `org.apache.ofbiz.shipment.shipment.ShipmentServices`
- `public org.apache.ofbiz.shipment.shipment.ShipmentServices();`
- `public static java.util.Map<java.lang.String, java.lang.Object> createShipmentEstimate(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> removeShipmentEstimate(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> calcShipmentCostEstimate(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> fillShipmentStagingTables(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> updateShipmentsFromStaging(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> clearShipmentStagingInfo(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> updatePurchaseShipmentFromReceipt(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> duplicateShipmentRouteSegment(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> quickScheduleShipmentRouteSegment(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> getShipmentPackageValueFromOrders(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> sendShipmentCompleteNotification(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> getShipmentGatewayConfigFromShipment(org.apache.ofbiz.entity.Delegator, java.lang.String, java.util.Locale);`

### `PackingServices` — class
Vollständiger Name: `org.apache.ofbiz.shipment.packing.PackingServices`
- `public org.apache.ofbiz.shipment.packing.PackingServices();`
- `public static java.util.Map<java.lang.String, java.lang.Object> addPackLine(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> packBulk(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> incrementPackageSeq(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> clearLastPackage(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> clearPackLine(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> clearPackAll(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> calcPackSessionAdditionalShippingCharge(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> completePack(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public static java.math.BigDecimal setSessionPackageWeights(org.apache.ofbiz.shipment.packing.PackingSession, java.util.Map<java.lang.String, java.lang.String>);`
- `public static void setSessionShipmentBoxTypes(org.apache.ofbiz.shipment.packing.PackingSession, java.util.Map<java.lang.String, java.lang.String>);`

### `DhlServices` — class
Vollständiger Name: `org.apache.ofbiz.shipment.thirdparty.dhl.DhlServices`
- `public org.apache.ofbiz.shipment.thirdparty.dhl.DhlServices();`
- `public static java.lang.String sendDhlRequest(java.lang.String, org.apache.ofbiz.entity.Delegator, java.lang.String, java.lang.String, java.util.Locale) `
- `public static java.util.Map<java.lang.String, java.lang.Object> dhlRateEstimate(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> handleDhlRateResponse(org.w3c.dom.Document, java.util.Locale);`
- `public static java.util.Map<java.lang.String, java.lang.Object> dhlRegisterInquire(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> handleDhlRegisterResponse(org.w3c.dom.Document, java.util.Locale);`
- `public static java.util.Map<java.lang.String, java.lang.Object> dhlShipmentConfirm(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> handleDhlShipmentConfirmResponse(java.lang.String, org.apache.ofbiz.entity.GenericValue, java.util.List<org.apache.ofbiz.entity.GenericValue>, java.util.Locale) `
- `public static org.w3c.dom.Document createAccessRequestDocument(org.apache.ofbiz.entity.Delegator, java.lang.String, java.lang.String);`
- `public static void handleErrors(org.w3c.dom.Element, java.util.List<java.lang.Object>, java.util.Locale);`

### `UspsServicesTests` — class
Vollständiger Name: `org.apache.ofbiz.shipment.thirdparty.usps.UspsServicesTests`
- `public org.apache.ofbiz.shipment.thirdparty.usps.UspsServicesTests(java.lang.String);`
- `public void testUspsTrackConfirm() `
- `public void testUspsAddressValidation() `
- `public void testUspsCityStateLookup() `
- `public void testUspsPriorityMailStandard() `
- `public void testUspsPackageServicesStandard() `
- `public void testUspsDomesticRate() `

### `WeightPackageServices` — class
Vollständiger Name: `org.apache.ofbiz.shipment.weightPackage.WeightPackageServices`
- `public org.apache.ofbiz.shipment.weightPackage.WeightPackageServices();`
- `public static java.util.Map<java.lang.String, java.lang.Object> setPackageInfo(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> updatePackedLine(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> deletePackedLine(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> completePackage(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> completeShipment(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> savePackagesInfo(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`

### `FedexServices` — class
Vollständiger Name: `org.apache.ofbiz.shipment.thirdparty.fedex.FedexServices`
- `public org.apache.ofbiz.shipment.thirdparty.fedex.FedexServices();`
- `public static java.lang.String sendFedexRequest(java.lang.String, org.apache.ofbiz.entity.Delegator, java.lang.String, java.lang.String, java.util.Locale) `
- `public static java.util.Map<java.lang.String, java.lang.Object> fedexSubscriptionRequest(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> fedexShipRequest(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> handleFedexShipReply(java.lang.String, org.apache.ofbiz.entity.GenericValue, java.util.List<org.apache.ofbiz.entity.GenericValue>, java.util.Locale) `
- `public static void handleErrors(org.w3c.dom.Element, java.util.List<java.lang.Object>, java.util.Locale);`

### `VerifyPickServices` — class
Vollständiger Name: `org.apache.ofbiz.shipment.verify.VerifyPickServices`
- `public org.apache.ofbiz.shipment.verify.VerifyPickServices();`
- `public static java.util.Map<java.lang.String, java.lang.Object> verifySingleItem(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> verifyBulkItem(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> completeVerifiedPick(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> cancelAllRows(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`

### `PackingEvent` — interface
Vollständiger Name: `org.apache.ofbiz.shipment.packing.PackingEvent`
- `public abstract void runEvent(org.apache.ofbiz.shipment.packing.PackingSession, int);`
- `public abstract java.lang.String receiveMessage();`
- `public abstract int getEventStatus();`
- `public abstract int getEventCode();`

### `ShipmentWorker` — class
Vollständiger Name: `org.apache.ofbiz.shipment.shipment.ShipmentWorker`
- `public static java.math.BigDecimal getShipmentPackageContentValue(org.apache.ofbiz.entity.GenericValue);`
- `public static java.util.List<java.util.Map<java.lang.String, java.math.BigDecimal>> getPackageSplit(org.apache.ofbiz.service.DispatchContext, java.util.List<java.util.Map<java.lang.String, java.lang.Object>>, java.math.BigDecimal);`
- `public static java.math.BigDecimal calcPackageWeight(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, java.math.BigDecimal>, java.util.List<java.util.Map<java.lang.String, java.lang.Object>>, java.math.BigDecimal);`
- `public static java.util.Map<java.lang.String, java.lang.Object> getProductItemInfo(java.util.List<java.util.Map<java.lang.String, java.lang.Object>>, java.lang.String);`

### `PickListServices` — class
Vollständiger Name: `org.apache.ofbiz.shipment.picklist.PickListServices`
- `public org.apache.ofbiz.shipment.picklist.PickListServices();`
- `public static java.util.Map<java.lang.String, java.lang.Object> convertOrderIdListToHeaders(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public static boolean isBinComplete(org.apache.ofbiz.entity.Delegator, java.lang.String) `

### `ShipmentEvents` — class
Vollständiger Name: `org.apache.ofbiz.shipment.shipment.ShipmentEvents`
- `public org.apache.ofbiz.shipment.shipment.ShipmentEvents();`
- `public static java.lang.String viewShipmentPackageRouteSegLabelImage(javax.servlet.http.HttpServletRequest, javax.servlet.http.HttpServletResponse);`
- `public static java.lang.String checkForceShipmentReceived(javax.servlet.http.HttpServletRequest, javax.servlet.http.HttpServletResponse);`

### `UspsMockApiServlet` — class
Vollständiger Name: `org.apache.ofbiz.shipment.thirdparty.usps.UspsMockApiServlet`
- `public org.apache.ofbiz.shipment.thirdparty.usps.UspsMockApiServlet();`
- `public void doPost(javax.servlet.http.HttpServletRequest, javax.servlet.http.HttpServletResponse) `
- `public void doGet(javax.servlet.http.HttpServletRequest, javax.servlet.http.HttpServletResponse) `

## Modul: testtools (7 Klassen, 28 public Methoden)

### `GroovyScriptTestCase` — class
Vollständiger Name: `org.apache.ofbiz.testtools.GroovyScriptTestCase`
- `public org.apache.ofbiz.testtools.GroovyScriptTestCase();`
- `public final void setDelegator(org.apache.ofbiz.entity.Delegator);`
- `public final org.apache.ofbiz.entity.Delegator getDelegator();`
- `public final org.apache.ofbiz.service.LocalDispatcher getDispatcher();`
- `public final void setDispatcher(org.apache.ofbiz.service.LocalDispatcher);`
- `public final void setSecurity(org.apache.ofbiz.security.Security);`
- `public final org.apache.ofbiz.security.Security getSecurity();`

### `TestRunContainer` — class
Vollständiger Name: `org.apache.ofbiz.testtools.TestRunContainer`
- `public org.apache.ofbiz.testtools.TestRunContainer();`
- `public void init(java.util.List<org.apache.ofbiz.base.start.StartupCommand>, java.lang.String, java.lang.String) `
- `public boolean start() `
- `public void stop();`
- `public java.lang.String getName();`

### `JunitSuiteWrapper` — class
Vollständiger Name: `org.apache.ofbiz.testtools.JunitSuiteWrapper`
- `public org.apache.ofbiz.testtools.JunitSuiteWrapper(java.lang.String, java.lang.String, java.lang.String);`
- `public void populateTestSuite(junit.framework.TestSuite);`
- `public java.util.List<org.apache.ofbiz.testtools.ModelTestSuite> getModelTestSuites();`
- `public java.util.List<junit.framework.Test> getAllTestList();`

### `SimpleMethodTest` — class
Vollständiger Name: `org.apache.ofbiz.testtools.SimpleMethodTest`
- `public org.apache.ofbiz.testtools.SimpleMethodTest(java.lang.String, org.w3c.dom.Element);`
- `public org.apache.ofbiz.testtools.SimpleMethodTest(java.lang.String, java.lang.String, java.lang.String);`
- `public int countTestCases();`
- `public void run(junit.framework.TestResult);`

### `EntityXmlAssertTest` — class
Vollständiger Name: `org.apache.ofbiz.testtools.EntityXmlAssertTest`
- `public org.apache.ofbiz.testtools.EntityXmlAssertTest(java.lang.String, org.w3c.dom.Element);`
- `public int countTestCases();`
- `public void run(junit.framework.TestResult);`

### `ServiceTest` — class
Vollständiger Name: `org.apache.ofbiz.testtools.ServiceTest`
- `public org.apache.ofbiz.testtools.ServiceTest(java.lang.String, org.w3c.dom.Element);`
- `public int countTestCases();`
- `public void run(junit.framework.TestResult);`

### `ModelTestSuite` — class
Vollständiger Name: `org.apache.ofbiz.testtools.ModelTestSuite`
- `public org.apache.ofbiz.testtools.ModelTestSuite(org.w3c.dom.Element, java.lang.String);`
- `public junit.framework.TestSuite makeTestSuite();`

## Modul: webapp (75 Klassen, 385 public Methoden)

### `LoginWorker` — class
Vollständiger Name: `org.apache.ofbiz.webapp.control.LoginWorker`
- `public static org.apache.ofbiz.base.util.StringUtil$StringWrapper makeLoginUrl(javax.servlet.jsp.PageContext);`
- `public static org.apache.ofbiz.base.util.StringUtil$StringWrapper makeLoginUrl(javax.servlet.http.HttpServletRequest);`
- `public static org.apache.ofbiz.base.util.StringUtil$StringWrapper makeLoginUrl(javax.servlet.jsp.PageContext, java.lang.String);`
- `public static org.apache.ofbiz.base.util.StringUtil$StringWrapper makeLoginUrl(javax.servlet.http.HttpServletRequest, java.lang.String);`
- `public static void setLoggedOut(java.lang.String, org.apache.ofbiz.entity.Delegator);`
- `public static org.apache.ofbiz.entity.GenericValue checkLogout(javax.servlet.http.HttpServletRequest, javax.servlet.http.HttpServletResponse);`
- `public static org.apache.ofbiz.entity.GenericValue checkImpersonationInProcess(javax.servlet.http.HttpServletRequest, javax.servlet.http.HttpServletResponse);`
- `public static java.lang.String extensionCheckLogin(javax.servlet.http.HttpServletRequest, javax.servlet.http.HttpServletResponse);`
- `public static java.lang.String extensionConnectLogin(javax.servlet.http.HttpServletRequest, javax.servlet.http.HttpServletResponse);`
- `public static java.lang.String checkLogin(javax.servlet.http.HttpServletRequest, javax.servlet.http.HttpServletResponse);`
- `public static java.lang.String login(javax.servlet.http.HttpServletRequest, javax.servlet.http.HttpServletResponse);`
- `public static java.lang.String impersonateLogin(javax.servlet.http.HttpServletRequest, javax.servlet.http.HttpServletResponse);`
- `public static java.lang.String depersonateLogin(javax.servlet.http.HttpServletRequest, javax.servlet.http.HttpServletResponse);`
- `public static java.lang.String doMainLogin(javax.servlet.http.HttpServletRequest, javax.servlet.http.HttpServletResponse, org.apache.ofbiz.entity.GenericValue, java.util.Map<java.lang.String, java.lang.Object>);`
- `public static void doBasicLogin(org.apache.ofbiz.entity.GenericValue, javax.servlet.http.HttpServletRequest, javax.servlet.http.HttpServletResponse);`
- *(... 23 weitere Methoden)*

### `ServerHitBin` — class
Vollständiger Name: `org.apache.ofbiz.webapp.stats.ServerHitBin`
- `public static void countRequest(java.lang.String, javax.servlet.http.HttpServletRequest, long, long, org.apache.ofbiz.entity.GenericValue);`
- `public static void countEvent(java.lang.String, javax.servlet.http.HttpServletRequest, long, long, org.apache.ofbiz.entity.GenericValue);`
- `public static void countView(java.lang.String, javax.servlet.http.HttpServletRequest, long, long, org.apache.ofbiz.entity.GenericValue);`
- `public static void countEntity(java.lang.String, javax.servlet.http.HttpServletRequest, long, long, org.apache.ofbiz.entity.GenericValue);`
- `public static void countService(java.lang.String, javax.servlet.http.HttpServletRequest, long, long, org.apache.ofbiz.entity.GenericValue);`
- `public org.apache.ofbiz.entity.Delegator getDelegator();`
- `public java.lang.String getId();`
- `public int getType();`
- `public long getStartTime();`
- `public long getEndTime();`
- `public java.lang.String getStartTimeString();`
- `public java.lang.String getEndTimeString();`
- `public long getBinLength();`
- `public double getBinLengthMinutes();`
- `public synchronized long getNumberHits();`
- *(... 8 weitere Methoden)*

### `RequestHandler` — class
Vollständiger Name: `org.apache.ofbiz.webapp.control.RequestHandler`
- `public static org.apache.ofbiz.webapp.control.RequestHandler getRequestHandler(javax.servlet.ServletContext);`
- `public static java.lang.String getRequestUri(java.lang.String);`
- `public static java.lang.String getOverrideViewUri(java.lang.String);`
- `public static java.lang.String makeUrl(javax.servlet.http.HttpServletRequest, javax.servlet.http.HttpServletResponse, java.lang.String);`
- `public static java.lang.String makeUrl(javax.servlet.http.HttpServletRequest, javax.servlet.http.HttpServletResponse, java.lang.String, boolean, boolean, boolean);`
- `public static org.apache.ofbiz.webapp.control.RequestHandler from(javax.servlet.http.HttpServletRequest);`
- `public org.apache.ofbiz.webapp.control.ConfigXMLReader$ControllerConfig getControllerConfig();`
- `public void doRequest(javax.servlet.http.HttpServletRequest, javax.servlet.http.HttpServletResponse, java.lang.String, org.apache.ofbiz.entity.GenericValue, org.apache.ofbiz.entity.Delegator) `
- `public java.lang.String runEvent(javax.servlet.http.HttpServletRequest, javax.servlet.http.HttpServletResponse, org.apache.ofbiz.webapp.control.ConfigXMLReader$Event, org.apache.ofbiz.webapp.control.ConfigXMLReader$RequestMap, java.lang.String) `
- `public java.lang.String getDefaultErrorPage(javax.servlet.http.HttpServletRequest) `
- `public java.lang.String getStatusCode(javax.servlet.http.HttpServletRequest);`
- `public org.apache.ofbiz.webapp.view.ViewFactory getViewFactory();`
- `public org.apache.ofbiz.webapp.event.EventFactory getEventFactory();`
- `public java.lang.String makeQueryString(javax.servlet.http.HttpServletRequest, org.apache.ofbiz.webapp.control.ConfigXMLReader$RequestResponse);`
- `public java.lang.String makeLinkWithQueryString(javax.servlet.http.HttpServletRequest, javax.servlet.http.HttpServletResponse, java.lang.String, org.apache.ofbiz.webapp.control.ConfigXMLReader$RequestResponse);`
- *(... 7 weitere Methoden)*

### `SeoConfigUtil` — class
Vollständiger Name: `org.apache.ofbiz.webapp.SeoConfigUtil`
- `public static void init();`
- `public static boolean isInitialed();`
- `public static boolean checkUseUrlRegexp();`
- `public static org.apache.oro.text.regex.Pattern getGeneralRegexpPattern();`
- `public static boolean checkCategoryUrl();`
- `public static boolean isCategoryUrlEnabled(java.lang.String);`
- `public static boolean isCategoryNameEnabled();`
- `public static java.lang.String getCategoryUrlSuffix();`
- `public static boolean isJSessionIdAnonEnabled();`
- `public static boolean isJSessionIdUserEnabled();`
- `public static java.util.List<org.apache.oro.text.regex.Pattern> getUserExceptionPatterns();`
- `public static java.util.Map<java.lang.String, java.lang.String> getCharFilters();`
- `public static java.util.Map<java.lang.String, org.apache.oro.text.regex.Pattern> getSeoPatterns();`
- `public static java.util.Map<java.lang.String, java.lang.String> getSeoReplacements();`
- `public static java.util.Map<java.lang.String, java.lang.String> getForwardReplacements();`
- *(... 5 weitere Methoden)*

### `ApacheFopWorker` — class
Vollständiger Name: `org.apache.ofbiz.webapp.view.ApacheFopWorker`
- `public static org.apache.fop.apps.FopFactory getFactoryInstance();`
- `public static void transform(java.io.File, java.io.File, java.io.File, java.lang.String) `
- `public static void transform(java.io.InputStream, java.io.OutputStream, java.io.InputStream, java.lang.String) `
- `public static void transform(javax.xml.transform.stream.StreamSource, javax.xml.transform.stream.StreamSource, org.apache.fop.apps.Fop) `
- `public static org.apache.fop.apps.Fop createFopInstance(java.io.OutputStream, java.lang.String) `
- `public static org.apache.fop.apps.Fop createFopInstance(java.io.OutputStream, java.lang.String, org.apache.fop.apps.FOUserAgent) `
- `public static java.io.File createTempFoXmlFile() `
- `public static java.io.File createTempResultFile() `
- `public static java.lang.String getEncryptionLengthDefault();`
- `public static java.lang.String getUserPasswordDefault();`
- `public static java.lang.String getOwnerPasswordDefault();`
- `public static java.lang.String getAllowPrintDefault();`
- `public static java.lang.String getAllowCopyContentDefault();`
- `public static java.lang.String getAllowEditContentDefault();`
- `public static java.lang.String getAllowEditAnnotationsDefault();`
- *(... 5 weitere Methoden)*

### `ControlEventListener` — class
Vollständiger Name: `org.apache.ofbiz.webapp.control.ControlEventListener`
- `public org.apache.ofbiz.webapp.control.ControlEventListener();`
- `public void sessionCreated(javax.servlet.http.HttpSessionEvent);`
- `public void sessionDestroyed(javax.servlet.http.HttpSessionEvent);`
- `public void logStats(javax.servlet.http.HttpSession, org.apache.ofbiz.entity.GenericValue);`
- `public static long getTotalActiveSessions();`
- `public static long getTotalPassiveSessions();`
- `public static long getTotalSessions();`
- `public static void countCreateSession();`
- `public static void countDestroySession();`
- `public static void countPassivateSession();`
- `public static void countActivateSession();`

### `JWTManager` — class
Vollständiger Name: `org.apache.ofbiz.webapp.control.JWTManager`
- `public org.apache.ofbiz.webapp.control.JWTManager();`
- `public static java.lang.String checkJWTLogin(javax.servlet.http.HttpServletRequest, javax.servlet.http.HttpServletResponse);`
- `public static java.lang.String getJWTKey(org.apache.ofbiz.entity.Delegator);`
- `public static java.lang.String getJWTKey(org.apache.ofbiz.entity.Delegator, java.lang.String);`
- `public static java.lang.String getAuthenticationToken(javax.servlet.http.HttpServletRequest, javax.servlet.http.HttpServletResponse);`
- `public static java.lang.String getHeaderAuthBearerToken(javax.servlet.http.HttpServletRequest);`
- `public static java.util.Map<java.lang.String, java.lang.Object> validateToken(java.lang.String, java.lang.String);`
- `public static java.util.Map<java.lang.String, java.lang.Object> validateToken(org.apache.ofbiz.entity.Delegator, java.lang.String, java.lang.String);`
- `public static java.lang.String createJwt(org.apache.ofbiz.entity.Delegator, java.util.Map<java.lang.String, java.lang.String>);`
- `public static java.lang.String createJwt(org.apache.ofbiz.entity.Delegator, java.util.Map<java.lang.String, java.lang.String>, int);`
- `public static java.lang.String createJwt(org.apache.ofbiz.entity.Delegator, java.util.Map<java.lang.String, java.lang.String>, java.lang.String, int);`

### `ResponseHelper` — class
Vollständiger Name: `org.apache.ofbiz.webapp.webdav.ResponseHelper`
- `public static void prepareResponse(javax.servlet.http.HttpServletResponse, int, java.lang.String);`
- `public org.apache.ofbiz.webapp.webdav.ResponseHelper();`
- `public org.w3c.dom.Element createElementSetValue(java.lang.String, java.lang.String);`
- `public org.w3c.dom.Element createHrefElement(java.lang.String);`
- `public org.w3c.dom.Element createMultiStatusElement();`
- `public org.w3c.dom.Element createResponseDescriptionElement(java.lang.String, java.lang.String);`
- `public org.w3c.dom.Element createResponseElement();`
- `public org.w3c.dom.Element createStatusElement(java.lang.String);`
- `public org.w3c.dom.Document getResponseDocument();`
- `public void writeResponse(javax.servlet.http.HttpServletResponse, java.io.Writer) `

### `WebSiteProperties` — class
Vollständiger Name: `org.apache.ofbiz.webapp.website.WebSiteProperties`
- `public static org.apache.ofbiz.webapp.website.WebSiteProperties defaults(org.apache.ofbiz.entity.Delegator);`
- `public static org.apache.ofbiz.webapp.website.WebSiteProperties from(javax.servlet.http.HttpServletRequest) `
- `public static org.apache.ofbiz.webapp.website.WebSiteProperties from(org.apache.ofbiz.entity.GenericValue);`
- `public java.lang.String getHttpPort();`
- `public java.lang.String getHttpHost();`
- `public java.lang.String getHttpsPort();`
- `public java.lang.String getHttpsHost();`
- `public boolean getEnableHttps();`
- `public java.lang.String getWebappPath();`
- `public java.lang.String toString();`

### `CoreEvents` — class
Vollständiger Name: `org.apache.ofbiz.webapp.event.CoreEvents`
- `public org.apache.ofbiz.webapp.event.CoreEvents();`
- `public static java.lang.String returnSuccess(javax.servlet.http.HttpServletRequest, javax.servlet.http.HttpServletResponse);`
- `public static java.lang.String returnError(javax.servlet.http.HttpServletRequest, javax.servlet.http.HttpServletResponse);`
- `public static java.lang.String returnNull(javax.servlet.http.HttpServletRequest, javax.servlet.http.HttpServletResponse);`
- `public static java.lang.String scheduleService(javax.servlet.http.HttpServletRequest, javax.servlet.http.HttpServletResponse);`
- `public static java.lang.String saveServiceResultsToSession(javax.servlet.http.HttpServletRequest, javax.servlet.http.HttpServletResponse);`
- `public static java.lang.Object getObjectFromServicePath(java.lang.String, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public static java.lang.String runService(javax.servlet.http.HttpServletRequest, javax.servlet.http.HttpServletResponse);`
- `public static java.lang.String streamFile(javax.servlet.http.HttpServletRequest, javax.servlet.http.HttpServletResponse);`

### `WebAppUtil` — class
Vollständiger Name: `org.apache.ofbiz.webapp.WebAppUtil`
- `public static java.lang.String getControlServletPath(org.apache.ofbiz.base.component.ComponentConfig$WebappInfo) `
- `public static boolean isDistributable(org.apache.ofbiz.base.component.ComponentConfig$WebappInfo) `
- `public static org.apache.ofbiz.base.component.ComponentConfig$WebappInfo getWebappInfoFromWebsiteId(java.lang.String) `
- `public static java.lang.String getWebSiteId(org.apache.ofbiz.base.component.ComponentConfig$WebappInfo) `
- `public static org.apache.ofbiz.service.LocalDispatcher getDispatcher(javax.servlet.ServletContext);`
- `public static void setAttributesFromRequestBody(javax.servlet.ServletRequest);`
- `public static org.apache.ofbiz.service.LocalDispatcher makeWebappDispatcher(javax.servlet.ServletContext, org.apache.ofbiz.entity.Delegator);`
- `public static org.apache.ofbiz.entity.Delegator getDelegator(javax.servlet.ServletContext);`
- `public static org.apache.ofbiz.security.Security getSecurity(javax.servlet.ServletContext);`

### `ControlServlet` — class
Vollständiger Name: `org.apache.ofbiz.webapp.control.ControlServlet`
- `public org.apache.ofbiz.webapp.control.ControlServlet();`
- `public void init() `
- `public void doPost(javax.servlet.http.HttpServletRequest, javax.servlet.http.HttpServletResponse) `
- `public void doDelete(javax.servlet.http.HttpServletRequest, javax.servlet.http.HttpServletResponse) `
- `public void doPut(javax.servlet.http.HttpServletRequest, javax.servlet.http.HttpServletResponse) `
- `public void doGet(javax.servlet.http.HttpServletRequest, javax.servlet.http.HttpServletResponse) `
- `public void handle(javax.servlet.http.HttpServletRequest, javax.servlet.http.HttpServletResponse) `

### `LoopWriter` — class
Vollständiger Name: `org.apache.ofbiz.webapp.ftl.LoopWriter`
- `public org.apache.ofbiz.webapp.ftl.LoopWriter(java.io.Writer);`
- `public int onStart() `
- `public int afterBody() `
- `public void onError(java.lang.Throwable) `
- `public void close() `
- `public void write(char[], int, int);`
- `public void flush() `

### `ConfigXMLReader` — class
Vollständiger Name: `org.apache.ofbiz.webapp.control.ConfigXMLReader`
- `public static org.apache.ofbiz.webapp.control.ConfigXMLReader$RequestResponse getEmptyNoneRequestResponse();`
- `public static java.util.Set<java.lang.String> findControllerFilesWithRequest(java.lang.String, java.lang.String) `
- `public static java.util.Set<java.lang.String> findControllerRequestUniqueForTargetType(java.lang.String, java.lang.String) `
- `public static org.apache.ofbiz.webapp.control.ConfigXMLReader$ControllerConfig getControllerConfig(org.apache.ofbiz.base.component.ComponentConfig$WebappInfo) `
- `public static org.apache.ofbiz.webapp.control.ConfigXMLReader$ControllerConfig getControllerConfig(java.net.URL) `
- `public static java.net.URL getControllerConfigURL(javax.servlet.ServletContext);`

### `FileUploadProgressListener` — class
Vollständiger Name: `org.apache.ofbiz.webapp.event.FileUploadProgressListener`
- `public org.apache.ofbiz.webapp.event.FileUploadProgressListener();`
- `public void update(long, long, int);`
- `public long getContentLength();`
- `public long getBytesRead();`
- `public int getItems();`
- `public boolean hasStarted();`

### `PropFindHelper` — class
Vollständiger Name: `org.apache.ofbiz.webapp.webdav.PropFindHelper`
- `public org.apache.ofbiz.webapp.webdav.PropFindHelper(org.w3c.dom.Document);`
- `public org.w3c.dom.Element createPropElement(java.util.List<org.w3c.dom.Element>);`
- `public org.w3c.dom.Element createPropStatElement(org.w3c.dom.Element, java.lang.String);`
- `public java.util.List<org.w3c.dom.Element> getFindPropsList(java.lang.String);`
- `public boolean isAllProp();`
- `public boolean isPropName();`

### `SameSiteFilter` — class
Vollständiger Name: `org.apache.ofbiz.webapp.control.SameSiteFilter`
- `public org.apache.ofbiz.webapp.control.SameSiteFilter();`
- `public void init(javax.servlet.FilterConfig) `
- `public void doFilter(javax.servlet.ServletRequest, javax.servlet.ServletResponse, javax.servlet.FilterChain) `
- `public static void addSameSiteCookieAttribute(javax.servlet.http.HttpServletResponse);`
- `public void destroy();`

### `OfbizCacheStorage` — class
Vollständiger Name: `org.apache.ofbiz.webapp.ftl.OfbizCacheStorage`
- `public org.apache.ofbiz.webapp.ftl.OfbizCacheStorage(java.lang.String);`
- `public java.lang.Object get(java.lang.Object);`
- `public void put(java.lang.Object, java.lang.Object);`
- `public void remove(java.lang.Object);`
- `public void clear();`

### `OfbizUrlBuilder` — class
Vollständiger Name: `org.apache.ofbiz.webapp.OfbizUrlBuilder`
- `public static org.apache.ofbiz.webapp.OfbizUrlBuilder from(javax.servlet.http.HttpServletRequest) `
- `public static org.apache.ofbiz.webapp.OfbizUrlBuilder from(org.apache.ofbiz.base.component.ComponentConfig$WebappInfo, org.apache.ofbiz.entity.Delegator) `
- `public boolean buildFullUrl(java.lang.Appendable, java.lang.String, boolean) `
- `public boolean buildHostPart(java.lang.Appendable, java.lang.String, boolean) `
- `public void buildPathPart(java.lang.Appendable, java.lang.String) `

### `VisitHandler` — class
Vollständiger Name: `org.apache.ofbiz.webapp.stats.VisitHandler`
- `public org.apache.ofbiz.webapp.stats.VisitHandler();`
- `public static void setUserLogin(javax.servlet.http.HttpSession, org.apache.ofbiz.entity.GenericValue, boolean);`
- `public static java.lang.String getVisitId(javax.servlet.http.HttpSession);`
- `public static org.apache.ofbiz.entity.GenericValue getVisit(javax.servlet.http.HttpSession);`
- `public static org.apache.ofbiz.entity.GenericValue getVisitor(javax.servlet.http.HttpServletRequest, javax.servlet.http.HttpServletResponse);`

## Modul: webtools (54 Klassen, 365 public Methoden)

### `ArtifactInfoFactory` — class
Vollständiger Name: `org.apache.ofbiz.webtools.artifactinfo.ArtifactInfoFactory`
- `public java.util.Map<java.lang.String, java.util.Set<org.apache.ofbiz.webtools.artifactinfo.ServiceEcaArtifactInfo>> getAllServiceEcaInfosReferringToServiceName();`
- `public java.util.Map<java.lang.String, java.util.Set<org.apache.ofbiz.webtools.artifactinfo.ServiceArtifactInfo>> getAllServiceInfosReferringToServiceName();`
- `public java.util.Map<java.lang.String, java.util.Set<org.apache.ofbiz.webtools.artifactinfo.FormWidgetArtifactInfo>> getAllFormInfosReferringToServiceName();`
- `public java.util.Map<java.lang.String, java.util.Set<org.apache.ofbiz.webtools.artifactinfo.FormWidgetArtifactInfo>> getAllFormInfosBasedOnServiceName();`
- `public java.util.Map<java.lang.String, java.util.Set<org.apache.ofbiz.webtools.artifactinfo.ScreenWidgetArtifactInfo>> getAllScreenInfosReferringToServiceName();`
- `public java.util.Map<java.lang.String, java.util.Set<org.apache.ofbiz.webtools.artifactinfo.ControllerRequestArtifactInfo>> getAllRequestInfosReferringToServiceName();`
- `public java.util.Map<java.lang.String, java.util.Set<org.apache.ofbiz.webtools.artifactinfo.ServiceArtifactInfo>> getAllServiceInfosReferringToEntityName();`
- `public java.util.Map<java.lang.String, java.util.Set<org.apache.ofbiz.webtools.artifactinfo.FormWidgetArtifactInfo>> getAllFormInfosReferringToEntityName();`
- `public java.util.Map<java.lang.String, java.util.Set<org.apache.ofbiz.webtools.artifactinfo.ScreenWidgetArtifactInfo>> getAllScreenInfosReferringToEntityName();`
- `public java.util.Map<org.apache.ofbiz.service.eca.ServiceEcaRule, java.util.Set<org.apache.ofbiz.webtools.artifactinfo.ServiceArtifactInfo>> getAllServiceInfosReferringToServiceEcaRule();`
- `public java.util.Map<java.lang.String, java.util.Set<org.apache.ofbiz.webtools.artifactinfo.FormWidgetArtifactInfo>> getAllFormInfosExtendingForm();`
- `public java.util.Map<java.lang.String, java.util.Set<org.apache.ofbiz.webtools.artifactinfo.ScreenWidgetArtifactInfo>> getAllScreenInfosReferringToForm();`
- `public java.util.Map<java.lang.String, java.util.Set<org.apache.ofbiz.webtools.artifactinfo.ScreenWidgetArtifactInfo>> getAllScreenInfosReferringToScreen();`
- `public java.util.Map<java.lang.String, java.util.Set<org.apache.ofbiz.webtools.artifactinfo.ControllerViewArtifactInfo>> getAllViewInfosReferringToScreen();`
- `public java.util.Map<java.lang.String, java.util.Set<org.apache.ofbiz.webtools.artifactinfo.ControllerRequestArtifactInfo>> getAllRequestInfosReferringToView();`
- *(... 26 weitere Methoden)*

### `ServiceArtifactInfo` — class
Vollständiger Name: `org.apache.ofbiz.webtools.artifactinfo.ServiceArtifactInfo`
- `public org.apache.ofbiz.webtools.artifactinfo.ServiceArtifactInfo(java.lang.String, org.apache.ofbiz.webtools.artifactinfo.ArtifactInfoFactory) `
- `public void populateAll() `
- `public org.apache.ofbiz.service.ModelService getModelService();`
- `public void setDisplayPrefix(java.lang.String);`
- `public java.lang.String getDisplayName();`
- `public java.lang.String getDisplayPrefixedName();`
- `public java.lang.String getDisplayType();`
- `public java.lang.String getType();`
- `public java.lang.String getUniqueId();`
- `public java.net.URL getLocationURL() `
- `public java.net.URL getImplementationLocationURL() `
- `public java.util.Set<org.apache.ofbiz.webtools.artifactinfo.EntityArtifactInfo> getEntitiesUsedByService();`
- `public java.util.Set<org.apache.ofbiz.webtools.artifactinfo.ServiceArtifactInfo> getServicesCallingService();`
- `public java.util.Set<org.apache.ofbiz.webtools.artifactinfo.ServiceArtifactInfo> getServicesCalledByService();`
- `public java.util.Set<org.apache.ofbiz.webtools.artifactinfo.ServiceArtifactInfo> getServicesCalledByServiceEcas();`
- *(... 11 weitere Methoden)*

### `ControllerRequestArtifactInfo` — class
Vollständiger Name: `org.apache.ofbiz.webtools.artifactinfo.ControllerRequestArtifactInfo`
- `public org.apache.ofbiz.webtools.artifactinfo.ControllerRequestArtifactInfo(java.net.URL, java.lang.String, org.apache.ofbiz.webtools.artifactinfo.ArtifactInfoFactory) `
- `public void populateAll() `
- `public java.net.URL getControllerXmlUrl();`
- `public java.lang.String getRequestUri();`
- `public java.lang.String getDisplayName();`
- `public java.lang.String getDisplayType();`
- `public java.lang.String getType();`
- `public java.lang.String getUniqueId();`
- `public java.net.URL getLocationURL() `
- `public boolean equals(java.lang.Object);`
- `public int hashCode();`
- `public org.apache.ofbiz.webtools.artifactinfo.ServiceArtifactInfo getServiceCalledByRequestEvent();`
- `public java.util.Set<org.apache.ofbiz.webtools.artifactinfo.FormWidgetArtifactInfo> getFormInfosReferringToRequest();`
- `public java.util.Set<org.apache.ofbiz.webtools.artifactinfo.FormWidgetArtifactInfo> getFormInfosTargetingRequest();`
- `public java.util.Set<org.apache.ofbiz.webtools.artifactinfo.ScreenWidgetArtifactInfo> getScreenInfosReferringToRequest();`
- *(... 3 weitere Methoden)*

### `EntityArtifactInfo` — class
Vollständiger Name: `org.apache.ofbiz.webtools.artifactinfo.EntityArtifactInfo`
- `public org.apache.ofbiz.webtools.artifactinfo.EntityArtifactInfo(java.lang.String, org.apache.ofbiz.webtools.artifactinfo.ArtifactInfoFactory) `
- `public void populateAll() `
- `public org.apache.ofbiz.entity.model.ModelEntity getModelEntity();`
- `public java.lang.String getDisplayName();`
- `public java.lang.String getDisplayType();`
- `public java.lang.String getType();`
- `public java.lang.String getUniqueId();`
- `public java.net.URL getLocationURL() `
- `public boolean equals(java.lang.Object);`
- `public int hashCode();`
- `public java.util.Set<org.apache.ofbiz.webtools.artifactinfo.EntityArtifactInfo> getEntitiesRelatedOne();`
- `public java.util.Set<org.apache.ofbiz.webtools.artifactinfo.EntityArtifactInfo> getEntitiesRelatedMany();`
- `public java.util.Set<org.apache.ofbiz.webtools.artifactinfo.ServiceArtifactInfo> getServicesUsingEntity();`
- `public java.util.Set<org.apache.ofbiz.webtools.artifactinfo.ServiceArtifactInfo> getServicesCalledByEntityEca();`
- `public java.util.Set<org.apache.ofbiz.entityext.eca.EntityEcaRule> getEntityEcaRules();`
- *(... 2 weitere Methoden)*

### `FormWidgetArtifactInfo` — class
Vollständiger Name: `org.apache.ofbiz.webtools.artifactinfo.FormWidgetArtifactInfo`
- `public org.apache.ofbiz.webtools.artifactinfo.FormWidgetArtifactInfo(java.lang.String, java.lang.String, org.apache.ofbiz.webtools.artifactinfo.ArtifactInfoFactory) `
- `public void populateAll() `
- `public java.lang.String getDisplayName();`
- `public java.lang.String getDisplayType();`
- `public java.lang.String getType();`
- `public java.lang.String getUniqueId();`
- `public java.net.URL getLocationURL() `
- `public boolean equals(java.lang.Object);`
- `public int hashCode();`
- `public java.util.Set<org.apache.ofbiz.webtools.artifactinfo.EntityArtifactInfo> getEntitiesUsedInForm();`
- `public java.util.Set<org.apache.ofbiz.webtools.artifactinfo.ServiceArtifactInfo> getServicesUsedInForm();`
- `public org.apache.ofbiz.webtools.artifactinfo.FormWidgetArtifactInfo getFormThisFormExtends();`
- `public java.util.Set<org.apache.ofbiz.webtools.artifactinfo.FormWidgetArtifactInfo> getFormsExtendingThisForm();`
- `public java.util.Set<org.apache.ofbiz.webtools.artifactinfo.ScreenWidgetArtifactInfo> getScreensIncludingThisForm();`
- `public java.util.Set<org.apache.ofbiz.webtools.artifactinfo.ControllerRequestArtifactInfo> getRequestsLinkedToInForm();`
- *(... 1 weitere Methoden)*

### `ScreenWidgetArtifactInfo` — class
Vollständiger Name: `org.apache.ofbiz.webtools.artifactinfo.ScreenWidgetArtifactInfo`
- `public org.apache.ofbiz.webtools.artifactinfo.ScreenWidgetArtifactInfo(java.lang.String, java.lang.String, org.apache.ofbiz.webtools.artifactinfo.ArtifactInfoFactory) `
- `public void populateAll() `
- `public java.lang.String getDisplayName();`
- `public java.lang.String getDisplayType();`
- `public java.lang.String getType();`
- `public java.lang.String getUniqueId();`
- `public java.net.URL getLocationURL() `
- `public boolean equals(java.lang.Object);`
- `public int hashCode();`
- `public java.util.Set<org.apache.ofbiz.webtools.artifactinfo.ControllerViewArtifactInfo> getViewsReferringToScreen();`
- `public java.util.Set<org.apache.ofbiz.webtools.artifactinfo.EntityArtifactInfo> getEntitiesUsedInScreen();`
- `public java.util.Set<org.apache.ofbiz.webtools.artifactinfo.ServiceArtifactInfo> getServicesUsedInScreen();`
- `public java.util.Set<org.apache.ofbiz.webtools.artifactinfo.FormWidgetArtifactInfo> getFormsIncludedInScreen();`
- `public java.util.Set<org.apache.ofbiz.webtools.artifactinfo.ScreenWidgetArtifactInfo> getScreensIncludedInScreen();`
- `public java.util.Set<org.apache.ofbiz.webtools.artifactinfo.ScreenWidgetArtifactInfo> getScreensIncludingThisScreen();`
- *(... 1 weitere Methoden)*

### `ServiceEcaArtifactInfo` — class
Vollständiger Name: `org.apache.ofbiz.webtools.artifactinfo.ServiceEcaArtifactInfo`
- `public org.apache.ofbiz.webtools.artifactinfo.ServiceEcaArtifactInfo(org.apache.ofbiz.service.eca.ServiceEcaRule, org.apache.ofbiz.webtools.artifactinfo.ArtifactInfoFactory) `
- `public void populateAll() `
- `public java.lang.String getDisplayName();`
- `public java.lang.String getDisplayType();`
- `public java.lang.String getType();`
- `public java.lang.String getUniqueId();`
- `public java.net.URL getLocationURL() `
- `public org.apache.ofbiz.service.eca.ServiceEcaRule getServiceEcaRule();`
- `public void setDisplayPrefix(java.lang.String);`
- `public void setDisplaySuffixNum(int);`
- `public java.lang.String getDisplayPrefixedName();`
- `public java.util.Set<org.apache.ofbiz.webtools.artifactinfo.ServiceArtifactInfo> getServicesCalledByServiceEcaActions();`
- `public java.util.Set<org.apache.ofbiz.webtools.artifactinfo.ServiceArtifactInfo> getServicesTriggeringServiceEca();`
- `public java.util.Map<java.lang.String, java.lang.Object> createEoModelMap(java.util.Set<org.apache.ofbiz.webtools.artifactinfo.ServiceArtifactInfo>, java.util.Set<org.apache.ofbiz.webtools.artifactinfo.ServiceArtifactInfo>, boolean);`
- `public boolean equals(java.lang.Object);`
- *(... 1 weitere Methoden)*

### `ArtifactInfoBase` — class
Vollständiger Name: `org.apache.ofbiz.webtools.artifactinfo.ArtifactInfoBase`
- `public org.apache.ofbiz.webtools.artifactinfo.ArtifactInfoFactory getAif();`
- `public org.apache.ofbiz.webtools.artifactinfo.ArtifactInfoBase(org.apache.ofbiz.webtools.artifactinfo.ArtifactInfoFactory);`
- `public int compareTo(org.apache.ofbiz.webtools.artifactinfo.ArtifactInfoBase);`
- `public boolean equals(java.lang.Object);`
- `public abstract java.lang.String getDisplayName();`
- `public abstract java.lang.String getDisplayType();`
- `public abstract java.net.URL getLocationURL() `
- `public abstract java.lang.String getType();`
- `public abstract java.lang.String getUniqueId();`
- `public int hashCode();`
- `public java.lang.String toString();`
- `public int compareTo(java.lang.Object);`

### `ControllerViewArtifactInfo` — class
Vollständiger Name: `org.apache.ofbiz.webtools.artifactinfo.ControllerViewArtifactInfo`
- `public org.apache.ofbiz.webtools.artifactinfo.ControllerViewArtifactInfo(java.net.URL, java.lang.String, org.apache.ofbiz.webtools.artifactinfo.ArtifactInfoFactory) `
- `public java.net.URL getControllerXmlUrl();`
- `public java.lang.String getViewUri();`
- `public java.lang.String getDisplayName();`
- `public java.lang.String getDisplayType();`
- `public java.lang.String getType();`
- `public java.lang.String getUniqueId();`
- `public java.net.URL getLocationURL() `
- `public boolean equals(java.lang.Object);`
- `public int hashCode();`
- `public java.util.Set<org.apache.ofbiz.webtools.artifactinfo.ControllerRequestArtifactInfo> getRequestsThatThisViewIsResponseTo();`
- `public org.apache.ofbiz.webtools.artifactinfo.ScreenWidgetArtifactInfo getScreenCalledByThisView();`

### `LabelManagerFactory` — class
Vollständiger Name: `org.apache.ofbiz.webtools.labelmanager.LabelManagerFactory`
- `public static synchronized org.apache.ofbiz.webtools.labelmanager.LabelManagerFactory getInstance() `
- `public void findMatchingLabels(java.lang.String, java.lang.String, java.lang.String, java.lang.String, boolean) `
- `public org.apache.ofbiz.webtools.labelmanager.LabelFile getLabelFile(java.lang.String);`
- `public java.util.Map<java.lang.String, org.apache.ofbiz.webtools.labelmanager.LabelInfo> getLabels();`
- `public java.util.Set<java.lang.String> getLocalesFound();`
- `public static java.util.Collection<org.apache.ofbiz.webtools.labelmanager.LabelFile> getFilesFound();`
- `public static java.util.Set<java.lang.String> getComponentNamesFound();`
- `public java.util.Set<java.lang.String> getLabelsList();`
- `public int getDuplicatedLocalesLabels();`
- `public java.util.List<org.apache.ofbiz.webtools.labelmanager.LabelInfo> getDuplicatedLocalesLabelsList();`
- `public int updateLabelValue(java.util.List<java.lang.String>, java.util.List<java.lang.String>, java.util.List<java.lang.String>, org.apache.ofbiz.webtools.labelmanager.LabelInfo, java.lang.String, java.lang.String, java.lang.String);`

### `WebToolsServices` — class
Vollständiger Name: `org.apache.ofbiz.webtools.WebToolsServices`
- `public org.apache.ofbiz.webtools.WebToolsServices();`
- `public static java.util.Map<java.lang.String, java.lang.Object> entityImport(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> entityImportDir(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> entityImportReaders(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> parseEntityXmlFile(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> entityExportAll(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> getEntityRefData(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> exportEntityEoModelBundle(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> entityMaintPermCheck(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> exportServiceEoModelBundle(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`

### `LabelInfo` — class
Vollständiger Name: `org.apache.ofbiz.webtools.labelmanager.LabelInfo`
- `public org.apache.ofbiz.webtools.labelmanager.LabelInfo(java.lang.String, java.lang.String, java.lang.String, java.lang.String, java.lang.String, java.lang.String);`
- `public java.lang.String getLabelKey();`
- `public java.lang.String getLabelKeyComment();`
- `public void setLabelKeyComment(java.lang.String);`
- `public java.lang.String getFileName();`
- `public org.apache.ofbiz.webtools.labelmanager.LabelValue getLabelValue(java.lang.String);`
- `public int getLabelValueSize();`
- `public boolean setLabelValue(java.lang.String, java.lang.String, java.lang.String, boolean);`

### `FindUtilCache` [Groovy] — class
Vollständiger Name: `org.apache.ofbiz.webtools.cache.FindUtilCache`
- `public org.apache.ofbiz.webtools.cache.FindUtilCache();`
- `public org.apache.ofbiz.webtools.cache.FindUtilCache(groovy.lang.Binding);`
- `public static void main(java.lang.String...);`
- `public java.lang.Object run();`
- `public static void __$swapInit();`

### `FindGeneric` [Groovy] — class
Vollständiger Name: `org.apache.ofbiz.webtools.entity.FindGeneric`
- `public org.apache.ofbiz.webtools.entity.FindGeneric();`
- `public org.apache.ofbiz.webtools.entity.FindGeneric(groovy.lang.Binding);`
- `public static void main(java.lang.String...);`
- `public java.lang.Object run();`
- `public java.util.List<java.lang.String> getFieldsToSelect(org.apache.ofbiz.entity.model.ModelEntity);`

### `LabelValue` — class
Vollständiger Name: `org.apache.ofbiz.webtools.labelmanager.LabelValue`
- `public org.apache.ofbiz.webtools.labelmanager.LabelValue(java.lang.String, java.lang.String);`
- `public java.lang.String getLabelValue();`
- `public java.lang.String getLabelComment();`
- `public void setLabelValue(java.lang.String);`
- `public void setLabelComment(java.lang.String);`

### `AvailableServices` [Groovy] — class
Vollständiger Name: `org.apache.ofbiz.webtools.service.AvailableServices`
- `public org.apache.ofbiz.webtools.service.AvailableServices();`
- `public org.apache.ofbiz.webtools.service.AvailableServices(groovy.lang.Binding);`
- `public static void main(java.lang.String...);`
- `public java.lang.Object run();`
- `public java.util.List getEcaListForService(java.lang.String);`

### `UtilCacheEvents` — class
Vollständiger Name: `org.apache.ofbiz.webtools.UtilCacheEvents`
- `public static java.lang.String removeElementEvent(javax.servlet.http.HttpServletRequest, javax.servlet.http.HttpServletResponse);`
- `public static java.lang.String clearEvent(javax.servlet.http.HttpServletRequest, javax.servlet.http.HttpServletResponse);`
- `public static java.lang.String clearAllEvent(javax.servlet.http.HttpServletRequest, javax.servlet.http.HttpServletResponse);`
- `public static java.lang.String clearSelectedCachesEvent(javax.servlet.http.HttpServletRequest, javax.servlet.http.HttpServletResponse);`
- `public static java.lang.String updateEvent(javax.servlet.http.HttpServletRequest, javax.servlet.http.HttpServletResponse);`

### `ArtifactInfo` [Groovy] — class
Vollständiger Name: `org.apache.ofbiz.webtools.artifactinfo.ArtifactInfo`
- `public org.apache.ofbiz.webtools.artifactinfo.ArtifactInfo();`
- `public org.apache.ofbiz.webtools.artifactinfo.ArtifactInfo(groovy.lang.Binding);`
- `public static void main(java.lang.String...);`
- `public java.lang.Object run();`

### `ComponentList` [Groovy] — class
Vollständiger Name: `org.apache.ofbiz.webtools.artifactinfo.ComponentList`
- `public org.apache.ofbiz.webtools.artifactinfo.ComponentList();`
- `public org.apache.ofbiz.webtools.artifactinfo.ComponentList(groovy.lang.Binding);`
- `public static void main(java.lang.String...);`
- `public java.lang.Object run();`

### `EditUtilCache` [Groovy] — class
Vollständiger Name: `org.apache.ofbiz.webtools.cache.EditUtilCache`
- `public org.apache.ofbiz.webtools.cache.EditUtilCache();`
- `public org.apache.ofbiz.webtools.cache.EditUtilCache(groovy.lang.Binding);`
- `public static void main(java.lang.String...);`
- `public java.lang.Object run();`

## Modul: widget (95 Klassen, 1279 public Methoden)

### `ModelForm` — class
Vollständiger Name: `org.apache.ofbiz.widget.model.ModelForm`
- `public java.util.List<org.apache.ofbiz.widget.model.ModelAction> getActions();`
- `public java.util.List<org.apache.ofbiz.widget.model.ModelForm$AltRowStyle> getAltRowStyles();`
- `public java.util.List<org.apache.ofbiz.widget.model.ModelForm$AltTarget> getAltTargets();`
- `public java.util.List<org.apache.ofbiz.widget.model.ModelForm$AutoFieldsEntity> getAutoFieldsEntities();`
- `public java.util.List<org.apache.ofbiz.widget.model.ModelForm$AutoFieldsService> getAutoFieldsServices();`
- `public java.lang.String getBoundaryCommentName();`
- `public boolean getClientAutocompleteFields();`
- `public java.lang.String getContainerId();`
- `public java.lang.String getContainerStyle();`
- `public java.lang.String getDefaultEntityName();`
- `public org.apache.ofbiz.widget.model.ModelForm$FieldGroup getDefaultFieldGroup();`
- `public java.util.Map<java.lang.String, ? extends java.lang.Object> getDefaultMap(java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public java.lang.String getDefaultMapName();`
- `public java.lang.String getDefaultRequiredFieldStyle();`
- `public java.lang.String getDefaultServiceName();`
- *(... 84 weitere Methoden)*

### `ModelFormFieldBuilder` — class
Vollständiger Name: `org.apache.ofbiz.widget.model.ModelFormFieldBuilder`
- `public org.apache.ofbiz.widget.model.ModelFormFieldBuilder();`
- `public org.apache.ofbiz.widget.model.ModelFormFieldBuilder(org.w3c.dom.Element, org.apache.ofbiz.widget.model.ModelForm, org.apache.ofbiz.entity.model.ModelReader, org.apache.ofbiz.service.DispatchContext);`
- `public org.apache.ofbiz.widget.model.ModelFormFieldBuilder(org.apache.ofbiz.widget.model.ModelFormField);`
- `public org.apache.ofbiz.widget.model.ModelFormFieldBuilder(org.apache.ofbiz.widget.model.ModelFormFieldBuilder);`
- `public org.apache.ofbiz.widget.model.ModelFormFieldBuilder addOnChangeUpdateArea(org.apache.ofbiz.widget.model.ModelForm$UpdateArea);`
- `public org.apache.ofbiz.widget.model.ModelFormFieldBuilder addOnClickUpdateArea(org.apache.ofbiz.widget.model.ModelForm$UpdateArea);`
- `public org.apache.ofbiz.widget.model.ModelFormField build();`
- `public org.apache.ofbiz.base.util.string.FlexibleStringExpander getAction();`
- `public java.lang.String getAttributeName();`
- `public boolean getEncodeOutput();`
- `public java.lang.String getEntityName();`
- `public org.apache.ofbiz.base.util.collections.FlexibleMapAccessor<java.lang.Object> getEntryAcsr();`
- `public java.lang.String getEvent();`
- `public org.apache.ofbiz.widget.model.FieldInfo getFieldInfo();`
- `public java.lang.String getFieldName();`
- *(... 75 weitere Methoden)*

### `MacroFormRenderer` — class
Vollständiger Name: `org.apache.ofbiz.widget.renderer.macro.MacroFormRenderer`
- `public org.apache.ofbiz.widget.renderer.macro.MacroFormRenderer(java.lang.String, javax.servlet.http.HttpServletRequest, javax.servlet.http.HttpServletResponse) `
- `public org.apache.ofbiz.widget.renderer.macro.MacroFormRenderer(java.lang.String, javax.servlet.http.HttpServletRequest, javax.servlet.http.HttpServletResponse, org.apache.ofbiz.widget.renderer.macro.FtlWriter, org.apache.ofbiz.widget.renderer.macro.RenderableFtlFormElementsBuilder) `
- `public boolean getRenderPagination();`
- `public void setRenderPagination(boolean);`
- `public void writeFtlElement(java.lang.Appendable, org.apache.ofbiz.widget.renderer.macro.renderable.RenderableFtl);`
- `public void renderLabel(java.lang.Appendable, java.util.Map<java.lang.String, java.lang.Object>, org.apache.ofbiz.widget.model.ModelScreenWidget$Label);`
- `public void renderDisplayField(java.lang.Appendable, java.util.Map<java.lang.String, java.lang.Object>, org.apache.ofbiz.widget.model.ModelFormField$DisplayField) `
- `public void renderHyperlinkField(java.lang.Appendable, java.util.Map<java.lang.String, java.lang.Object>, org.apache.ofbiz.widget.model.ModelFormField$HyperlinkField) `
- `public void renderMenuField(java.lang.Appendable, java.util.Map<java.lang.String, java.lang.Object>, org.apache.ofbiz.widget.model.ModelFormField$MenuField) `
- `public void renderTextField(java.lang.Appendable, java.util.Map<java.lang.String, java.lang.Object>, org.apache.ofbiz.widget.model.ModelFormField$TextField);`
- `public void renderTextareaField(java.lang.Appendable, java.util.Map<java.lang.String, java.lang.Object>, org.apache.ofbiz.widget.model.ModelFormField$TextareaField);`
- `public void renderDateTimeField(java.lang.Appendable, java.util.Map<java.lang.String, java.lang.Object>, org.apache.ofbiz.widget.model.ModelFormField$DateTimeField);`
- `public void renderDropDownField(java.lang.Appendable, java.util.Map<java.lang.String, java.lang.Object>, org.apache.ofbiz.widget.model.ModelFormField$DropDownField) `
- `public void renderCheckField(java.lang.Appendable, java.util.Map<java.lang.String, java.lang.Object>, org.apache.ofbiz.widget.model.ModelFormField$CheckField) `
- `public void renderRadioField(java.lang.Appendable, java.util.Map<java.lang.String, java.lang.Object>, org.apache.ofbiz.widget.model.ModelFormField$RadioField) `
- *(... 57 weitere Methoden)*

### `ModelFormField` — class
Vollständiger Name: `org.apache.ofbiz.widget.model.ModelFormField`
- `public static org.apache.ofbiz.widget.model.ModelFormField from(java.util.function.Consumer<org.apache.ofbiz.widget.model.ModelFormFieldBuilder>);`
- `public static org.apache.ofbiz.widget.model.ModelFormField from(org.apache.ofbiz.widget.model.ModelFormFieldBuilder);`
- `public org.apache.ofbiz.base.util.string.FlexibleStringExpander getAction();`
- `public java.lang.String getAction(java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public java.lang.String getAttributeName();`
- `public java.lang.String getCurrentContainerId(java.util.Map<java.lang.String, java.lang.Object>);`
- `public boolean getEncodeOutput();`
- `public java.lang.String getEntityName();`
- `public java.lang.String getEntry(java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public java.lang.String getEntry(java.util.Map<java.lang.String, ? extends java.lang.Object>, java.lang.String);`
- `public org.apache.ofbiz.base.util.collections.FlexibleMapAccessor<java.lang.Object> getEntryAcsr();`
- `public java.lang.String getEntryName();`
- `public java.lang.String getEvent();`
- `public org.apache.ofbiz.widget.model.FieldInfo getFieldInfo();`
- `public java.lang.String getFieldName();`
- *(... 51 weitere Methoden)*

### `FoFormRenderer` — class
Vollständiger Name: `org.apache.ofbiz.widget.renderer.fo.FoFormRenderer`
- `public org.apache.ofbiz.widget.renderer.fo.FoFormRenderer();`
- `public org.apache.ofbiz.widget.renderer.fo.FoFormRenderer(javax.servlet.http.HttpServletRequest, javax.servlet.http.HttpServletResponse) `
- `public void renderDisplayField(java.lang.Appendable, java.util.Map<java.lang.String, java.lang.Object>, org.apache.ofbiz.widget.model.ModelFormField$DisplayField) `
- `public void renderHyperlinkField(java.lang.Appendable, java.util.Map<java.lang.String, java.lang.Object>, org.apache.ofbiz.widget.model.ModelFormField$HyperlinkField) `
- `public void renderMenuField(java.lang.Appendable, java.util.Map<java.lang.String, java.lang.Object>, org.apache.ofbiz.widget.model.ModelFormField$MenuField) `
- `public void renderTextField(java.lang.Appendable, java.util.Map<java.lang.String, java.lang.Object>, org.apache.ofbiz.widget.model.ModelFormField$TextField) `
- `public void renderTextareaField(java.lang.Appendable, java.util.Map<java.lang.String, java.lang.Object>, org.apache.ofbiz.widget.model.ModelFormField$TextareaField) `
- `public void renderDateTimeField(java.lang.Appendable, java.util.Map<java.lang.String, java.lang.Object>, org.apache.ofbiz.widget.model.ModelFormField$DateTimeField) `
- `public void renderDropDownField(java.lang.Appendable, java.util.Map<java.lang.String, java.lang.Object>, org.apache.ofbiz.widget.model.ModelFormField$DropDownField) `
- `public void renderCheckField(java.lang.Appendable, java.util.Map<java.lang.String, java.lang.Object>, org.apache.ofbiz.widget.model.ModelFormField$CheckField) `
- `public void renderRadioField(java.lang.Appendable, java.util.Map<java.lang.String, java.lang.Object>, org.apache.ofbiz.widget.model.ModelFormField$RadioField) `
- `public void renderSubmitField(java.lang.Appendable, java.util.Map<java.lang.String, java.lang.Object>, org.apache.ofbiz.widget.model.ModelFormField$SubmitField) `
- `public void renderResetField(java.lang.Appendable, java.util.Map<java.lang.String, java.lang.Object>, org.apache.ofbiz.widget.model.ModelFormField$ResetField) `
- `public void renderHiddenField(java.lang.Appendable, java.util.Map<java.lang.String, java.lang.Object>, org.apache.ofbiz.widget.model.ModelFormField$HiddenField) `
- `public void renderHiddenField(java.lang.Appendable, java.util.Map<java.lang.String, java.lang.Object>, org.apache.ofbiz.widget.model.ModelFormField, java.lang.String) `
- *(... 47 weitere Methoden)*

### `FormStringRenderer` — interface
Vollständiger Name: `org.apache.ofbiz.widget.renderer.FormStringRenderer`
- `public abstract void renderDisplayField(java.lang.Appendable, java.util.Map<java.lang.String, java.lang.Object>, org.apache.ofbiz.widget.model.ModelFormField$DisplayField) `
- `public abstract void renderHyperlinkField(java.lang.Appendable, java.util.Map<java.lang.String, java.lang.Object>, org.apache.ofbiz.widget.model.ModelFormField$HyperlinkField) `
- `public abstract void renderMenuField(java.lang.Appendable, java.util.Map<java.lang.String, java.lang.Object>, org.apache.ofbiz.widget.model.ModelFormField$MenuField) `
- `public abstract void renderTextField(java.lang.Appendable, java.util.Map<java.lang.String, java.lang.Object>, org.apache.ofbiz.widget.model.ModelFormField$TextField) `
- `public abstract void renderTextareaField(java.lang.Appendable, java.util.Map<java.lang.String, java.lang.Object>, org.apache.ofbiz.widget.model.ModelFormField$TextareaField) `
- `public abstract void renderDateTimeField(java.lang.Appendable, java.util.Map<java.lang.String, java.lang.Object>, org.apache.ofbiz.widget.model.ModelFormField$DateTimeField) `
- `public abstract void renderDropDownField(java.lang.Appendable, java.util.Map<java.lang.String, java.lang.Object>, org.apache.ofbiz.widget.model.ModelFormField$DropDownField) `
- `public abstract void renderCheckField(java.lang.Appendable, java.util.Map<java.lang.String, java.lang.Object>, org.apache.ofbiz.widget.model.ModelFormField$CheckField) `
- `public abstract void renderRadioField(java.lang.Appendable, java.util.Map<java.lang.String, java.lang.Object>, org.apache.ofbiz.widget.model.ModelFormField$RadioField) `
- `public abstract void renderSubmitField(java.lang.Appendable, java.util.Map<java.lang.String, java.lang.Object>, org.apache.ofbiz.widget.model.ModelFormField$SubmitField) `
- `public abstract void renderResetField(java.lang.Appendable, java.util.Map<java.lang.String, java.lang.Object>, org.apache.ofbiz.widget.model.ModelFormField$ResetField) `
- `public abstract void renderHiddenField(java.lang.Appendable, java.util.Map<java.lang.String, java.lang.Object>, org.apache.ofbiz.widget.model.ModelFormField, java.lang.String) `
- `public abstract void renderHiddenField(java.lang.Appendable, java.util.Map<java.lang.String, java.lang.Object>, org.apache.ofbiz.widget.model.ModelFormField$HiddenField) `
- `public abstract void renderIgnoredField(java.lang.Appendable, java.util.Map<java.lang.String, java.lang.Object>, org.apache.ofbiz.widget.model.ModelFormField$IgnoredField) `
- `public abstract void renderFieldTitle(java.lang.Appendable, java.util.Map<java.lang.String, java.lang.Object>, org.apache.ofbiz.widget.model.ModelFormField) `
- *(... 43 weitere Methoden)*

### `ArtifactInfoGatherer` — class
Vollständiger Name: `org.apache.ofbiz.widget.artifact.ArtifactInfoGatherer`
- `public org.apache.ofbiz.widget.artifact.ArtifactInfoGatherer(org.apache.ofbiz.widget.artifact.ArtifactInfoContext);`
- `public void visit(org.apache.ofbiz.widget.model.ModelFormAction$CallParentActions) `
- `public void visit(org.apache.ofbiz.widget.model.ModelScreenWidget$Column) `
- `public void visit(org.apache.ofbiz.widget.model.ModelScreenWidget$ColumnContainer) `
- `public void visit(org.apache.ofbiz.widget.model.ModelScreenWidget$Container) `
- `public void visit(org.apache.ofbiz.widget.model.ModelScreenWidget$Content) `
- `public void visit(org.apache.ofbiz.widget.model.ModelScreenWidget$DecoratorScreen) `
- `public void visit(org.apache.ofbiz.widget.model.ModelScreenWidget$DecoratorSection) `
- `public void visit(org.apache.ofbiz.widget.model.ModelScreenWidget$DecoratorSectionInclude) `
- `public void visit(org.apache.ofbiz.widget.model.AbstractModelAction$EntityAnd) `
- `public void visit(org.apache.ofbiz.widget.model.AbstractModelAction$EntityCondition) `
- `public void visit(org.apache.ofbiz.widget.model.AbstractModelAction$EntityOne) `
- `public void visit(org.apache.ofbiz.widget.model.ModelScreenWidget$Form) `
- `public void visit(org.apache.ofbiz.widget.model.ModelScreenWidget$Grid) `
- `public void visit(org.apache.ofbiz.widget.model.AbstractModelAction$GetRelated) `
- *(... 37 weitere Methoden)*

### `ModelMenu` — class
Vollständiger Name: `org.apache.ofbiz.widget.model.ModelMenu`
- `public org.apache.ofbiz.widget.model.ModelMenu(org.w3c.dom.Element, java.lang.String, org.apache.ofbiz.widget.renderer.VisualTheme);`
- `public void accept(org.apache.ofbiz.widget.model.ModelWidgetVisitor) `
- `public java.util.List<org.apache.ofbiz.widget.model.ModelAction> getActions();`
- `public java.lang.String getBoundaryCommentName();`
- `public java.lang.String getCurrentMenuName(java.util.Map<java.lang.String, java.lang.Object>);`
- `public java.lang.String getDefaultAlign();`
- `public java.lang.String getDefaultAlignStyle();`
- `public org.apache.ofbiz.base.util.string.FlexibleStringExpander getDefaultAssociatedContentId();`
- `public java.lang.String getDefaultAssociatedContentId(java.util.Map<java.lang.String, java.lang.Object>);`
- `public java.lang.String getDefaultCellWidth();`
- `public java.lang.String getDefaultDisabledTitleStyle();`
- `public java.lang.String getDefaultEntityName();`
- `public java.lang.Boolean getDefaultHideIfSelected();`
- `public java.lang.String getDefaultMenuItemName();`
- `public java.lang.String getDefaultPermissionEntityAction();`
- *(... 29 weitere Methoden)*

### `ModelMenuItem` — class
Vollständiger Name: `org.apache.ofbiz.widget.model.ModelMenuItem`
- `public org.apache.ofbiz.widget.model.ModelMenuItem(org.w3c.dom.Element, org.apache.ofbiz.widget.model.ModelMenu);`
- `public org.apache.ofbiz.widget.model.ModelMenuItem(org.apache.ofbiz.widget.model.ModelMenuItem, org.apache.ofbiz.widget.model.ModelMenu, org.apache.ofbiz.widget.model.ModelMenuItem);`
- `public void accept(org.apache.ofbiz.widget.model.ModelWidgetVisitor) `
- `public java.util.List<org.apache.ofbiz.widget.model.ModelAction> getActions();`
- `public java.lang.String getAlign();`
- `public java.lang.String getAlignStyle();`
- `public org.apache.ofbiz.base.util.string.FlexibleStringExpander getAssociatedContentId();`
- `public java.lang.String getAssociatedContentId(java.util.Map<java.lang.String, java.lang.Object>);`
- `public java.lang.String getCellWidth();`
- `public org.apache.ofbiz.widget.model.ModelMenuCondition getCondition();`
- `public java.lang.String getDisabledTitleStyle();`
- `public java.lang.String getDisableIfEmpty();`
- `public java.lang.String getEntityName();`
- `public java.lang.Boolean getHideIfSelected();`
- `public org.apache.ofbiz.widget.model.ModelMenuItem$MenuLink getLink();`
- *(... 21 weitere Methoden)*

### `XmlWidgetVisitor` — class
Vollständiger Name: `org.apache.ofbiz.widget.model.XmlWidgetVisitor`
- `public org.apache.ofbiz.widget.model.XmlWidgetVisitor(java.lang.Appendable);`
- `public void visit(org.apache.ofbiz.widget.model.ModelScreenWidget$Column) `
- `public void visit(org.apache.ofbiz.widget.model.ModelScreenWidget$ColumnContainer) `
- `public void visit(org.apache.ofbiz.widget.model.ModelScreenWidget$Container) `
- `public void visit(org.apache.ofbiz.widget.model.ModelScreenWidget$Content) `
- `public void visit(org.apache.ofbiz.widget.model.ModelScreenWidget$DecoratorScreen) `
- `public void visit(org.apache.ofbiz.widget.model.ModelScreenWidget$DecoratorSection) `
- `public void visit(org.apache.ofbiz.widget.model.ModelScreenWidget$DecoratorSectionInclude) `
- `public void visit(org.apache.ofbiz.widget.model.ModelScreenWidget$Form) `
- `public void visit(org.apache.ofbiz.widget.model.ModelScreenWidget$HorizontalSeparator) `
- `public void visit(org.apache.ofbiz.widget.model.HtmlWidget$HtmlTemplate) `
- `public void visit(org.apache.ofbiz.widget.model.HtmlWidget$HtmlTemplateDecorator) `
- `public void visit(org.apache.ofbiz.widget.model.HtmlWidget$HtmlTemplateDecoratorSection) `
- `public void visit(org.apache.ofbiz.widget.model.HtmlWidget) `
- `public void visit(org.apache.ofbiz.widget.model.ModelScreenWidget$IncludeScreen) `
- *(... 20 weitere Methoden)*

### `MacroScreenRenderer` — class
Vollständiger Name: `org.apache.ofbiz.widget.renderer.macro.MacroScreenRenderer`
- `public org.apache.ofbiz.widget.renderer.macro.MacroScreenRenderer(org.apache.ofbiz.widget.model.ModelTheme, java.lang.String) `
- `public org.apache.ofbiz.widget.renderer.macro.MacroScreenRenderer(java.lang.String, java.lang.String) `
- `public org.apache.ofbiz.widget.renderer.macro.MacroScreenRenderer(java.lang.String, java.lang.String, java.lang.Appendable) `
- `public java.lang.String getRendererName();`
- `public void renderBegin(java.lang.Appendable, java.util.Map<java.lang.String, java.lang.Object>) `
- `public void renderEnd(java.lang.Appendable, java.util.Map<java.lang.String, java.lang.Object>) `
- `public void renderScreenBegin(java.lang.Appendable, java.util.Map<java.lang.String, java.lang.Object>, org.apache.ofbiz.widget.model.ModelScreen) `
- `public void renderScreenEnd(java.lang.Appendable, java.util.Map<java.lang.String, java.lang.Object>, org.apache.ofbiz.widget.model.ModelScreen) `
- `public void renderSectionBegin(java.lang.Appendable, java.util.Map<java.lang.String, java.lang.Object>, org.apache.ofbiz.widget.model.ModelScreenWidget$Section) `
- `public void renderSectionEnd(java.lang.Appendable, java.util.Map<java.lang.String, java.lang.Object>, org.apache.ofbiz.widget.model.ModelScreenWidget$Section) `
- `public void renderContainerBegin(java.lang.Appendable, java.util.Map<java.lang.String, java.lang.Object>, org.apache.ofbiz.widget.model.ModelScreenWidget$Container) `
- `public void renderContainerEnd(java.lang.Appendable, java.util.Map<java.lang.String, java.lang.Object>, org.apache.ofbiz.widget.model.ModelScreenWidget$Container) `
- `public void renderLabel(java.lang.Appendable, java.util.Map<java.lang.String, java.lang.Object>, org.apache.ofbiz.widget.model.ModelScreenWidget$Label) `
- `public void renderHorizontalSeparator(java.lang.Appendable, java.util.Map<java.lang.String, java.lang.Object>, org.apache.ofbiz.widget.model.ModelScreenWidget$HorizontalSeparator) `
- `public void renderLink(java.lang.Appendable, java.util.Map<java.lang.String, java.lang.Object>, org.apache.ofbiz.widget.model.ModelScreenWidget$ScreenLink) `
- *(... 20 weitere Methoden)*

### `ModelWidgetVisitor` — interface
Vollständiger Name: `org.apache.ofbiz.widget.model.ModelWidgetVisitor`
- `public abstract void visit(org.apache.ofbiz.widget.model.HtmlWidget) `
- `public abstract void visit(org.apache.ofbiz.widget.model.HtmlWidget$HtmlTemplate) `
- `public abstract void visit(org.apache.ofbiz.widget.model.HtmlWidget$HtmlTemplateDecorator) `
- `public abstract void visit(org.apache.ofbiz.widget.model.HtmlWidget$HtmlTemplateDecoratorSection) `
- `public abstract void visit(org.apache.ofbiz.widget.model.IterateSectionWidget) `
- `public abstract void visit(org.apache.ofbiz.widget.model.ModelSingleForm) `
- `public abstract void visit(org.apache.ofbiz.widget.model.ModelGrid) `
- `public abstract void visit(org.apache.ofbiz.widget.model.ModelMenu) `
- `public abstract void visit(org.apache.ofbiz.widget.model.ModelMenuItem) `
- `public abstract void visit(org.apache.ofbiz.widget.model.ModelScreen) `
- `public abstract void visit(org.apache.ofbiz.widget.model.ModelScreenWidget$ColumnContainer) `
- `public abstract void visit(org.apache.ofbiz.widget.model.ModelScreenWidget$Container) `
- `public abstract void visit(org.apache.ofbiz.widget.model.ModelScreenWidget$Content) `
- `public abstract void visit(org.apache.ofbiz.widget.model.ModelScreenWidget$DecoratorScreen) `
- `public abstract void visit(org.apache.ofbiz.widget.model.ModelScreenWidget$DecoratorSection) `
- *(... 18 weitere Methoden)*

### `ScreenStringRenderer` — interface
Vollständiger Name: `org.apache.ofbiz.widget.renderer.ScreenStringRenderer`
- `public abstract java.lang.String getRendererName();`
- `public abstract void renderBegin(java.lang.Appendable, java.util.Map<java.lang.String, java.lang.Object>) `
- `public abstract void renderEnd(java.lang.Appendable, java.util.Map<java.lang.String, java.lang.Object>) `
- `public abstract void renderScreenBegin(java.lang.Appendable, java.util.Map<java.lang.String, java.lang.Object>, org.apache.ofbiz.widget.model.ModelScreen) `
- `public abstract void renderScreenEnd(java.lang.Appendable, java.util.Map<java.lang.String, java.lang.Object>, org.apache.ofbiz.widget.model.ModelScreen) `
- `public abstract void renderSectionBegin(java.lang.Appendable, java.util.Map<java.lang.String, java.lang.Object>, org.apache.ofbiz.widget.model.ModelScreenWidget$Section) `
- `public abstract void renderSectionEnd(java.lang.Appendable, java.util.Map<java.lang.String, java.lang.Object>, org.apache.ofbiz.widget.model.ModelScreenWidget$Section) `
- `public abstract void renderColumnContainer(java.lang.Appendable, java.util.Map<java.lang.String, java.lang.Object>, org.apache.ofbiz.widget.model.ModelScreenWidget$ColumnContainer) `
- `public abstract void renderContainerBegin(java.lang.Appendable, java.util.Map<java.lang.String, java.lang.Object>, org.apache.ofbiz.widget.model.ModelScreenWidget$Container) `
- `public abstract void renderContainerEnd(java.lang.Appendable, java.util.Map<java.lang.String, java.lang.Object>, org.apache.ofbiz.widget.model.ModelScreenWidget$Container) `
- `public abstract void renderContentBegin(java.lang.Appendable, java.util.Map<java.lang.String, java.lang.Object>, org.apache.ofbiz.widget.model.ModelScreenWidget$Content) `
- `public abstract void renderContentBody(java.lang.Appendable, java.util.Map<java.lang.String, java.lang.Object>, org.apache.ofbiz.widget.model.ModelScreenWidget$Content) `
- `public abstract void renderContentEnd(java.lang.Appendable, java.util.Map<java.lang.String, java.lang.Object>, org.apache.ofbiz.widget.model.ModelScreenWidget$Content) `
- `public abstract void renderSubContentBegin(java.lang.Appendable, java.util.Map<java.lang.String, java.lang.Object>, org.apache.ofbiz.widget.model.ModelScreenWidget$SubContent) `
- `public abstract void renderSubContentBody(java.lang.Appendable, java.util.Map<java.lang.String, java.lang.Object>, org.apache.ofbiz.widget.model.ModelScreenWidget$SubContent) `
- *(... 16 weitere Methoden)*

### `ModelTheme` — class
Vollständiger Name: `org.apache.ofbiz.widget.model.ModelTheme`
- `public org.apache.ofbiz.widget.model.ModelTheme(org.w3c.dom.Element);`
- `public java.lang.String getName();`
- `public java.util.List<java.lang.String> getVisualThemeIds();`
- `public org.apache.ofbiz.widget.renderer.VisualTheme getVisualTheme(java.lang.String);`
- `public java.lang.Integer getDefaultViewSize();`
- `public java.lang.Integer getAutocompleterDefaultViewSize();`
- `public java.lang.Integer getAutocompleterDefaultMinLength();`
- `public java.lang.Boolean getAutocompleterDisplayReturnField();`
- `public java.lang.Integer getAutocompleterDefaultDelay();`
- `public java.lang.Integer getLinkDefaultLayeredModalHeight();`
- `public java.lang.Integer getLinkDefaultLayeredModalWidth();`
- `public java.lang.Integer getLookupHeight();`
- `public java.lang.Integer getLookupWidth();`
- `public java.lang.String getLookupPosition();`
- `public java.lang.String getLookupShowDescription();`
- *(... 15 weitere Methoden)*

### `XmlWidgetFieldVisitor` — class
Vollständiger Name: `org.apache.ofbiz.widget.model.XmlWidgetFieldVisitor`
- `public org.apache.ofbiz.widget.model.XmlWidgetFieldVisitor(java.lang.Appendable);`
- `public void visit(org.apache.ofbiz.widget.model.ModelFormField$CheckField) `
- `public void visit(org.apache.ofbiz.widget.model.ModelFormField$ContainerField) `
- `public void visit(org.apache.ofbiz.widget.model.ModelFormField$DateFindField) `
- `public void visit(org.apache.ofbiz.widget.model.ModelFormField$DateTimeField) `
- `public void visit(org.apache.ofbiz.widget.model.ModelFormField$DisplayEntityField) `
- `public void visit(org.apache.ofbiz.widget.model.ModelFormField$DisplayField) `
- `public void visit(org.apache.ofbiz.widget.model.ModelFormField$DropDownField) `
- `public void visit(org.apache.ofbiz.widget.model.ModelFormField$FileField) `
- `public void visit(org.apache.ofbiz.widget.model.ModelFormField$HiddenField) `
- `public void visit(org.apache.ofbiz.widget.model.ModelFormField$HyperlinkField) `
- `public void visit(org.apache.ofbiz.widget.model.ModelFormField$FormField) `
- `public void visit(org.apache.ofbiz.widget.model.ModelFormField$GridField) `
- `public void visit(org.apache.ofbiz.widget.model.ModelFormField$MenuField) `
- `public void visit(org.apache.ofbiz.widget.model.ModelFormField$ScreenField) `
- *(... 11 weitere Methoden)*

### `ModelFieldVisitor` — interface
Vollständiger Name: `org.apache.ofbiz.widget.model.ModelFieldVisitor`
- `public abstract void visit(org.apache.ofbiz.widget.model.ModelFormField$CheckField) `
- `public abstract void visit(org.apache.ofbiz.widget.model.ModelFormField$ContainerField) `
- `public abstract void visit(org.apache.ofbiz.widget.model.ModelFormField$DateFindField) `
- `public abstract void visit(org.apache.ofbiz.widget.model.ModelFormField$DateTimeField) `
- `public abstract void visit(org.apache.ofbiz.widget.model.ModelFormField$DisplayEntityField) `
- `public abstract void visit(org.apache.ofbiz.widget.model.ModelFormField$DisplayField) `
- `public abstract void visit(org.apache.ofbiz.widget.model.ModelFormField$DropDownField) `
- `public abstract void visit(org.apache.ofbiz.widget.model.ModelFormField$FileField) `
- `public abstract void visit(org.apache.ofbiz.widget.model.ModelFormField$FormField) `
- `public abstract void visit(org.apache.ofbiz.widget.model.ModelFormField$GridField) `
- `public abstract void visit(org.apache.ofbiz.widget.model.ModelFormField$HiddenField) `
- `public abstract void visit(org.apache.ofbiz.widget.model.ModelFormField$HyperlinkField) `
- `public abstract void visit(org.apache.ofbiz.widget.model.ModelFormField$IgnoredField) `
- `public abstract void visit(org.apache.ofbiz.widget.model.ModelFormField$ImageField) `
- `public abstract void visit(org.apache.ofbiz.widget.model.ModelFormField$LookupField) `
- *(... 10 weitere Methoden)*

### `HtmlMenuRenderer` — class
Vollständiger Name: `org.apache.ofbiz.widget.renderer.html.HtmlMenuRenderer`
- `public javax.servlet.http.HttpServletRequest getRequest();`
- `public javax.servlet.http.HttpServletResponse getResponse();`
- `public org.apache.ofbiz.widget.renderer.html.HtmlMenuRenderer(javax.servlet.http.HttpServletRequest, javax.servlet.http.HttpServletResponse);`
- `public void appendOfbizUrl(java.lang.Appendable, java.lang.String) `
- `public void appendContentUrl(java.lang.Appendable, java.lang.String) `
- `public void appendTooltip(java.lang.Appendable, java.util.Map<java.lang.String, java.lang.Object>, org.apache.ofbiz.widget.model.ModelMenuItem) `
- `public void renderFormatSimpleWrapperRows(java.lang.Appendable, java.util.Map<java.lang.String, java.lang.Object>, java.lang.Object) `
- `public void renderMenuItem(java.lang.Appendable, java.util.Map<java.lang.String, java.lang.Object>, org.apache.ofbiz.widget.model.ModelMenuItem) `
- `public boolean isDisableIfEmpty(org.apache.ofbiz.widget.model.ModelMenuItem, java.util.Map<java.lang.String, java.lang.Object>);`
- `public void renderMenuOpen(java.lang.Appendable, java.util.Map<java.lang.String, java.lang.Object>, org.apache.ofbiz.widget.model.ModelMenu) `
- `public void renderMenuClose(java.lang.Appendable, java.util.Map<java.lang.String, java.lang.Object>, org.apache.ofbiz.widget.model.ModelMenu) `
- `public void renderFormatSimpleWrapperOpen(java.lang.Appendable, java.util.Map<java.lang.String, java.lang.Object>, org.apache.ofbiz.widget.model.ModelMenu) `
- `public void renderFormatSimpleWrapperClose(java.lang.Appendable, java.util.Map<java.lang.String, java.lang.Object>, org.apache.ofbiz.widget.model.ModelMenu) `
- `public void setRequest(javax.servlet.http.HttpServletRequest);`
- `public void setResponse(javax.servlet.http.HttpServletResponse);`
- *(... 7 weitere Methoden)*

### `ModelTree` — class
Vollständiger Name: `org.apache.ofbiz.widget.model.ModelTree`
- `public org.apache.ofbiz.widget.model.ModelTree(org.w3c.dom.Element, java.lang.String);`
- `public void accept(org.apache.ofbiz.widget.model.ModelWidgetVisitor) `
- `public java.lang.String getBoundaryCommentName();`
- `public java.lang.String getDefaultEntityName();`
- `public java.lang.String getDefaultPkName(java.util.Map<java.lang.String, java.lang.Object>);`
- `public java.lang.String getExpandCollapseRequest(java.util.Map<java.lang.String, java.lang.Object>);`
- `public int getOpenDepth();`
- `public int getPostTrailOpenDepth();`
- `public java.lang.String getRenderStyle();`
- `public java.lang.String getRootNodeName();`
- `public java.lang.String getTrailName(java.util.Map<java.lang.String, java.lang.Object>);`
- `public java.lang.String getWrapStyle(java.util.Map<java.lang.String, java.lang.Object>);`
- `public void renderTreeString(java.lang.Appendable, java.util.Map<java.lang.String, java.lang.Object>, org.apache.ofbiz.widget.renderer.TreeStringRenderer) `
- `public java.lang.String getDefaultRenderStyle();`
- `public org.apache.ofbiz.base.util.string.FlexibleStringExpander getDefaultWrapStyleExdr();`
- *(... 5 weitere Methoden)*

### `HtmlMenuWrapper` — class
Vollständiger Name: `org.apache.ofbiz.widget.renderer.html.HtmlMenuWrapper`
- `public org.apache.ofbiz.widget.renderer.html.HtmlMenuWrapper(java.lang.String, java.lang.String, javax.servlet.http.HttpServletRequest, javax.servlet.http.HttpServletResponse) `
- `public void init(java.lang.String, java.lang.String, javax.servlet.http.HttpServletRequest, javax.servlet.http.HttpServletResponse) `
- `public org.apache.ofbiz.widget.renderer.MenuStringRenderer getMenuRenderer();`
- `public java.lang.String renderMenuString() `
- `public void setIsError(boolean);`
- `public boolean getIsError();`
- `public void setMenuOverrideName(java.lang.String);`
- `public void putInContext(java.lang.String, java.lang.Object);`
- `public void putInContext(java.lang.String, java.lang.String, java.lang.Object);`
- `public java.lang.Object getFromContext(java.lang.String);`
- `public java.lang.Object getFromContext(java.lang.String, java.lang.String);`
- `public org.apache.ofbiz.widget.model.ModelMenu getModelMenu();`
- `public org.apache.ofbiz.widget.renderer.MenuStringRenderer getRenderer();`
- `public void setRenderer(org.apache.ofbiz.widget.renderer.MenuStringRenderer);`
- `public void setRequest(javax.servlet.http.HttpServletRequest);`
- *(... 5 weitere Methoden)*

### `XmlWidgetActionVisitor` — class
Vollständiger Name: `org.apache.ofbiz.widget.model.XmlWidgetActionVisitor`
- `public org.apache.ofbiz.widget.model.XmlWidgetActionVisitor(java.lang.Appendable);`
- `public void visit(org.apache.ofbiz.widget.model.ModelFormAction$CallParentActions) `
- `public void visit(org.apache.ofbiz.widget.model.AbstractModelAction$EntityAnd) `
- `public void visit(org.apache.ofbiz.widget.model.ModelTreeAction$EntityAnd) `
- `public void visit(org.apache.ofbiz.widget.model.AbstractModelAction$EntityCondition) `
- `public void visit(org.apache.ofbiz.widget.model.ModelTreeAction$EntityCondition) `
- `public void visit(org.apache.ofbiz.widget.model.AbstractModelAction$EntityOne) `
- `public void visit(org.apache.ofbiz.widget.model.AbstractModelAction$GetRelated) `
- `public void visit(org.apache.ofbiz.widget.model.AbstractModelAction$GetRelatedOne) `
- `public void visit(org.apache.ofbiz.widget.model.AbstractModelAction$PropertyMap) `
- `public void visit(org.apache.ofbiz.widget.model.AbstractModelAction$PropertyToField) `
- `public void visit(org.apache.ofbiz.widget.model.AbstractModelAction$Script) `
- `public void visit(org.apache.ofbiz.widget.model.ModelTreeAction$Script) `
- `public void visit(org.apache.ofbiz.widget.model.AbstractModelAction$Service) `
- `public void visit(org.apache.ofbiz.widget.model.ModelFormAction$Service) `
- *(... 3 weitere Methoden)*

## Modul: workeffort (23 Klassen, 146 public Methoden)

### `WorkEffortContentWrapper` — class
Vollständiger Name: `org.apache.ofbiz.workeffort.content.WorkEffortContentWrapper`
- `public org.apache.ofbiz.workeffort.content.WorkEffortContentWrapper(org.apache.ofbiz.service.LocalDispatcher, org.apache.ofbiz.entity.GenericValue, java.util.Locale, java.lang.String);`
- `public org.apache.ofbiz.workeffort.content.WorkEffortContentWrapper(org.apache.ofbiz.entity.GenericValue, javax.servlet.http.HttpServletRequest);`
- `public java.lang.String get(java.lang.String, boolean, java.lang.String);`
- `public org.apache.ofbiz.base.util.StringUtil$StringWrapper get(java.lang.String, java.lang.String);`
- `public java.lang.String getContentId(java.lang.String);`
- `public java.lang.String getContentName(java.lang.String);`
- `public java.sql.Timestamp getFromDate(java.lang.String);`
- `public java.lang.String getDataResourceId(java.lang.String);`
- `public java.util.List<java.lang.String> getList(java.lang.String);`
- `public java.lang.String getTypeDescription(java.lang.String);`
- `public java.lang.String getContent(java.lang.String, boolean, java.lang.String);`
- `public java.lang.String getContent(java.lang.String, java.lang.String);`
- `public static java.lang.String getWorkEffortContentAsText(org.apache.ofbiz.entity.GenericValue, java.lang.String, javax.servlet.http.HttpServletRequest, java.lang.String);`
- `public static java.lang.String getWorkEffortContentAsText(org.apache.ofbiz.entity.GenericValue, java.lang.String, java.util.Locale, org.apache.ofbiz.service.LocalDispatcher, java.lang.String);`
- `public static java.lang.String getWorkEffortContentAsText(org.apache.ofbiz.entity.GenericValue, java.lang.String, java.util.Locale, java.lang.String, org.apache.ofbiz.entity.Delegator, org.apache.ofbiz.service.LocalDispatcher, boolean, java.lang.String);`
- *(... 6 weitere Methoden)*

### `WorkEffortServicesScript` [Groovy] — class
Vollständiger Name: `org.apache.ofbiz.workeffort.workeffort.workeffort.WorkEffortServicesScript`
- `public org.apache.ofbiz.workeffort.workeffort.workeffort.WorkEffortServicesScript();`
- `public org.apache.ofbiz.workeffort.workeffort.workeffort.WorkEffortServicesScript(groovy.lang.Binding);`
- `public static void main(java.lang.String...);`
- `public java.lang.Object run();`
- `public java.util.Map checkAndCreateWorkEffort();`
- `public java.util.Map checkAndUpdateWorkEffort();`
- `public java.util.Map createWorkEffortAndPartyAssign();`
- `public java.util.Map createWorkEffort();`
- `public java.util.Map updateWorkEffort();`
- `public java.util.Map deleteWorkEffort();`
- `public java.util.Map copyWorkEffort();`
- `public java.util.Map duplicateWorkEffort();`
- `public void duplicateWorkEffortAssoc(java.lang.String, java.lang.String, java.lang.String, java.lang.String);`
- `public java.util.Map assocAcceptedCustRequestToWorkEffort();`
- `public java.util.Map assignPartyToWorkEffort();`
- *(... 5 weitere Methoden)*

### `ICalRecurConverter` — class
Vollständiger Name: `org.apache.ofbiz.workeffort.workeffort.ICalRecurConverter`
- `public static void convert(org.apache.ofbiz.service.calendar.TemporalExpression, net.fortuna.ical4j.model.PropertyList);`
- `public void visit(org.apache.ofbiz.service.calendar.TemporalExpressions$Difference);`
- `public void visit(org.apache.ofbiz.service.calendar.TemporalExpressions$HourRange);`
- `public void visit(org.apache.ofbiz.service.calendar.TemporalExpressions$Intersection);`
- `public void visit(org.apache.ofbiz.service.calendar.TemporalExpressions$MinuteRange);`
- `public void visit(org.apache.ofbiz.service.calendar.TemporalExpressions$Null);`
- `public void visit(org.apache.ofbiz.service.calendar.TemporalExpressions$Substitution);`
- `public void visit(org.apache.ofbiz.service.calendar.TemporalExpressions$DateRange);`
- `public void visit(org.apache.ofbiz.service.calendar.TemporalExpressions$DayInMonth);`
- `public void visit(org.apache.ofbiz.service.calendar.TemporalExpressions$DayOfMonthRange);`
- `public void visit(org.apache.ofbiz.service.calendar.TemporalExpressions$DayOfWeekRange);`
- `public void visit(org.apache.ofbiz.service.calendar.TemporalExpressions$Frequency);`
- `public void visit(org.apache.ofbiz.service.calendar.TemporalExpressions$MonthRange);`
- `public void visit(org.apache.ofbiz.service.calendar.TemporalExpressions$Union);`

### `WorkEffortServices` — class
Vollständiger Name: `org.apache.ofbiz.workeffort.workeffort.WorkEffortServices`
- `public org.apache.ofbiz.workeffort.workeffort.WorkEffortServices();`
- `public static java.util.Map<java.lang.String, java.lang.Object> getWorkEffortAssignedEventsForRole(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> getWorkEffortAssignedEventsForRoleOfAllParties(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> getWorkEffortAssignedTasks(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> getWorkEffortAssignedActivities(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> getWorkEffortAssignedActivitiesByRole(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> getWorkEffortAssignedActivitiesByGroup(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> getWorkEffort(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> getWorkEffortEventsByPeriod(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> getProductManufacturingSummaryByFacility(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> processWorkEffortEventReminders(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> processWorkEffortEventReminder(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`
- `public static java.util.Map<java.lang.String, java.lang.Object> removeDuplicateWorkEfforts(org.apache.ofbiz.service.DispatchContext, java.util.Map<java.lang.String, ? extends java.lang.Object>);`

### `WorkEffortSearchSession` — class
Vollständiger Name: `org.apache.ofbiz.workeffort.workeffort.WorkEffortSearchSession`
- `public org.apache.ofbiz.workeffort.workeffort.WorkEffortSearchSession();`
- `public static org.apache.ofbiz.workeffort.workeffort.WorkEffortSearchSession$WorkEffortSearchOptions getWorkEffortSearchOptions(javax.servlet.http.HttpSession);`
- `public static void processSearchParameters(java.util.Map<java.lang.String, java.lang.Object>, javax.servlet.http.HttpServletRequest);`
- `public static void searchAddConstraint(org.apache.ofbiz.workeffort.workeffort.WorkEffortSearch$WorkEffortSearchConstraint, javax.servlet.http.HttpSession);`
- `public static void searchSetSortOrder(org.apache.ofbiz.workeffort.workeffort.WorkEffortSearch$ResultSortOrder, javax.servlet.http.HttpSession);`
- `public static java.util.List<org.apache.ofbiz.workeffort.workeffort.WorkEffortSearchSession$WorkEffortSearchOptions> getSearchOptionsHistoryList(javax.servlet.http.HttpSession);`
- `public static java.util.List<java.lang.String> searchGetConstraintStrings(boolean, javax.servlet.http.HttpSession, org.apache.ofbiz.entity.Delegator);`
- `public static java.lang.String searchGetSortOrderString(boolean, javax.servlet.http.HttpServletRequest);`
- `public static void checkSaveSearchOptionsHistory(javax.servlet.http.HttpSession);`
- `public static void searchRemoveConstraint(int, javax.servlet.http.HttpSession);`
- `public static void searchClear(javax.servlet.http.HttpSession);`

### `ICalWorker` — class
Vollständiger Name: `org.apache.ofbiz.workeffort.workeffort.ICalWorker`
- `public static org.apache.ofbiz.workeffort.workeffort.ICalWorker$ResponseProperties createForbiddenResponse(java.lang.String);`
- `public static org.apache.ofbiz.workeffort.workeffort.ICalWorker$ResponseProperties createNotAuthorizedResponse(java.lang.String);`
- `public static org.apache.ofbiz.workeffort.workeffort.ICalWorker$ResponseProperties createNotFoundResponse(java.lang.String);`
- `public static org.apache.ofbiz.workeffort.workeffort.ICalWorker$ResponseProperties createOkResponse(java.lang.String);`
- `public static org.apache.ofbiz.workeffort.workeffort.ICalWorker$ResponseProperties createPartialContentResponse(java.lang.String);`
- `public static void handleGetRequest(javax.servlet.http.HttpServletRequest, javax.servlet.http.HttpServletResponse, javax.servlet.ServletContext) `
- `public static void handlePropFindRequest(javax.servlet.http.HttpServletRequest, javax.servlet.http.HttpServletResponse, javax.servlet.ServletContext) `
- `public static void handlePutRequest(javax.servlet.http.HttpServletRequest, javax.servlet.http.HttpServletResponse, javax.servlet.ServletContext) `

### `IsCalOwner` [Groovy] — class
Vollständiger Name: `org.apache.ofbiz.workeffort.ical.IsCalOwner`
- `public org.apache.ofbiz.workeffort.ical.IsCalOwner();`
- `public org.apache.ofbiz.workeffort.ical.IsCalOwner(groovy.lang.Binding);`
- `public static void main(java.lang.String...);`
- `public java.lang.Object run();`

### `CreateUrlParam` [Groovy] — class
Vollständiger Name: `org.apache.ofbiz.workeffort.workeffort.calendar.CreateUrlParam`
- `public org.apache.ofbiz.workeffort.workeffort.calendar.CreateUrlParam();`
- `public org.apache.ofbiz.workeffort.workeffort.calendar.CreateUrlParam(groovy.lang.Binding);`
- `public static void main(java.lang.String...);`
- `public java.lang.Object run();`

### `Days` [Groovy] — class
Vollständiger Name: `org.apache.ofbiz.workeffort.workeffort.calendar.Days`
- `public org.apache.ofbiz.workeffort.workeffort.calendar.Days();`
- `public org.apache.ofbiz.workeffort.workeffort.calendar.Days(groovy.lang.Binding);`
- `public static void main(java.lang.String...);`
- `public java.lang.Object run();`

### `Month` [Groovy] — class
Vollständiger Name: `org.apache.ofbiz.workeffort.workeffort.calendar.Month`
- `public org.apache.ofbiz.workeffort.workeffort.calendar.Month();`
- `public org.apache.ofbiz.workeffort.workeffort.calendar.Month(groovy.lang.Binding);`
- `public static void main(java.lang.String...);`
- `public java.lang.Object run();`

### `Upcoming` [Groovy] — class
Vollständiger Name: `org.apache.ofbiz.workeffort.workeffort.calendar.Upcoming`
- `public org.apache.ofbiz.workeffort.workeffort.calendar.Upcoming();`
- `public org.apache.ofbiz.workeffort.workeffort.calendar.Upcoming(groovy.lang.Binding);`
- `public static void main(java.lang.String...);`
- `public java.lang.Object run();`

### `Week` [Groovy] — class
Vollständiger Name: `org.apache.ofbiz.workeffort.workeffort.calendar.Week`
- `public org.apache.ofbiz.workeffort.workeffort.calendar.Week();`
- `public org.apache.ofbiz.workeffort.workeffort.calendar.Week(groovy.lang.Binding);`
- `public static void main(java.lang.String...);`
- `public java.lang.Object run();`

### `WorkEffortContentWrapperScript` [Groovy] — class
Vollständiger Name: `org.apache.ofbiz.workeffort.workeffort.content.WorkEffortContentWrapperScript`
- `public org.apache.ofbiz.workeffort.workeffort.content.WorkEffortContentWrapperScript();`
- `public org.apache.ofbiz.workeffort.workeffort.content.WorkEffortContentWrapperScript(groovy.lang.Binding);`
- `public static void main(java.lang.String...);`
- `public java.lang.Object run();`

### `WorkEffortSearchOptions` [Groovy] — class
Vollständiger Name: `org.apache.ofbiz.workeffort.workeffort.find.WorkEffortSearchOptions`
- `public org.apache.ofbiz.workeffort.workeffort.find.WorkEffortSearchOptions();`
- `public org.apache.ofbiz.workeffort.workeffort.find.WorkEffortSearchOptions(groovy.lang.Binding);`
- `public static void main(java.lang.String...);`
- `public java.lang.Object run();`

### `WorkEffortSearchResults` [Groovy] — class
Vollständiger Name: `org.apache.ofbiz.workeffort.workeffort.find.WorkEffortSearchResults`
- `public org.apache.ofbiz.workeffort.workeffort.find.WorkEffortSearchResults();`
- `public org.apache.ofbiz.workeffort.workeffort.find.WorkEffortSearchResults(groovy.lang.Binding);`
- `public static void main(java.lang.String...);`
- `public java.lang.Object run();`

### `RequestList` [Groovy] — class
Vollständiger Name: `org.apache.ofbiz.workeffort.workeffort.request.RequestList`
- `public org.apache.ofbiz.workeffort.workeffort.request.RequestList();`
- `public org.apache.ofbiz.workeffort.workeffort.request.RequestList(groovy.lang.Binding);`
- `public static void main(java.lang.String...);`
- `public java.lang.Object run();`

### `WorkEffortKeywordIndex` — class
Vollständiger Name: `org.apache.ofbiz.workeffort.workeffort.WorkEffortKeywordIndex`
- `public org.apache.ofbiz.workeffort.workeffort.WorkEffortKeywordIndex();`
- `public static void indexKeywords(org.apache.ofbiz.entity.GenericValue) `
- `public static void addWeightedDataResourceString(org.apache.ofbiz.entity.GenericValue, int, java.util.List<java.lang.String>, org.apache.ofbiz.entity.Delegator, org.apache.ofbiz.entity.GenericValue);`
- `public static void addWeightedKeywordSourceString(org.apache.ofbiz.entity.GenericValue, java.lang.String, java.util.List<java.lang.String>);`

### `ICalConverter` — class
Vollständiger Name: `org.apache.ofbiz.workeffort.workeffort.ICalConverter`
- `public org.apache.ofbiz.workeffort.workeffort.ICalConverter();`
- `public static org.apache.ofbiz.workeffort.workeffort.ICalWorker$ResponseProperties getICalendar(java.lang.String, java.util.Map<java.lang.String, java.lang.Object>) `
- `public static org.apache.ofbiz.workeffort.workeffort.ICalWorker$ResponseProperties storeCalendar(java.io.InputStream, java.util.Map<java.lang.String, java.lang.Object>) `

### `WorkEffortSearch` — class
Vollständiger Name: `org.apache.ofbiz.workeffort.workeffort.WorkEffortSearch`
- `public org.apache.ofbiz.workeffort.workeffort.WorkEffortSearch();`
- `public static java.util.ArrayList<java.lang.String> searchWorkEfforts(java.util.List<? extends org.apache.ofbiz.workeffort.workeffort.WorkEffortSearch$WorkEffortSearchConstraint>, org.apache.ofbiz.workeffort.workeffort.WorkEffortSearch$ResultSortOrder, org.apache.ofbiz.entity.Delegator, java.lang.String);`
- `public static void getAllSubWorkEffortIds(java.lang.String, java.util.Set<java.lang.String>, org.apache.ofbiz.entity.Delegator, java.sql.Timestamp);`

### `WorkEffortWorker` — class
Vollständiger Name: `org.apache.ofbiz.workeffort.workeffort.WorkEffortWorker`
- `public static java.util.List<org.apache.ofbiz.entity.GenericValue> getLowestLevelWorkEfforts(org.apache.ofbiz.entity.Delegator, java.lang.String, java.lang.String);`
- `public static java.util.List<org.apache.ofbiz.entity.GenericValue> getLowestLevelWorkEfforts(org.apache.ofbiz.entity.Delegator, java.lang.String, java.lang.String, java.lang.String, java.lang.String);`
- `public static java.util.List<org.apache.ofbiz.entity.GenericValue> removeDuplicateWorkEfforts(java.util.List<org.apache.ofbiz.entity.GenericValue>);`
