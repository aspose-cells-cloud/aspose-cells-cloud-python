# coding: utf-8
"""
<copyright company="Aspose" file="CopyOptionspy.cs">
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

class CopyOptions(object):

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
        'column_character_width' : 'bool',
        'copy_invalid_formulas_as_values' : 'bool',
        'copy_names' : 'bool',
        'extend_to_adjacent_range' : 'bool',
        'refer_to_destination_sheet' : 'bool',
        'refer_to_sheet_with_same_name' : 'bool',
        'copy_theme' : 'bool'
    }

    attribute_map = {
        'column_character_width' : 'ColumnCharacterWidth' ,
        'copy_invalid_formulas_as_values' : 'CopyInvalidFormulasAsValues' ,
        'copy_names' : 'CopyNames' ,
        'extend_to_adjacent_range' : 'ExtendToAdjacentRange' ,
        'refer_to_destination_sheet' : 'ReferToDestinationSheet' ,
        'refer_to_sheet_with_same_name' : 'ReferToSheetWithSameName' ,
        'copy_theme' : 'CopyTheme' 
    }

    @staticmethod
    def get_swagger_types():
        return CopyOptions.swagger_types

    @staticmethod
    def get_attribute_map():
        return CopyOptions.attribute_map

    def get_from_container(self, attr):
        if attr in self.container:
            return self.container[attr]
        return None

    def __init__(self,column_character_width=None ,copy_invalid_formulas_as_values=None ,copy_names=None ,extend_to_adjacent_range=None ,refer_to_destination_sheet=None ,refer_to_sheet_with_same_name=None ,copy_theme=None   ,**kw):
        """
        Associative dict for storing property values
        """
        self.container = {}

        """
        CopyOptions - a model defined in Swagger
        """
        self.container['column_character_width'] = None 
        self.container['copy_invalid_formulas_as_values'] = None 
        self.container['copy_names'] = None 
        self.container['extend_to_adjacent_range'] = None 
        self.container['refer_to_destination_sheet'] = None 
        self.container['refer_to_sheet_with_same_name'] = None 
        self.container['copy_theme'] = None 
        params = locals()
        self.column_character_width = column_character_width
        if 'column_character_width' in params:
            self.column_character_width = params["column_character_width"]


             
        self.copy_invalid_formulas_as_values = copy_invalid_formulas_as_values
        if 'copy_invalid_formulas_as_values' in params:
            self.copy_invalid_formulas_as_values = params["copy_invalid_formulas_as_values"]


             
        self.copy_names = copy_names
        if 'copy_names' in params:
            self.copy_names = params["copy_names"]


             
        self.extend_to_adjacent_range = extend_to_adjacent_range
        if 'extend_to_adjacent_range' in params:
            self.extend_to_adjacent_range = params["extend_to_adjacent_range"]


             
        self.refer_to_destination_sheet = refer_to_destination_sheet
        if 'refer_to_destination_sheet' in params:
            self.refer_to_destination_sheet = params["refer_to_destination_sheet"]


             
        self.refer_to_sheet_with_same_name = refer_to_sheet_with_same_name
        if 'refer_to_sheet_with_same_name' in params:
            self.refer_to_sheet_with_same_name = params["refer_to_sheet_with_same_name"]


             
        self.copy_theme = copy_theme
        if 'copy_theme' in params:
            self.copy_theme = params["copy_theme"]


             

    @property
    def column_character_width(self):
        return self.container['column_character_width']

    @column_character_width.setter
    def column_character_width(self, column_character_width):
        self.container['column_character_width'] = column_character_width 
    @property
    def copy_invalid_formulas_as_values(self):
        return self.container['copy_invalid_formulas_as_values']

    @copy_invalid_formulas_as_values.setter
    def copy_invalid_formulas_as_values(self, copy_invalid_formulas_as_values):
        self.container['copy_invalid_formulas_as_values'] = copy_invalid_formulas_as_values 
    @property
    def copy_names(self):
        return self.container['copy_names']

    @copy_names.setter
    def copy_names(self, copy_names):
        self.container['copy_names'] = copy_names 
    @property
    def extend_to_adjacent_range(self):
        return self.container['extend_to_adjacent_range']

    @extend_to_adjacent_range.setter
    def extend_to_adjacent_range(self, extend_to_adjacent_range):
        self.container['extend_to_adjacent_range'] = extend_to_adjacent_range 
    @property
    def refer_to_destination_sheet(self):
        return self.container['refer_to_destination_sheet']

    @refer_to_destination_sheet.setter
    def refer_to_destination_sheet(self, refer_to_destination_sheet):
        self.container['refer_to_destination_sheet'] = refer_to_destination_sheet 
    @property
    def refer_to_sheet_with_same_name(self):
        return self.container['refer_to_sheet_with_same_name']

    @refer_to_sheet_with_same_name.setter
    def refer_to_sheet_with_same_name(self, refer_to_sheet_with_same_name):
        self.container['refer_to_sheet_with_same_name'] = refer_to_sheet_with_same_name 
    @property
    def copy_theme(self):
        return self.container['copy_theme']

    @copy_theme.setter
    def copy_theme(self, copy_theme):
        self.container['copy_theme'] = copy_theme 

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
        if not isinstance(other, CopyOptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other    