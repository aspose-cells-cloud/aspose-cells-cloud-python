# coding: utf-8
"""
<copyright company="Aspose" file="RemoveCharactersByCharacterpy.cs">
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

class RemoveCharactersByCharacter(object):

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
        'remove_text_method' : 'str',
        'remove_characters' : 'list[str]',
        'remove_character_sets_type' : 'str'
    }

    attribute_map = {
        'remove_text_method' : 'RemoveTextMethod' ,
        'remove_characters' : 'RemoveCharacters' ,
        'remove_character_sets_type' : 'RemoveCharacterSetsType' 
    }

    @staticmethod
    def get_swagger_types():
        return RemoveCharactersByCharacter.swagger_types

    @staticmethod
    def get_attribute_map():
        return RemoveCharactersByCharacter.attribute_map

    def get_from_container(self, attr):
        if attr in self.container:
            return self.container[attr]
        return None

    def __init__(self,remove_text_method=None ,remove_characters=None ,remove_character_sets_type=None   ,**kw):
        """
        Associative dict for storing property values
        """
        self.container = {}

        """
        RemoveCharactersByCharacter - a model defined in Swagger
        """
        self.container['remove_text_method'] = None 
        self.container['remove_characters'] = None 
        self.container['remove_character_sets_type'] = None 
        params = locals()
        self.remove_text_method = remove_text_method
        if 'remove_text_method' in params:
            self.remove_text_method = params["remove_text_method"]


             
        self.remove_characters = remove_characters
        if 'remove_characters' in params:
            self.remove_characters = params["remove_characters"]


             
        self.remove_character_sets_type = remove_character_sets_type
        if 'remove_character_sets_type' in params:
            self.remove_character_sets_type = params["remove_character_sets_type"]


             

    @property
    def remove_text_method(self):
        return self.container['remove_text_method']

    @remove_text_method.setter
    def remove_text_method(self, remove_text_method):
        self.container['remove_text_method'] = remove_text_method 
    @property
    def remove_characters(self):
        return self.container['remove_characters']

    @remove_characters.setter
    def remove_characters(self, remove_characters):
        self.container['remove_characters'] = remove_characters 
    @property
    def remove_character_sets_type(self):
        return self.container['remove_character_sets_type']

    @remove_character_sets_type.setter
    def remove_character_sets_type(self, remove_character_sets_type):
        self.container['remove_character_sets_type'] = remove_character_sets_type 

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
        if not isinstance(other, RemoveCharactersByCharacter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other    