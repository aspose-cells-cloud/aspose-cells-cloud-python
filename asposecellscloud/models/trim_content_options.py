# coding: utf-8
"""
<copyright company="Aspose" file="TrimContentOptionspy.cs">
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

class TrimContentOptions(object):

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
        'data_source' : 'DataSource',
        'file_info' : 'FileInfo',
        'trim_content' : 'str',
        'trim_leading' : 'bool',
        'trim_trailing' : 'bool',
        'trim_space_between_word_to1' : 'bool',
        'trim_non_breaking_spaces' : 'bool',
        'remove_extra_line_breaks' : 'bool',
        'remove_all_line_breaks' : 'bool',
        'scope_options' : 'ScopeOptions'
    }

    attribute_map = {
        'data_source' : 'DataSource' ,
        'file_info' : 'FileInfo' ,
        'trim_content' : 'TrimContent' ,
        'trim_leading' : 'TrimLeading' ,
        'trim_trailing' : 'TrimTrailing' ,
        'trim_space_between_word_to1' : 'TrimSpaceBetweenWordTo1' ,
        'trim_non_breaking_spaces' : 'TrimNonBreakingSpaces' ,
        'remove_extra_line_breaks' : 'RemoveExtraLineBreaks' ,
        'remove_all_line_breaks' : 'RemoveAllLineBreaks' ,
        'scope_options' : 'ScopeOptions' 
    }

    @staticmethod
    def get_swagger_types():
        return TrimContentOptions.swagger_types

    @staticmethod
    def get_attribute_map():
        return TrimContentOptions.attribute_map

    def get_from_container(self, attr):
        if attr in self.container:
            return self.container[attr]
        return None

    def __init__(self,data_source=None ,file_info=None ,trim_content=None ,trim_leading=None ,trim_trailing=None ,trim_space_between_word_to1=None ,trim_non_breaking_spaces=None ,remove_extra_line_breaks=None ,remove_all_line_breaks=None ,scope_options=None   ,**kw):
        """
        Associative dict for storing property values
        """
        self.container = {}

        """
        TrimContentOptions - a model defined in Swagger
        """
        self.container['data_source'] = None 
        self.container['file_info'] = None 
        self.container['trim_content'] = None 
        self.container['trim_leading'] = None 
        self.container['trim_trailing'] = None 
        self.container['trim_space_between_word_to1'] = None 
        self.container['trim_non_breaking_spaces'] = None 
        self.container['remove_extra_line_breaks'] = None 
        self.container['remove_all_line_breaks'] = None 
        self.container['scope_options'] = None 
        params = locals()
        self.data_source = data_source
        if 'data_source' in params:
            self.data_source = params["data_source"]


             
        self.file_info = file_info
        if 'file_info' in params:
            self.file_info = params["file_info"]


             
        self.trim_content = trim_content
        if 'trim_content' in params:
            self.trim_content = params["trim_content"]


             
        self.trim_leading = trim_leading
        if 'trim_leading' in params:
            self.trim_leading = params["trim_leading"]


             
        self.trim_trailing = trim_trailing
        if 'trim_trailing' in params:
            self.trim_trailing = params["trim_trailing"]


             
        self.trim_space_between_word_to1 = trim_space_between_word_to1
        if 'trim_space_between_word_to1' in params:
            self.trim_space_between_word_to1 = params["trim_space_between_word_to1"]


             
        self.trim_non_breaking_spaces = trim_non_breaking_spaces
        if 'trim_non_breaking_spaces' in params:
            self.trim_non_breaking_spaces = params["trim_non_breaking_spaces"]


             
        self.remove_extra_line_breaks = remove_extra_line_breaks
        if 'remove_extra_line_breaks' in params:
            self.remove_extra_line_breaks = params["remove_extra_line_breaks"]


             
        self.remove_all_line_breaks = remove_all_line_breaks
        if 'remove_all_line_breaks' in params:
            self.remove_all_line_breaks = params["remove_all_line_breaks"]


             
        self.scope_options = scope_options
        if 'scope_options' in params:
            self.scope_options = params["scope_options"]


             

    @property
    def data_source(self):
        return self.container['data_source']

    @data_source.setter
    def data_source(self, data_source):
        self.container['data_source'] = data_source 
    @property
    def file_info(self):
        return self.container['file_info']

    @file_info.setter
    def file_info(self, file_info):
        self.container['file_info'] = file_info 
    @property
    def trim_content(self):
        return self.container['trim_content']

    @trim_content.setter
    def trim_content(self, trim_content):
        self.container['trim_content'] = trim_content 
    @property
    def trim_leading(self):
        return self.container['trim_leading']

    @trim_leading.setter
    def trim_leading(self, trim_leading):
        self.container['trim_leading'] = trim_leading 
    @property
    def trim_trailing(self):
        return self.container['trim_trailing']

    @trim_trailing.setter
    def trim_trailing(self, trim_trailing):
        self.container['trim_trailing'] = trim_trailing 
    @property
    def trim_space_between_word_to1(self):
        return self.container['trim_space_between_word_to1']

    @trim_space_between_word_to1.setter
    def trim_space_between_word_to1(self, trim_space_between_word_to1):
        self.container['trim_space_between_word_to1'] = trim_space_between_word_to1 
    @property
    def trim_non_breaking_spaces(self):
        return self.container['trim_non_breaking_spaces']

    @trim_non_breaking_spaces.setter
    def trim_non_breaking_spaces(self, trim_non_breaking_spaces):
        self.container['trim_non_breaking_spaces'] = trim_non_breaking_spaces 
    @property
    def remove_extra_line_breaks(self):
        return self.container['remove_extra_line_breaks']

    @remove_extra_line_breaks.setter
    def remove_extra_line_breaks(self, remove_extra_line_breaks):
        self.container['remove_extra_line_breaks'] = remove_extra_line_breaks 
    @property
    def remove_all_line_breaks(self):
        return self.container['remove_all_line_breaks']

    @remove_all_line_breaks.setter
    def remove_all_line_breaks(self, remove_all_line_breaks):
        self.container['remove_all_line_breaks'] = remove_all_line_breaks 
    @property
    def scope_options(self):
        return self.container['scope_options']

    @scope_options.setter
    def scope_options(self, scope_options):
        self.container['scope_options'] = scope_options 

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
        if not isinstance(other, TrimContentOptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other    