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


class SourceApplication(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, product=None, application_id=None, name=None):
        """
        SourceApplication - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'product': 'str',
            'application_id': 'str',
            'name': 'str'
        }

        self.attribute_map = {
            'product': 'product',
            'application_id': 'application_id',
            'name': 'name'
        }

        self._product = product
        self._application_id = application_id
        self._name = name

    @property
    def product(self):
        """
        Gets the product of this SourceApplication.
        Read-only [Product](#type-product) type for the application. See [Product](#type-product) for possible values

        :return: The product of this SourceApplication.
        :rtype: str
        """
        return self._product

    @product.setter
    def product(self, product):
        """
        Sets the product of this SourceApplication.
        Read-only [Product](#type-product) type for the application. See [Product](#type-product) for possible values

        :param product: The product of this SourceApplication.
        :type: str
        """

        self._product = product

    @property
    def application_id(self):
        """
        Gets the application_id of this SourceApplication.
        Read-only Square ID assigned to the application. Only used for [Product](#type-product) type `EXTERNAL_API`.

        :return: The application_id of this SourceApplication.
        :rtype: str
        """
        return self._application_id

    @application_id.setter
    def application_id(self, application_id):
        """
        Sets the application_id of this SourceApplication.
        Read-only Square ID assigned to the application. Only used for [Product](#type-product) type `EXTERNAL_API`.

        :param application_id: The application_id of this SourceApplication.
        :type: str
        """

        self._application_id = application_id

    @property
    def name(self):
        """
        Gets the name of this SourceApplication.
        Read-only display name assigned to the application (e.g. `\"Custom Application\"`, `\"Square POS 4.74 for Android\"`).

        :return: The name of this SourceApplication.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this SourceApplication.
        Read-only display name assigned to the application (e.g. `\"Custom Application\"`, `\"Square POS 4.74 for Android\"`).

        :param name: The name of this SourceApplication.
        :type: str
        """

        self._name = name

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
