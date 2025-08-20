# **Spreadsheet Cloud API: renameWorksheetInSpreadsheet**

The Web API endpoint allows users to rename a specified worksheet within a workbook. This function provides a straightforward way to update worksheet names, enhancing workbook organization and readability. 


## **Quick Start**

- **Base URL**: `http://api.aspose.cloud/v4.0`
- **Authentication Method**: `JWT (OAuth2, application)`  **Token URL**: `https://api.aspose.cloud/connect/token`
- **Example** 

## **Interface Details**

### **Endpoint** 

```
PUT http://api.aspose.cloud/v4.0/cells/spreadsheet/rename/worksheet
```
### **Function Description**
By using the RenameWorksheet API, you can dynamically manage the structure of your workbook, updating worksheet names to maintain a clear and organized spreadsheet environment. This feature enhances your ability to manage and optimize your workbook efficiently.**Considerations**: Ensure that the provided sourceName is correct and matches an existing worksheet in the workbook. Ensure that the targetName is unique and does not conflict with other worksheet names in the workbook.Be cautious when renaming worksheets, as this action may affect existing references and formulas.**Error Handling:** If the sourceName does not match any existing worksheet, the function may throw an exception or return an error message. If the targetName is not unique or is invalid, the function may throw an exception or return an error message.

### The request parameters of **renameWorksheetInSpreadsheet** API are: 

| Parameter Name | Type | Path/Query String/HTTPBody | Description | 
| :- | :- | :- |:- | 
|Spreadsheet|File|FormData|Upload spreadsheet file.|
|sourceName|String|Query|The current name of the worksheet to be renamed.|
|targetName|String|Query|The new name for the worksheet.|
|outPath|String|Query|(Optional) The folder path where the workbook is stored. The default is null.|
|outStorageName|String|Query|Output file Storage Name.|
|regoin|String|Query|The spreadsheet region setting.|
|password|String|Query|The password for opening spreadsheet file.|

### **Response Description**
```json
{
File
}
```


## OpenAPI Specification

The [OpenAPI Specification](https://reference.aspose.cloud/cells/#/ManagementController/RenameWorksheetInSpreadsheet) defines a publicly accessible programming interface and lets you carry out REST interactions directly from a web browser.
