Python Cloud SDK wraps Aspose.Cells REST API so you could seamlessly integrate Microsoft Excel® spreadsheet generation, manipulation, conversion & inspection features into your own Python applications.

[Aspose.Cells Cloud SDK for Python](https://products.aspose.cloud/cells/python) offers Excel® file creation, manipulation, conversion, & rendering. Developers can format worksheets, rows, columns or cells to the most granular level, create & manipulate chart & pivot tables, render worksheets, charts and specific data ranges to PDF & images, add & calculate Excel's built-in and custom formulas and much more. Feel free to explore the [Developer's Guide](https://docs.aspose.cloud/display/cellscloud/Developer+Guide) for all usage scenarios. 

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

## Feature & Enhancements in Version 20.9

- Support sparkline groups.
- Add API about updating pivot field.
- Enhancement for add chart API.

## Read & Write Spreadsheet Formats

**Microsoft Excel:** XLS, XLSX, XLSB, XLSM, XLT, XLTX, XLTM
**OpenOffice:** ODS
**SpreadsheetML:** XML
**Text:** CSV, TSV, TXT (TabDelimited)
**Web:** HTML, MHTML
**PDF**

## Save Spreadsheet As

DIF, HTML, MHTML,PNG,JPG, TIFF, XPS, SVG, MD (Markdown), ODS ,xlsx,xls,xlsb, PDF,XML,TXT,CSV

## Read Spreadsheet Formats

SXC, FODS

## Storage API Support

Since version 19.9, SDK includes support of storage operations for better user experience and unification, so now there's no need to use 2 different SDKs!

It gives you an ability to:

- Upload, download, copy, move and delete files, including versions handling (if you are using Cloud storage that supports this feature - true by default).
- Create, copy, move and delete folders.
- Copy and move files and folders across separate storages in scope of a single operation.
- Check if certain file, folder or storage exists.

## Getting Started with Aspose.Cells Cloud SDK for Python

Firstly, create an account at [Aspose for Cloud](https://dashboard.aspose.cloud/#/apps) to get your application information and free quota to use the API. Now execute `pip install asposecellscloud` from the command line to get the get the SDK from PIP. The complete source code is available at [GitHub Repository](https://github.com/aspose-cells-cloud/aspose-cells-cloud-python).

## Create Spreadsheet from a Template in the Cloud via Python

```python

    #Instantiate Aspose Cells API SDK
    cellsApi = asposecellscloud.apis.cells_api.CellsApi(GetAPPSID(),GetAPPKey(),"v3.0")

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
    cellsApi = asposecellscloud.apis.cells_api.CellsApi(GetAPPSID(),GetAPPKey(),"v3.0")

    fullfilename = os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" + "Book1.xlsx"
    format ='pdf'       
    password = None
    outPath = None      
    result = cellsApi.cells_workbook_put_convert_workbook(fullfilename,format=format)
    # self.assertEqual(result.code,200)
```

[Product Page](https://products.aspose.cloud/cells/python) | [Documentation](https://docs.aspose.cloud/display/cellscloud/Home) | [Live Demo](https://products.aspose.app/cells/family) | [API Reference](https://apireference.aspose.cloud/cells/) | [Code Samples](https://github.com/aspose-cells-cloud/aspose-cells-cloud-python) | [Blog](https://blog.aspose.cloud/category/cells/) | [Free Support](https://forum.aspose.cloud/c/cells) | [Free Trial](https://dashboard.aspose.cloud/#/apps)