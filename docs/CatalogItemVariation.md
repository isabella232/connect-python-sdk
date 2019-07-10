# CatalogItemVariation
> squareconnect.models.catalog_item_variation

### Description

An item variation (i.e., product) in the Catalog object model. Each item may have a maximum of 250 item variations.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**item_id** | **str** | The ID of the [CatalogItem](#type-catalogitem) associated with this item variation. Searchable. | [optional] 
**name** | **str** | The item variation&#39;s name. Searchable. This field has max length of 255 Unicode code points. | [optional] 
**sku** | **str** | The item variation&#39;s SKU, if any. Searchable. | [optional] 
**upc** | **str** | The item variation&#39;s UPC, if any. Searchable in the Connect API. This field is only exposed in the Connect API. It is not exposed in Square&#39;s Dashboard, Square Point of Sale app or Retail Point of Sale app. | [optional] 
**ordinal** | **int** | The order in which this item variation should be displayed. This value is read-only. On writes, the ordinal for each item variation within a parent [CatalogItem](#type-catalogitem) is set according to the item variations&#39;s position. On reads, the value is not guaranteed to be sequential or unique. | [optional] 
**pricing_type** | **str** | Indicates whether the item variation&#39;s price is fixed or determined at the time of sale. See [CatalogPricingType](#type-catalogpricingtype) for possible values | [optional] 
**price_money** | [**Money**](Money.md) | The item variation&#39;s price, if fixed pricing is used. | [optional] 
**location_overrides** | [**list[ItemVariationLocationOverrides]**](ItemVariationLocationOverrides.md) | Per-[location](#type-location) price and inventory overrides. | [optional] 
**track_inventory** | **bool** | If &#x60;true&#x60;, inventory tracking is active for the variation. | [optional] 
**inventory_alert_type** | **str** | Indicates whether the item variation displays an alert when its inventory quantity is less than or equal to its &#x60;inventory_alert_threshold&#x60;. See [InventoryAlertType](#type-inventoryalerttype) for possible values | [optional] 
**inventory_alert_threshold** | **int** | If the inventory quantity for the variation is less than or equal to this value and &#x60;inventory_alert_type&#x60; is &#x60;LOW_QUANTITY&#x60;, the variation displays an alert in the merchant dashboard.  This value is always an integer. | [optional] 
**user_data** | **str** | Arbitrary user metadata to associate with the item variation. Cannot exceed 255 characters. Searchable. | [optional] 
**service_duration** | **int** | If the [CatalogItem](#type-catalogitem) that owns this item variation is of type &#x60;APPOINTMENTS_SERVICE&#x60;, then this is the duration of the service in milliseconds. For example, a 30 minute appointment would have the value &#x60;1800000&#x60;, which is equal to 30 (minutes) * 60 (seconds per minute) * 1000 (milliseconds per second). | [optional] 
**measurement_unit_id** | **str** | ID of the ‘CatalogMeasurementUnit’ that is used to measure the quantity sold of this item variation. If left unset, the item will be sold in whole quantities. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


