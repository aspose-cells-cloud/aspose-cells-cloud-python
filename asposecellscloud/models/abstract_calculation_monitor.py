# coding: utf-8
"""
<copyright company="Aspose" file="AbstractCalculationMonitorpy.cs">
  Copyright (c) 2025 Aspose.Cells Cloud
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

class AbstractCalculationMonitor(object):

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
        'original_value' : 'str',
        'value_changed' : 'bool',
        'calculated_value' : 'str'
    }

    attribute_map = {
        'original_value' : 'OriginalValue' ,
        'value_changed' : 'ValueChanged' ,
        'calculated_value' : 'CalculatedValue' 
    }

    @staticmethod
    def get_swagger_types():
        return AbstractCalculationMonitor.swagger_types

    @staticmethod
    def get_attribute_map():
        return AbstractCalculationMonitor.attribute_map

    def get_from_container(self, attr):
        if attr in self.container:
            return self.container[attr]
        return None

    def __init__(self,original_value=None ,value_changed=None ,calculated_value=None   ,**kw):
        """
        Associative dict for storing property values
        """
        self.container = {}

        """
        AbstractCalculationMonitor - a model defined in Swagger
        """
        self.container['original_value'] = None 
        self.container['value_changed'] = None 
        self.container['calculated_value'] = None 
        params = locals()
        self.original_value = original_value
        if 'original_value' in params:
            self.original_value = params["original_value"]


             
        self.value_changed = value_changed
        if 'value_changed' in params:
            self.value_changed = params["value_changed"]


             
        self.calculated_value = calculated_value
        if 'calculated_value' in params:
            self.calculated_value = params["calculated_value"]


             

    @property
    def original_value(self):
        return self.container['original_value']

    @original_value.setter
    def original_value(self, original_value):
        self.container['original_value'] = original_value 
    @property
    def value_changed(self):
        return self.container['value_changed']

    @value_changed.setter
    def value_changed(self, value_changed):
        self.container['value_changed'] = value_changed 
    @property
    def calculated_value(self):
        return self.container['calculated_value']

    @calculated_value.setter
    def calculated_value(self, calculated_value):
        self.container['calculated_value'] = calculated_value 

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
        if not isinstance(other, AbstractCalculationMonitor):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other    