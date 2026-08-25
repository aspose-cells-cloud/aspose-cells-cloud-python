"""Data models for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class ImageOrPrintOptions:
    """ImageOrPrintOptions."""
    text_cross_type: Optional[str] = None
    gridline_type: Optional[str] = None
    output_blank_page_when_nothing_to_print: Optional[bool] = None
    check_workbook_default_font: Optional[bool] = None
    default_font: Optional[str] = None
    is_optimized: Optional[bool] = None
    page_count: Optional[int] = None
    page_index: Optional[int] = None
    is_font_substitution_char_granularity: Optional[bool] = None
    transparent: Optional[bool] = None
    only_area: Optional[bool] = None
    svg_fit_to_view_port: Optional[bool] = None
    embeded_image_name_in_svg: Optional[str] = None
    all_columns_in_one_page_per_sheet: Optional[bool] = None
    print_with_status_dialog: Optional[bool] = None
    horizontal_resolution: Optional[int] = None
    vertical_resolution: Optional[int] = None
    default_edit_language: Optional[str] = None
    tiff_color_depth: Optional[str] = None
    tiff_compression: Optional[str] = None
    printing_page: Optional[str] = None
    quality: Optional[int] = None
    image_type: Optional[str] = None
    one_page_per_sheet: Optional[bool] = None
    tiff_binarization_method: Optional[str] = None

    def to_dict(self) -> Dict[str, Any]:
        result: Dict[str, Any] = {}
        if self.text_cross_type is not None:
            result["TextCrossType"] = self.text_cross_type
        if self.gridline_type is not None:
            result["GridlineType"] = self.gridline_type
        if self.output_blank_page_when_nothing_to_print is not None:
            result["OutputBlankPageWhenNothingToPrint"] = self.output_blank_page_when_nothing_to_print
        if self.check_workbook_default_font is not None:
            result["CheckWorkbookDefaultFont"] = self.check_workbook_default_font
        if self.default_font is not None:
            result["DefaultFont"] = self.default_font
        if self.is_optimized is not None:
            result["IsOptimized"] = self.is_optimized
        if self.page_count is not None:
            result["PageCount"] = self.page_count
        if self.page_index is not None:
            result["PageIndex"] = self.page_index
        if self.is_font_substitution_char_granularity is not None:
            result["IsFontSubstitutionCharGranularity"] = self.is_font_substitution_char_granularity
        if self.transparent is not None:
            result["Transparent"] = self.transparent
        if self.only_area is not None:
            result["OnlyArea"] = self.only_area
        if self.svg_fit_to_view_port is not None:
            result["SVGFitToViewPort"] = self.svg_fit_to_view_port
        if self.embeded_image_name_in_svg is not None:
            result["EmbededImageNameInSvg"] = self.embeded_image_name_in_svg
        if self.all_columns_in_one_page_per_sheet is not None:
            result["AllColumnsInOnePagePerSheet"] = self.all_columns_in_one_page_per_sheet
        if self.print_with_status_dialog is not None:
            result["PrintWithStatusDialog"] = self.print_with_status_dialog
        if self.horizontal_resolution is not None:
            result["HorizontalResolution"] = self.horizontal_resolution
        if self.vertical_resolution is not None:
            result["VerticalResolution"] = self.vertical_resolution
        if self.default_edit_language is not None:
            result["DefaultEditLanguage"] = self.default_edit_language
        if self.tiff_color_depth is not None:
            result["TiffColorDepth"] = self.tiff_color_depth
        if self.tiff_compression is not None:
            result["TiffCompression"] = self.tiff_compression
        if self.printing_page is not None:
            result["PrintingPage"] = self.printing_page
        if self.quality is not None:
            result["Quality"] = self.quality
        if self.image_type is not None:
            result["ImageType"] = self.image_type
        if self.one_page_per_sheet is not None:
            result["OnePagePerSheet"] = self.one_page_per_sheet
        if self.tiff_binarization_method is not None:
            result["TiffBinarizationMethod"] = self.tiff_binarization_method
        return result

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), default=str)
