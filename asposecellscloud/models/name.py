# coding: utf-8
"""
<copyright company="Aspose" file="Namepy.cs">
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

class Name(object):

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
        'comment' : 'str',
        'worksheet_index' : 'int',
        'is_referred' : 'bool',
        'is_visible' : 'bool',
        'r1_c1_refers_to' : 'str',
        'refers_to' : 'str',
        'text' : 'str',
        'link' : 'Link'
    }

    attribute_map = {
        'comment' : 'Comment' ,
        'worksheet_index' : 'WorksheetIndex' ,
        'is_referred' : 'IsReferred' ,
        'is_visible' : 'IsVisible' ,
        'r1_c1_refers_to' : 'R1C1RefersTo' ,
        'refers_to' : 'RefersTo' ,
        'text' : 'Text' ,
        'link' : 'link' 
    }

    @staticmethod
    def get_swagger_types():
        return Name.swagger_types

    @staticmethod
    def get_attribute_map():
        return Name.attribute_map

    def get_from_container(self, attr):
        if attr in self.container:
            return self.container[attr]
        return None

    def __init__(self,comment=None ,worksheet_index=None ,is_referred=None ,is_visible=None ,r1_c1_refers_to=None ,refers_to=None ,text=None ,link=None   ,**kw):
        """
        Associative dict for storing property values
        """
        self.container = {}

        """
        Name - a model defined in Swagger
        """
        self.container['comment'] = None 
        self.container['worksheet_index'] = None 
        self.container['is_referred'] = None 
        self.container['is_visible'] = None 
        self.container['r1_c1_refers_to'] = None 
        self.container['refers_to'] = None 
        self.container['text'] = None 
        self.container['link'] = None 
        params = locals()
        self.comment = comment
        if 'comment' in params:
            self.comment = params["comment"]


             
        self.worksheet_index = worksheet_index
        if 'worksheet_index' in params:
            self.worksheet_index = params["worksheet_index"]


             
        self.is_referred = is_referred
        if 'is_referred' in params:
            self.is_referred = params["is_referred"]


             
        self.is_visible = is_visible
        if 'is_visible' in params:
            self.is_visible = params["is_visible"]


             
        self.r1_c1_refers_to = r1_c1_refers_to
        if 'r1_c1_refers_to' in params:
            self.r1_c1_refers_to = params["r1_c1_refers_to"]


             
        self.refers_to = refers_to
        if 'refers_to' in params:
            self.refers_to = params["refers_to"]


             
        self.text = text
        if 'text' in params:
            self.text = params["text"]


             
        self.link = link
        if 'link' in params:
            self.link = params["link"]


             

    @property
    def comment(self):
        return self.container['comment']

    @comment.setter
    def comment(self, comment):
        self.container['comment'] = comment 
    @property
    def worksheet_index(self):
        return self.container['worksheet_index']

    @worksheet_index.setter
    def worksheet_index(self, worksheet_index):
        self.container['worksheet_index'] = worksheet_index 
    @property
    def is_referred(self):
        return self.container['is_referred']

    @is_referred.setter
    def is_referred(self, is_referred):
        self.container['is_referred'] = is_referred 
    @property
    def is_visible(self):
        return self.container['is_visible']

    @is_visible.setter
    def is_visible(self, is_visible):
        self.container['is_visible'] = is_visible 
    @property
    def r1_c1_refers_to(self):
        return self.container['r1_c1_refers_to']

    @r1_c1_refers_to.setter
    def r1_c1_refers_to(self, r1_c1_refers_to):
        self.container['r1_c1_refers_to'] = r1_c1_refers_to 
    @property
    def refers_to(self):
        return self.container['refers_to']

    @refers_to.setter
    def refers_to(self, refers_to):
        self.container['refers_to'] = refers_to 
    @property
    def text(self):
        return self.container['text']

    @text.setter
    def text(self, text):
        self.container['text'] = text 
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
        if not isinstance(other, Name):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other    