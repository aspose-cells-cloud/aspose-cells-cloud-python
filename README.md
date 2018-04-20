# aspose-cells-cloud-python

Aspose.Cells Cloud SDK for Python allows you to use Aspose.Cells APIs in your Python applications

- Package version: 18.2
- Build package: io.swagger.codegen.languages.PythonClientCodegen

## Requirements.

Python 2.7 and 3.5

## Installation & Usage
### pip install

```sh
pip install asposecellscloud
```
(you may need to run `pip` with root permission: `sudo pip install asposecellscloud`)

Then import the package:
```python
import asposecellscloud 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import asposecellscloud
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import asposecellscloud
from asposecellscloud.rest import ApiException
from pprint import pprint
# create an instance of the API class
api_instance = asposecellscloud.CellsApi()
name = 'name_example' # str | The workbook name.
sheet_name = 'sheet_name_example' # str | The worksheet name.
column_index = 56 # int | The column index.
columns = 56 # int | The columns.
update_reference = true # bool | The update reference.
folder = 'folder_example' # str | The workbook folder. (optional)

try:
    # Delete worksheet columns.
    api_response = api_instance.cells_delete_worksheet_columns(name, sheet_name, column_index, columns, update_reference, folder=folder)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CellsApi->cells_delete_worksheet_columns: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://api.aspose.cloud/v1.1/*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*CellsApi* | [**cells_delete_worksheet_columns**](docs/CellsApi.md#cells_delete_worksheet_columns) | **DELETE** /cells/{name}/worksheets/{sheetName}/cells/columns/{columnIndex} | Delete worksheet columns.
*CellsApi* | [**cells_delete_worksheet_row**](docs/CellsApi.md#cells_delete_worksheet_row) | **DELETE** /cells/{name}/worksheets/{sheetName}/cells/rows/{rowIndex} | Delete worksheet row.
*CellsApi* | [**cells_delete_worksheet_rows**](docs/CellsApi.md#cells_delete_worksheet_rows) | **DELETE** /cells/{name}/worksheets/{sheetName}/cells/rows | Delete several worksheet rows.
*CellsApi* | [**cells_get_worksheet_cell**](docs/CellsApi.md#cells_get_worksheet_cell) | **GET** /cells/{name}/worksheets/{sheetName}/cells/{cellOrMethodName} | Read cell data by cell&#39;s name.
*CellsApi* | [**cells_get_worksheet_cell_style**](docs/CellsApi.md#cells_get_worksheet_cell_style) | **GET** /cells/{name}/worksheets/{sheetName}/cells/{cellName}/style | Read cell&#39;s style info.
*CellsApi* | [**cells_get_worksheet_cells**](docs/CellsApi.md#cells_get_worksheet_cells) | **GET** /cells/{name}/worksheets/{sheetName}/cells | Get cells info.
*CellsApi* | [**cells_get_worksheet_column**](docs/CellsApi.md#cells_get_worksheet_column) | **GET** /cells/{name}/worksheets/{sheetName}/cells/columns/{columnIndex} | Read worksheet column data by column&#39;s index.
*CellsApi* | [**cells_get_worksheet_columns**](docs/CellsApi.md#cells_get_worksheet_columns) | **GET** /cells/{name}/worksheets/{sheetName}/cells/columns | Read worksheet columns info.
*CellsApi* | [**cells_get_worksheet_row**](docs/CellsApi.md#cells_get_worksheet_row) | **GET** /cells/{name}/worksheets/{sheetName}/cells/rows/{rowIndex} | Read worksheet row data by row&#39;s index.
*CellsApi* | [**cells_get_worksheet_rows**](docs/CellsApi.md#cells_get_worksheet_rows) | **GET** /cells/{name}/worksheets/{sheetName}/cells/rows | Read worksheet rows info.
*CellsApi* | [**cells_post_cell_calculate**](docs/CellsApi.md#cells_post_cell_calculate) | **POST** /cells/{name}/worksheets/{sheetName}/cells/{cellName}/calculate | Cell calculate formula
*CellsApi* | [**cells_post_cell_characters**](docs/CellsApi.md#cells_post_cell_characters) | **POST** /cells/{name}/worksheets/{sheetName}/cells/{cellName}/characters | Set cell characters 
*CellsApi* | [**cells_post_clear_contents**](docs/CellsApi.md#cells_post_clear_contents) | **POST** /cells/{name}/worksheets/{sheetName}/cells/clearcontents | Clear cells contents.
*CellsApi* | [**cells_post_clear_formats**](docs/CellsApi.md#cells_post_clear_formats) | **POST** /cells/{name}/worksheets/{sheetName}/cells/clearformats | Clear cells contents.
*CellsApi* | [**cells_post_column_style**](docs/CellsApi.md#cells_post_column_style) | **POST** /cells/{name}/worksheets/{sheetName}/cells/columns/{columnIndex}/style | Set column style
*CellsApi* | [**cells_post_copy_cell_into_cell**](docs/CellsApi.md#cells_post_copy_cell_into_cell) | **POST** /cells/{name}/worksheets/{sheetName}/cells/{destCellName}/copy | Copy cell into cell
*CellsApi* | [**cells_post_copy_worksheet_columns**](docs/CellsApi.md#cells_post_copy_worksheet_columns) | **POST** /cells/{name}/worksheets/{sheetName}/cells/columns/copy | Copy worksheet columns.
*CellsApi* | [**cells_post_copy_worksheet_rows**](docs/CellsApi.md#cells_post_copy_worksheet_rows) | **POST** /cells/{name}/worksheets/{sheetName}/cells/rows/copy | Copy worksheet rows.
*CellsApi* | [**cells_post_group_worksheet_columns**](docs/CellsApi.md#cells_post_group_worksheet_columns) | **POST** /cells/{name}/worksheets/{sheetName}/cells/columns/group | Group worksheet columns.
*CellsApi* | [**cells_post_group_worksheet_rows**](docs/CellsApi.md#cells_post_group_worksheet_rows) | **POST** /cells/{name}/worksheets/{sheetName}/cells/rows/group | Group worksheet rows.
*CellsApi* | [**cells_post_hide_worksheet_columns**](docs/CellsApi.md#cells_post_hide_worksheet_columns) | **POST** /cells/{name}/worksheets/{sheetName}/cells/columns/hide | Hide worksheet columns.
*CellsApi* | [**cells_post_hide_worksheet_rows**](docs/CellsApi.md#cells_post_hide_worksheet_rows) | **POST** /cells/{name}/worksheets/{sheetName}/cells/rows/hide | Hide worksheet rows.
*CellsApi* | [**cells_post_row_style**](docs/CellsApi.md#cells_post_row_style) | **POST** /cells/{name}/worksheets/{sheetName}/cells/rows/{rowIndex}/style | Set row style.
*CellsApi* | [**cells_post_set_cell_html_string**](docs/CellsApi.md#cells_post_set_cell_html_string) | **POST** /cells/{name}/worksheets/{sheetName}/cells/{cellName}/htmlstring | Set htmlstring value into cell
*CellsApi* | [**cells_post_set_cell_range_value**](docs/CellsApi.md#cells_post_set_cell_range_value) | **POST** /cells/{name}/worksheets/{sheetName}/cells | Set cell range value 
*CellsApi* | [**cells_post_set_worksheet_column_width**](docs/CellsApi.md#cells_post_set_worksheet_column_width) | **POST** /cells/{name}/worksheets/{sheetName}/cells/columns/{columnIndex} | Set worksheet column width.
*CellsApi* | [**cells_post_ungroup_worksheet_columns**](docs/CellsApi.md#cells_post_ungroup_worksheet_columns) | **POST** /cells/{name}/worksheets/{sheetName}/cells/columns/ungroup | Ungroup worksheet columns.
*CellsApi* | [**cells_post_ungroup_worksheet_rows**](docs/CellsApi.md#cells_post_ungroup_worksheet_rows) | **POST** /cells/{name}/worksheets/{sheetName}/cells/rows/ungroup | Ungroup worksheet rows.
*CellsApi* | [**cells_post_unhide_worksheet_columns**](docs/CellsApi.md#cells_post_unhide_worksheet_columns) | **POST** /cells/{name}/worksheets/{sheetName}/cells/columns/unhide | Unhide worksheet columns.
*CellsApi* | [**cells_post_unhide_worksheet_rows**](docs/CellsApi.md#cells_post_unhide_worksheet_rows) | **POST** /cells/{name}/worksheets/{sheetName}/cells/rows/unhide | Unhide worksheet rows.
*CellsApi* | [**cells_post_update_worksheet_cell_style**](docs/CellsApi.md#cells_post_update_worksheet_cell_style) | **POST** /cells/{name}/worksheets/{sheetName}/cells/{cellName}/style | Update cell&#39;s style.
*CellsApi* | [**cells_post_update_worksheet_range_style**](docs/CellsApi.md#cells_post_update_worksheet_range_style) | **POST** /cells/{name}/worksheets/{sheetName}/cells/style | Update cell&#39;s range style.
*CellsApi* | [**cells_post_update_worksheet_row**](docs/CellsApi.md#cells_post_update_worksheet_row) | **POST** /cells/{name}/worksheets/{sheetName}/cells/rows/{rowIndex} | Update worksheet row.
*CellsApi* | [**cells_post_worksheet_cell_set_value**](docs/CellsApi.md#cells_post_worksheet_cell_set_value) | **POST** /cells/{name}/worksheets/{sheetName}/cells/{cellName} | Set cell value.
*CellsApi* | [**cells_post_worksheet_merge**](docs/CellsApi.md#cells_post_worksheet_merge) | **POST** /cells/{name}/worksheets/{sheetName}/cells/merge | Merge cells.
*CellsApi* | [**cells_post_worksheet_unmerge**](docs/CellsApi.md#cells_post_worksheet_unmerge) | **POST** /cells/{name}/worksheets/{sheetName}/cells/unmerge | Unmerge cells.
*CellsApi* | [**cells_put_insert_worksheet_columns**](docs/CellsApi.md#cells_put_insert_worksheet_columns) | **PUT** /cells/{name}/worksheets/{sheetName}/cells/columns/{columnIndex} | Insert worksheet columns.
*CellsApi* | [**cells_put_insert_worksheet_row**](docs/CellsApi.md#cells_put_insert_worksheet_row) | **PUT** /cells/{name}/worksheets/{sheetName}/cells/rows/{rowIndex} | Insert new worksheet row.
*CellsApi* | [**cells_put_insert_worksheet_rows**](docs/CellsApi.md#cells_put_insert_worksheet_rows) | **PUT** /cells/{name}/worksheets/{sheetName}/cells/rows | Insert several new worksheet rows.
*CellsAutoFilterApi* | [**cells_auto_filter_delete_worksheet_date_filter**](docs/CellsAutoFilterApi.md#cells_auto_filter_delete_worksheet_date_filter) | **DELETE** /cells/{name}/worksheets/{sheetName}/autoFilter/dateFilter | Removes a date filter.             
*CellsAutoFilterApi* | [**cells_auto_filter_delete_worksheet_filter**](docs/CellsAutoFilterApi.md#cells_auto_filter_delete_worksheet_filter) | **DELETE** /cells/{name}/worksheets/{sheetName}/autoFilter/filter | Delete a filter for a filter column.             
*CellsAutoFilterApi* | [**cells_auto_filter_get_worksheet_auto_filter**](docs/CellsAutoFilterApi.md#cells_auto_filter_get_worksheet_auto_filter) | **GET** /cells/{name}/worksheets/{sheetName}/autoFilter | Get Auto filter Description
*CellsAutoFilterApi* | [**cells_auto_filter_post_worksheet_auto_filter_refresh**](docs/CellsAutoFilterApi.md#cells_auto_filter_post_worksheet_auto_filter_refresh) | **POST** /cells/{name}/worksheets/{sheetName}/autoFilter/refresh | 
*CellsAutoFilterApi* | [**cells_auto_filter_post_worksheet_match_blanks**](docs/CellsAutoFilterApi.md#cells_auto_filter_post_worksheet_match_blanks) | **POST** /cells/{name}/worksheets/{sheetName}/autoFilter/matchBlanks | Match all blank cell in the list.
*CellsAutoFilterApi* | [**cells_auto_filter_post_worksheet_match_non_blanks**](docs/CellsAutoFilterApi.md#cells_auto_filter_post_worksheet_match_non_blanks) | **POST** /cells/{name}/worksheets/{sheetName}/autoFilter/matchNonBlanks | Match all not blank cell in the list.             
*CellsAutoFilterApi* | [**cells_auto_filter_put_worksheet_color_filter**](docs/CellsAutoFilterApi.md#cells_auto_filter_put_worksheet_color_filter) | **PUT** /cells/{name}/worksheets/{sheetName}/autoFilter/colorFilter | 
*CellsAutoFilterApi* | [**cells_auto_filter_put_worksheet_custom_filter**](docs/CellsAutoFilterApi.md#cells_auto_filter_put_worksheet_custom_filter) | **PUT** /cells/{name}/worksheets/{sheetName}/autoFilter/custom | Filters a list with a custom criteria.             
*CellsAutoFilterApi* | [**cells_auto_filter_put_worksheet_date_filter**](docs/CellsAutoFilterApi.md#cells_auto_filter_put_worksheet_date_filter) | **PUT** /cells/{name}/worksheets/{sheetName}/autoFilter/dateFilter | add date filter in worksheet 
*CellsAutoFilterApi* | [**cells_auto_filter_put_worksheet_dynamic_filter**](docs/CellsAutoFilterApi.md#cells_auto_filter_put_worksheet_dynamic_filter) | **PUT** /cells/{name}/worksheets/{sheetName}/autoFilter/dynamicFilter | 
*CellsAutoFilterApi* | [**cells_auto_filter_put_worksheet_filter**](docs/CellsAutoFilterApi.md#cells_auto_filter_put_worksheet_filter) | **PUT** /cells/{name}/worksheets/{sheetName}/autoFilter/filter | Adds a filter for a filter column.             
*CellsAutoFilterApi* | [**cells_auto_filter_put_worksheet_filter_top10**](docs/CellsAutoFilterApi.md#cells_auto_filter_put_worksheet_filter_top10) | **PUT** /cells/{name}/worksheets/{sheetName}/autoFilter/filterTop10 | Filter the top 10 item in the list
*CellsAutoFilterApi* | [**cells_auto_filter_put_worksheet_icon_filter**](docs/CellsAutoFilterApi.md#cells_auto_filter_put_worksheet_icon_filter) | **PUT** /cells/{name}/worksheets/{sheetName}/autoFilter/iconFilter | Adds an icon filter.
*CellsAutoshapesApi* | [**cells_autoshapes_get_worksheet_autoshape**](docs/CellsAutoshapesApi.md#cells_autoshapes_get_worksheet_autoshape) | **GET** /cells/{name}/worksheets/{sheetName}/autoshapes/{autoshapeNumber} | Get autoshape info.
*CellsAutoshapesApi* | [**cells_autoshapes_get_worksheet_autoshapes**](docs/CellsAutoshapesApi.md#cells_autoshapes_get_worksheet_autoshapes) | **GET** /cells/{name}/worksheets/{sheetName}/autoshapes | Get worksheet autoshapes info.
*CellsChartAreaApi* | [**cells_chart_area_get_chart_area**](docs/CellsChartAreaApi.md#cells_chart_area_get_chart_area) | **GET** /cells/{name}/worksheets/{sheetName}/charts/{chartIndex}/chartArea | Get chart area info.
*CellsChartAreaApi* | [**cells_chart_area_get_chart_area_border**](docs/CellsChartAreaApi.md#cells_chart_area_get_chart_area_border) | **GET** /cells/{name}/worksheets/{sheetName}/charts/{chartIndex}/chartArea/border | Get chart area border info.
*CellsChartAreaApi* | [**cells_chart_area_get_chart_area_fill_format**](docs/CellsChartAreaApi.md#cells_chart_area_get_chart_area_fill_format) | **GET** /cells/{name}/worksheets/{sheetName}/charts/{chartIndex}/chartArea/fillFormat | Get chart area fill format info.
*CellsChartsApi* | [**cells_charts_delete_worksheet_chart_legend**](docs/CellsChartsApi.md#cells_charts_delete_worksheet_chart_legend) | **DELETE** /cells/{name}/worksheets/{sheetName}/charts/{chartIndex}/legend | Hide legend in chart
*CellsChartsApi* | [**cells_charts_delete_worksheet_chart_title**](docs/CellsChartsApi.md#cells_charts_delete_worksheet_chart_title) | **DELETE** /cells/{name}/worksheets/{sheetName}/charts/{chartIndex}/title | Hide title in chart
*CellsChartsApi* | [**cells_charts_delete_worksheet_clear_charts**](docs/CellsChartsApi.md#cells_charts_delete_worksheet_clear_charts) | **DELETE** /cells/{name}/worksheets/{sheetName}/charts | Clear the charts.
*CellsChartsApi* | [**cells_charts_delete_worksheet_delete_chart**](docs/CellsChartsApi.md#cells_charts_delete_worksheet_delete_chart) | **DELETE** /cells/{name}/worksheets/{sheetName}/charts/{chartIndex} | Delete worksheet chart by index.
*CellsChartsApi* | [**cells_charts_get_worksheet_chart**](docs/CellsChartsApi.md#cells_charts_get_worksheet_chart) | **GET** /cells/{name}/worksheets/{sheetName}/charts/{chartNumber} | Get chart info.
*CellsChartsApi* | [**cells_charts_get_worksheet_chart_legend**](docs/CellsChartsApi.md#cells_charts_get_worksheet_chart_legend) | **GET** /cells/{name}/worksheets/{sheetName}/charts/{chartIndex}/legend | Get chart legend
*CellsChartsApi* | [**cells_charts_get_worksheet_chart_title**](docs/CellsChartsApi.md#cells_charts_get_worksheet_chart_title) | **GET** /cells/{name}/worksheets/{sheetName}/charts/{chartIndex}/title | Get chart title
*CellsChartsApi* | [**cells_charts_get_worksheet_charts**](docs/CellsChartsApi.md#cells_charts_get_worksheet_charts) | **GET** /cells/{name}/worksheets/{sheetName}/charts | Get worksheet charts info.
*CellsChartsApi* | [**cells_charts_post_worksheet_chart**](docs/CellsChartsApi.md#cells_charts_post_worksheet_chart) | **POST** /cells/{name}/worksheets/{sheetName}/charts/{chartIndex} | Update chart propreties
*CellsChartsApi* | [**cells_charts_post_worksheet_chart_legend**](docs/CellsChartsApi.md#cells_charts_post_worksheet_chart_legend) | **POST** /cells/{name}/worksheets/{sheetName}/charts/{chartIndex}/legend | Update chart legend
*CellsChartsApi* | [**cells_charts_post_worksheet_chart_title**](docs/CellsChartsApi.md#cells_charts_post_worksheet_chart_title) | **POST** /cells/{name}/worksheets/{sheetName}/charts/{chartIndex}/title | Update chart title
*CellsChartsApi* | [**cells_charts_put_worksheet_add_chart**](docs/CellsChartsApi.md#cells_charts_put_worksheet_add_chart) | **PUT** /cells/{name}/worksheets/{sheetName}/charts | Add new chart to worksheet.
*CellsChartsApi* | [**cells_charts_put_worksheet_chart_legend**](docs/CellsChartsApi.md#cells_charts_put_worksheet_chart_legend) | **PUT** /cells/{name}/worksheets/{sheetName}/charts/{chartIndex}/legend | Show legend in chart
*CellsChartsApi* | [**cells_charts_put_worksheet_chart_title**](docs/CellsChartsApi.md#cells_charts_put_worksheet_chart_title) | **PUT** /cells/{name}/worksheets/{sheetName}/charts/{chartIndex}/title | Add chart title / Set chart title visible
*CellsConditionalFormattingsApi* | [**cells_conditional_formattings_delete_worksheet_conditional_formatting**](docs/CellsConditionalFormattingsApi.md#cells_conditional_formattings_delete_worksheet_conditional_formatting) | **DELETE** /cells/{name}/worksheets/{sheetName}/conditionalFormattings/{index} | Remove conditional formatting
*CellsConditionalFormattingsApi* | [**cells_conditional_formattings_delete_worksheet_conditional_formatting_area**](docs/CellsConditionalFormattingsApi.md#cells_conditional_formattings_delete_worksheet_conditional_formatting_area) | **DELETE** /cells/{name}/worksheets/{sheetName}/conditionalFormattings/area | Remove cell area from conditional formatting.
*CellsConditionalFormattingsApi* | [**cells_conditional_formattings_delete_worksheet_conditional_formattings**](docs/CellsConditionalFormattingsApi.md#cells_conditional_formattings_delete_worksheet_conditional_formattings) | **DELETE** /cells/{name}/worksheets/{sheetName}/conditionalFormattings | Clear all condition formattings
*CellsConditionalFormattingsApi* | [**cells_conditional_formattings_get_worksheet_conditional_formatting**](docs/CellsConditionalFormattingsApi.md#cells_conditional_formattings_get_worksheet_conditional_formatting) | **GET** /cells/{name}/worksheets/{sheetName}/conditionalFormattings/{index} | Get conditional formatting
*CellsConditionalFormattingsApi* | [**cells_conditional_formattings_get_worksheet_conditional_formattings**](docs/CellsConditionalFormattingsApi.md#cells_conditional_formattings_get_worksheet_conditional_formattings) | **GET** /cells/{name}/worksheets/{sheetName}/conditionalFormattings | Get conditional formattings 
*CellsConditionalFormattingsApi* | [**cells_conditional_formattings_put_worksheet_conditional_formatting**](docs/CellsConditionalFormattingsApi.md#cells_conditional_formattings_put_worksheet_conditional_formatting) | **PUT** /cells/{name}/worksheets/{sheetName}/conditionalFormattings | Add a condition formatting.
*CellsConditionalFormattingsApi* | [**cells_conditional_formattings_put_worksheet_format_condition**](docs/CellsConditionalFormattingsApi.md#cells_conditional_formattings_put_worksheet_format_condition) | **PUT** /cells/{name}/worksheets/{sheetName}/conditionalFormattings/{index} | Add a format condition.
*CellsConditionalFormattingsApi* | [**cells_conditional_formattings_put_worksheet_format_condition_area**](docs/CellsConditionalFormattingsApi.md#cells_conditional_formattings_put_worksheet_format_condition_area) | **PUT** /cells/{name}/worksheets/{sheetName}/conditionalFormattings/{index}/area | add a cell area for format condition             
*CellsConditionalFormattingsApi* | [**cells_conditional_formattings_put_worksheet_format_condition_condition**](docs/CellsConditionalFormattingsApi.md#cells_conditional_formattings_put_worksheet_format_condition_condition) | **PUT** /cells/{name}/worksheets/{sheetName}/conditionalFormattings/{index}/condition | Add a condition for format condition.
*CellsHypelinksApi* | [**cells_hypelinks_delete_worksheet_hyperlink**](docs/CellsHypelinksApi.md#cells_hypelinks_delete_worksheet_hyperlink) | **DELETE** /cells/{name}/worksheets/{sheetName}/hyperlinks/{hyperlinkIndex} | Delete worksheet hyperlink by index.
*CellsHypelinksApi* | [**cells_hypelinks_delete_worksheet_hyperlinks**](docs/CellsHypelinksApi.md#cells_hypelinks_delete_worksheet_hyperlinks) | **DELETE** /cells/{name}/worksheets/{sheetName}/hyperlinks | Delete all hyperlinks in worksheet.
*CellsHypelinksApi* | [**cells_hypelinks_get_worksheet_hyperlink**](docs/CellsHypelinksApi.md#cells_hypelinks_get_worksheet_hyperlink) | **GET** /cells/{name}/worksheets/{sheetName}/hyperlinks/{hyperlinkIndex} | Get worksheet hyperlink by index.
*CellsHypelinksApi* | [**cells_hypelinks_get_worksheet_hyperlinks**](docs/CellsHypelinksApi.md#cells_hypelinks_get_worksheet_hyperlinks) | **GET** /cells/{name}/worksheets/{sheetName}/hyperlinks | Get worksheet hyperlinks.
*CellsHypelinksApi* | [**cells_hypelinks_post_worksheet_hyperlink**](docs/CellsHypelinksApi.md#cells_hypelinks_post_worksheet_hyperlink) | **POST** /cells/{name}/worksheets/{sheetName}/hyperlinks/{hyperlinkIndex} | Update worksheet hyperlink by index.
*CellsHypelinksApi* | [**cells_hypelinks_put_worksheet_hyperlink**](docs/CellsHypelinksApi.md#cells_hypelinks_put_worksheet_hyperlink) | **PUT** /cells/{name}/worksheets/{sheetName}/hyperlinks | Add worksheet hyperlink.
*CellsListObjectsApi* | [**cells_list_objects_delete_worksheet_list_object**](docs/CellsListObjectsApi.md#cells_list_objects_delete_worksheet_list_object) | **DELETE** /cells/{name}/worksheets/{sheetName}/listobjects/{listObjectIndex} | Delete worksheet list object by index
*CellsListObjectsApi* | [**cells_list_objects_delete_worksheet_list_objects**](docs/CellsListObjectsApi.md#cells_list_objects_delete_worksheet_list_objects) | **DELETE** /cells/{name}/worksheets/{sheetName}/listobjects | Delete worksheet list objects
*CellsListObjectsApi* | [**cells_list_objects_get_worksheet_list_object**](docs/CellsListObjectsApi.md#cells_list_objects_get_worksheet_list_object) | **GET** /cells/{name}/worksheets/{sheetName}/listobjects/{listobjectindex} | Get worksheet list object info by index.
*CellsListObjectsApi* | [**cells_list_objects_get_worksheet_list_objects**](docs/CellsListObjectsApi.md#cells_list_objects_get_worksheet_list_objects) | **GET** /cells/{name}/worksheets/{sheetName}/listobjects | Get worksheet listobjects info.
*CellsListObjectsApi* | [**cells_list_objects_post_worksheet_list_object**](docs/CellsListObjectsApi.md#cells_list_objects_post_worksheet_list_object) | **POST** /cells/{name}/worksheets/{sheetName}/listobjects/{listObjectIndex} | Update  list object 
*CellsListObjectsApi* | [**cells_list_objects_post_worksheet_list_object_convert_to_range**](docs/CellsListObjectsApi.md#cells_list_objects_post_worksheet_list_object_convert_to_range) | **POST** /cells/{name}/worksheets/{sheetName}/listobjects/{listObjectIndex}/ConvertToRange | 
*CellsListObjectsApi* | [**cells_list_objects_post_worksheet_list_object_sort_table**](docs/CellsListObjectsApi.md#cells_list_objects_post_worksheet_list_object_sort_table) | **POST** /cells/{name}/worksheets/{sheetName}/listobjects/{listObjectIndex}/sort | 
*CellsListObjectsApi* | [**cells_list_objects_post_worksheet_list_object_summarize_with_pivot_table**](docs/CellsListObjectsApi.md#cells_list_objects_post_worksheet_list_object_summarize_with_pivot_table) | **POST** /cells/{name}/worksheets/{sheetName}/listobjects/{listObjectIndex}/SummarizeWithPivotTable | 
*CellsListObjectsApi* | [**cells_list_objects_put_worksheet_list_object**](docs/CellsListObjectsApi.md#cells_list_objects_put_worksheet_list_object) | **PUT** /cells/{name}/worksheets/{sheetName}/listobjects | Add a list object into worksheet.
*CellsOleObjectsApi* | [**cells_ole_objects_delete_worksheet_ole_object**](docs/CellsOleObjectsApi.md#cells_ole_objects_delete_worksheet_ole_object) | **DELETE** /cells/{name}/worksheets/{sheetName}/oleobjects/{oleObjectIndex} | Delete OLE object.
*CellsOleObjectsApi* | [**cells_ole_objects_delete_worksheet_ole_objects**](docs/CellsOleObjectsApi.md#cells_ole_objects_delete_worksheet_ole_objects) | **DELETE** /cells/{name}/worksheets/{sheetName}/oleobjects | Delete all OLE objects.
*CellsOleObjectsApi* | [**cells_ole_objects_get_worksheet_ole_object**](docs/CellsOleObjectsApi.md#cells_ole_objects_get_worksheet_ole_object) | **GET** /cells/{name}/worksheets/{sheetName}/oleobjects/{objectNumber} | Get OLE object info.
*CellsOleObjectsApi* | [**cells_ole_objects_get_worksheet_ole_objects**](docs/CellsOleObjectsApi.md#cells_ole_objects_get_worksheet_ole_objects) | **GET** /cells/{name}/worksheets/{sheetName}/oleobjects | Get worksheet OLE objects info.
*CellsOleObjectsApi* | [**cells_ole_objects_post_update_worksheet_ole_object**](docs/CellsOleObjectsApi.md#cells_ole_objects_post_update_worksheet_ole_object) | **POST** /cells/{name}/worksheets/{sheetName}/oleobjects/{oleObjectIndex} | Update OLE object.
*CellsOleObjectsApi* | [**cells_ole_objects_put_worksheet_ole_object**](docs/CellsOleObjectsApi.md#cells_ole_objects_put_worksheet_ole_object) | **PUT** /cells/{name}/worksheets/{sheetName}/oleobjects | Add OLE object
*CellsPageBreaksApi* | [**cells_page_breaks_delete_horizontal_page_break**](docs/CellsPageBreaksApi.md#cells_page_breaks_delete_horizontal_page_break) | **DELETE** /cells/{name}/worksheets/{sheetName}/horizontalpagebreaks/{index} | 
*CellsPageBreaksApi* | [**cells_page_breaks_delete_horizontal_page_breaks**](docs/CellsPageBreaksApi.md#cells_page_breaks_delete_horizontal_page_breaks) | **DELETE** /cells/{name}/worksheets/{sheetName}/horizontalpagebreaks | 
*CellsPageBreaksApi* | [**cells_page_breaks_delete_vertical_page_break**](docs/CellsPageBreaksApi.md#cells_page_breaks_delete_vertical_page_break) | **DELETE** /cells/{name}/worksheets/{sheetName}/verticalpagebreaks/{index} | 
*CellsPageBreaksApi* | [**cells_page_breaks_delete_vertical_page_breaks**](docs/CellsPageBreaksApi.md#cells_page_breaks_delete_vertical_page_breaks) | **DELETE** /cells/{name}/worksheets/{sheetName}/verticalpagebreaks | 
*CellsPageBreaksApi* | [**cells_page_breaks_get_horizontal_page_break**](docs/CellsPageBreaksApi.md#cells_page_breaks_get_horizontal_page_break) | **GET** /cells/{name}/worksheets/{sheetName}/horizontalpagebreaks/{index} | 
*CellsPageBreaksApi* | [**cells_page_breaks_get_horizontal_page_breaks**](docs/CellsPageBreaksApi.md#cells_page_breaks_get_horizontal_page_breaks) | **GET** /cells/{name}/worksheets/{sheetName}/horizontalpagebreaks | 
*CellsPageBreaksApi* | [**cells_page_breaks_get_vertical_page_break**](docs/CellsPageBreaksApi.md#cells_page_breaks_get_vertical_page_break) | **GET** /cells/{name}/worksheets/{sheetName}/verticalpagebreaks/{index} | 
*CellsPageBreaksApi* | [**cells_page_breaks_get_vertical_page_breaks**](docs/CellsPageBreaksApi.md#cells_page_breaks_get_vertical_page_breaks) | **GET** /cells/{name}/worksheets/{sheetName}/verticalpagebreaks | 
*CellsPageBreaksApi* | [**cells_page_breaks_put_horizontal_page_break**](docs/CellsPageBreaksApi.md#cells_page_breaks_put_horizontal_page_break) | **PUT** /cells/{name}/worksheets/{sheetName}/horizontalpagebreaks | 
*CellsPageBreaksApi* | [**cells_page_breaks_put_vertical_page_break**](docs/CellsPageBreaksApi.md#cells_page_breaks_put_vertical_page_break) | **PUT** /cells/{name}/worksheets/{sheetName}/verticalpagebreaks | 
*CellsPageSetupApi* | [**cells_page_setup_delete_header_footer**](docs/CellsPageSetupApi.md#cells_page_setup_delete_header_footer) | **DELETE** /cells/{name}/worksheets/{sheetName}/pagesetup/clearheaderfooter | clear header footer
*CellsPageSetupApi* | [**cells_page_setup_get_footer**](docs/CellsPageSetupApi.md#cells_page_setup_get_footer) | **GET** /cells/{name}/worksheets/{sheetName}/pagesetup/footer | get page footer information
*CellsPageSetupApi* | [**cells_page_setup_get_header**](docs/CellsPageSetupApi.md#cells_page_setup_get_header) | **GET** /cells/{name}/worksheets/{sheetName}/pagesetup/header | get page header information
*CellsPageSetupApi* | [**cells_page_setup_get_page_setup**](docs/CellsPageSetupApi.md#cells_page_setup_get_page_setup) | **GET** /cells/{name}/worksheets/{sheetName}/pagesetup | Get Page Setup information.             
*CellsPageSetupApi* | [**cells_page_setup_post_footer**](docs/CellsPageSetupApi.md#cells_page_setup_post_footer) | **POST** /cells/{name}/worksheets/{sheetName}/pagesetup/footer | update  page footer information 
*CellsPageSetupApi* | [**cells_page_setup_post_header**](docs/CellsPageSetupApi.md#cells_page_setup_post_header) | **POST** /cells/{name}/worksheets/{sheetName}/pagesetup/header | update  page header information 
*CellsPageSetupApi* | [**cells_page_setup_post_page_setup**](docs/CellsPageSetupApi.md#cells_page_setup_post_page_setup) | **POST** /cells/{name}/worksheets/{sheetName}/pagesetup | Update Page Setup information.
*CellsPicturesApi* | [**cells_pictures_delete_worksheet_picture**](docs/CellsPicturesApi.md#cells_pictures_delete_worksheet_picture) | **DELETE** /cells/{name}/worksheets/{sheetName}/pictures/{pictureIndex} | Delete a picture object in worksheet
*CellsPicturesApi* | [**cells_pictures_delete_worksheet_pictures**](docs/CellsPicturesApi.md#cells_pictures_delete_worksheet_pictures) | **DELETE** /cells/{name}/worksheets/{sheetName}/pictures | Delete all pictures in worksheet.
*CellsPicturesApi* | [**cells_pictures_get_worksheet_picture**](docs/CellsPicturesApi.md#cells_pictures_get_worksheet_picture) | **GET** /cells/{name}/worksheets/{sheetName}/pictures/{pictureNumber} | GRead worksheet picture by number.
*CellsPicturesApi* | [**cells_pictures_get_worksheet_pictures**](docs/CellsPicturesApi.md#cells_pictures_get_worksheet_pictures) | **GET** /cells/{name}/worksheets/{sheetName}/pictures | Read worksheet pictures.
*CellsPicturesApi* | [**cells_pictures_post_worksheet_picture**](docs/CellsPicturesApi.md#cells_pictures_post_worksheet_picture) | **POST** /cells/{name}/worksheets/{sheetName}/pictures/{pictureIndex} | Update worksheet picture by index.
*CellsPicturesApi* | [**cells_pictures_put_worksheet_add_picture**](docs/CellsPicturesApi.md#cells_pictures_put_worksheet_add_picture) | **PUT** /cells/{name}/worksheets/{sheetName}/pictures | Add a new worksheet picture.
*CellsPivotTablesApi* | [**cells_pivot_tables_delete_pivot_table_field**](docs/CellsPivotTablesApi.md#cells_pivot_tables_delete_pivot_table_field) | **DELETE** /cells/{name}/worksheets/{sheetName}/pivottables/{pivotTableIndex}/PivotField | Delete pivot field into into pivot table
*CellsPivotTablesApi* | [**cells_pivot_tables_delete_worksheet_pivot_table**](docs/CellsPivotTablesApi.md#cells_pivot_tables_delete_worksheet_pivot_table) | **DELETE** /cells/{name}/worksheets/{sheetName}/pivottables/{pivotTableIndex} | Delete worksheet pivot table by index
*CellsPivotTablesApi* | [**cells_pivot_tables_delete_worksheet_pivot_table_filter**](docs/CellsPivotTablesApi.md#cells_pivot_tables_delete_worksheet_pivot_table_filter) | **DELETE** /cells/{name}/worksheets/{sheetName}/pivottables/{pivotTableIndex}/PivotFilters/{fieldIndex} | delete  pivot filter for piovt table             
*CellsPivotTablesApi* | [**cells_pivot_tables_delete_worksheet_pivot_table_filters**](docs/CellsPivotTablesApi.md#cells_pivot_tables_delete_worksheet_pivot_table_filters) | **DELETE** /cells/{name}/worksheets/{sheetName}/pivottables/{pivotTableIndex}/PivotFilters | delete all pivot filters for piovt table
*CellsPivotTablesApi* | [**cells_pivot_tables_delete_worksheet_pivot_tables**](docs/CellsPivotTablesApi.md#cells_pivot_tables_delete_worksheet_pivot_tables) | **DELETE** /cells/{name}/worksheets/{sheetName}/pivottables | Delete worksheet pivot tables
*CellsPivotTablesApi* | [**cells_pivot_tables_get_pivot_table_field**](docs/CellsPivotTablesApi.md#cells_pivot_tables_get_pivot_table_field) | **GET** /cells/{name}/worksheets/{sheetName}/pivottables/{pivotTableIndex}/PivotField | Get pivot field into into pivot table
*CellsPivotTablesApi* | [**cells_pivot_tables_get_worksheet_pivot_table**](docs/CellsPivotTablesApi.md#cells_pivot_tables_get_worksheet_pivot_table) | **GET** /cells/{name}/worksheets/{sheetName}/pivottables/{pivottableIndex} | Get worksheet pivottable info by index.
*CellsPivotTablesApi* | [**cells_pivot_tables_get_worksheet_pivot_table_filter**](docs/CellsPivotTablesApi.md#cells_pivot_tables_get_worksheet_pivot_table_filter) | **GET** /cells/{name}/worksheets/{sheetName}/pivottables/{pivotTableIndex}/PivotFilters/{filterIndex} | 
*CellsPivotTablesApi* | [**cells_pivot_tables_get_worksheet_pivot_table_filters**](docs/CellsPivotTablesApi.md#cells_pivot_tables_get_worksheet_pivot_table_filters) | **GET** /cells/{name}/worksheets/{sheetName}/pivottables/{pivotTableIndex}/PivotFilters | 
*CellsPivotTablesApi* | [**cells_pivot_tables_get_worksheet_pivot_tables**](docs/CellsPivotTablesApi.md#cells_pivot_tables_get_worksheet_pivot_tables) | **GET** /cells/{name}/worksheets/{sheetName}/pivottables | Get worksheet pivottables info.
*CellsPivotTablesApi* | [**cells_pivot_tables_post_pivot_table_cell_style**](docs/CellsPivotTablesApi.md#cells_pivot_tables_post_pivot_table_cell_style) | **POST** /cells/{name}/worksheets/{sheetName}/pivottables/{pivotTableIndex}/Format | Update cell style for pivot table
*CellsPivotTablesApi* | [**cells_pivot_tables_post_pivot_table_field_hide_item**](docs/CellsPivotTablesApi.md#cells_pivot_tables_post_pivot_table_field_hide_item) | **POST** /cells/{name}/worksheets/{sheetName}/pivottables/{pivotTableIndex}/PivotField/Hide | 
*CellsPivotTablesApi* | [**cells_pivot_tables_post_pivot_table_field_move_to**](docs/CellsPivotTablesApi.md#cells_pivot_tables_post_pivot_table_field_move_to) | **POST** /cells/{name}/worksheets/{sheetName}/pivottables/{pivotTableIndex}/PivotField/Move | 
*CellsPivotTablesApi* | [**cells_pivot_tables_post_pivot_table_style**](docs/CellsPivotTablesApi.md#cells_pivot_tables_post_pivot_table_style) | **POST** /cells/{name}/worksheets/{sheetName}/pivottables/{pivotTableIndex}/FormatAll | Update style for pivot table
*CellsPivotTablesApi* | [**cells_pivot_tables_post_worksheet_pivot_table_calculate**](docs/CellsPivotTablesApi.md#cells_pivot_tables_post_worksheet_pivot_table_calculate) | **POST** /cells/{name}/worksheets/{sheetName}/pivottables/{pivotTableIndex}/Calculate | Calculates pivottable&#39;s data to cells.
*CellsPivotTablesApi* | [**cells_pivot_tables_post_worksheet_pivot_table_move**](docs/CellsPivotTablesApi.md#cells_pivot_tables_post_worksheet_pivot_table_move) | **POST** /cells/{name}/worksheets/{sheetName}/pivottables/{pivotTableIndex}/Move | 
*CellsPivotTablesApi* | [**cells_pivot_tables_put_pivot_table_field**](docs/CellsPivotTablesApi.md#cells_pivot_tables_put_pivot_table_field) | **PUT** /cells/{name}/worksheets/{sheetName}/pivottables/{pivotTableIndex}/PivotField | Add pivot field into into pivot table
*CellsPivotTablesApi* | [**cells_pivot_tables_put_worksheet_pivot_table**](docs/CellsPivotTablesApi.md#cells_pivot_tables_put_worksheet_pivot_table) | **PUT** /cells/{name}/worksheets/{sheetName}/pivottables | Add a pivot table into worksheet.
*CellsPivotTablesApi* | [**cells_pivot_tables_put_worksheet_pivot_table_filter**](docs/CellsPivotTablesApi.md#cells_pivot_tables_put_worksheet_pivot_table_filter) | **PUT** /cells/{name}/worksheets/{sheetName}/pivottables/{pivotTableIndex}/PivotFilters | Add pivot filter for piovt table index
*CellsPropertiesApi* | [**cells_properties_delete_document_properties**](docs/CellsPropertiesApi.md#cells_properties_delete_document_properties) | **DELETE** /cells/{name}/documentproperties | Delete all custom document properties and clean built-in ones.
*CellsPropertiesApi* | [**cells_properties_delete_document_property**](docs/CellsPropertiesApi.md#cells_properties_delete_document_property) | **DELETE** /cells/{name}/documentproperties/{propertyName} | Delete document property.
*CellsPropertiesApi* | [**cells_properties_get_document_properties**](docs/CellsPropertiesApi.md#cells_properties_get_document_properties) | **GET** /cells/{name}/documentproperties | Read document properties.
*CellsPropertiesApi* | [**cells_properties_get_document_property**](docs/CellsPropertiesApi.md#cells_properties_get_document_property) | **GET** /cells/{name}/documentproperties/{propertyName} | Read document property by name.
*CellsPropertiesApi* | [**cells_properties_put_document_property**](docs/CellsPropertiesApi.md#cells_properties_put_document_property) | **PUT** /cells/{name}/documentproperties/{propertyName} | Set/create document property.
*CellsRangesApi* | [**cells_ranges_get_worksheet_cells_range_value**](docs/CellsRangesApi.md#cells_ranges_get_worksheet_cells_range_value) | **GET** /cells/{name}/worksheets/{sheetName}/ranges/value | Get cells list in a range by range name or row column indexes  
*CellsRangesApi* | [**cells_ranges_post_worksheet_cells_range_column_width**](docs/CellsRangesApi.md#cells_ranges_post_worksheet_cells_range_column_width) | **POST** /cells/{name}/worksheets/{sheetName}/ranges/columnWidth | Set column width of range
*CellsRangesApi* | [**cells_ranges_post_worksheet_cells_range_merge**](docs/CellsRangesApi.md#cells_ranges_post_worksheet_cells_range_merge) | **POST** /cells/{name}/worksheets/{sheetName}/ranges/merge | Combines a range of cells into a single cell.              
*CellsRangesApi* | [**cells_ranges_post_worksheet_cells_range_move_to**](docs/CellsRangesApi.md#cells_ranges_post_worksheet_cells_range_move_to) | **POST** /cells/{name}/worksheets/{sheetName}/ranges/moveto | Move the current range to the dest range.             
*CellsRangesApi* | [**cells_ranges_post_worksheet_cells_range_outline_border**](docs/CellsRangesApi.md#cells_ranges_post_worksheet_cells_range_outline_border) | **POST** /cells/{name}/worksheets/{sheetName}/ranges/outlineBorder | Sets outline border around a range of cells.
*CellsRangesApi* | [**cells_ranges_post_worksheet_cells_range_row_height**](docs/CellsRangesApi.md#cells_ranges_post_worksheet_cells_range_row_height) | **POST** /cells/{name}/worksheets/{sheetName}/ranges/rowHeight | set row height of range
*CellsRangesApi* | [**cells_ranges_post_worksheet_cells_range_style**](docs/CellsRangesApi.md#cells_ranges_post_worksheet_cells_range_style) | **POST** /cells/{name}/worksheets/{sheetName}/ranges/style | Sets the style of the range.             
*CellsRangesApi* | [**cells_ranges_post_worksheet_cells_range_unmerge**](docs/CellsRangesApi.md#cells_ranges_post_worksheet_cells_range_unmerge) | **POST** /cells/{name}/worksheets/{sheetName}/ranges/unmerge | Unmerges merged cells of this range.             
*CellsRangesApi* | [**cells_ranges_post_worksheet_cells_range_value**](docs/CellsRangesApi.md#cells_ranges_post_worksheet_cells_range_value) | **POST** /cells/{name}/worksheets/{sheetName}/ranges/value | Puts a value into the range, if appropriate the value will be converted to other data type and cell&#39;s number format will be reset.             
*CellsRangesApi* | [**cells_ranges_post_worksheet_cells_ranges**](docs/CellsRangesApi.md#cells_ranges_post_worksheet_cells_ranges) | **POST** /cells/{name}/worksheets/{sheetName}/ranges | copy range in the worksheet
*CellsSaveAsApi* | [**cells_save_as_post_document_save_as**](docs/CellsSaveAsApi.md#cells_save_as_post_document_save_as) | **POST** /cells/{name}/SaveAs | Convert document and save result to storage.
*CellsShapesApi* | [**cells_shapes_delete_worksheet_shape**](docs/CellsShapesApi.md#cells_shapes_delete_worksheet_shape) | **DELETE** /cells/{name}/worksheets/{sheetName}/shapes/{shapeindex} | Delete a shape in worksheet
*CellsShapesApi* | [**cells_shapes_delete_worksheet_shapes**](docs/CellsShapesApi.md#cells_shapes_delete_worksheet_shapes) | **DELETE** /cells/{name}/worksheets/{sheetName}/shapes | delete all shapes in worksheet
*CellsShapesApi* | [**cells_shapes_get_worksheet_shape**](docs/CellsShapesApi.md#cells_shapes_get_worksheet_shape) | **GET** /cells/{name}/worksheets/{sheetName}/shapes/{shapeindex} | Get worksheet shape
*CellsShapesApi* | [**cells_shapes_get_worksheet_shapes**](docs/CellsShapesApi.md#cells_shapes_get_worksheet_shapes) | **GET** /cells/{name}/worksheets/{sheetName}/shapes | Get worksheet shapes 
*CellsShapesApi* | [**cells_shapes_post_worksheet_shape**](docs/CellsShapesApi.md#cells_shapes_post_worksheet_shape) | **POST** /cells/{name}/worksheets/{sheetName}/shapes/{shapeindex} | Update a shape in worksheet
*CellsShapesApi* | [**cells_shapes_put_worksheet_shape**](docs/CellsShapesApi.md#cells_shapes_put_worksheet_shape) | **PUT** /cells/{name}/worksheets/{sheetName}/shapes | Add shape in worksheet
*CellsTaskApi* | [**cells_task_post_run_task**](docs/CellsTaskApi.md#cells_task_post_run_task) | **POST** /cells/task/runtask | Run tasks  
*CellsWorkbookApi* | [**cells_workbook_delete_decrypt_document**](docs/CellsWorkbookApi.md#cells_workbook_delete_decrypt_document) | **DELETE** /cells/{name}/encryption | Decrypt document.
*CellsWorkbookApi* | [**cells_workbook_delete_document_unprotect_from_changes**](docs/CellsWorkbookApi.md#cells_workbook_delete_document_unprotect_from_changes) | **DELETE** /cells/{name}/writeProtection | Unprotect document from changes.
*CellsWorkbookApi* | [**cells_workbook_delete_unprotect_document**](docs/CellsWorkbookApi.md#cells_workbook_delete_unprotect_document) | **DELETE** /cells/{name}/protection | Unprotect document.
*CellsWorkbookApi* | [**cells_workbook_delete_workbook_name**](docs/CellsWorkbookApi.md#cells_workbook_delete_workbook_name) | **DELETE** /cells/{name}/names/{nameName} | Clean workbook&#39;s names.
*CellsWorkbookApi* | [**cells_workbook_delete_workbook_names**](docs/CellsWorkbookApi.md#cells_workbook_delete_workbook_names) | **DELETE** /cells/{name}/names | Clean workbook&#39;s names.
*CellsWorkbookApi* | [**cells_workbook_get_workbook**](docs/CellsWorkbookApi.md#cells_workbook_get_workbook) | **GET** /cells/{name} | Read workbook info or export.
*CellsWorkbookApi* | [**cells_workbook_get_workbook_default_style**](docs/CellsWorkbookApi.md#cells_workbook_get_workbook_default_style) | **GET** /cells/{name}/defaultstyle | Read workbook default style info.
*CellsWorkbookApi* | [**cells_workbook_get_workbook_name**](docs/CellsWorkbookApi.md#cells_workbook_get_workbook_name) | **GET** /cells/{name}/names/{nameName} | Read workbook&#39;s name.
*CellsWorkbookApi* | [**cells_workbook_get_workbook_name_value**](docs/CellsWorkbookApi.md#cells_workbook_get_workbook_name_value) | **GET** /cells/{name}/names/{nameName}/value | Get workbook&#39;s name value.
*CellsWorkbookApi* | [**cells_workbook_get_workbook_names**](docs/CellsWorkbookApi.md#cells_workbook_get_workbook_names) | **GET** /cells/{name}/names | Read workbook&#39;s names.
*CellsWorkbookApi* | [**cells_workbook_get_workbook_settings**](docs/CellsWorkbookApi.md#cells_workbook_get_workbook_settings) | **GET** /cells/{name}/settings | Get Workbook Settings DTO
*CellsWorkbookApi* | [**cells_workbook_get_workbook_text_items**](docs/CellsWorkbookApi.md#cells_workbook_get_workbook_text_items) | **GET** /cells/{name}/textItems | Read workbook&#39;s text items.
*CellsWorkbookApi* | [**cells_workbook_post_autofit_workbook_rows**](docs/CellsWorkbookApi.md#cells_workbook_post_autofit_workbook_rows) | **POST** /cells/{name}/autofitrows | Autofit workbook rows.
*CellsWorkbookApi* | [**cells_workbook_post_encrypt_document**](docs/CellsWorkbookApi.md#cells_workbook_post_encrypt_document) | **POST** /cells/{name}/encryption | Encript document.
*CellsWorkbookApi* | [**cells_workbook_post_import_data**](docs/CellsWorkbookApi.md#cells_workbook_post_import_data) | **POST** /cells/{name}/importdata | 
*CellsWorkbookApi* | [**cells_workbook_post_protect_document**](docs/CellsWorkbookApi.md#cells_workbook_post_protect_document) | **POST** /cells/{name}/protection | Protect document.
*CellsWorkbookApi* | [**cells_workbook_post_workbook_calculate_formula**](docs/CellsWorkbookApi.md#cells_workbook_post_workbook_calculate_formula) | **POST** /cells/{name}/calculateformula | Calculate all formulas in workbook.
*CellsWorkbookApi* | [**cells_workbook_post_workbook_get_smart_marker_result**](docs/CellsWorkbookApi.md#cells_workbook_post_workbook_get_smart_marker_result) | **POST** /cells/{name}/smartmarker | Smart marker processing result.
*CellsWorkbookApi* | [**cells_workbook_post_workbook_settings**](docs/CellsWorkbookApi.md#cells_workbook_post_workbook_settings) | **POST** /cells/{name}/settings | Update Workbook setting 
*CellsWorkbookApi* | [**cells_workbook_post_workbook_split**](docs/CellsWorkbookApi.md#cells_workbook_post_workbook_split) | **POST** /cells/{name}/split | Split workbook.
*CellsWorkbookApi* | [**cells_workbook_post_workbooks_merge**](docs/CellsWorkbookApi.md#cells_workbook_post_workbooks_merge) | **POST** /cells/{name}/merge | Merge workbooks.
*CellsWorkbookApi* | [**cells_workbook_post_workbooks_text_replace**](docs/CellsWorkbookApi.md#cells_workbook_post_workbooks_text_replace) | **POST** /cells/{name}/replaceText | Replace text.
*CellsWorkbookApi* | [**cells_workbook_post_workbooks_text_search**](docs/CellsWorkbookApi.md#cells_workbook_post_workbooks_text_search) | **POST** /cells/{name}/findText | Search text.
*CellsWorkbookApi* | [**cells_workbook_put_convert_workbook**](docs/CellsWorkbookApi.md#cells_workbook_put_convert_workbook) | **PUT** /cells/convert | Convert workbook from request content to some format.
*CellsWorkbookApi* | [**cells_workbook_put_document_protect_from_changes**](docs/CellsWorkbookApi.md#cells_workbook_put_document_protect_from_changes) | **PUT** /cells/{name}/writeProtection | Protect document from changes.
*CellsWorkbookApi* | [**cells_workbook_put_workbook_create**](docs/CellsWorkbookApi.md#cells_workbook_put_workbook_create) | **PUT** /cells/{name} | Create new workbook using deferent methods.
*CellsWorksheetValidationsApi* | [**cells_worksheet_validations_delete_worksheet_validation**](docs/CellsWorksheetValidationsApi.md#cells_worksheet_validations_delete_worksheet_validation) | **DELETE** /cells/{name}/worksheets/{sheetName}/validations/{validationIndex} | Delete worksheet validation by index.
*CellsWorksheetValidationsApi* | [**cells_worksheet_validations_get_worksheet_validation**](docs/CellsWorksheetValidationsApi.md#cells_worksheet_validations_get_worksheet_validation) | **GET** /cells/{name}/worksheets/{sheetName}/validations/{validationIndex} | Get worksheet validation by index.
*CellsWorksheetValidationsApi* | [**cells_worksheet_validations_get_worksheet_validations**](docs/CellsWorksheetValidationsApi.md#cells_worksheet_validations_get_worksheet_validations) | **GET** /cells/{name}/worksheets/{sheetName}/validations | Get worksheet validations.
*CellsWorksheetValidationsApi* | [**cells_worksheet_validations_post_worksheet_validation**](docs/CellsWorksheetValidationsApi.md#cells_worksheet_validations_post_worksheet_validation) | **POST** /cells/{name}/worksheets/{sheetName}/validations/{validationIndex} | Update worksheet validation by index.
*CellsWorksheetValidationsApi* | [**cells_worksheet_validations_put_worksheet_validation**](docs/CellsWorksheetValidationsApi.md#cells_worksheet_validations_put_worksheet_validation) | **PUT** /cells/{name}/worksheets/{sheetName}/validations | Add worksheet validation at index.
*CellsWorksheetsApi* | [**cells_worksheets_delete_unprotect_worksheet**](docs/CellsWorksheetsApi.md#cells_worksheets_delete_unprotect_worksheet) | **DELETE** /cells/{name}/worksheets/{sheetName}/protection | Unprotect worksheet.
*CellsWorksheetsApi* | [**cells_worksheets_delete_worksheet**](docs/CellsWorksheetsApi.md#cells_worksheets_delete_worksheet) | **DELETE** /cells/{name}/worksheets/{sheetName} | Delete worksheet.
*CellsWorksheetsApi* | [**cells_worksheets_delete_worksheet_background**](docs/CellsWorksheetsApi.md#cells_worksheets_delete_worksheet_background) | **DELETE** /cells/{name}/worksheets/{sheetName}/background | Set worksheet background image.
*CellsWorksheetsApi* | [**cells_worksheets_delete_worksheet_comment**](docs/CellsWorksheetsApi.md#cells_worksheets_delete_worksheet_comment) | **DELETE** /cells/{name}/worksheets/{sheetName}/comments/{cellName} | Delete worksheet&#39;s cell comment.
*CellsWorksheetsApi* | [**cells_worksheets_delete_worksheet_comments**](docs/CellsWorksheetsApi.md#cells_worksheets_delete_worksheet_comments) | **DELETE** /cells/{name}/worksheets/{sheetName}/comments | Delete all comments for worksheet.
*CellsWorksheetsApi* | [**cells_worksheets_delete_worksheet_freeze_panes**](docs/CellsWorksheetsApi.md#cells_worksheets_delete_worksheet_freeze_panes) | **DELETE** /cells/{name}/worksheets/{sheetName}/freezepanes | Unfreeze panes
*CellsWorksheetsApi* | [**cells_worksheets_get_named_ranges**](docs/CellsWorksheetsApi.md#cells_worksheets_get_named_ranges) | **GET** /cells/{name}/worksheets/ranges | Read worksheets ranges info.
*CellsWorksheetsApi* | [**cells_worksheets_get_worksheet**](docs/CellsWorksheetsApi.md#cells_worksheets_get_worksheet) | **GET** /cells/{name}/worksheets/{sheetName} | Read worksheet info or export.
*CellsWorksheetsApi* | [**cells_worksheets_get_worksheet_calculate_formula**](docs/CellsWorksheetsApi.md#cells_worksheets_get_worksheet_calculate_formula) | **GET** /cells/{name}/worksheets/{sheetName}/formulaResult | Calculate formula value.
*CellsWorksheetsApi* | [**cells_worksheets_get_worksheet_comment**](docs/CellsWorksheetsApi.md#cells_worksheets_get_worksheet_comment) | **GET** /cells/{name}/worksheets/{sheetName}/comments/{cellName} | Get worksheet comment by cell name.
*CellsWorksheetsApi* | [**cells_worksheets_get_worksheet_comments**](docs/CellsWorksheetsApi.md#cells_worksheets_get_worksheet_comments) | **GET** /cells/{name}/worksheets/{sheetName}/comments | Get worksheet comments.
*CellsWorksheetsApi* | [**cells_worksheets_get_worksheet_merged_cell**](docs/CellsWorksheetsApi.md#cells_worksheets_get_worksheet_merged_cell) | **GET** /cells/{name}/worksheets/{sheetName}/mergedCells/{mergedCellIndex} | Get worksheet merged cell by its index.
*CellsWorksheetsApi* | [**cells_worksheets_get_worksheet_merged_cells**](docs/CellsWorksheetsApi.md#cells_worksheets_get_worksheet_merged_cells) | **GET** /cells/{name}/worksheets/{sheetName}/mergedCells | Get worksheet merged cells.
*CellsWorksheetsApi* | [**cells_worksheets_get_worksheet_text_items**](docs/CellsWorksheetsApi.md#cells_worksheets_get_worksheet_text_items) | **GET** /cells/{name}/worksheets/{sheetName}/textItems | Get worksheet text items.
*CellsWorksheetsApi* | [**cells_worksheets_get_worksheets**](docs/CellsWorksheetsApi.md#cells_worksheets_get_worksheets) | **GET** /cells/{name}/worksheets | Read worksheets info.
*CellsWorksheetsApi* | [**cells_worksheets_post_autofit_worksheet_columns**](docs/CellsWorksheetsApi.md#cells_worksheets_post_autofit_worksheet_columns) | **POST** /cells/{name}/worksheets/{sheetName}/autofitcolumns | 
*CellsWorksheetsApi* | [**cells_worksheets_post_autofit_worksheet_row**](docs/CellsWorksheetsApi.md#cells_worksheets_post_autofit_worksheet_row) | **POST** /cells/{name}/worksheets/{sheetName}/autofitrow | 
*CellsWorksheetsApi* | [**cells_worksheets_post_autofit_worksheet_rows**](docs/CellsWorksheetsApi.md#cells_worksheets_post_autofit_worksheet_rows) | **POST** /cells/{name}/worksheets/{sheetName}/autofitrows | Autofit worksheet rows.
*CellsWorksheetsApi* | [**cells_worksheets_post_copy_worksheet**](docs/CellsWorksheetsApi.md#cells_worksheets_post_copy_worksheet) | **POST** /cells/{name}/worksheets/{sheetName}/copy | 
*CellsWorksheetsApi* | [**cells_worksheets_post_move_worksheet**](docs/CellsWorksheetsApi.md#cells_worksheets_post_move_worksheet) | **POST** /cells/{name}/worksheets/{sheetName}/position | Move worksheet.
*CellsWorksheetsApi* | [**cells_worksheets_post_rename_worksheet**](docs/CellsWorksheetsApi.md#cells_worksheets_post_rename_worksheet) | **POST** /cells/{name}/worksheets/{sheetName}/rename | Rename worksheet
*CellsWorksheetsApi* | [**cells_worksheets_post_update_worksheet_property**](docs/CellsWorksheetsApi.md#cells_worksheets_post_update_worksheet_property) | **POST** /cells/{name}/worksheets/{sheetName} | Update worksheet property
*CellsWorksheetsApi* | [**cells_worksheets_post_update_worksheet_zoom**](docs/CellsWorksheetsApi.md#cells_worksheets_post_update_worksheet_zoom) | **POST** /cells/{name}/worksheets/{sheetName}/zoom | 
*CellsWorksheetsApi* | [**cells_worksheets_post_worksheet_comment**](docs/CellsWorksheetsApi.md#cells_worksheets_post_worksheet_comment) | **POST** /cells/{name}/worksheets/{sheetName}/comments/{cellName} | Update worksheet&#39;s cell comment.
*CellsWorksheetsApi* | [**cells_worksheets_post_worksheet_range_sort**](docs/CellsWorksheetsApi.md#cells_worksheets_post_worksheet_range_sort) | **POST** /cells/{name}/worksheets/{sheetName}/sort | Sort worksheet range.
*CellsWorksheetsApi* | [**cells_worksheets_post_worksheet_text_search**](docs/CellsWorksheetsApi.md#cells_worksheets_post_worksheet_text_search) | **POST** /cells/{name}/worksheets/{sheetName}/findText | Search text.
*CellsWorksheetsApi* | [**cells_worksheets_post_worsheet_text_replace**](docs/CellsWorksheetsApi.md#cells_worksheets_post_worsheet_text_replace) | **POST** /cells/{name}/worksheets/{sheetName}/replaceText | Replace text.
*CellsWorksheetsApi* | [**cells_worksheets_put_add_new_worksheet**](docs/CellsWorksheetsApi.md#cells_worksheets_put_add_new_worksheet) | **PUT** /cells/{name}/worksheets/{sheetName} | Add new worksheet.
*CellsWorksheetsApi* | [**cells_worksheets_put_change_visibility_worksheet**](docs/CellsWorksheetsApi.md#cells_worksheets_put_change_visibility_worksheet) | **PUT** /cells/{name}/worksheets/{sheetName}/visible | Change worksheet visibility.
*CellsWorksheetsApi* | [**cells_worksheets_put_protect_worksheet**](docs/CellsWorksheetsApi.md#cells_worksheets_put_protect_worksheet) | **PUT** /cells/{name}/worksheets/{sheetName}/protection | Protect worksheet.
*CellsWorksheetsApi* | [**cells_worksheets_put_worksheet_background**](docs/CellsWorksheetsApi.md#cells_worksheets_put_worksheet_background) | **PUT** /cells/{name}/worksheets/{sheetName}/background | Set worksheet background image.
*CellsWorksheetsApi* | [**cells_worksheets_put_worksheet_comment**](docs/CellsWorksheetsApi.md#cells_worksheets_put_worksheet_comment) | **PUT** /cells/{name}/worksheets/{sheetName}/comments/{cellName} | Add worksheet&#39;s cell comment.
*CellsWorksheetsApi* | [**cells_worksheets_put_worksheet_freeze_panes**](docs/CellsWorksheetsApi.md#cells_worksheets_put_worksheet_freeze_panes) | **PUT** /cells/{name}/worksheets/{sheetName}/freezepanes | Set freeze panes
*OAuthApi* | [**o_auth_post**](docs/OAuthApi.md#o_auth_post) | **POST** /oauth2/token | Get Access token


## Documentation For Models

 - [AboveAverage](docs/AboveAverage.md)
 - [AccessTokenResponse](docs/AccessTokenResponse.md)
 - [Area](docs/Area.md)
 - [AutoFitterOptions](docs/AutoFitterOptions.md)
 - [Border](docs/Border.md)
 - [CalculationOptions](docs/CalculationOptions.md)
 - [CellArea](docs/CellArea.md)
 - [CellValue](docs/CellValue.md)
 - [CellsColor](docs/CellsColor.md)
 - [Color](docs/Color.md)
 - [ColorFilter](docs/ColorFilter.md)
 - [ColorFilterRequest](docs/ColorFilterRequest.md)
 - [ColorScale](docs/ColorScale.md)
 - [ConditionalFormattingIcon](docs/ConditionalFormattingIcon.md)
 - [ConditionalFormattingValue](docs/ConditionalFormattingValue.md)
 - [CopyOptions](docs/CopyOptions.md)
 - [CreatePivotTableRequest](docs/CreatePivotTableRequest.md)
 - [CustomFilter](docs/CustomFilter.md)
 - [CustomParserConfig](docs/CustomParserConfig.md)
 - [DataBar](docs/DataBar.md)
 - [DataBarBorder](docs/DataBarBorder.md)
 - [DataSorter](docs/DataSorter.md)
 - [DynamicFilter](docs/DynamicFilter.md)
 - [FileSource](docs/FileSource.md)
 - [FillFormat](docs/FillFormat.md)
 - [FilterColumn](docs/FilterColumn.md)
 - [Font](docs/Font.md)
 - [FontSetting](docs/FontSetting.md)
 - [GradientFill](docs/GradientFill.md)
 - [GradientFillStop](docs/GradientFillStop.md)
 - [HorizontalPageBreak](docs/HorizontalPageBreak.md)
 - [IconFilter](docs/IconFilter.md)
 - [IconSet](docs/IconSet.md)
 - [ImportOption](docs/ImportOption.md)
 - [Line](docs/Line.md)
 - [Link](docs/Link.md)
 - [LinkElement](docs/LinkElement.md)
 - [ListColumn](docs/ListColumn.md)
 - [MultipleFilter](docs/MultipleFilter.md)
 - [MultipleFilters](docs/MultipleFilters.md)
 - [NegativeBarFormat](docs/NegativeBarFormat.md)
 - [OperateObject](docs/OperateObject.md)
 - [OperateObjectPosition](docs/OperateObjectPosition.md)
 - [OperateParameter](docs/OperateParameter.md)
 - [PageSection](docs/PageSection.md)
 - [PasswordRequest](docs/PasswordRequest.md)
 - [PasteOptions](docs/PasteOptions.md)
 - [PatternFill](docs/PatternFill.md)
 - [PicFormatOption](docs/PicFormatOption.md)
 - [PivotField](docs/PivotField.md)
 - [PivotFilter](docs/PivotFilter.md)
 - [PivotItem](docs/PivotItem.md)
 - [PivotTableFieldRequest](docs/PivotTableFieldRequest.md)
 - [ProtectSheetParameter](docs/ProtectSheetParameter.md)
 - [Range](docs/Range.md)
 - [RangeCopyRequest](docs/RangeCopyRequest.md)
 - [RangeSetOutlineBorderRequest](docs/RangeSetOutlineBorderRequest.md)
 - [RangeSetStyleRequest](docs/RangeSetStyleRequest.md)
 - [Ranges](docs/Ranges.md)
 - [ResultDestination](docs/ResultDestination.md)
 - [SaaSposeResponse](docs/SaaSposeResponse.md)
 - [SaveOptions](docs/SaveOptions.md)
 - [SaveResult](docs/SaveResult.md)
 - [ShadowEffect](docs/ShadowEffect.md)
 - [SingleValue](docs/SingleValue.md)
 - [SolidFill](docs/SolidFill.md)
 - [SortKey](docs/SortKey.md)
 - [SplitResult](docs/SplitResult.md)
 - [TaskData](docs/TaskData.md)
 - [TaskDescription](docs/TaskDescription.md)
 - [TaskParameter](docs/TaskParameter.md)
 - [TextureFill](docs/TextureFill.md)
 - [ThemeColor](docs/ThemeColor.md)
 - [TilePicOption](docs/TilePicOption.md)
 - [Top10](docs/Top10.md)
 - [Top10Filter](docs/Top10Filter.md)
 - [ValueType](docs/ValueType.md)
 - [VerticalPageBreak](docs/VerticalPageBreak.md)
 - [Workbook](docs/Workbook.md)
 - [WorkbookEncryptionRequest](docs/WorkbookEncryptionRequest.md)
 - [WorkbookProtectionRequest](docs/WorkbookProtectionRequest.md)
 - [WorkbookSettings](docs/WorkbookSettings.md)
 - [Worksheet](docs/Worksheet.md)
 - [WorksheetMovingRequest](docs/WorksheetMovingRequest.md)
 - [AutoFilter](docs/AutoFilter.md)
 - [AutoFilterResponse](docs/AutoFilterResponse.md)
 - [AutoShapes](docs/AutoShapes.md)
 - [AutoShapesResponse](docs/AutoShapesResponse.md)
 - [Cell](docs/Cell.md)
 - [CellResponse](docs/CellResponse.md)
 - [Cells](docs/Cells.md)
 - [CellsDocumentProperties](docs/CellsDocumentProperties.md)
 - [CellsDocumentPropertiesResponse](docs/CellsDocumentPropertiesResponse.md)
 - [CellsDocumentProperty](docs/CellsDocumentProperty.md)
 - [CellsDocumentPropertyResponse](docs/CellsDocumentPropertyResponse.md)
 - [CellsObjectOperateTaskParameter](docs/CellsObjectOperateTaskParameter.md)
 - [CellsResponse](docs/CellsResponse.md)
 - [Chart](docs/Chart.md)
 - [ChartAreaResponse](docs/ChartAreaResponse.md)
 - [ChartFrame](docs/ChartFrame.md)
 - [ChartOperateParameter](docs/ChartOperateParameter.md)
 - [Charts](docs/Charts.md)
 - [ChartsResponse](docs/ChartsResponse.md)
 - [Column](docs/Column.md)
 - [ColumnResponse](docs/ColumnResponse.md)
 - [Columns](docs/Columns.md)
 - [ColumnsResponse](docs/ColumnsResponse.md)
 - [Comment](docs/Comment.md)
 - [CommentResponse](docs/CommentResponse.md)
 - [Comments](docs/Comments.md)
 - [CommentsResponse](docs/CommentsResponse.md)
 - [ConditionalFormatting](docs/ConditionalFormatting.md)
 - [ConditionalFormattingResponse](docs/ConditionalFormattingResponse.md)
 - [ConditionalFormattings](docs/ConditionalFormattings.md)
 - [ConditionalFormattingsResponse](docs/ConditionalFormattingsResponse.md)
 - [ConvertTaskParameter](docs/ConvertTaskParameter.md)
 - [FillFormatResponse](docs/FillFormatResponse.md)
 - [FormatCondition](docs/FormatCondition.md)
 - [HorizontalPageBreakResponse](docs/HorizontalPageBreakResponse.md)
 - [HorizontalPageBreaks](docs/HorizontalPageBreaks.md)
 - [HorizontalPageBreaksResponse](docs/HorizontalPageBreaksResponse.md)
 - [Hyperlink](docs/Hyperlink.md)
 - [HyperlinkResponse](docs/HyperlinkResponse.md)
 - [Hyperlinks](docs/Hyperlinks.md)
 - [HyperlinksResponse](docs/HyperlinksResponse.md)
 - [ImportBatchDataOption](docs/ImportBatchDataOption.md)
 - [ImportCSVDataOption](docs/ImportCSVDataOption.md)
 - [ImportDataTaskParameter](docs/ImportDataTaskParameter.md)
 - [ImportDoubleArrayOption](docs/ImportDoubleArrayOption.md)
 - [ImportIntArrayOption](docs/ImportIntArrayOption.md)
 - [ImportStringArrayOption](docs/ImportStringArrayOption.md)
 - [LegendResponse](docs/LegendResponse.md)
 - [LineFormat](docs/LineFormat.md)
 - [LineResponse](docs/LineResponse.md)
 - [ListObject](docs/ListObject.md)
 - [ListObjectOperateParameter](docs/ListObjectOperateParameter.md)
 - [ListObjectResponse](docs/ListObjectResponse.md)
 - [ListObjects](docs/ListObjects.md)
 - [ListObjectsResponse](docs/ListObjectsResponse.md)
 - [MergedCell](docs/MergedCell.md)
 - [MergedCellResponse](docs/MergedCellResponse.md)
 - [MergedCells](docs/MergedCells.md)
 - [MergedCellsResponse](docs/MergedCellsResponse.md)
 - [Name](docs/Name.md)
 - [NameResponse](docs/NameResponse.md)
 - [Names](docs/Names.md)
 - [NamesResponse](docs/NamesResponse.md)
 - [OleObjectResponse](docs/OleObjectResponse.md)
 - [OleObjects](docs/OleObjects.md)
 - [OleObjectsResponse](docs/OleObjectsResponse.md)
 - [PageBreakOperateParameter](docs/PageBreakOperateParameter.md)
 - [PageSectionsResponse](docs/PageSectionsResponse.md)
 - [PageSetup](docs/PageSetup.md)
 - [PageSetupOperateParameter](docs/PageSetupOperateParameter.md)
 - [PageSetupResponse](docs/PageSetupResponse.md)
 - [PictureResponse](docs/PictureResponse.md)
 - [Pictures](docs/Pictures.md)
 - [PicturesResponse](docs/PicturesResponse.md)
 - [PivotFieldResponse](docs/PivotFieldResponse.md)
 - [PivotFilterResponse](docs/PivotFilterResponse.md)
 - [PivotFiltersResponse](docs/PivotFiltersResponse.md)
 - [PivotTable](docs/PivotTable.md)
 - [PivotTableOperateParameter](docs/PivotTableOperateParameter.md)
 - [PivotTableResponse](docs/PivotTableResponse.md)
 - [PivotTables](docs/PivotTables.md)
 - [PivotTablesResponse](docs/PivotTablesResponse.md)
 - [RangeValueResponse](docs/RangeValueResponse.md)
 - [RangesResponse](docs/RangesResponse.md)
 - [Row](docs/Row.md)
 - [RowResponse](docs/RowResponse.md)
 - [Rows](docs/Rows.md)
 - [RowsResponse](docs/RowsResponse.md)
 - [SaveResponse](docs/SaveResponse.md)
 - [SaveResultTaskParameter](docs/SaveResultTaskParameter.md)
 - [Shape](docs/Shape.md)
 - [ShapeOperateParameter](docs/ShapeOperateParameter.md)
 - [ShapeResponse](docs/ShapeResponse.md)
 - [Shapes](docs/Shapes.md)
 - [ShapesResponse](docs/ShapesResponse.md)
 - [SingleValueResponse](docs/SingleValueResponse.md)
 - [SmartMarkerTaskParameter](docs/SmartMarkerTaskParameter.md)
 - [SplitResultDocument](docs/SplitResultDocument.md)
 - [SplitResultResponse](docs/SplitResultResponse.md)
 - [SplitWorkbookTaskParameter](docs/SplitWorkbookTaskParameter.md)
 - [Style](docs/Style.md)
 - [StyleResponse](docs/StyleResponse.md)
 - [TextItem](docs/TextItem.md)
 - [TextItems](docs/TextItems.md)
 - [TextItemsResponse](docs/TextItemsResponse.md)
 - [TextOptions](docs/TextOptions.md)
 - [TitleResponse](docs/TitleResponse.md)
 - [Validation](docs/Validation.md)
 - [ValidationResponse](docs/ValidationResponse.md)
 - [Validations](docs/Validations.md)
 - [ValidationsResponse](docs/ValidationsResponse.md)
 - [VerticalPageBreakResponse](docs/VerticalPageBreakResponse.md)
 - [VerticalPageBreaks](docs/VerticalPageBreaks.md)
 - [VerticalPageBreaksResponse](docs/VerticalPageBreaksResponse.md)
 - [WorkbookOperateParameter](docs/WorkbookOperateParameter.md)
 - [WorkbookReplaceResponse](docs/WorkbookReplaceResponse.md)
 - [WorkbookResponse](docs/WorkbookResponse.md)
 - [WorkbookSettingsOperateParameter](docs/WorkbookSettingsOperateParameter.md)
 - [WorkbookSettingsResponse](docs/WorkbookSettingsResponse.md)
 - [WorksheetReplaceResponse](docs/WorksheetReplaceResponse.md)
 - [WorksheetResponse](docs/WorksheetResponse.md)
 - [Worksheets](docs/Worksheets.md)
 - [WorksheetsResponse](docs/WorksheetsResponse.md)
 - [ChartArea](docs/ChartArea.md)
 - [Legend](docs/Legend.md)
 - [OleObject](docs/OleObject.md)
 - [Picture](docs/Picture.md)
 - [Title](docs/Title.md)


## Documentation For Authorization


## appsid

- **Type**: API key
- **API key parameter name**: appsid
- **Location**: URL query string

## oauth

- **Type**: OAuth
- **Flow**: implicit
- **Authorization URL**: 
- **Scopes**: 
 - **write:pets**: modify pets in your account

## signature

- **Type**: API key
- **API key parameter name**: signature
- **Location**: URL query string




