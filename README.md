![](https://img.shields.io/badge/REST%20API-v3.0-lightgrey) ![PyPI](https://img.shields.io/pypi/v/asposecellscloud) ![PyPI - Python Version](https://img.shields.io/pypi/pyversions/asposecellscloud) ![PyPI - Downloads](https://img.shields.io/pypi/dm/asposecellscloud)  [![GitHub license](https://img.shields.io/github/license/aspose-cells-cloud/aspose-cells-cloud-python)](https://github.com/aspose-cells-cloud/aspose-cells-cloud-python/blob/master/LICENSE) ![GitHub commits since latest release (by date)](https://img.shields.io/github/commits-since/aspose-cells-cloud/aspose-cells-cloud-python/24.2.1)


# Python SDK for Spreadsheet Processing in Cloud

The Python Cloud SDK wraps the Aspose.Cells REST API, enabling seamless integration of Microsoft Excel® spreadsheet generation, manipulation, conversion, and inspection features into Python applications.

With [Aspose.Cells Cloud SDK for Python](https://products.aspose.cloud/cells/python), developers can perform a wide range of tasks, including Excel® file creation, editing, conversion, and rendering. They can format worksheets, rows, columns, or cells at a granular level, create and manipulate charts and pivot tables, render worksheets, charts, and specific data ranges to PDF and images, add and calculate Excel's built-in and custom formulas, and much more.



## Manipulate Excel Files in the Cloud with Python

- Generate Excel files using the API.
- Generate and update Pivot Tables and charts.
- Implement and manage sparklines and conditional formatting.
- Convert charts, worksheets, or data ranges to images or PDF.
- Handle comments and hyperlinks.
- Apply complex formulas and compute results via the API.
- Implement protection on workbooks, worksheets, cells, columns, or rows.
- Create and manage named ranges.
- Populate worksheets using Smart Markers.
- Convert worksheets to PDF, XPS, and SVG formats.
- Convert files to and from popular Excel formats.

## Feature & Enhancements in Version 24.2.1

Full list of issues covering all changes in this release:

- Add the analyze excel api for analyze controller.
 
## Read & Write Spreadsheet Formats

**Microsoft Excel:** XLS, XLSX, XLSB, XLSM, XLT, XLTX, XLTM

**OpenOffice:** ODS

**SpreadsheetML:** XML

**Text:** CSV, TSV, TXT (TabDelimited)

**Web:** HTML, MHTML

## Save Spreadsheets As

**Microsoft Excel:** XLS, XLSX, XLSB

**OpenOffice:** ODS

**SpreadsheetML:** XML

**Text:** CSV, TSV, TXT (TabDelimited)

**Web:** HTML, MHTML

**Fixed Layout:** PDF, XPS

**Images:** PNG, JPG, TIFF, SVG

**Markdown:** MD

**Other:** DIF

## Read Other Formats

SXC, FODS

## Integrated Storage API

Since version 19.9, the SDK includes support for storage operations, enhancing user experience and unification. It provides the following capabilities:

- Upload, download, copy, move, and delete files, including handling versions (if supported by the cloud storage provider, defaulting to true).
- Create, copy, move, and delete folders.
- Copy and move files and folders across different storages in a single operation.
- Check the existence of specific files, folders, or storage locations.
 

## Gett Started with Aspose.Cells Cloud SDK for Python

1. Create an account at Aspose for Cloud to obtain your application information.
2. Execute `pip install asposecellscloud` from the command line to install the SDK from PIP.
3. The complete source code is also available at the GitHub Repository.


## Create Spreadsheet from a Template in the Cloud via Python

```python
    cellsApi = CellsApi("YourClientId","YourClientSecret","v3.0","https://api.aspose.cloud")
    remote_folder = 'TestData/In'
    local_name = 'Book1.xlsx'
    report_data_xml = 'ReportData.xml'
    remote_name = 'Book1.xlsx'
    
    request =  PostWorkbookGetSmartMarkerResultRequest( remote_name,xml_file= remote_folder + '/' +report_data_xml,folder= remote_folder,out_path= 'OutResult/SmartMarkerResult.xlsx',storage_name= '',out_storage_name= '')
    cellsApi.post_workbook_get_smart_marker_result(request)
```

## Convert Excel to PDF via Python 

```python
    #Instantiate Aspose Cells API SDK
    cellsApi = CellsApi("YourClientId","YourClientSecret","v3.0","https://api.aspose.cloud")
    local_name = 'Book1.xlsx'
    format = 'pdf'
    mapFiles = { 
        local_name:  "TestData/" +local_name             
    }
    request =  PutConvertWorkbookRequest( mapFiles,format= format)
    cellsApi.put_convert_workbook(request)
```

## Aspose.Cells Cloud SDKs in Popular Languages

| .NET | Java | PHP | Ruby | Node.js | Android | Swift | Perl | GO |
|---|---|---|---|---|---|---|---|---|
| [GitHub](https://github.com/aspose-cells-cloud/aspose-cells-cloud-dotnet) | [GitHub](https://github.com/aspose-cells-cloud/aspose-cells-cloud-java) | [GitHub](https://github.com/aspose-cells-cloud/aspose-cells-cloud-php) | [GitHub](https://github.com/aspose-cells-cloud/aspose-cells-cloud-ruby)  | [GitHub](https://github.com/aspose-cells-cloud/aspose-cells-cloud-node) | [GitHub](https://github.com/aspose-cells-cloud/aspose-cells-cloud-android)  | [GitHub](https://github.com/aspose-cells-cloud/aspose-cells-cloud-swift) | [GitHub](https://github.com/aspose-cells-cloud/aspose-cells-cloud-perl) | [GitHub](https://github.com/aspose-cells-cloud/aspose-cells-cloud-go) |
| [NuGet](https://www.nuget.org/packages/Aspose.Cells-Cloud/) | [Maven](https://repository.aspose.cloud/webapp/#/artifacts/browse/tree/General/repo/com/aspose/aspose-cells-cloud) | [Composer](https://packagist.org/packages/aspose/cells-sdk-php) | [GEM](https://rubygems.org/gems/aspose_cells_cloud)  | [NPM](https://www.npmjs.com/package/asposecellscloud) | [Maven](https://repository.aspose.cloud/webapp/#/artifacts/browse/tree/General/repo/com/aspose/aspose-cells-cloud-android) | [POD](https://cocoapods.org/pods/AsposeCellsCloud) |  [CPAN](https://metacpan.org/release/AsposeCellsCloud-CellsApi) | [GO](https://pkg.go.dev/github.com/aspose-cells-cloud/aspose-cells-cloud-go/v20?tab=overview) |


[Product Page](https://products.aspose.cloud/cells/python) | [Documentation](https://docs.aspose.cloud/cells/) | [Live Demo](https://products.aspose.app/cells/family) | [API Reference](https://apireference.aspose.cloud/cells/) | [Code Samples](https://github.com/aspose-cells-cloud/aspose-cells-cloud-python/tree/master/test) | [Blog](https://blog.aspose.cloud/category/cells/) | [Free Support](https://forum.aspose.cloud/c/cells) | [Free Trial](https://dashboard.aspose.cloud/#/apps)
