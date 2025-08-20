# **Spreadsheet Cloud API: convertWorksheetToImage**

Converts a worksheet of spreadsheet on a local drive to the image format. 


## **Quick Start**

- **Base URL**: `http://api.aspose.cloud/v4.0`
- **Authentication Method**: `JWT (OAuth2, application)`  **Token URL**: `https://api.aspose.cloud/connect/token`
- **Example** 

## **Interface Details**

### **Endpoint** 

```
PUT http://api.aspose.cloud/v4.0/cells/convert/worksheet/image
```
### **Function Description**
This method reads a spreadsheet file from the local file system, converts it's worksheet to the desired image format (e.g., svg, png, ...), and returns the converted result.The source file path and target format must be specified correctly.Ensure that the necessary permissions are in place to read the source file and write the converted file if applicable.The conversion process occurs entirely on the cloud server, eliminating the need for any cloud storage or external downloads.If the source file does not exist, is inaccessible, or if an error occurs during the conversion process, an appropriate exception will be thrown.Supported formats for conversion depend on the available libraries and their capabilities.

### The request parameters of **convertWorksheetToImage** API are: 

| Parameter Name | Type | Path/Query String/HTTPBody | Description | 
| :- | :- | :- |:- | 
|Spreadsheet|File|FormData|Upload spreadsheet file.|
|worksheet|String|Query|worksheet name of spreadsheet.|
|format|String|Query|image format:svg, png, and so on.|
|outPath|String|Query|(Optional) The folder path where the workbook is stored. The default is null.|
|outStorageName|String|Query|Output file Storage Name.|
|fontsLocation|String|Query|Use Custom fonts.|
|regoin|String|Query|The spreadsheet region setting.|
|password|String|Query|The password for opening spreadsheet file.|

### **Response Description**
```json
{
File
}
```


## OpenAPI Specification

The [OpenAPI Specification](https://reference.aspose.cloud/cells/#/ConversionController/ConvertWorksheetToImage) defines a publicly accessible programming interface and lets you carry out REST interactions directly from a web browser.
