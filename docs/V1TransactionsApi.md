# V1TransactionsApi
> squareconnect.apis.v1_transactions_api

All endpoints are relative to [Square Connect V2 Documentation](https://docs.connect.squareup.com/api/connect/v2/#navsection-endpoints)


Method | HTTP request 
------------- | -------------
[**create_refund**](V1TransactionsApi.md#create_refund) | **POST** /v1/{location_id}/refunds
[**list_bank_accounts**](V1TransactionsApi.md#list_bank_accounts) | **GET** /v1/{location_id}/bank-accounts
[**list_orders**](V1TransactionsApi.md#list_orders) | **GET** /v1/{location_id}/orders
[**list_payments**](V1TransactionsApi.md#list_payments) | **GET** /v1/{location_id}/payments
[**list_refunds**](V1TransactionsApi.md#list_refunds) | **GET** /v1/{location_id}/refunds
[**list_settlements**](V1TransactionsApi.md#list_settlements) | **GET** /v1/{location_id}/settlements
[**retrieve_bank_account**](V1TransactionsApi.md#retrieve_bank_account) | **GET** /v1/{location_id}/bank-accounts/{bank_account_id}
[**retrieve_order**](V1TransactionsApi.md#retrieve_order) | **GET** /v1/{location_id}/orders/{order_id}
[**retrieve_payment**](V1TransactionsApi.md#retrieve_payment) | **GET** /v1/{location_id}/payments/{payment_id}
[**retrieve_settlement**](V1TransactionsApi.md#retrieve_settlement) | **GET** /v1/{location_id}/settlements/{settlement_id}
[**update_order**](V1TransactionsApi.md#update_order) | **PUT** /v1/{location_id}/orders/{order_id}


# **create_refund**
> V1Refund create_refund(location_id, body)

### Description

Issues a refund for a previously processed payment. You must issue a refund within 60 days of the associated payment.  You cannot issue a partial refund for a split tender payment. You must instead issue a full or partial refund for a particular tender, by providing the applicable tender id to the V1CreateRefund endpoint. Issuing a full refund for a split tender payment refunds all tenders associated with the payment.  Issuing a refund for a card payment is not reversible. For development purposes, you can create fake cash payments in Square Point of Sale and refund them.

### Parameters

Name | Type | Notes | Default Value
------------- | ------------- | ------------- | -------------
 **location_id** | **str**| 
 **body** | [**V1CreateRefundRequest**](V1CreateRefundRequest.md)| 

### Return type

[**V1Refund**](V1Refund.md)

### Authorization

Assign your **Access Token** from developer portal to the authorization parameter.

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_bank_accounts**
> list[V1BankAccount] list_bank_accounts(location_id)

### Description

Provides non-confidential details for all of a location's associated bank accounts. This endpoint does not provide full bank account numbers, and there is no way to obtain a full bank account number with the Connect API.

### Parameters

Name | Type | Notes | Default Value
------------- | ------------- | ------------- | -------------
 **location_id** | **str**| 

### Return type

[**list[V1BankAccount]**](V1BankAccount.md)

### Authorization

Assign your **Access Token** from developer portal to the authorization parameter.

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_orders**
> list[V1Order] list_orders(location_id, order=order, limit=limit, batch_token=batch_token)

### Description

Provides summary information for a merchant's online store orders.

### Parameters

Name | Type | Notes | Default Value
------------- | ------------- | ------------- | -------------
 **location_id** | **str**| 
 **order** | **str**| [optional] 
 **limit** | **int**| [optional] 
 **batch_token** | **str**| [optional] 

### Return type

[**list[V1Order]**](V1Order.md)

### Authorization

Assign your **Access Token** from developer portal to the authorization parameter.

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_payments**
> list[V1Payment] list_payments(location_id, order=order, begin_time=begin_time, end_time=end_time, limit=limit, batch_token=batch_token, include_partial=include_partial)

### Description

Provides summary information for all payments taken for a given Square account during a date range. Date ranges cannot exceed 1 year in length. See Date ranges for details of inclusive and exclusive dates.  *Note**: Details for payments processed with Square Point of Sale while in offline mode may not be transmitted to Square for up to 72 hours. Offline payments have a `created_at` value that reflects the time the payment was originally processed, not the time it was subsequently transmitted to Square. Consequently, the ListPayments endpoint might list an offline payment chronologically between online payments that were seen in a previous request.

### Parameters

Name | Type | Notes | Default Value
------------- | ------------- | ------------- | -------------
 **location_id** | **str**| 
 **order** | **str**| [optional] 
 **begin_time** | **str**| [optional] 
 **end_time** | **str**| [optional] 
 **limit** | **int**| [optional] 
 **batch_token** | **str**| [optional] 
 **include_partial** | **bool**| [optional] 

### Return type

[**list[V1Payment]**](V1Payment.md)

### Authorization

Assign your **Access Token** from developer portal to the authorization parameter.

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_refunds**
> list[V1Refund] list_refunds(location_id, order=order, begin_time=begin_time, end_time=end_time, limit=limit, batch_token=batch_token)

### Description

Provides the details for all refunds initiated by a merchant or any of the merchant's mobile staff during a date range. Date ranges cannot exceed one year in length.

### Parameters

Name | Type | Notes | Default Value
------------- | ------------- | ------------- | -------------
 **location_id** | **str**| 
 **order** | **str**| [optional] 
 **begin_time** | **str**| [optional] 
 **end_time** | **str**| [optional] 
 **limit** | **int**| [optional] 
 **batch_token** | **str**| [optional] 

### Return type

[**list[V1Refund]**](V1Refund.md)

### Authorization

Assign your **Access Token** from developer portal to the authorization parameter.

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_settlements**
> list[V1Settlement] list_settlements(location_id, order=order, begin_time=begin_time, end_time=end_time, limit=limit, status=status, batch_token=batch_token)

### Description

Provides summary information for all deposits and withdrawals initiated by Square to a linked bank account during a date range. Date ranges cannot exceed one year in length.  *Note**: the ListSettlements endpoint does not provide entry information.

### Parameters

Name | Type | Notes | Default Value
------------- | ------------- | ------------- | -------------
 **location_id** | **str**| 
 **order** | **str**| [optional] 
 **begin_time** | **str**| [optional] 
 **end_time** | **str**| [optional] 
 **limit** | **int**| [optional] 
 **status** | **str**| [optional] 
 **batch_token** | **str**| [optional] 

### Return type

[**list[V1Settlement]**](V1Settlement.md)

### Authorization

Assign your **Access Token** from developer portal to the authorization parameter.

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_bank_account**
> V1BankAccount retrieve_bank_account(location_id, bank_account_id)

### Description

Provides non-confidential details for a merchant's associated bank account. This endpoint does not provide full bank account numbers, and there is no way to obtain a full bank account number with the Connect API.

### Parameters

Name | Type | Notes | Default Value
------------- | ------------- | ------------- | -------------
 **location_id** | **str**| 
 **bank_account_id** | **str**| 

### Return type

[**V1BankAccount**](V1BankAccount.md)

### Authorization

Assign your **Access Token** from developer portal to the authorization parameter.

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_order**
> V1Order retrieve_order(location_id, order_id)

### Description

Provides comprehensive information for a single online store order, including the order's history.

### Parameters

Name | Type | Notes | Default Value
------------- | ------------- | ------------- | -------------
 **location_id** | **str**| 
 **order_id** | **str**| 

### Return type

[**V1Order**](V1Order.md)

### Authorization

Assign your **Access Token** from developer portal to the authorization parameter.

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_payment**
> V1Payment retrieve_payment(location_id, payment_id)

### Description

Provides comprehensive information for a single payment.

### Parameters

Name | Type | Notes | Default Value
------------- | ------------- | ------------- | -------------
 **location_id** | **str**| 
 **payment_id** | **str**| 

### Return type

[**V1Payment**](V1Payment.md)

### Authorization

Assign your **Access Token** from developer portal to the authorization parameter.

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_settlement**
> V1Settlement retrieve_settlement(location_id, settlement_id)

### Description

Provides comprehensive information for a single settlement.  The returned `Settlement` objects include an `entries` field that lists the transactions that contribute to the settlement total. Most settlement entries correspond to a payment payout, but settlement entries are also generated for less common events, like refunds, manual adjustments, or chargeback holds.  Square initiates its regular deposits as indicated in the [Deposit Options with Square](https://squareup.com/help/us/en/article/3807) help article. Details for a regular deposit are usually not available from Connect API endpoints before 10 p.m. PST the same day.  Square does not know when an initiated settlement **completes**, only whether it has failed. A completed settlement is typically reflected in a bank account within 3 business days, but in exceptional cases it may take longer.

### Parameters

Name | Type | Notes | Default Value
------------- | ------------- | ------------- | -------------
 **location_id** | **str**| 
 **settlement_id** | **str**| 

### Return type

[**V1Settlement**](V1Settlement.md)

### Authorization

Assign your **Access Token** from developer portal to the authorization parameter.

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_order**
> V1Order update_order(location_id, order_id, body)

### Description

Updates the details of an online store order. Every update you perform on an order corresponds to one of three actions:

### Parameters

Name | Type | Notes | Default Value
------------- | ------------- | ------------- | -------------
 **location_id** | **str**| 
 **order_id** | **str**| 
 **body** | [**V1UpdateOrderRequest**](V1UpdateOrderRequest.md)| 

### Return type

[**V1Order**](V1Order.md)

### Authorization

Assign your **Access Token** from developer portal to the authorization parameter.

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

