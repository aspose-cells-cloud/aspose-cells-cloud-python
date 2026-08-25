"""Data models for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class ImageSaveOptions:
    """ImageSaveOptions."""
    chart_image_type: Optional[str] = None
    embeded_image_name_in_svg: Optional[str] = None
    horizontal_resolution: Optional[int] = None
    image_format: Optional[str] = None
    is_cell_auto_fit: Optional[bool] = None
    one_page_per_sheet: Optional[bool] = None
    only_area: Optional[bool] = None
    printing_page: Optional[str] = None
    print_with_status_dialog: Optional[bool] = None
    quality: Optional[int] = None
    tiff_compression: Optional[str] = None
    vertical_resolution: Optional[int] = None
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
        if self.chart_image_type is not None:
            result["ChartImageType"] = self.chart_image_type
        if self.embeded_image_name_in_svg is not None:
            result["EmbededImageNameInSvg"] = self.embeded_image_name_in_svg
        if self.horizontal_resolution is not None:
            result["HorizontalResolution"] = self.horizontal_resolution
        if self.image_format is not None:
            result["ImageFormat"] = self.image_format
        if self.is_cell_auto_fit is not None:
            result["IsCellAutoFit"] = self.is_cell_auto_fit
        if self.one_page_per_sheet is not None:
            result["OnePagePerSheet"] = self.one_page_per_sheet
        if self.only_area is not None:
            result["OnlyArea"] = self.only_area
        if self.printing_page is not None:
            result["PrintingPage"] = self.printing_page
        if self.print_with_status_dialog is not None:
            result["PrintWithStatusDialog"] = self.print_with_status_dialog
        if self.quality is not None:
            result["Quality"] = self.quality
        if self.tiff_compression is not None:
            result["TiffCompression"] = self.tiff_compression
        if self.vertical_resolution is not None:
            result["VerticalResolution"] = self.vertical_resolution
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
