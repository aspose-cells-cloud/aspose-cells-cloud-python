# coding: utf-8
"""
<copyright company="Aspose" file="QueryTablepy.cs">
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

class QueryTable(object):

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
        'connection_id' : 'int',
        'name' : 'str',
        'result_range' : 'Range',
        'preserve_formatting' : 'bool',
        'adjust_column_width' : 'bool'
    }

    attribute_map = {
        'connection_id' : 'ConnectionId' ,
        'name' : 'Name' ,
        'result_range' : 'ResultRange' ,
        'preserve_formatting' : 'PreserveFormatting' ,
        'adjust_column_width' : 'AdjustColumnWidth' 
    }

    @staticmethod
    def get_swagger_types():
        return QueryTable.swagger_types

    @staticmethod
    def get_attribute_map():
        return QueryTable.attribute_map

    def get_from_container(self, attr):
        if attr in self.container:
            return self.container[attr]
        return None

    def __init__(self,connection_id=None ,name=None ,result_range=None ,preserve_formatting=None ,adjust_column_width=None   ,**kw):
        """
        Associative dict for storing property values
        """
        self.container = {}

        """
        QueryTable - a model defined in Swagger
        """
        self.container['connection_id'] = None 
        self.container['name'] = None 
        self.container['result_range'] = None 
        self.container['preserve_formatting'] = None 
        self.container['adjust_column_width'] = None 
        params = locals()
        self.connection_id = connection_id
        if 'connection_id' in params:
            self.connection_id = params["connection_id"]


             
        self.name = name
        if 'name' in params:
            self.name = params["name"]


             
        self.result_range = result_range
        if 'result_range' in params:
            self.result_range = params["result_range"]


             
        self.preserve_formatting = preserve_formatting
        if 'preserve_formatting' in params:
            self.preserve_formatting = params["preserve_formatting"]


             
        self.adjust_column_width = adjust_column_width
        if 'adjust_column_width' in params:
            self.adjust_column_width = params["adjust_column_width"]


             

    @property
    def connection_id(self):
        return self.container['connection_id']

    @connection_id.setter
    def connection_id(self, connection_id):
        self.container['connection_id'] = connection_id 
    @property
    def name(self):
        return self.container['name']

    @name.setter
    def name(self, name):
        self.container['name'] = name 
    @property
    def result_range(self):
        return self.container['result_range']

    @result_range.setter
    def result_range(self, result_range):
        self.container['result_range'] = result_range 
    @property
    def preserve_formatting(self):
        return self.container['preserve_formatting']

    @preserve_formatting.setter
    def preserve_formatting(self, preserve_formatting):
        self.container['preserve_formatting'] = preserve_formatting 
    @property
    def adjust_column_width(self):
        return self.container['adjust_column_width']

    @adjust_column_width.setter
    def adjust_column_width(self, adjust_column_width):
        self.container['adjust_column_width'] = adjust_column_width 

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
        if not isinstance(other, QueryTable):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other    