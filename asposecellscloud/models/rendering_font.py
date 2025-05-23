# coding: utf-8
"""
<copyright company="Aspose" file="RenderingFontpy.cs">
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

class RenderingFont(object):

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
        'name' : 'str',
        'size' : 'float',
        'bold' : 'bool',
        'italic' : 'bool',
        'color' : 'Color'
    }

    attribute_map = {
        'name' : 'Name' ,
        'size' : 'Size' ,
        'bold' : 'Bold' ,
        'italic' : 'Italic' ,
        'color' : 'Color' 
    }

    @staticmethod
    def get_swagger_types():
        return RenderingFont.swagger_types

    @staticmethod
    def get_attribute_map():
        return RenderingFont.attribute_map

    def get_from_container(self, attr):
        if attr in self.container:
            return self.container[attr]
        return None

    def __init__(self,name=None ,size=None ,bold=None ,italic=None ,color=None   ,**kw):
        """
        Associative dict for storing property values
        """
        self.container = {}

        """
        RenderingFont - a model defined in Swagger
        """
        self.container['name'] = None 
        self.container['size'] = None 
        self.container['bold'] = None 
        self.container['italic'] = None 
        self.container['color'] = None 
        params = locals()
        self.name = name
        if 'name' in params:
            self.name = params["name"]


             
        self.size = size
        if 'size' in params:
            self.size = params["size"]


             
        self.bold = bold
        if 'bold' in params:
            self.bold = params["bold"]


             
        self.italic = italic
        if 'italic' in params:
            self.italic = params["italic"]


             
        self.color = color
        if 'color' in params:
            self.color = params["color"]


             

    @property
    def name(self):
        return self.container['name']

    @name.setter
    def name(self, name):
        self.container['name'] = name 
    @property
    def size(self):
        return self.container['size']

    @size.setter
    def size(self, size):
        self.container['size'] = size 
    @property
    def bold(self):
        return self.container['bold']

    @bold.setter
    def bold(self, bold):
        self.container['bold'] = bold 
    @property
    def italic(self):
        return self.container['italic']

    @italic.setter
    def italic(self, italic):
        self.container['italic'] = italic 
    @property
    def color(self):
        return self.container['color']

    @color.setter
    def color(self, color):
        self.container['color'] = color 

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
        if not isinstance(other, RenderingFont):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other    