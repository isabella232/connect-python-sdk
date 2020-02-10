## Customer

Represents a Square customer profile, which can have one or more
cards on file associated with it.

### Structure

`Customer`

### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `string` |  | A unique, Square-assigned object ID. |
| `created_at` | `string` |  | The time when the customer profile was created, in RFC 3339 format. |
| `updated_at` | `string` |  | The time when the customer profile was last updated, in RFC 3339 format. |
| `cards` | [`List of Card`](/doc/models/card.md) | Optional | Payment details of cards stored on file for the customer profile. |
| `given_name` | `string` | Optional | The given (i.e., first) name associated with the customer profile. |
| `family_name` | `string` | Optional | The family (i.e., last) name associated with the customer profile. |
| `nickname` | `string` | Optional | A nickname for the customer profile. |
| `company_name` | `string` | Optional | A business name associated with the customer profile. |
| `email_address` | `string` | Optional | The email address associated with the customer profile. |
| `address` | [`Address`](/doc/models/address.md) | Optional | Represents a physical address. |
| `phone_number` | `string` | Optional | The 11-digit phone number associated with the customer profile. |
| `birthday` | `string` | Optional | The birthday associated with the customer profile, in RFC-3339 format.<br>Year is optional, timezone and times are not allowed.<br>For example: `0000-09-01T00:00:00-00:00` indicates a birthday on September 1st.<br>`1998-09-01T00:00:00-00:00` indications a birthday on September 1st __1998__. |
| `reference_id` | `string` | Optional | An optional, second ID used to associate the customer profile with an<br>entity in another system. |
| `note` | `string` | Optional | A custom note associated with the customer profile. |
| `preferences` | [`Customer Preferences`](/doc/models/customer-preferences.md) | Optional | Represents communication preferences for the customer profile. |
| `groups` | [`List of Customer Group Info`](/doc/models/customer-group-info.md) | Optional | The groups the customer belongs to. |
| `creation_source` | [`str (Customer Creation Source)`](/doc/models/customer-creation-source.md) | Optional | Indicates the method used to create the customer profile. |

### Example (as JSON)

```json
{
  "id": "id0",
  "created_at": "created_at2",
  "updated_at": "updated_at4",
  "cards": null,
  "given_name": null,
  "family_name": null,
  "nickname": null,
  "company_name": null,
  "email_address": null,
  "address": null,
  "phone_number": null,
  "birthday": null,
  "reference_id": null,
  "note": null,
  "preferences": null,
  "groups": null,
  "creation_source": null
}
```
