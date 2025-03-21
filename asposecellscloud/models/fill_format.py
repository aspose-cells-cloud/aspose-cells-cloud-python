# coding: utf-8
"""
<copyright company="Aspose" file="FillFormatpy.cs">
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

class FillFormat(object):

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
        'type' : 'str',
        'solid_fill' : 'SolidFill',
        'pattern_fill' : 'PatternFill',
        'texture_fill' : 'TextureFill',
        'gradient_fill' : 'GradientFill',
        'image_data' : 'str'
    }

    attribute_map = {
        'type' : 'Type' ,
        'solid_fill' : 'SolidFill' ,
        'pattern_fill' : 'PatternFill' ,
        'texture_fill' : 'TextureFill' ,
        'gradient_fill' : 'GradientFill' ,
        'image_data' : 'ImageData' 
    }

    @staticmethod
    def get_swagger_types():
        return FillFormat.swagger_types

    @staticmethod
    def get_attribute_map():
        return FillFormat.attribute_map

    def get_from_container(self, attr):
        if attr in self.container:
            return self.container[attr]
        return None

    def __init__(self,type=None ,solid_fill=None ,pattern_fill=None ,texture_fill=None ,gradient_fill=None ,image_data=None   ,**kw):
        """
        Associative dict for storing property values
        """
        self.container = {}

        """
        FillFormat - a model defined in Swagger
        """
        self.container['type'] = None 
        self.container['solid_fill'] = None 
        self.container['pattern_fill'] = None 
        self.container['texture_fill'] = None 
        self.container['gradient_fill'] = None 
        self.container['image_data'] = None 
        params = locals()
        self.type = type
        if 'type' in params:
            self.type = params["type"]


             
        self.solid_fill = solid_fill
        if 'solid_fill' in params:
            self.solid_fill = params["solid_fill"]


             
        self.pattern_fill = pattern_fill
        if 'pattern_fill' in params:
            self.pattern_fill = params["pattern_fill"]


             
        self.texture_fill = texture_fill
        if 'texture_fill' in params:
            self.texture_fill = params["texture_fill"]


             
        self.gradient_fill = gradient_fill
        if 'gradient_fill' in params:
            self.gradient_fill = params["gradient_fill"]


             
        self.image_data = image_data
        if 'image_data' in params:
            self.image_data = params["image_data"]


             

    @property
    def type(self):
        return self.container['type']

    @type.setter
    def type(self, type):
        self.container['type'] = type 
    @property
    def solid_fill(self):
        return self.container['solid_fill']

    @solid_fill.setter
    def solid_fill(self, solid_fill):
        self.container['solid_fill'] = solid_fill 
    @property
    def pattern_fill(self):
        return self.container['pattern_fill']

    @pattern_fill.setter
    def pattern_fill(self, pattern_fill):
        self.container['pattern_fill'] = pattern_fill 
    @property
    def texture_fill(self):
        return self.container['texture_fill']

    @texture_fill.setter
    def texture_fill(self, texture_fill):
        self.container['texture_fill'] = texture_fill 
    @property
    def gradient_fill(self):
        return self.container['gradient_fill']

    @gradient_fill.setter
    def gradient_fill(self, gradient_fill):
        self.container['gradient_fill'] = gradient_fill 
    @property
    def image_data(self):
        return self.container['image_data']

    @image_data.setter
    def image_data(self, image_data):
        self.container['image_data'] = image_data 

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
        if not isinstance(other, FillFormat):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other    