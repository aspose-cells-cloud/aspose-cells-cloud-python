![](https://img.shields.io/badge/REST%20API-v3.0-lightgrey) ![PyPI](https://img.shields.io/pypi/v/asposecellscloud) ![PyPI - Python Version](https://img.shields.io/pypi/pyversions/asposecellscloud) ![PyPI - Downloads](https://img.shields.io/pypi/dm/asposecellscloud)  [![GitHub license](https://img.shields.io/github/license/aspose-cells-cloud/aspose-cells-cloud-python)](https://github.com/aspose-cells-cloud/aspose-cells-cloud-python/blob/master/LICENSE) ![GitHub commits since latest release (by date)](https://img.shields.io/github/commits-since/aspose-cells-cloud/aspose-cells-cloud-python/22.9)


# Python SDK for Spreadsheet Processing in Cloud

Python Cloud SDK wraps Aspose.Cells REST API so you could seamlessly integrate Microsoft Excel® spreadsheet generation, manipulation, conversion & inspection features into your own Python applications. 

[Aspose.Cells Cloud SDK for Python](https://products.aspose.cloud/cells/python) offers Excel® file creation, editing, conversion, & rendering. Developers can format worksheets, rows, columns or cells to the most granular level, create & manipulate chart & pivot tables, render worksheets, charts and specific data ranges to PDF & images, add & calculate Excel's built-in and custom formulas and much more.

## Manipulate Excel Files in the Cloud with Python

- Create Excel files via API.
- Create & refresh Pivot Tables & charts.
- Create & manipulate spark-lines & conditional formatting.
- Convert charts, worksheets or data ranges to images or PDF.
- Manage comments & hyperlinks.
- Set complex formulas & calculate results via API.
- Set protection on workbook, worksheet, cell, column or row.
- Create & manipulate named ranges.
- Populate worksheets through Smart Markers.
- Convert worksheets to PDF, XPS & SVG formats.
- Inter-convert files to popular Excel formats.

## Feature & Enhancements in Version 22.9

- Add api for converting workbook to png.
- Add api for converting workbook to pdf.
- Add api for converting workbook to docx.
 
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

Since version 19.9, SDK includes support of storage operations for better user experience and unification. It gives you an ability to;

- Upload, download, copy, move and delete files, including versions handling (if you are using Cloud storage that supports this feature - true by default).
- Create, copy, move and delete folders.
- Copy and move files and folders across separate storages in scope of a single operation.
- Check if certain file, folder or storage exists.

## Gett Started with Aspose.Cells Cloud SDK for Python

Firstly, create an account at [Aspose for Cloud](https://dashboard.aspose.cloud/#/apps) to get your application information. Next, execute `pip install asposecellscloud` from the command line to get the SDK from PIP. The complete source code is also available at [GitHub Repository](https://github.com/aspose-cells-cloud/aspose-cells-cloud-python).

## Create Spreadsheet from a Template in the Cloud via Python

```python

    #Instantiate Aspose Cells API SDK
    cellsApi = asposecellscloud.apis.cells_api.CellsApi(GetClientId(),GetClientSecret(),"v3.0")

    templateFile ='Book1.xlsx'       
    folder = "Temp"
    name = "NewBook" + datetime.now().strftime("%Y%m%d%H%M%S") + ".xlsx"    
    dataFile = "ReportData.xml"  
    template_file = folder + "/" + templateFile
    data_file = folder + "/" + dataFile
    fullfilename = os.path.dirname(os.path.realpath(__file__)) +  "/" + templateFile
    api.upload_file(template_file, fullfilename)
    fullfilename = os.path.dirname(os.path.realpath(__file__)) +  "/" + data_file
    api.upload_file(data_file, fullfilename)
    result = cellsApi.cells_workbook_put_workbook_create(name, template_file=template_file, data_file=data_file,  folder=folder)
    self.assertEqual(result.code,200)
```

## Convert Excel to PDF via Python 

```python
    #Instantiate Aspose Cells API SDK
    cellsApi = asposecellscloud.apis.cells_api.CellsApi(GetClientId(),GetClientSecret(),"v3.0")

    fullfilename = os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" + "Book1.xlsx"
    format ='pdf'       
    password = None
    outPath = None      
    result = cellsApi.cells_workbook_put_convert_workbook(fullfilename,format=format)
    # self.assertEqual(result.code,200)
```

## Aspose.Cells Cloud SDKs in Popular Languages

| .NET | Java | PHP | Ruby | Node.js | Android | Swift | Perl | GO |
|---|---|---|---|---|---|---|---|---|
| [GitHub](https://github.com/aspose-cells-cloud/aspose-cells-cloud-dotnet) | [GitHub](https://github.com/aspose-cells-cloud/aspose-cells-cloud-java) | [GitHub](https://github.com/aspose-cells-cloud/aspose-cells-cloud-php) | [GitHub](https://github.com/aspose-cells-cloud/aspose-cells-cloud-ruby)  | [GitHub](https://github.com/aspose-cells-cloud/aspose-cells-cloud-node) | [GitHub](https://github.com/aspose-cells-cloud/aspose-cells-cloud-android)  | [GitHub](https://github.com/aspose-cells-cloud/aspose-cells-cloud-swift) | [GitHub](https://github.com/aspose-cells-cloud/aspose-cells-cloud-perl) | [GitHub](https://github.com/aspose-cells-cloud/aspose-cells-cloud-go) |
| [NuGet](https://www.nuget.org/packages/Aspose.Cells-Cloud/) | [Maven](https://repository.aspose.cloud/webapp/#/artifacts/browse/tree/General/repo/com/aspose/aspose-cells-cloud) | [Composer](https://packagist.org/packages/aspose/cells-sdk-php) | [GEM](https://rubygems.org/gems/aspose_cells_cloud)  | [NPM](https://www.npmjs.com/package/asposecellscloud) | [Maven](https://repository.aspose.cloud/webapp/#/artifacts/browse/tree/General/repo/com/aspose/aspose-cells-cloud-android) | [POD](https://cocoapods.org/pods/AsposeCellsCloud) |  [CPAN](https://metacpan.org/release/AsposeCellsCloud-CellsApi) | [GO](https://pkg.go.dev/github.com/aspose-cells-cloud/aspose-cells-cloud-go/v20?tab=overview) |


[Product Page](https://products.aspose.cloud/cells/python) | [Documentation](https://docs.aspose.cloud/cells/) | [Live Demo](https://products.aspose.app/cells/family) | [API Reference](https://apireference.aspose.cloud/cells/) | [Code Samples](https://github.com/aspose-cells-cloud/aspose-cells-cloud-python/tree/master/test) | [Blog](https://blog.aspose.cloud/category/cells/) | [Free Support](https://forum.aspose.cloud/c/cells) | [Free Trial](https://dashboard.aspose.cloud/#/apps)
