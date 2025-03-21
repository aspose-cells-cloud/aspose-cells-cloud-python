# coding: utf-8
"""
<copyright company="Aspose" file="ChartOperateParameterpy.cs">
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

class ChartOperateParameter(object):

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
        'chart_index' : 'int',
        'chart_type' : 'str',
        'upper_left_row' : 'int',
        'upper_left_column' : 'int',
        'lower_right_row' : 'int',
        'lower_right_column' : 'int',
        'area' : 'str',
        'is_vertical' : 'bool',
        'category_data' : 'str',
        'is_auto_get_serial_name' : 'bool',
        'title' : 'str',
        'operate_type' : 'str'
    }

    attribute_map = {
        'chart_index' : 'ChartIndex' ,
        'chart_type' : 'ChartType' ,
        'upper_left_row' : 'UpperLeftRow' ,
        'upper_left_column' : 'UpperLeftColumn' ,
        'lower_right_row' : 'LowerRightRow' ,
        'lower_right_column' : 'LowerRightColumn' ,
        'area' : 'Area' ,
        'is_vertical' : 'IsVertical' ,
        'category_data' : 'CategoryData' ,
        'is_auto_get_serial_name' : 'IsAutoGetSerialName' ,
        'title' : 'Title' ,
        'operate_type' : 'OperateType' 
    }

    @staticmethod
    def get_swagger_types():
        return ChartOperateParameter.swagger_types

    @staticmethod
    def get_attribute_map():
        return ChartOperateParameter.attribute_map

    def get_from_container(self, attr):
        if attr in self.container:
            return self.container[attr]
        return None

    def __init__(self,chart_index=None ,chart_type=None ,upper_left_row=None ,upper_left_column=None ,lower_right_row=None ,lower_right_column=None ,area=None ,is_vertical=None ,category_data=None ,is_auto_get_serial_name=None ,title=None ,operate_type=None   ,**kw):
        """
        Associative dict for storing property values
        """
        self.container = {}

        """
        ChartOperateParameter - a model defined in Swagger
        """
        self.container['chart_index'] = None 
        self.container['chart_type'] = None 
        self.container['upper_left_row'] = None 
        self.container['upper_left_column'] = None 
        self.container['lower_right_row'] = None 
        self.container['lower_right_column'] = None 
        self.container['area'] = None 
        self.container['is_vertical'] = None 
        self.container['category_data'] = None 
        self.container['is_auto_get_serial_name'] = None 
        self.container['title'] = None 
        self.container['operate_type'] = None 
        params = locals()
        self.chart_index = chart_index
        if 'chart_index' in params:
            self.chart_index = params["chart_index"]


             
        self.chart_type = chart_type
        if 'chart_type' in params:
            self.chart_type = params["chart_type"]


             
        self.upper_left_row = upper_left_row
        if 'upper_left_row' in params:
            self.upper_left_row = params["upper_left_row"]


             
        self.upper_left_column = upper_left_column
        if 'upper_left_column' in params:
            self.upper_left_column = params["upper_left_column"]


             
        self.lower_right_row = lower_right_row
        if 'lower_right_row' in params:
            self.lower_right_row = params["lower_right_row"]


             
        self.lower_right_column = lower_right_column
        if 'lower_right_column' in params:
            self.lower_right_column = params["lower_right_column"]


             
        self.area = area
        if 'area' in params:
            self.area = params["area"]


             
        self.is_vertical = is_vertical
        if 'is_vertical' in params:
            self.is_vertical = params["is_vertical"]


             
        self.category_data = category_data
        if 'category_data' in params:
            self.category_data = params["category_data"]


             
        self.is_auto_get_serial_name = is_auto_get_serial_name
        if 'is_auto_get_serial_name' in params:
            self.is_auto_get_serial_name = params["is_auto_get_serial_name"]


             
        self.title = title
        if 'title' in params:
            self.title = params["title"]


             
        self.operate_type = operate_type
        if 'operate_type' in params:
            self.operate_type = params["operate_type"]


             

    @property
    def chart_index(self):
        return self.container['chart_index']

    @chart_index.setter
    def chart_index(self, chart_index):
        self.container['chart_index'] = chart_index 
    @property
    def chart_type(self):
        return self.container['chart_type']

    @chart_type.setter
    def chart_type(self, chart_type):
        self.container['chart_type'] = chart_type 
    @property
    def upper_left_row(self):
        return self.container['upper_left_row']

    @upper_left_row.setter
    def upper_left_row(self, upper_left_row):
        self.container['upper_left_row'] = upper_left_row 
    @property
    def upper_left_column(self):
        return self.container['upper_left_column']

    @upper_left_column.setter
    def upper_left_column(self, upper_left_column):
        self.container['upper_left_column'] = upper_left_column 
    @property
    def lower_right_row(self):
        return self.container['lower_right_row']

    @lower_right_row.setter
    def lower_right_row(self, lower_right_row):
        self.container['lower_right_row'] = lower_right_row 
    @property
    def lower_right_column(self):
        return self.container['lower_right_column']

    @lower_right_column.setter
    def lower_right_column(self, lower_right_column):
        self.container['lower_right_column'] = lower_right_column 
    @property
    def area(self):
        return self.container['area']

    @area.setter
    def area(self, area):
        self.container['area'] = area 
    @property
    def is_vertical(self):
        return self.container['is_vertical']

    @is_vertical.setter
    def is_vertical(self, is_vertical):
        self.container['is_vertical'] = is_vertical 
    @property
    def category_data(self):
        return self.container['category_data']

    @category_data.setter
    def category_data(self, category_data):
        self.container['category_data'] = category_data 
    @property
    def is_auto_get_serial_name(self):
        return self.container['is_auto_get_serial_name']

    @is_auto_get_serial_name.setter
    def is_auto_get_serial_name(self, is_auto_get_serial_name):
        self.container['is_auto_get_serial_name'] = is_auto_get_serial_name 
    @property
    def title(self):
        return self.container['title']

    @title.setter
    def title(self, title):
        self.container['title'] = title 
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
        if not isinstance(other, ChartOperateParameter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other    