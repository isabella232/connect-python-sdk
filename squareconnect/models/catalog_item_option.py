# coding: utf-8

"""
Copyright 2017 Square, Inc.

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""


from pprint import pformat
from six import iteritems
import re


class CatalogItemOption(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, name=None, display_name=None, description=None, show_colors=None, values=None, item_count=None):
        """
        CatalogItemOption - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'name': 'str',
            'display_name': 'str',
            'description': 'str',
            'show_colors': 'bool',
            'values': 'list[CatalogObject]',
            'item_count': 'int'
        }

        self.attribute_map = {
            'name': 'name',
            'display_name': 'display_name',
            'description': 'description',
            'show_colors': 'show_colors',
            'values': 'values',
            'item_count': 'item_count'
        }

        self._name = name
        self._display_name = display_name
        self._description = description
        self._show_colors = show_colors
        self._values = values
        self._item_count = item_count

    @property
    def name(self):
        """
        Gets the name of this CatalogItemOption.
        The item option's display name for the seller. Must be unique across all item options. Searchable.

        :return: The name of this CatalogItemOption.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this CatalogItemOption.
        The item option's display name for the seller. Must be unique across all item options. Searchable.

        :param name: The name of this CatalogItemOption.
        :type: str
        """

        self._name = name

    @property
    def display_name(self):
        """
        Gets the display_name of this CatalogItemOption.
        The item option's display name for the customer. Searchable.

        :return: The display_name of this CatalogItemOption.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CatalogItemOption.
        The item option's display name for the customer. Searchable.

        :param display_name: The display_name of this CatalogItemOption.
        :type: str
        """

        self._display_name = display_name

    @property
    def description(self):
        """
        Gets the description of this CatalogItemOption.
        The item option's human-readable description. Displays for in the Square Point of Sale app for the seller and in the Online Store or on receipts for the buyer.

        :return: The description of this CatalogItemOption.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this CatalogItemOption.
        The item option's human-readable description. Displays for in the Square Point of Sale app for the seller and in the Online Store or on receipts for the buyer.

        :param description: The description of this CatalogItemOption.
        :type: str
        """

        self._description = description

    @property
    def show_colors(self):
        """
        Gets the show_colors of this CatalogItemOption.
        If true, display colors for entries in `values` when present.

        :return: The show_colors of this CatalogItemOption.
        :rtype: bool
        """
        return self._show_colors

    @show_colors.setter
    def show_colors(self, show_colors):
        """
        Sets the show_colors of this CatalogItemOption.
        If true, display colors for entries in `values` when present.

        :param show_colors: The show_colors of this CatalogItemOption.
        :type: bool
        """

        self._show_colors = show_colors

    @property
    def values(self):
        """
        Gets the values of this CatalogItemOption.
        A list of [CatalogObject](#type-catalogobject)s containing the [CatalogItemOptionValue](#type-catalogitemoptionvalue)s for this item.

        :return: The values of this CatalogItemOption.
        :rtype: list[CatalogObject]
        """
        return self._values

    @values.setter
    def values(self, values):
        """
        Sets the values of this CatalogItemOption.
        A list of [CatalogObject](#type-catalogobject)s containing the [CatalogItemOptionValue](#type-catalogitemoptionvalue)s for this item.

        :param values: The values of this CatalogItemOption.
        :type: list[CatalogObject]
        """

        self._values = values

    @property
    def item_count(self):
        """
        Gets the item_count of this CatalogItemOption.
        The number of [CatalogItem](#type-catalogitem)s currently associated with this item option. Present only if the `include_counts` was specified in the request. Any count over 100 will be returned as `100`.

        :return: The item_count of this CatalogItemOption.
        :rtype: int
        """
        return self._item_count

    @item_count.setter
    def item_count(self, item_count):
        """
        Sets the item_count of this CatalogItemOption.
        The number of [CatalogItem](#type-catalogitem)s currently associated with this item option. Present only if the `include_counts` was specified in the request. Any count over 100 will be returned as `100`.

        :param item_count: The item_count of this CatalogItemOption.
        :type: int
        """

        self._item_count = item_count

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
