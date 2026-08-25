"""Data models for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class SpreadsheetML2003SaveOptions:
    """SpreadsheetML2003SaveOptions."""
    export_column_index_of_cell: Optional[bool] = None
    is_indented_formatting: Optional[bool] = None
    limit_as_xls: Optional[bool] = None
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
        if self.export_column_index_of_cell is not None:
            result["ExportColumnIndexOfCell"] = self.export_column_index_of_cell
        if self.is_indented_formatting is not None:
            result["IsIndentedFormatting"] = self.is_indented_formatting
        if self.limit_as_xls is not None:
            result["LimitAsXls"] = self.limit_as_xls
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
