# CreateOrderRequest
> squareconnect.models.create_order_request

### Description



## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order** | [**Order**](Order.md) | The order to create. If this field is set, then the only other top-level field that can be set is the idempotency_key. | [optional] 
**idempotency_key** | **str** | A value you specify that uniquely identifies this order among orders you&#39;ve created.  If you&#39;re unsure whether a particular order was created successfully, you can reattempt it with the same idempotency key without worrying about creating duplicate orders.  See [Idempotency](/basics/api101/idempotency) for more information. | [optional] 
**reference_id** | **str** | __Deprecated__: Please set the reference_id on the nested [order](#type-order) field instead.  An optional ID you can associate with the order for your own purposes (such as to associate the order with an entity ID in your own database).  This value cannot exceed 40 characters. | [optional] 
**line_items** | [**list[CreateOrderRequestLineItem]**](CreateOrderRequestLineItem.md) | __Deprecated__: Please set the line_items on the nested [order](#type-order) field instead.  The line items to associate with this order.  Each line item represents a different product to include in a purchase. | [optional] 
**taxes** | [**list[CreateOrderRequestTax]**](CreateOrderRequestTax.md) | __Deprecated__: Please set the taxes on the nested [order](#type-order) field instead.  The taxes to include on the order. | [optional] 
**discounts** | [**list[CreateOrderRequestDiscount]**](CreateOrderRequestDiscount.md) | __Deprecated__: Please set the discounts on the nested [order](#type-order) field instead.  The discounts to include on the order. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


