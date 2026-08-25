"""Data models for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class WorkbookSettings:
    """Represents all settings of the workbook."""
    auto_compress_pictures: Optional[bool] = None
    auto_recover: Optional[bool] = None
    build_version: Optional[str] = None
    calc_mode: Optional[str] = None
    calculation_id: Optional[str] = None
    check_comptiliblity: Optional[bool] = None
    check_excel_restriction: Optional[bool] = None
    crash_save: Optional[bool] = None
    create_calc_chain: Optional[bool] = None
    data_extract_load: Optional[bool] = None
    date1904: Optional[bool] = None
    display_drawing_objects: Optional[str] = None
    enable_macros: Optional[bool] = None
    first_visible_tab: Optional[int] = None
    hide_pivot_field_list: Optional[bool] = None
    is_default_encrypted: Optional[bool] = None
    is_hidden: Optional[bool] = None
    is_h_scroll_bar_visible: Optional[bool] = None
    is_minimized: Optional[bool] = None
    is_v_scroll_bar_visible: Optional[bool] = None
    iteration: Optional[bool] = None
    language_code: Optional[str] = None
    max_change: Optional[float] = None
    max_iteration: Optional[int] = None
    memory_setting: Optional[str] = None
    number_decimal_separator: Optional[str] = None
    number_group_separator: Optional[str] = None
    parsing_formula_on_open: Optional[bool] = None
    precision_as_displayed: Optional[bool] = None
    recalculate_before_save: Optional[bool] = None
    re_calculate_on_open: Optional[bool] = None
    recommend_read_only: Optional[bool] = None
    region: Optional[str] = None
    remove_personal_information: Optional[bool] = None
    repair_load: Optional[bool] = None
    shared: Optional[bool] = None
    sheet_tab_bar_width: Optional[int] = None
    show_tabs: Optional[bool] = None
    update_adjacent_cells_border: Optional[bool] = None
    update_links_type: Optional[str] = None
    window_height: Optional[float] = None
    window_left: Optional[float] = None
    window_top: Optional[float] = None
    window_width: Optional[float] = None
    author: Optional[str] = None
    check_custom_number_format: Optional[bool] = None
    protection_type: Optional[str] = None
    globalization_settings: Optional[GlobalizationSettings] = None
    password: Optional[str] = None
    write_protection: Optional[WriteProtection] = None
    is_encrypted: Optional[bool] = None
    is_protected: Optional[bool] = None
    max_row: Optional[int] = None
    max_column: Optional[int] = None
    significant_digits: Optional[int] = None
    check_compatibility: Optional[bool] = None
    paper_size: Optional[str] = None
    max_rows_of_shared_formula: Optional[int] = None
    compliance: Optional[str] = None
    quote_prefix_to_style: Optional[bool] = None
    formula_settings: Optional[FormulaSettings] = None
    force_full_calculate: Optional[bool] = None

    def to_dict(self) -> Dict[str, Any]:
        result: Dict[str, Any] = {}
        if self.auto_compress_pictures is not None:
            result["AutoCompressPictures"] = self.auto_compress_pictures
        if self.auto_recover is not None:
            result["AutoRecover"] = self.auto_recover
        if self.build_version is not None:
            result["BuildVersion"] = self.build_version
        if self.calc_mode is not None:
            result["CalcMode"] = self.calc_mode
        if self.calculation_id is not None:
            result["CalculationId"] = self.calculation_id
        if self.check_comptiliblity is not None:
            result["CheckComptiliblity"] = self.check_comptiliblity
        if self.check_excel_restriction is not None:
            result["CheckExcelRestriction"] = self.check_excel_restriction
        if self.crash_save is not None:
            result["CrashSave"] = self.crash_save
        if self.create_calc_chain is not None:
            result["CreateCalcChain"] = self.create_calc_chain
        if self.data_extract_load is not None:
            result["DataExtractLoad"] = self.data_extract_load
        if self.date1904 is not None:
            result["Date1904"] = self.date1904
        if self.display_drawing_objects is not None:
            result["DisplayDrawingObjects"] = self.display_drawing_objects
        if self.enable_macros is not None:
            result["EnableMacros"] = self.enable_macros
        if self.first_visible_tab is not None:
            result["FirstVisibleTab"] = self.first_visible_tab
        if self.hide_pivot_field_list is not None:
            result["HidePivotFieldList"] = self.hide_pivot_field_list
        if self.is_default_encrypted is not None:
            result["IsDefaultEncrypted"] = self.is_default_encrypted
        if self.is_hidden is not None:
            result["IsHidden"] = self.is_hidden
        if self.is_h_scroll_bar_visible is not None:
            result["IsHScrollBarVisible"] = self.is_h_scroll_bar_visible
        if self.is_minimized is not None:
            result["IsMinimized"] = self.is_minimized
        if self.is_v_scroll_bar_visible is not None:
            result["IsVScrollBarVisible"] = self.is_v_scroll_bar_visible
        if self.iteration is not None:
            result["Iteration"] = self.iteration
        if self.language_code is not None:
            result["LanguageCode"] = self.language_code
        if self.max_change is not None:
            result["MaxChange"] = self.max_change
        if self.max_iteration is not None:
            result["MaxIteration"] = self.max_iteration
        if self.memory_setting is not None:
            result["MemorySetting"] = self.memory_setting
        if self.number_decimal_separator is not None:
            result["NumberDecimalSeparator"] = self.number_decimal_separator
        if self.number_group_separator is not None:
            result["NumberGroupSeparator"] = self.number_group_separator
        if self.parsing_formula_on_open is not None:
            result["ParsingFormulaOnOpen"] = self.parsing_formula_on_open
        if self.precision_as_displayed is not None:
            result["PrecisionAsDisplayed"] = self.precision_as_displayed
        if self.recalculate_before_save is not None:
            result["RecalculateBeforeSave"] = self.recalculate_before_save
        if self.re_calculate_on_open is not None:
            result["ReCalculateOnOpen"] = self.re_calculate_on_open
        if self.recommend_read_only is not None:
            result["RecommendReadOnly"] = self.recommend_read_only
        if self.region is not None:
            result["Region"] = self.region
        if self.remove_personal_information is not None:
            result["RemovePersonalInformation"] = self.remove_personal_information
        if self.repair_load is not None:
            result["RepairLoad"] = self.repair_load
        if self.shared is not None:
            result["Shared"] = self.shared
        if self.sheet_tab_bar_width is not None:
            result["SheetTabBarWidth"] = self.sheet_tab_bar_width
        if self.show_tabs is not None:
            result["ShowTabs"] = self.show_tabs
        if self.update_adjacent_cells_border is not None:
            result["UpdateAdjacentCellsBorder"] = self.update_adjacent_cells_border
        if self.update_links_type is not None:
            result["UpdateLinksType"] = self.update_links_type
        if self.window_height is not None:
            result["WindowHeight"] = self.window_height
        if self.window_left is not None:
            result["WindowLeft"] = self.window_left
        if self.window_top is not None:
            result["WindowTop"] = self.window_top
        if self.window_width is not None:
            result["WindowWidth"] = self.window_width
        if self.author is not None:
            result["Author"] = self.author
        if self.check_custom_number_format is not None:
            result["CheckCustomNumberFormat"] = self.check_custom_number_format
        if self.protection_type is not None:
            result["ProtectionType"] = self.protection_type
        if self.globalization_settings is not None:
            result["GlobalizationSettings"] = self.globalization_settings.to_dict()
        if self.password is not None:
            result["Password"] = self.password
        if self.write_protection is not None:
            result["WriteProtection"] = self.write_protection.to_dict()
        if self.is_encrypted is not None:
            result["IsEncrypted"] = self.is_encrypted
        if self.is_protected is not None:
            result["IsProtected"] = self.is_protected
        if self.max_row is not None:
            result["MaxRow"] = self.max_row
        if self.max_column is not None:
            result["MaxColumn"] = self.max_column
        if self.significant_digits is not None:
            result["SignificantDigits"] = self.significant_digits
        if self.check_compatibility is not None:
            result["CheckCompatibility"] = self.check_compatibility
        if self.paper_size is not None:
            result["PaperSize"] = self.paper_size
        if self.max_rows_of_shared_formula is not None:
            result["MaxRowsOfSharedFormula"] = self.max_rows_of_shared_formula
        if self.compliance is not None:
            result["Compliance"] = self.compliance
        if self.quote_prefix_to_style is not None:
            result["QuotePrefixToStyle"] = self.quote_prefix_to_style
        if self.formula_settings is not None:
            result["FormulaSettings"] = self.formula_settings.to_dict()
        if self.force_full_calculate is not None:
            result["ForceFullCalculate"] = self.force_full_calculate
        return result

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), default=str)
