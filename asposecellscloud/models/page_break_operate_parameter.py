# coding: utf-8
"""
<copyright company="Aspose" file="PageBreakOperateParameterpy.cs">
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

class PageBreakOperateParameter(object):

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
        'page_break_type' : 'str',
        'index' : 'int',
        'row' : 'int',
        'column' : 'int',
        'start_index' : 'int',
        'end_index' : 'int',
        'operate_type' : 'str'
    }

    attribute_map = {
        'page_break_type' : 'PageBreakType' ,
        'index' : 'Index' ,
        'row' : 'Row' ,
        'column' : 'Column' ,
        'start_index' : 'StartIndex' ,
        'end_index' : 'EndIndex' ,
        'operate_type' : 'OperateType' 
    }

    @staticmethod
    def get_swagger_types():
        return PageBreakOperateParameter.swagger_types

    @staticmethod
    def get_attribute_map():
        return PageBreakOperateParameter.attribute_map

    def get_from_container(self, attr):
        if attr in self.container:
            return self.container[attr]
        return None

    def __init__(self,page_break_type=None ,index=None ,row=None ,column=None ,start_index=None ,end_index=None ,operate_type=None   ,**kw):
        """
        Associative dict for storing property values
        """
        self.container = {}

        """
        PageBreakOperateParameter - a model defined in Swagger
        """
        self.container['page_break_type'] = None 
        self.container['index'] = None 
        self.container['row'] = None 
        self.container['column'] = None 
        self.container['start_index'] = None 
        self.container['end_index'] = None 
        self.container['operate_type'] = None 
        params = locals()
        self.page_break_type = page_break_type
        if 'page_break_type' in params:
            self.page_break_type = params["page_break_type"]


             
        self.index = index
        if 'index' in params:
            self.index = params["index"]


             
        self.row = row
        if 'row' in params:
            self.row = params["row"]


             
        self.column = column
        if 'column' in params:
            self.column = params["column"]


             
        self.start_index = start_index
        if 'start_index' in params:
            self.start_index = params["start_index"]


             
        self.end_index = end_index
        if 'end_index' in params:
            self.end_index = params["end_index"]


             
        self.operate_type = operate_type
        if 'operate_type' in params:
            self.operate_type = params["operate_type"]


             

    @property
    def page_break_type(self):
        return self.container['page_break_type']

    @page_break_type.setter
    def page_break_type(self, page_break_type):
        self.container['page_break_type'] = page_break_type 
    @property
    def index(self):
        return self.container['index']

    @index.setter
    def index(self, index):
        self.container['index'] = index 
    @property
    def row(self):
        return self.container['row']

    @row.setter
    def row(self, row):
        self.container['row'] = row 
    @property
    def column(self):
        return self.container['column']

    @column.setter
    def column(self, column):
        self.container['column'] = column 
    @property
    def start_index(self):
        return self.container['start_index']

    @start_index.setter
    def start_index(self, start_index):
        self.container['start_index'] = start_index 
    @property
    def end_index(self):
        return self.container['end_index']

    @end_index.setter
    def end_index(self, end_index):
        self.container['end_index'] = end_index 
    @property
    def operate_type(self):
        return self.container['operate_type']

    @operate_type.setter
    def operate_type(self, operate_type):
        self.container['operate_type'] = operate_type 

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
        if not isinstance(other, PageBreakOperateParameter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other    