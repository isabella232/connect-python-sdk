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


class CatalogItemOptionValueForItemVariation(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, item_option_id=None, item_option_value_id=None):
        """
        CatalogItemOptionValueForItemVariation - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'item_option_id': 'str',
            'item_option_value_id': 'str'
        }

        self.attribute_map = {
            'item_option_id': 'item_option_id',
            'item_option_value_id': 'item_option_value_id'
        }

        self._item_option_id = item_option_id
        self._item_option_value_id = item_option_value_id

    @property
    def item_option_id(self):
        """
        Gets the item_option_id of this CatalogItemOptionValueForItemVariation.
        The unique id of an item option.

        :return: The item_option_id of this CatalogItemOptionValueForItemVariation.
        :rtype: str
        """
        return self._item_option_id

    @item_option_id.setter
    def item_option_id(self, item_option_id):
        """
        Sets the item_option_id of this CatalogItemOptionValueForItemVariation.
        The unique id of an item option.

        :param item_option_id: The item_option_id of this CatalogItemOptionValueForItemVariation.
        :type: str
        """

        self._item_option_id = item_option_id

    @property
    def item_option_value_id(self):
        """
        Gets the item_option_value_id of this CatalogItemOptionValueForItemVariation.
        The unique id of the selected value for the item option.

        :return: The item_option_value_id of this CatalogItemOptionValueForItemVariation.
        :rtype: str
        """
        return self._item_option_value_id

    @item_option_value_id.setter
    def item_option_value_id(self, item_option_value_id):
        """
        Sets the item_option_value_id of this CatalogItemOptionValueForItemVariation.
        The unique id of the selected value for the item option.

        :param item_option_value_id: The item_option_value_id of this CatalogItemOptionValueForItemVariation.
        :type: str
        """

        self._item_option_value_id = item_option_value_id

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
