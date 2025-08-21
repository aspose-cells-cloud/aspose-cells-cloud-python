# **Spreadsheet Cloud API: deleteWorksheetFromSpreadsheet**

The Web API endpoint allows users to delete a specified worksheet from a workbook. This function provides a straightforward way to manage workbook structure by removing unnecessary or redundant worksheets. 


## **Quick Start**

- **Base URL**: `http://api.aspose.cloud/v4.0`
- **Authentication Method**: `JWT (OAuth2, application)`  **Token URL**: `https://api.aspose.cloud/connect/token`
- **Example** 

## **Interface Details**

### **Endpoint** 

```
PUT http://api.aspose.cloud/v4.0/cells/spreadsheet/delete/worksheet
```
### **Function Description**
By using the Web API, you can dynamically manage the structure of your workbook, removing specified worksheets to maintain a clean and organized spreadsheet environment. This feature enhances your ability to manage and optimize your workbook efficiently.**Considerations**: Ensure that the provided worksheet name is correct and matches an existing worksheet in the workbook. Be cautious when deleting worksheets, as this action cannot be undone.**Error Handling**: If the worksheet name is not provided or does not match any existing worksheet, the function may throw an exception or return an error message. Ensure proper error handling to manage cases where the worksheet does not exist.

### The request parameters of **deleteWorksheetFromSpreadsheet** API are: 

| Parameter Name | Type | Path/Query String/HTTPBody | Description | 
| :- | :- | :- |:- | 
|Spreadsheet|File|FormData|Upload spreadsheet file.|
|sheetName|String|Query|Specifies the name or identifier of the worksheet to be deleted. This parameter is required and must match the name of an existing worksheet in the workbook.|
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

The [OpenAPI Specification](https://reference.aspose.cloud/cells/#/ManagementController/DeleteWorksheetFromSpreadsheet) defines a publicly accessible programming interface and lets you carry out REST interactions directly from a web browser.
