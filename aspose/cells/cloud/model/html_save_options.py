"""Data models for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class HtmlSaveOptions:
    """HtmlSaveOptions."""
    export_page_headers: Optional[bool] = None
    export_page_footers: Optional[bool] = None
    export_row_column_headings: Optional[bool] = None
    show_all_sheets: Optional[bool] = None
    image_options: Optional[ImageOrPrintOptions] = None
    save_as_single_file: Optional[bool] = None
    export_hidden_worksheet: Optional[bool] = None
    export_grid_lines: Optional[bool] = None
    presentation_preference: Optional[bool] = None
    cell_css_prefix: Optional[str] = None
    table_css_id: Optional[str] = None
    is_full_path_link: Optional[bool] = None
    export_worksheet_css_separately: Optional[bool] = None
    export_similar_border_style: Optional[bool] = None
    merge_empty_td_forcely: Optional[bool] = None
    export_cell_coordinate: Optional[bool] = None
    export_extra_headings: Optional[bool] = None
    export_headings: Optional[bool] = None
    export_formula: Optional[bool] = None
    add_tooltip_text: Optional[bool] = None
    export_bogus_row_data: Optional[bool] = None
    exclude_unused_styles: Optional[bool] = None
    export_document_properties: Optional[bool] = None
    export_worksheet_properties: Optional[bool] = None
    export_workbook_properties: Optional[bool] = None
    export_frame_scripts_and_properties: Optional[bool] = None
    attached_files_directory: Optional[str] = None
    attached_files_url_prefix: Optional[str] = None
    encoding: Optional[str] = None
    export_active_worksheet_only: Optional[bool] = None
    export_chart_image_format: Optional[str] = None
    export_images_as_base64: Optional[bool] = None
    hidden_col_display_type: Optional[str] = None
    hidden_row_display_type: Optional[str] = None
    html_cross_string_type: Optional[str] = None
    is_exp_image_to_temp_dir: Optional[bool] = None
    page_title: Optional[str] = None
    parse_html_tag_in_cell: Optional[bool] = None
    cell_name_attribute: Optional[str] = None
    save_format: Optional[str] = None
    cached_file_folder: Optional[str] = None
    clear_data: Optional[bool] = None
    create_directory: Optional[bool] = None
    enable_http_compression: Optional[bool] = None
    refresh_chart_cache: Optional[bool] = None
    sort_names: Optional[bool] = None
    validate_merged_areas: Optional[bool] = None
    merge_areas: Optional[bool] = None
    sort_external_names: Optional[bool] = None
    check_excel_restriction: Optional[bool] = None
    update_smart_art: Optional[bool] = None
    encrypt_document_properties: Optional[bool] = None

    def to_dict(self) -> Dict[str, Any]:
        result: Dict[str, Any] = {}
        if self.export_page_headers is not None:
            result["ExportPageHeaders"] = self.export_page_headers
        if self.export_page_footers is not None:
            result["ExportPageFooters"] = self.export_page_footers
        if self.export_row_column_headings is not None:
            result["ExportRowColumnHeadings"] = self.export_row_column_headings
        if self.show_all_sheets is not None:
            result["ShowAllSheets"] = self.show_all_sheets
        if self.image_options is not None:
            result["ImageOptions"] = self.image_options.to_dict()
        if self.save_as_single_file is not None:
            result["SaveAsSingleFile"] = self.save_as_single_file
        if self.export_hidden_worksheet is not None:
            result["ExportHiddenWorksheet"] = self.export_hidden_worksheet
        if self.export_grid_lines is not None:
            result["ExportGridLines"] = self.export_grid_lines
        if self.presentation_preference is not None:
            result["PresentationPreference"] = self.presentation_preference
        if self.cell_css_prefix is not None:
            result["CellCssPrefix"] = self.cell_css_prefix
        if self.table_css_id is not None:
            result["TableCssId"] = self.table_css_id
        if self.is_full_path_link is not None:
            result["IsFullPathLink"] = self.is_full_path_link
        if self.export_worksheet_css_separately is not None:
            result["ExportWorksheetCSSSeparately"] = self.export_worksheet_css_separately
        if self.export_similar_border_style is not None:
            result["ExportSimilarBorderStyle"] = self.export_similar_border_style
        if self.merge_empty_td_forcely is not None:
            result["MergeEmptyTdForcely"] = self.merge_empty_td_forcely
        if self.export_cell_coordinate is not None:
            result["ExportCellCoordinate"] = self.export_cell_coordinate
        if self.export_extra_headings is not None:
            result["ExportExtraHeadings"] = self.export_extra_headings
        if self.export_headings is not None:
            result["ExportHeadings"] = self.export_headings
        if self.export_formula is not None:
            result["ExportFormula"] = self.export_formula
        if self.add_tooltip_text is not None:
            result["AddTooltipText"] = self.add_tooltip_text
        if self.export_bogus_row_data is not None:
            result["ExportBogusRowData"] = self.export_bogus_row_data
        if self.exclude_unused_styles is not None:
            result["ExcludeUnusedStyles"] = self.exclude_unused_styles
        if self.export_document_properties is not None:
            result["ExportDocumentProperties"] = self.export_document_properties
        if self.export_worksheet_properties is not None:
            result["ExportWorksheetProperties"] = self.export_worksheet_properties
        if self.export_workbook_properties is not None:
            result["ExportWorkbookProperties"] = self.export_workbook_properties
        if self.export_frame_scripts_and_properties is not None:
            result["ExportFrameScriptsAndProperties"] = self.export_frame_scripts_and_properties
        if self.attached_files_directory is not None:
            result["AttachedFilesDirectory"] = self.attached_files_directory
        if self.attached_files_url_prefix is not None:
            result["AttachedFilesUrlPrefix"] = self.attached_files_url_prefix
        if self.encoding is not None:
            result["Encoding"] = self.encoding
        if self.export_active_worksheet_only is not None:
            result["ExportActiveWorksheetOnly"] = self.export_active_worksheet_only
        if self.export_chart_image_format is not None:
            result["ExportChartImageFormat"] = self.export_chart_image_format
        if self.export_images_as_base64 is not None:
            result["ExportImagesAsBase64"] = self.export_images_as_base64
        if self.hidden_col_display_type is not None:
            result["HiddenColDisplayType"] = self.hidden_col_display_type
        if self.hidden_row_display_type is not None:
            result["HiddenRowDisplayType"] = self.hidden_row_display_type
        if self.html_cross_string_type is not None:
            result["HtmlCrossStringType"] = self.html_cross_string_type
        if self.is_exp_image_to_temp_dir is not None:
            result["IsExpImageToTempDir"] = self.is_exp_image_to_temp_dir
        if self.page_title is not None:
            result["PageTitle"] = self.page_title
        if self.parse_html_tag_in_cell is not None:
            result["ParseHtmlTagInCell"] = self.parse_html_tag_in_cell
        if self.cell_name_attribute is not None:
            result["CellNameAttribute"] = self.cell_name_attribute
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
        if self.merge_areas is not None:
            result["MergeAreas"] = self.merge_areas
        if self.sort_external_names is not None:
            result["SortExternalNames"] = self.sort_external_names
        if self.check_excel_restriction is not None:
            result["CheckExcelRestriction"] = self.check_excel_restriction
        if self.update_smart_art is not None:
            result["UpdateSmartArt"] = self.update_smart_art
        if self.encrypt_document_properties is not None:
            result["EncryptDocumentProperties"] = self.encrypt_document_properties
        return result

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), default=str)
