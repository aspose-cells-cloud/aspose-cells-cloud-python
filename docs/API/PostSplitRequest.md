# **Spreadsheet Cloud API: postSplit**

Split Excel spreadsheet files based on worksheets and create output files in various formats. 


## **Quick Start**

- **Base URL**: `http://api.aspose.cloud/v3.0`
- **Authentication Method**: `JWT (OAuth2, application)`  **Token URL**: `https://api.aspose.cloud/connect/token`
- **Example** 

## **Interface Details**

### **Endpoint** 

```
POST http://api.aspose.cloud/v3.0/cells/split
```
### **Function Description**
PageTitle: Split Excel spreadsheet files based on worksheets and create output files in various formats.PageDescription: Aspose.Cells Cloud provides robust support for splitting Excel spreadsheet files based on worksheets and create output files in various formats, a process known for its intricacy.HeadTitle:  Split Excel spreadsheet files based on worksheets and create output files in various formats.HeadSummary: Aspose.Cells Cloud provides robust support for splitting Excel spreadsheet files based on worksheets and create output files in various formats, a process known for its intricacy.HeadContent: Aspose.Cells Cloud provides REST API which supports splitting Excel spreadsheet files based on worksheets and create output files in various formats and offers SDKs for multiple programming languages. These programming languages are include of Net, Java, Go, NodeJS, Python, and so on.

### The request parameters of **postSplit** API are: 

| Parameter Name | Type | Path/Query String/HTTPBody | Description | 
| :- | :- | :- |:- | 
|File|File|FormData|File to upload|
|outFormat|String|Query|The output data file format.(CSV/XLS/HTML/MHTML/ODS/PDF/XML/TXT/TIFF/XLSB/XLSM/XLSX/XLTM/XLTX/XPS/PNG/JPG/JPEG/GIF/EMF/BMP/MD[Markdown]/Numbers)|
|password|String|Query|The password needed to open an Excel file.|
|from|Integer|Query|sheet index|
|to|Integer|Query|sheet index|
|checkExcelRestriction|Boolean|Query|Whether check restriction of excel file when user modify cells related objects.|
|region|String|Query|The regional settings for workbook.|

### **Response Description**
```json
{
  "Name": "FilesResult",
  "Description": [
    "Class features: Weekly lectures, group projects, midterm and final exams, and participation in class discussions."
  ],
  "Type": "Class",
  "IsAbstract": false,
  "Properties": [
    {
      "Name": "Files",
      "Description": [
        "A property named **Files** of type **IList FileInfo ** containing a collection of file information objects."
      ],
      "Nullable": true,
      "ReadOnly": false,
      "IsInherit": false,
      "DataType": {
        "Identifier": "Container",
        "Reference": "FileInfo",
        "ElementDataType": {
          "Identifier": "Class",
          "Reference": "FileInfo",
          "Name": "class:fileinfo"
        },
        "Name": "container"
      }
    }
  ]
}
```


## OpenAPI Specification

The [OpenAPI Specification](https://reference.aspose.cloud/cells/#/LightCellsController/PostSplit) defines a publicly accessible programming interface and lets you carry out REST interactions directly from a web browser.
