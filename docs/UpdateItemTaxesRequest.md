# UpdateItemTaxesRequest
> squareconnect.models.update_item_taxes_request

### Description



## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**item_ids** | **list[str]** | The [CatalogItem](#type-catalogitem)s whose enabled/disabled [CatalogTax](#type-catalogtax)es are being updated. | 
**taxes_to_enable** | **list[str]** | The set of [CatalogTax](#type-catalogtax)es (referenced by ID) to enable for the [CatalogItem](#type-catalogitem). | [optional] 
**taxes_to_disable** | **list[str]** | The set of [CatalogTax](#type-catalogtax)es (referenced by ID) to disable for the [CatalogItem](#type-catalogitem). | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


