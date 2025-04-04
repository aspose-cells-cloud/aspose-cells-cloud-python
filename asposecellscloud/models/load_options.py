# coding: utf-8
"""
<copyright company="Aspose" file="LoadOptionspy.cs">
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

class LoadOptions(object):

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
        'convert_numeric_data' : 'str',
        'interrupt_monitor' : 'str',
        'language_code' : 'str',
        'load_data_options' : 'str',
        'load_format' : 'str',
        'only_load_document_properties' : 'str',
        'parsing_formula_on_open' : 'str',
        'password' : 'str',
        'region' : 'str',
        'standard_font' : 'str',
        'standard_font_size' : 'float'
    }

    attribute_map = {
        'convert_numeric_data' : 'ConvertNumericData' ,
        'interrupt_monitor' : 'InterruptMonitor' ,
        'language_code' : 'LanguageCode' ,
        'load_data_options' : 'LoadDataOptions' ,
        'load_format' : 'LoadFormat' ,
        'only_load_document_properties' : 'OnlyLoadDocumentProperties' ,
        'parsing_formula_on_open' : 'ParsingFormulaOnOpen' ,
        'password' : 'Password' ,
        'region' : 'Region' ,
        'standard_font' : 'StandardFont' ,
        'standard_font_size' : 'StandardFontSize' 
    }

    @staticmethod
    def get_swagger_types():
        return LoadOptions.swagger_types

    @staticmethod
    def get_attribute_map():
        return LoadOptions.attribute_map

    def get_from_container(self, attr):
        if attr in self.container:
            return self.container[attr]
        return None

    def __init__(self,convert_numeric_data=None ,interrupt_monitor=None ,language_code=None ,load_data_options=None ,load_format=None ,only_load_document_properties=None ,parsing_formula_on_open=None ,password=None ,region=None ,standard_font=None ,standard_font_size=None   ,**kw):
        """
        Associative dict for storing property values
        """
        self.container = {}

        """
        LoadOptions - a model defined in Swagger
        """
        self.container['convert_numeric_data'] = None 
        self.container['interrupt_monitor'] = None 
        self.container['language_code'] = None 
        self.container['load_data_options'] = None 
        self.container['load_format'] = None 
        self.container['only_load_document_properties'] = None 
        self.container['parsing_formula_on_open'] = None 
        self.container['password'] = None 
        self.container['region'] = None 
        self.container['standard_font'] = None 
        self.container['standard_font_size'] = None 
        params = locals()
        self.convert_numeric_data = convert_numeric_data
        if 'convert_numeric_data' in params:
            self.convert_numeric_data = params["convert_numeric_data"]


             
        self.interrupt_monitor = interrupt_monitor
        if 'interrupt_monitor' in params:
            self.interrupt_monitor = params["interrupt_monitor"]


             
        self.language_code = language_code
        if 'language_code' in params:
            self.language_code = params["language_code"]


             
        self.load_data_options = load_data_options
        if 'load_data_options' in params:
            self.load_data_options = params["load_data_options"]


             
        self.load_format = load_format
        if 'load_format' in params:
            self.load_format = params["load_format"]


             
        self.only_load_document_properties = only_load_document_properties
        if 'only_load_document_properties' in params:
            self.only_load_document_properties = params["only_load_document_properties"]


             
        self.parsing_formula_on_open = parsing_formula_on_open
        if 'parsing_formula_on_open' in params:
            self.parsing_formula_on_open = params["parsing_formula_on_open"]


             
        self.password = password
        if 'password' in params:
            self.password = params["password"]


             
        self.region = region
        if 'region' in params:
            self.region = params["region"]


             
        self.standard_font = standard_font
        if 'standard_font' in params:
            self.standard_font = params["standard_font"]


             
        self.standard_font_size = standard_font_size
        if 'standard_font_size' in params:
            self.standard_font_size = params["standard_font_size"]


             

    @property
    def convert_numeric_data(self):
        return self.container['convert_numeric_data']

    @convert_numeric_data.setter
    def convert_numeric_data(self, convert_numeric_data):
        self.container['convert_numeric_data'] = convert_numeric_data 
    @property
    def interrupt_monitor(self):
        return self.container['interrupt_monitor']

    @interrupt_monitor.setter
    def interrupt_monitor(self, interrupt_monitor):
        self.container['interrupt_monitor'] = interrupt_monitor 
    @property
    def language_code(self):
        return self.container['language_code']

    @language_code.setter
    def language_code(self, language_code):
        self.container['language_code'] = language_code 
    @property
    def load_data_options(self):
        return self.container['load_data_options']

    @load_data_options.setter
    def load_data_options(self, load_data_options):
        self.container['load_data_options'] = load_data_options 
    @property
    def load_format(self):
        return self.container['load_format']

    @load_format.setter
    def load_format(self, load_format):
        self.container['load_format'] = load_format 
    @property
    def only_load_document_properties(self):
        return self.container['only_load_document_properties']

    @only_load_document_properties.setter
    def only_load_document_properties(self, only_load_document_properties):
        self.container['only_load_document_properties'] = only_load_document_properties 
    @property
    def parsing_formula_on_open(self):
        return self.container['parsing_formula_on_open']

    @parsing_formula_on_open.setter
    def parsing_formula_on_open(self, parsing_formula_on_open):
        self.container['parsing_formula_on_open'] = parsing_formula_on_open 
    @property
    def password(self):
        return self.container['password']

    @password.setter
    def password(self, password):
        self.container['password'] = password 
    @property
    def region(self):
        return self.container['region']

    @region.setter
    def region(self, region):
        self.container['region'] = region 
    @property
    def standard_font(self):
        return self.container['standard_font']

    @standard_font.setter
    def standard_font(self, standard_font):
        self.container['standard_font'] = standard_font 
    @property
    def standard_font_size(self):
        return self.container['standard_font_size']

    @standard_font_size.setter
    def standard_font_size(self, standard_font_size):
        self.container['standard_font_size'] = standard_font_size 

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
        if not isinstance(other, LoadOptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other    