# **Spreadsheet Cloud API: sawpRange**

The Swap Ranges for Excel API provides a powerful tool to move any two columns, rows, ranges, or individual cells within an Excel file. This API allows users to re-arrange their tables quickly and efficiently, ensuring that the original data formatting is preserved and all existing formulas continue to function correctly. By leveraging this API, users can streamline their data manipulation tasks and maintain the integrity of their spreadsheets. 


## **Quick Start**

- **Base URL**: `http://api.aspose.cloud/v4.0`
- **Authentication Method**: `JWT (OAuth2, application)`  **Token URL**: `https://api.aspose.cloud/connect/token`
- **Example** 

## **Interface Details**

### **Endpoint** 

```
PUT http://api.aspose.cloud/v4.0/cells/swap/range
```
### **Function Description**
This API is designed to enhance productivity by simplifying the process of re-arranging data in Excel files. Users can easily swap columns, rows, ranges, or individual cells without worrying about losing data formatting or breaking formulas. The API ensures that the re-arranged tables remain functional and visually consistent with the original data. This feature is particularly useful for users who frequently need to manipulate large datasets or perform complex data re-arrangements.

### The request parameters of **sawpRange** API are: 

| Parameter Name | Type | Path/Query String/HTTPBody | Description | 
| :- | :- | :- |:- | 
|Spreadsheet|File|FormData|Upload spreadsheet file.|
|worksheet1|String|Query||
|range1|String|Query||
|worksheet2|String|Query||
|range2|String|Query||
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

The [OpenAPI Specification](https://reference.aspose.cloud/cells/#/TransformController/SawpRange) defines a publicly accessible programming interface and lets you carry out REST interactions directly from a web browser.
