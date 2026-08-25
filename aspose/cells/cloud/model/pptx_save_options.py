"""Data models for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class PptxSaveOptions:
    """PptxSaveOptions."""
    ignore_hidden_rows: Optional[bool] = None
    adjust_font_size_for_row_type: Optional[str] = None
    export_view_type: Optional[str] = None
    default_font: Optional[str] = None
    check_workbook_default_font: Optional[bool] = None
    check_font_compatibility: Optional[bool] = None
    is_font_substitution_char_granularity: Optional[bool] = None
    one_page_per_sheet: Optional[bool] = None
    all_columns_in_one_page_per_sheet: Optional[bool] = None
    ignore_error: Optional[bool] = None
    output_blank_page_when_nothing_to_print: Optional[bool] = None
    page_index: Optional[int] = None
    page_count: Optional[int] = None
    printing_page_type: Optional[str] = None
    gridline_type: Optional[str] = None
    text_cross_type: Optional[str] = None
    default_edit_language: Optional[str] = None
    emf_render_setting: Optional[str] = None
    merge_areas: Optional[bool] = None
    sort_external_names: Optional[bool] = None
    update_smart_art: Optional[bool] = None
    save_format: Optional[str] = None
    cached_file_folder: Optional[str] = None
    clear_data: Optional[bool] = None
    create_directory: Optional[bool] = None
    enable_http_compression: Optional[bool] = None
    refresh_chart_cache: Optional[bool] = None
    sort_names: Optional[bool] = None
    validate_merged_areas: Optional[bool] = None
    check_excel_restriction: Optional[bool] = None
    encrypt_document_properties: Optional[bool] = None

    def to_dict(self) -> Dict[str, Any]:
        result: Dict[str, Any] = {}
        if self.ignore_hidden_rows is not None:
            result["IgnoreHiddenRows"] = self.ignore_hidden_rows
        if self.adjust_font_size_for_row_type is not None:
            result["AdjustFontSizeForRowType"] = self.adjust_font_size_for_row_type
        if self.export_view_type is not None:
            result["ExportViewType"] = self.export_view_type
        if self.default_font is not None:
            result["DefaultFont"] = self.default_font
        if self.check_workbook_default_font is not None:
            result["CheckWorkbookDefaultFont"] = self.check_workbook_default_font
        if self.check_font_compatibility is not None:
            result["CheckFontCompatibility"] = self.check_font_compatibility
        if self.is_font_substitution_char_granularity is not None:
            result["IsFontSubstitutionCharGranularity"] = self.is_font_substitution_char_granularity
        if self.one_page_per_sheet is not None:
            result["OnePagePerSheet"] = self.one_page_per_sheet
        if self.all_columns_in_one_page_per_sheet is not None:
            result["AllColumnsInOnePagePerSheet"] = self.all_columns_in_one_page_per_sheet
        if self.ignore_error is not None:
            result["IgnoreError"] = self.ignore_error
        if self.output_blank_page_when_nothing_to_print is not None:
            result["OutputBlankPageWhenNothingToPrint"] = self.output_blank_page_when_nothing_to_print
        if self.page_index is not None:
            result["PageIndex"] = self.page_index
        if self.page_count is not None:
            result["PageCount"] = self.page_count
        if self.printing_page_type is not None:
            result["PrintingPageType"] = self.printing_page_type
        if self.gridline_type is not None:
            result["GridlineType"] = self.gridline_type
        if self.text_cross_type is not None:
            result["TextCrossType"] = self.text_cross_type
        if self.default_edit_language is not None:
            result["DefaultEditLanguage"] = self.default_edit_language
        if self.emf_render_setting is not None:
            result["EmfRenderSetting"] = self.emf_render_setting
        if self.merge_areas is not None:
            result["MergeAreas"] = self.merge_areas
        if self.sort_external_names is not None:
            result["SortExternalNames"] = self.sort_external_names
        if self.update_smart_art is not None:
            result["UpdateSmartArt"] = self.update_smart_art
        if self.save_format is not None:
            result["SaveFormat"] = self.save_format
        if self.cached_file_folder is not None:
            result["CachedFileFolder"] = self.cached_file_folder
        if self.clear_data is not None:
            result["ClearData"] = self.clear_data
        if self.create_directory is not None:
            result["CreateDirectory"] = self.create_directory
        if self.enable_http_compression is not None:
            result["EnableHTTPCompression"] = self.enable_http_compression
        if self.refresh_chart_cache is not None:
            result["RefreshChartCache"] = self.refresh_chart_cache
        if self.sort_names is not None:
            result["SortNames"] = self.sort_names
        if self.validate_merged_areas is not None:
            result["ValidateMergedAreas"] = self.validate_merged_areas
        if self.check_excel_restriction is not None:
            result["CheckExcelRestriction"] = self.check_excel_restriction
        if self.encrypt_document_properties is not None:
            result["EncryptDocumentProperties"] = self.encrypt_document_properties
        return result

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), default=str)
