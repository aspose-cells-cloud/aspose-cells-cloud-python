# coding: utf-8
"""
<copyright company="Aspose" file="DataTransformationRequestpy.cs">
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

class DataTransformationRequest(object):

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
        'file_info' : 'FileInfo',
        'transformation' : 'Transformation',
        'load_data' : 'LoadData',
        'region' : 'str',
        'out_format' : 'str'
    }

    attribute_map = {
        'file_info' : 'FileInfo' ,
        'transformation' : 'Transformation' ,
        'load_data' : 'LoadData' ,
        'region' : 'Region' ,
        'out_format' : 'OutFormat' 
    }

    @staticmethod
    def get_swagger_types():
        return DataTransformationRequest.swagger_types

    @staticmethod
    def get_attribute_map():
        return DataTransformationRequest.attribute_map

    def get_from_container(self, attr):
        if attr in self.container:
            return self.container[attr]
        return None

    def __init__(self,file_info=None ,transformation=None ,load_data=None ,region=None ,out_format=None   ,**kw):
        """
        Associative dict for storing property values
        """
        self.container = {}

        """
        DataTransformationRequest - a model defined in Swagger
        """
        self.container['file_info'] = None 
        self.container['transformation'] = None 
        self.container['load_data'] = None 
        self.container['region'] = None 
        self.container['out_format'] = None 
        params = locals()
        self.file_info = file_info
        if 'file_info' in params:
            self.file_info = params["file_info"]


             
        self.transformation = transformation
        if 'transformation' in params:
            self.transformation = params["transformation"]


             
        self.load_data = load_data
        if 'load_data' in params:
            self.load_data = params["load_data"]


             
        self.region = region
        if 'region' in params:
            self.region = params["region"]


             
        self.out_format = out_format
        if 'out_format' in params:
            self.out_format = params["out_format"]


             

    @property
    def file_info(self):
        return self.container['file_info']

    @file_info.setter
    def file_info(self, file_info):
        self.container['file_info'] = file_info 
    @property
    def transformation(self):
        return self.container['transformation']

    @transformation.setter
    def transformation(self, transformation):
        self.container['transformation'] = transformation 
    @property
    def load_data(self):
        return self.container['load_data']

    @load_data.setter
    def load_data(self, load_data):
        self.container['load_data'] = load_data 
    @property
    def region(self):
        return self.container['region']

    @region.setter
    def region(self, region):
        self.container['region'] = region 
    @property
    def out_format(self):
        return self.container['out_format']

    @out_format.setter
    def out_format(self, out_format):
        self.container['out_format'] = out_format 

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
        if not isinstance(other, DataTransformationRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other    