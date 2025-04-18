# coding: utf-8
"""
<copyright company="Aspose" file="FormulaSettingspy.cs">
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

class FormulaSettings(object):

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
        'calculate_on_open' : 'bool',
        'calculate_on_save' : 'bool',
        'force_full_calculation' : 'bool',
        'calculation_mode' : 'str',
        'calculation_id' : 'str',
        'enable_iterative_calculation' : 'bool',
        'max_iteration' : 'int',
        'max_change' : 'float',
        'precision_as_displayed' : 'bool',
        'enable_calculation_chain' : 'bool',
        'preserve_padding_spaces' : 'bool'
    }

    attribute_map = {
        'calculate_on_open' : 'CalculateOnOpen' ,
        'calculate_on_save' : 'CalculateOnSave' ,
        'force_full_calculation' : 'ForceFullCalculation' ,
        'calculation_mode' : 'CalculationMode' ,
        'calculation_id' : 'CalculationId' ,
        'enable_iterative_calculation' : 'EnableIterativeCalculation' ,
        'max_iteration' : 'MaxIteration' ,
        'max_change' : 'MaxChange' ,
        'precision_as_displayed' : 'PrecisionAsDisplayed' ,
        'enable_calculation_chain' : 'EnableCalculationChain' ,
        'preserve_padding_spaces' : 'PreservePaddingSpaces' 
    }

    @staticmethod
    def get_swagger_types():
        return FormulaSettings.swagger_types

    @staticmethod
    def get_attribute_map():
        return FormulaSettings.attribute_map

    def get_from_container(self, attr):
        if attr in self.container:
            return self.container[attr]
        return None

    def __init__(self,calculate_on_open=None ,calculate_on_save=None ,force_full_calculation=None ,calculation_mode=None ,calculation_id=None ,enable_iterative_calculation=None ,max_iteration=None ,max_change=None ,precision_as_displayed=None ,enable_calculation_chain=None ,preserve_padding_spaces=None   ,**kw):
        """
        Associative dict for storing property values
        """
        self.container = {}

        """
        FormulaSettings - a model defined in Swagger
        """
        self.container['calculate_on_open'] = None 
        self.container['calculate_on_save'] = None 
        self.container['force_full_calculation'] = None 
        self.container['calculation_mode'] = None 
        self.container['calculation_id'] = None 
        self.container['enable_iterative_calculation'] = None 
        self.container['max_iteration'] = None 
        self.container['max_change'] = None 
        self.container['precision_as_displayed'] = None 
        self.container['enable_calculation_chain'] = None 
        self.container['preserve_padding_spaces'] = None 
        params = locals()
        self.calculate_on_open = calculate_on_open
        if 'calculate_on_open' in params:
            self.calculate_on_open = params["calculate_on_open"]


             
        self.calculate_on_save = calculate_on_save
        if 'calculate_on_save' in params:
            self.calculate_on_save = params["calculate_on_save"]


             
        self.force_full_calculation = force_full_calculation
        if 'force_full_calculation' in params:
            self.force_full_calculation = params["force_full_calculation"]


             
        self.calculation_mode = calculation_mode
        if 'calculation_mode' in params:
            self.calculation_mode = params["calculation_mode"]


             
        self.calculation_id = calculation_id
        if 'calculation_id' in params:
            self.calculation_id = params["calculation_id"]


             
        self.enable_iterative_calculation = enable_iterative_calculation
        if 'enable_iterative_calculation' in params:
            self.enable_iterative_calculation = params["enable_iterative_calculation"]


             
        self.max_iteration = max_iteration
        if 'max_iteration' in params:
            self.max_iteration = params["max_iteration"]


             
        self.max_change = max_change
        if 'max_change' in params:
            self.max_change = params["max_change"]


             
        self.precision_as_displayed = precision_as_displayed
        if 'precision_as_displayed' in params:
            self.precision_as_displayed = params["precision_as_displayed"]


             
        self.enable_calculation_chain = enable_calculation_chain
        if 'enable_calculation_chain' in params:
            self.enable_calculation_chain = params["enable_calculation_chain"]


             
        self.preserve_padding_spaces = preserve_padding_spaces
        if 'preserve_padding_spaces' in params:
            self.preserve_padding_spaces = params["preserve_padding_spaces"]


             

    @property
    def calculate_on_open(self):
        return self.container['calculate_on_open']

    @calculate_on_open.setter
    def calculate_on_open(self, calculate_on_open):
        self.container['calculate_on_open'] = calculate_on_open 
    @property
    def calculate_on_save(self):
        return self.container['calculate_on_save']

    @calculate_on_save.setter
    def calculate_on_save(self, calculate_on_save):
        self.container['calculate_on_save'] = calculate_on_save 
    @property
    def force_full_calculation(self):
        return self.container['force_full_calculation']

    @force_full_calculation.setter
    def force_full_calculation(self, force_full_calculation):
        self.container['force_full_calculation'] = force_full_calculation 
    @property
    def calculation_mode(self):
        return self.container['calculation_mode']

    @calculation_mode.setter
    def calculation_mode(self, calculation_mode):
        self.container['calculation_mode'] = calculation_mode 
    @property
    def calculation_id(self):
        return self.container['calculation_id']

    @calculation_id.setter
    def calculation_id(self, calculation_id):
        self.container['calculation_id'] = calculation_id 
    @property
    def enable_iterative_calculation(self):
        return self.container['enable_iterative_calculation']

    @enable_iterative_calculation.setter
    def enable_iterative_calculation(self, enable_iterative_calculation):
        self.container['enable_iterative_calculation'] = enable_iterative_calculation 
    @property
    def max_iteration(self):
        return self.container['max_iteration']

    @max_iteration.setter
    def max_iteration(self, max_iteration):
        self.container['max_iteration'] = max_iteration 
    @property
    def max_change(self):
        return self.container['max_change']

    @max_change.setter
    def max_change(self, max_change):
        self.container['max_change'] = max_change 
    @property
    def precision_as_displayed(self):
        return self.container['precision_as_displayed']

    @precision_as_displayed.setter
    def precision_as_displayed(self, precision_as_displayed):
        self.container['precision_as_displayed'] = precision_as_displayed 
    @property
    def enable_calculation_chain(self):
        return self.container['enable_calculation_chain']

    @enable_calculation_chain.setter
    def enable_calculation_chain(self, enable_calculation_chain):
        self.container['enable_calculation_chain'] = enable_calculation_chain 
    @property
    def preserve_padding_spaces(self):
        return self.container['preserve_padding_spaces']

    @preserve_padding_spaces.setter
    def preserve_padding_spaces(self, preserve_padding_spaces):
        self.container['preserve_padding_spaces'] = preserve_padding_spaces 

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
        if not isinstance(other, FormulaSettings):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other    