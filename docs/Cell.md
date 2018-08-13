# Cell

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**link** | [**Link**](Link.md) |  | [optional] 
**style** | [**LinkElement**](LinkElement.md) |  | [optional] 
**html_string** | **str** | Gets and sets the html string which contains data and some formattings in this cell.              | [optional] 
**name** | **str** | Gets the name of the cell.              | [optional] 
**column** | **int** | Gets column number (zero based) of the cell.              | 
**worksheet** | **str** | Gets the parent worksheet. | [optional] 
**is_in_table** | **bool** | Indicates whethe this cell is part of table formula.              | 
**is_array_header** | **bool** | Inidicates the cell&#39;s formula is and array formula and it is the first cell of the array. | 
**value** | **str** |  | [optional] 
**is_formula** | **bool** | Represents if the specified cell contains formula.              | 
**is_style_set** | **bool** | Indicates if the cell&#39;s style is set. If return false, it means this cell has a default cell format.              | 
**is_in_array** | **bool** | Indicates whether the cell formula is an array formula. | 
**is_error_value** | **bool** | Checks if a formula can properly evaluate a result.              | 
**is_merged** | **bool** | Checks if a cell is part of a merged range or not.              | 
**formula** | **str** | Gets or sets a formula of the Aspose.Cells.Cell. | [optional] 
**type** | **str** | Specifies a cell value type. | [optional] 
**row** | **int** | Gets row number (zero based) of the cell.              | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


