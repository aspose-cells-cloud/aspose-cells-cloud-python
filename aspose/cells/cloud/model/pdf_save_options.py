"""Data models for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class PdfSaveOptions:
    """PdfSaveOptions."""
    display_doc_title: Optional[bool] = None
    export_document_structure: Optional[bool] = None
    emf_render_setting: Optional[str] = None
    custom_properties_export: Optional[str] = None
    optimization_type: Optional[str] = None
    producer: Optional[str] = None
    pdf_compression: Optional[str] = None
    font_encoding: Optional[str] = None
    watermark: Optional[RenderingWatermark] = None
    calculate_formula: Optional[bool] = None
    check_font_compatibility: Optional[bool] = None
    compliance: Optional[str] = None
    default_font: Optional[str] = None
    one_page_per_sheet: Optional[bool] = None
    printing_page_type: Optional[str] = None
    security_options: Optional[PdfSecurityOptions] = None
    desired_ppi: Optional[int] = None
    jpeg_quality: Optional[int] = None
    image_type: Optional[str] = None
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
        if self.display_doc_title is not None:
            result["DisplayDocTitle"] = self.display_doc_title
        if self.export_document_structure is not None:
            result["ExportDocumentStructure"] = self.export_document_structure
        if self.emf_render_setting is not None:
            result["EmfRenderSetting"] = self.emf_render_setting
        if self.custom_properties_export is not None:
            result["CustomPropertiesExport"] = self.custom_properties_export
        if self.optimization_type is not None:
            result["OptimizationType"] = self.optimization_type
        if self.producer is not None:
            result["Producer"] = self.producer
        if self.pdf_compression is not None:
            result["PdfCompression"] = self.pdf_compression
        if self.font_encoding is not None:
            result["FontEncoding"] = self.font_encoding
        if self.watermark is not None:
            result["Watermark"] = self.watermark.to_dict()
        if self.calculate_formula is not None:
            result["CalculateFormula"] = self.calculate_formula
        if self.check_font_compatibility is not None:
            result["CheckFontCompatibility"] = self.check_font_compatibility
        if self.compliance is not None:
            result["Compliance"] = self.compliance
        if self.default_font is not None:
            result["DefaultFont"] = self.default_font
        if self.one_page_per_sheet is not None:
            result["OnePagePerSheet"] = self.one_page_per_sheet
        if self.printing_page_type is not None:
            result["PrintingPageType"] = self.printing_page_type
        if self.security_options is not None:
            result["SecurityOptions"] = self.security_options.to_dict()
        if self.desired_ppi is not None:
            result["desiredPPI"] = self.desired_ppi
        if self.jpeg_quality is not None:
            result["jpegQuality"] = self.jpeg_quality
        if self.image_type is not None:
            result["ImageType"] = self.image_type
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
