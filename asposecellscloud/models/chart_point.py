# coding: utf-8
"""
<copyright company="Aspose" file="ChartPointpy.cs">
  Copyright (c) 2023 Aspose.Cells Cloud
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

class ChartPoint(object):

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
        'area' : 'Area',
        'border' : 'Line',
        'data_labels' : 'DataLabels',
        'explosion' : 'int',
        'marker' : 'Marker',
        'shadow' : 'bool',
        'x_value' : 'str',
        'y_value' : 'str',
        'link' : 'Link'
    }

    attribute_map = {
        'area' : 'Area' ,
        'border' : 'Border' ,
        'data_labels' : 'DataLabels' ,
        'explosion' : 'Explosion' ,
        'marker' : 'Marker' ,
        'shadow' : 'Shadow' ,
        'x_value' : 'XValue' ,
        'y_value' : 'YValue' ,
        'link' : 'link' 
    }

    @staticmethod
    def get_swagger_types():
        return ChartPoint.swagger_types

    @staticmethod
    def get_attribute_map():
        return ChartPoint.attribute_map

    def get_from_container(self, attr):
        if attr in self.container:
            return self.container[attr]
        return None

    def __init__(self,area=None ,border=None ,data_labels=None ,explosion=None ,marker=None ,shadow=None ,x_value=None ,y_value=None ,link=None   ,**kw):
        """
        Associative dict for storing property values
        """
        self.container = {}

        """
        ChartPoint - a model defined in Swagger
        """
        self.container['area'] = None 
        self.container['border'] = None 
        self.container['data_labels'] = None 
        self.container['explosion'] = None 
        self.container['marker'] = None 
        self.container['shadow'] = None 
        self.container['x_value'] = None 
        self.container['y_value'] = None 
        self.container['link'] = None 
        params = locals()
        self.area = area
        if 'area' in params:
            self.area = params["area"]


             
        self.border = border
        if 'border' in params:
            self.border = params["border"]


             
        self.data_labels = data_labels
        if 'data_labels' in params:
            self.data_labels = params["data_labels"]


             
        self.explosion = explosion
        if 'explosion' in params:
            self.explosion = params["explosion"]


             
        self.marker = marker
        if 'marker' in params:
            self.marker = params["marker"]


             
        self.shadow = shadow
        if 'shadow' in params:
            self.shadow = params["shadow"]


             
        self.x_value = x_value
        if 'x_value' in params:
            self.x_value = params["x_value"]


             
        self.y_value = y_value
        if 'y_value' in params:
            self.y_value = params["y_value"]


             
        self.link = link
        if 'link' in params:
            self.link = params["link"]


             

    @property
    def area(self):
        return self.container['area']

    @area.setter
    def area(self, area):
        self.container['area'] = area 
    @property
    def border(self):
        return self.container['border']

    @border.setter
    def border(self, border):
        self.container['border'] = border 
    @property
    def data_labels(self):
        return self.container['data_labels']

    @data_labels.setter
    def data_labels(self, data_labels):
        self.container['data_labels'] = data_labels 
    @property
    def explosion(self):
        return self.container['explosion']

    @explosion.setter
    def explosion(self, explosion):
        self.container['explosion'] = explosion 
    @property
    def marker(self):
        return self.container['marker']

    @marker.setter
    def marker(self, marker):
        self.container['marker'] = marker 
    @property
    def shadow(self):
        return self.container['shadow']

    @shadow.setter
    def shadow(self, shadow):
        self.container['shadow'] = shadow 
    @property
    def x_value(self):
        return self.container['x_value']

    @x_value.setter
    def x_value(self, x_value):
        self.container['x_value'] = x_value 
    @property
    def y_value(self):
        return self.container['y_value']

    @y_value.setter
    def y_value(self, y_value):
        self.container['y_value'] = y_value 
    @property
    def link(self):
        return self.container['link']

    @link.setter
    def link(self, link):
        self.container['link'] = link 

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
        if not isinstance(other, ChartPoint):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other    