# coding: utf-8
"""
<copyright company="Aspose" file="PivotColumnpy.cs">
  Copyright (c) 2024 Aspose.Cells Cloud
</copyright>
<summary>
 Permission is hereby granted, free of charge, to any person obtaining a copy
 of this software and associated documentation files (the "Software"), to deal
 in the Software without restriction, including without limitation the rights
 to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 copies of the Software, and to permit persons to whom the Software is
 furnished to do so, subject to the following conditions:

 The above copyright notice and this permission notice shall be included in all
 copies or substantial portions of the Software.

 THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
 SOFTWARE.
</summary>
"""

from pprint import pformat
from six import iteritems
import re

class PivotColumn(object):

    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    swagger_types = {
        'pivot_column_name' : 'str',
        'value_column_names' : 'list[str]'
    }

    attribute_map = {
        'pivot_column_name' : 'PivotColumnName' ,
        'value_column_names' : 'ValueColumnNames' 
    }

    @staticmethod
    def get_swagger_types():
        return PivotColumn.swagger_types

    @staticmethod
    def get_attribute_map():
        return PivotColumn.attribute_map

    def get_from_container(self, attr):
        if attr in self.container:
            return self.container[attr]
        return None

    def __init__(self,pivot_column_name=None ,value_column_names=None   ,**kw):
        """
        Associative dict for storing property values
        """
        self.container = {}

        """
        PivotColumn - a model defined in Swagger
        """
        self.container['pivot_column_name'] = None 
        self.container['value_column_names'] = None 
        params = locals()
        self.pivot_column_name = pivot_column_name
        if 'pivot_column_name' in params:
            self.pivot_column_name = params["pivot_column_name"]


             
        self.value_column_names = value_column_names
        if 'value_column_names' in params:
            self.value_column_names = params["value_column_names"]


             

    @property
    def pivot_column_name(self):
        return self.container['pivot_column_name']

    @pivot_column_name.setter
    def pivot_column_name(self, pivot_column_name):
        self.container['pivot_column_name'] = pivot_column_name 
    @property
    def value_column_names(self):
        return self.container['value_column_names']

    @value_column_names.setter
    def value_column_names(self, value_column_names):
        self.container['value_column_names'] = value_column_names 

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.get_swagger_types()):
            value = self.get_from_container(attr)
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
        if not isinstance(other, PivotColumn):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other    