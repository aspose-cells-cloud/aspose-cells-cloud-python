# coding: utf-8
"""
<copyright company="Aspose" file="SaveResultTaskParameterpy.cs">
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

class SaveResultTaskParameter(object):

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
        'result_source' : 'str',
        'result_destination' : 'ResultDestination'
    }

    attribute_map = {
        'result_source' : 'ResultSource' ,
        'result_destination' : 'ResultDestination' 
    }

    @staticmethod
    def get_swagger_types():
        return SaveResultTaskParameter.swagger_types

    @staticmethod
    def get_attribute_map():
        return SaveResultTaskParameter.attribute_map

    def get_from_container(self, attr):
        if attr in self.container:
            return self.container[attr]
        return None

    def __init__(self,result_source=None ,result_destination=None   ,**kw):
        """
        Associative dict for storing property values
        """
        self.container = {}

        """
        SaveResultTaskParameter - a model defined in Swagger
        """
        self.container['result_source'] = None 
        self.container['result_destination'] = None 
        params = locals()
        self.result_source = result_source
        if 'result_source' in params:
            self.result_source = params["result_source"]


             
        self.result_destination = result_destination
        if 'result_destination' in params:
            self.result_destination = params["result_destination"]


             

    @property
    def result_source(self):
        return self.container['result_source']

    @result_source.setter
    def result_source(self, result_source):
        self.container['result_source'] = result_source 
    @property
    def result_destination(self):
        return self.container['result_destination']

    @result_destination.setter
    def result_destination(self, result_destination):
        self.container['result_destination'] = result_destination 

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
        if not isinstance(other, SaveResultTaskParameter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other    