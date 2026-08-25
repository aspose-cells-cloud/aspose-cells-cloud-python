"""Data models for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class SqlScriptSaveOptions:
    """SqlScriptSaveOptions."""
    check_if_table_exists: Optional[bool] = None
    column_type_map: Optional[str] = None
    check_all_data_for_column_type: Optional[bool] = None
    add_blank_line_between_rows: Optional[bool] = None
    separator: Optional[str] = None
    operator_type: Optional[str] = None
    primary_key: Optional[int] = None
    create_table: Optional[bool] = None
    id_name: Optional[str] = None
    start_id: Optional[int] = None
    table_name: Optional[str] = None
    export_as_string: Optional[bool] = None
    export_area: Optional[CellArea] = None
    has_header_row: Optional[bool] = None
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
        if self.check_if_table_exists is not None:
            result["CheckIfTableExists"] = self.check_if_table_exists
        if self.column_type_map is not None:
            result["ColumnTypeMap"] = self.column_type_map
        if self.check_all_data_for_column_type is not None:
            result["CheckAllDataForColumnType"] = self.check_all_data_for_column_type
        if self.add_blank_line_between_rows is not None:
            result["AddBlankLineBetweenRows"] = self.add_blank_line_between_rows
        if self.separator is not None:
            result["Separator"] = self.separator
        if self.operator_type is not None:
            result["OperatorType"] = self.operator_type
        if self.primary_key is not None:
            result["PrimaryKey"] = self.primary_key
        if self.create_table is not None:
            result["CreateTable"] = self.create_table
        if self.id_name is not None:
            result["IdName"] = self.id_name
        if self.start_id is not None:
            result["StartId"] = self.start_id
        if self.table_name is not None:
            result["TableName"] = self.table_name
        if self.export_as_string is not None:
            result["ExportAsString"] = self.export_as_string
        if self.export_area is not None:
            result["ExportArea"] = self.export_area.to_dict()
        if self.has_header_row is not None:
            result["HasHeaderRow"] = self.has_header_row
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
