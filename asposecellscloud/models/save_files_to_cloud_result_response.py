# coding: utf-8
"""
<copyright company="Aspose" file="SaveFilesToCloudResultResponsepy.cs">
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

class SaveFilesToCloudResultResponse(object):

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
        'save_files_to_cloud_result' : 'SaveFilesToCloudResult',
        'code' : 'int',
        'status' : 'str'
    }

    attribute_map = {
        'save_files_to_cloud_result' : 'SaveFilesToCloudResult' ,
        'code' : 'Code' ,
        'status' : 'Status' 
    }

    @staticmethod
    def get_swagger_types():
        return SaveFilesToCloudResultResponse.swagger_types

    @staticmethod
    def get_attribute_map():
        return SaveFilesToCloudResultResponse.attribute_map

    def get_from_container(self, attr):
        if attr in self.container:
            return self.container[attr]
        return None

    def __init__(self,save_files_to_cloud_result=None ,code=None ,status=None   ,**kw):
        """
        Associative dict for storing property values
        """
        self.container = {}

        """
        SaveFilesToCloudResultResponse - a model defined in Swagger
        """
        self.container['save_files_to_cloud_result'] = None 
        self.container['code'] = None 
        self.container['status'] = None 
        params = locals()
        self.save_files_to_cloud_result = save_files_to_cloud_result
        if 'save_files_to_cloud_result' in params:
            self.save_files_to_cloud_result = params["save_files_to_cloud_result"]


             
        self.code = code
        if 'code' in params:
            self.code = params["code"]


             
        self.status = status
        if 'status' in params:
            self.status = params["status"]


             

    @property
    def save_files_to_cloud_result(self):
        return self.container['save_files_to_cloud_result']

    @save_files_to_cloud_result.setter
    def save_files_to_cloud_result(self, save_files_to_cloud_result):
        self.container['save_files_to_cloud_result'] = save_files_to_cloud_result 
    @property
    def code(self):
        return self.container['code']

    @code.setter
    def code(self, code):
        self.container['code'] = code 
    @property
    def status(self):
        return self.container['status']

    @status.setter
    def status(self, status):
        self.container['status'] = status 

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
        if not isinstance(other, SaveFilesToCloudResultResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other    