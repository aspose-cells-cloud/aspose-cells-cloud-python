# **Spreadsheet Cloud API: getWorksheetShapes**

Retrieve descriptions of shapes in the worksheet. 


## **Quick Start**

- **Base URL**: `http://api.aspose.cloud/v3.0`
- **Authentication Method**: `JWT (OAuth2, application)`  **Token URL**: `https://api.aspose.cloud/connect/token`
- **Example** 

## **Interface Details**

### **Endpoint** 

```
GET http://api.aspose.cloud/v3.0/cells/{name}/worksheets/{sheetName}/shapes
```
### **Function Description**
PageTitle:  Retrieve descriptions of shapes in the worksheet.PageDescription: Aspose.Cells Cloud provides robust support for obtaining descriptions of shapes in the worksheet, a process known for its intricacy.HeadTitle: Retrieve descriptions of shapes in the worksheet.HeadSummary: Aspose.Cells Cloud provides robust support for obtaining descriptions of shapes in the worksheet, a process known for its intricacy.HeadContent: Aspose.Cells Cloud provides REST API which supports obtaining descriptions of shapes in the worksheet and offers SDKs for multiple programming languages. These programming languages are include of Net, Java, Go, NodeJS, Python, and so on.

### The request parameters of **getWorksheetShapes** API are: 

| Parameter Name | Type | Path/Query String/HTTPBody | Description | 
| :- | :- | :- |:- | 
|name|String|Path|The file name.|
|sheetName|String|Path|The worksheet name.|
|folder|String|Query|The folder where the file is situated.|
|storageName|String|Query|The storage name where the file is situated.|

### **Response Description**
```json
{
  "Name": "ShapesResponse",
  "Description": [
    "Represents the Shapes Response."
  ],
  "Type": "Class",
  "ParentName": "CellsCloudResponse",
  "IsAbstract": false,
  "Properties": [
    {
      "Name": "Shapes",
      "Description": [
        "The class has a property called \"Shapes\" with XML serialization attribute \"XmlElement\" for specifying the element name in the XML representation."
      ],
      "Nullable": true,
      "ReadOnly": false,
      "IsInherit": false,
      "DataType": {
        "Identifier": "Class",
        "Reference": "Shapes",
        "Name": "class:shapes"
      }
    },
    {
      "Name": "Code",
      "Nullable": true,
      "ReadOnly": false,
      "IsInherit": true,
      "DataType": {
        "Identifier": "Integer",
        "Name": "integer"
      }
    },
    {
      "Name": "Status",
      "Nullable": true,
      "ReadOnly": false,
      "IsInherit": true,
      "DataType": {
        "Identifier": "String",
        "Name": "string"
      }
    }
  ]
}
```


## OpenAPI Specification

The [OpenAPI Specification](https://reference.aspose.cloud/cells/#/ShapesController/GetWorksheetShapes) defines a publicly accessible programming interface and lets you carry out REST interactions directly from a web browser.
