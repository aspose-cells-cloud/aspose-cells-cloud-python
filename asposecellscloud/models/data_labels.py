# coding: utf-8
"""
<copyright company="Aspose" file="DataLabelspy.cs">
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

class DataLabels(object):

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
        'is_auto_text' : 'bool',
        'is_deleted' : 'bool',
        'linked_source' : 'str',
        'number' : 'int',
        'number_format' : 'str',
        'number_format_linked' : 'bool',
        'position' : 'str',
        'rotation_angle' : 'int',
        'separator' : 'str',
        'show_bubble_size' : 'bool',
        'show_category_name' : 'bool',
        'show_legend_key' : 'bool',
        'show_percentage' : 'bool',
        'show_series_name' : 'bool',
        'show_value' : 'bool',
        'text' : 'str',
        'text_direction' : 'str',
        'text_horizontal_alignment' : 'str',
        'text_vertical_alignment' : 'str',
        'area' : 'Area',
        'auto_scale_font' : 'bool',
        'background_mode' : 'str',
        'border' : 'Line',
        'font' : 'Font',
        'is_automatic_size' : 'bool',
        'is_inner_mode' : 'bool',
        'shadow' : 'bool',
        'width' : 'int',
        'height' : 'int',
        'x' : 'int',
        'y' : 'int'
    }

    attribute_map = {
        'is_auto_text' : 'IsAutoText' ,
        'is_deleted' : 'IsDeleted' ,
        'linked_source' : 'LinkedSource' ,
        'number' : 'Number' ,
        'number_format' : 'NumberFormat' ,
        'number_format_linked' : 'NumberFormatLinked' ,
        'position' : 'Position' ,
        'rotation_angle' : 'RotationAngle' ,
        'separator' : 'Separator' ,
        'show_bubble_size' : 'ShowBubbleSize' ,
        'show_category_name' : 'ShowCategoryName' ,
        'show_legend_key' : 'ShowLegendKey' ,
        'show_percentage' : 'ShowPercentage' ,
        'show_series_name' : 'ShowSeriesName' ,
        'show_value' : 'ShowValue' ,
        'text' : 'Text' ,
        'text_direction' : 'TextDirection' ,
        'text_horizontal_alignment' : 'TextHorizontalAlignment' ,
        'text_vertical_alignment' : 'TextVerticalAlignment' ,
        'area' : 'Area' ,
        'auto_scale_font' : 'AutoScaleFont' ,
        'background_mode' : 'BackgroundMode' ,
        'border' : 'Border' ,
        'font' : 'Font' ,
        'is_automatic_size' : 'IsAutomaticSize' ,
        'is_inner_mode' : 'IsInnerMode' ,
        'shadow' : 'Shadow' ,
        'width' : 'Width' ,
        'height' : 'Height' ,
        'x' : 'X' ,
        'y' : 'Y' 
    }

    @staticmethod
    def get_swagger_types():
        return DataLabels.swagger_types

    @staticmethod
    def get_attribute_map():
        return DataLabels.attribute_map

    def get_from_container(self, attr):
        if attr in self.container:
            return self.container[attr]
        return None

    def __init__(self,is_auto_text=None ,is_deleted=None ,linked_source=None ,number=None ,number_format=None ,number_format_linked=None ,position=None ,rotation_angle=None ,separator=None ,show_bubble_size=None ,show_category_name=None ,show_legend_key=None ,show_percentage=None ,show_series_name=None ,show_value=None ,text=None ,text_direction=None ,text_horizontal_alignment=None ,text_vertical_alignment=None ,area=None ,auto_scale_font=None ,background_mode=None ,border=None ,font=None ,is_automatic_size=None ,is_inner_mode=None ,shadow=None ,width=None ,height=None ,x=None ,y=None   ,**kw):
        """
        Associative dict for storing property values
        """
        self.container = {}

        """
        DataLabels - a model defined in Swagger
        """
        self.container['is_auto_text'] = None 
        self.container['is_deleted'] = None 
        self.container['linked_source'] = None 
        self.container['number'] = None 
        self.container['number_format'] = None 
        self.container['number_format_linked'] = None 
        self.container['position'] = None 
        self.container['rotation_angle'] = None 
        self.container['separator'] = None 
        self.container['show_bubble_size'] = None 
        self.container['show_category_name'] = None 
        self.container['show_legend_key'] = None 
        self.container['show_percentage'] = None 
        self.container['show_series_name'] = None 
        self.container['show_value'] = None 
        self.container['text'] = None 
        self.container['text_direction'] = None 
        self.container['text_horizontal_alignment'] = None 
        self.container['text_vertical_alignment'] = None 
        self.container['area'] = None 
        self.container['auto_scale_font'] = None 
        self.container['background_mode'] = None 
        self.container['border'] = None 
        self.container['font'] = None 
        self.container['is_automatic_size'] = None 
        self.container['is_inner_mode'] = None 
        self.container['shadow'] = None 
        self.container['width'] = None 
        self.container['height'] = None 
        self.container['x'] = None 
        self.container['y'] = None 
        params = locals()
        self.is_auto_text = is_auto_text
        if 'is_auto_text' in params:
            self.is_auto_text = params["is_auto_text"]


             
        self.is_deleted = is_deleted
        if 'is_deleted' in params:
            self.is_deleted = params["is_deleted"]


             
        self.linked_source = linked_source
        if 'linked_source' in params:
            self.linked_source = params["linked_source"]


             
        self.number = number
        if 'number' in params:
            self.number = params["number"]


             
        self.number_format = number_format
        if 'number_format' in params:
            self.number_format = params["number_format"]


             
        self.number_format_linked = number_format_linked
        if 'number_format_linked' in params:
            self.number_format_linked = params["number_format_linked"]


             
        self.position = position
        if 'position' in params:
            self.position = params["position"]


             
        self.rotation_angle = rotation_angle
        if 'rotation_angle' in params:
            self.rotation_angle = params["rotation_angle"]


             
        self.separator = separator
        if 'separator' in params:
            self.separator = params["separator"]


             
        self.show_bubble_size = show_bubble_size
        if 'show_bubble_size' in params:
            self.show_bubble_size = params["show_bubble_size"]


             
        self.show_category_name = show_category_name
        if 'show_category_name' in params:
            self.show_category_name = params["show_category_name"]


             
        self.show_legend_key = show_legend_key
        if 'show_legend_key' in params:
            self.show_legend_key = params["show_legend_key"]


             
        self.show_percentage = show_percentage
        if 'show_percentage' in params:
            self.show_percentage = params["show_percentage"]


             
        self.show_series_name = show_series_name
        if 'show_series_name' in params:
            self.show_series_name = params["show_series_name"]


             
        self.show_value = show_value
        if 'show_value' in params:
            self.show_value = params["show_value"]


             
        self.text = text
        if 'text' in params:
            self.text = params["text"]


             
        self.text_direction = text_direction
        if 'text_direction' in params:
            self.text_direction = params["text_direction"]


             
        self.text_horizontal_alignment = text_horizontal_alignment
        if 'text_horizontal_alignment' in params:
            self.text_horizontal_alignment = params["text_horizontal_alignment"]


             
        self.text_vertical_alignment = text_vertical_alignment
        if 'text_vertical_alignment' in params:
            self.text_vertical_alignment = params["text_vertical_alignment"]


             
        self.area = area
        if 'area' in params:
            self.area = params["area"]


             
        self.auto_scale_font = auto_scale_font
        if 'auto_scale_font' in params:
            self.auto_scale_font = params["auto_scale_font"]


             
        self.background_mode = background_mode
        if 'background_mode' in params:
            self.background_mode = params["background_mode"]


             
        self.border = border
        if 'border' in params:
            self.border = params["border"]


             
        self.font = font
        if 'font' in params:
            self.font = params["font"]


             
        self.is_automatic_size = is_automatic_size
        if 'is_automatic_size' in params:
            self.is_automatic_size = params["is_automatic_size"]


             
        self.is_inner_mode = is_inner_mode
        if 'is_inner_mode' in params:
            self.is_inner_mode = params["is_inner_mode"]


             
        self.shadow = shadow
        if 'shadow' in params:
            self.shadow = params["shadow"]


             
        self.width = width
        if 'width' in params:
            self.width = params["width"]


             
        self.height = height
        if 'height' in params:
            self.height = params["height"]


             
        self.x = x
        if 'x' in params:
            self.x = params["x"]


             
        self.y = y
        if 'y' in params:
            self.y = params["y"]


             

    @property
    def is_auto_text(self):
        return self.container['is_auto_text']

    @is_auto_text.setter
    def is_auto_text(self, is_auto_text):
        self.container['is_auto_text'] = is_auto_text 
    @property
    def is_deleted(self):
        return self.container['is_deleted']

    @is_deleted.setter
    def is_deleted(self, is_deleted):
        self.container['is_deleted'] = is_deleted 
    @property
    def linked_source(self):
        return self.container['linked_source']

    @linked_source.setter
    def linked_source(self, linked_source):
        self.container['linked_source'] = linked_source 
    @property
    def number(self):
        return self.container['number']

    @number.setter
    def number(self, number):
        self.container['number'] = number 
    @property
    def number_format(self):
        return self.container['number_format']

    @number_format.setter
    def number_format(self, number_format):
        self.container['number_format'] = number_format 
    @property
    def number_format_linked(self):
        return self.container['number_format_linked']

    @number_format_linked.setter
    def number_format_linked(self, number_format_linked):
        self.container['number_format_linked'] = number_format_linked 
    @property
    def position(self):
        return self.container['position']

    @position.setter
    def position(self, position):
        self.container['position'] = position 
    @property
    def rotation_angle(self):
        return self.container['rotation_angle']

    @rotation_angle.setter
    def rotation_angle(self, rotation_angle):
        self.container['rotation_angle'] = rotation_angle 
    @property
    def separator(self):
        return self.container['separator']

    @separator.setter
    def separator(self, separator):
        self.container['separator'] = separator 
    @property
    def show_bubble_size(self):
        return self.container['show_bubble_size']

    @show_bubble_size.setter
    def show_bubble_size(self, show_bubble_size):
        self.container['show_bubble_size'] = show_bubble_size 
    @property
    def show_category_name(self):
        return self.container['show_category_name']

    @show_category_name.setter
    def show_category_name(self, show_category_name):
        self.container['show_category_name'] = show_category_name 
    @property
    def show_legend_key(self):
        return self.container['show_legend_key']

    @show_legend_key.setter
    def show_legend_key(self, show_legend_key):
        self.container['show_legend_key'] = show_legend_key 
    @property
    def show_percentage(self):
        return self.container['show_percentage']

    @show_percentage.setter
    def show_percentage(self, show_percentage):
        self.container['show_percentage'] = show_percentage 
    @property
    def show_series_name(self):
        return self.container['show_series_name']

    @show_series_name.setter
    def show_series_name(self, show_series_name):
        self.container['show_series_name'] = show_series_name 
    @property
    def show_value(self):
        return self.container['show_value']

    @show_value.setter
    def show_value(self, show_value):
        self.container['show_value'] = show_value 
    @property
    def text(self):
        return self.container['text']

    @text.setter
    def text(self, text):
        self.container['text'] = text 
    @property
    def text_direction(self):
        return self.container['text_direction']

    @text_direction.setter
    def text_direction(self, text_direction):
        self.container['text_direction'] = text_direction 
    @property
    def text_horizontal_alignment(self):
        return self.container['text_horizontal_alignment']

    @text_horizontal_alignment.setter
    def text_horizontal_alignment(self, text_horizontal_alignment):
        self.container['text_horizontal_alignment'] = text_horizontal_alignment 
    @property
    def text_vertical_alignment(self):
        return self.container['text_vertical_alignment']

    @text_vertical_alignment.setter
    def text_vertical_alignment(self, text_vertical_alignment):
        self.container['text_vertical_alignment'] = text_vertical_alignment 
    @property
    def area(self):
        return self.container['area']

    @area.setter
    def area(self, area):
        self.container['area'] = area 
    @property
    def auto_scale_font(self):
        return self.container['auto_scale_font']

    @auto_scale_font.setter
    def auto_scale_font(self, auto_scale_font):
        self.container['auto_scale_font'] = auto_scale_font 
    @property
    def background_mode(self):
        return self.container['background_mode']

    @background_mode.setter
    def background_mode(self, background_mode):
        self.container['background_mode'] = background_mode 
    @property
    def border(self):
        return self.container['border']

    @border.setter
    def border(self, border):
        self.container['border'] = border 
    @property
    def font(self):
        return self.container['font']

    @font.setter
    def font(self, font):
        self.container['font'] = font 
    @property
    def is_automatic_size(self):
        return self.container['is_automatic_size']

    @is_automatic_size.setter
    def is_automatic_size(self, is_automatic_size):
        self.container['is_automatic_size'] = is_automatic_size 
    @property
    def is_inner_mode(self):
        return self.container['is_inner_mode']

    @is_inner_mode.setter
    def is_inner_mode(self, is_inner_mode):
        self.container['is_inner_mode'] = is_inner_mode 
    @property
    def shadow(self):
        return self.container['shadow']

    @shadow.setter
    def shadow(self, shadow):
        self.container['shadow'] = shadow 
    @property
    def width(self):
        return self.container['width']

    @width.setter
    def width(self, width):
        self.container['width'] = width 
    @property
    def height(self):
        return self.container['height']

    @height.setter
    def height(self, height):
        self.container['height'] = height 
    @property
    def x(self):
        return self.container['x']

    @x.setter
    def x(self, x):
        self.container['x'] = x 
    @property
    def y(self):
        return self.container['y']

    @y.setter
    def y(self, y):
        self.container['y'] = y 

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
        if not isinstance(other, DataLabels):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other    