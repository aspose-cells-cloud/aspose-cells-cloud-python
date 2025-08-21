# Aspose.Cells Cloud SDK for Python – Usage Guide

Aspose.Cells Cloud SDK for Python is a simple and easy-to-use Python library that allows you to interact with the Aspose.Cells Cloud API.

## Installation

```bash
python -m pip install asposecellscloud
```

---

## Get Your Credentials

1. Sign up: <https://id.containerize.com/signup>  
2. Create an application in the [Dashboard](https://dashboard.aspose.cloud/#/applications) to obtain your **Client ID** and **Client Secret**.

## Quick-Start Template

### Initialize the Client

```python
import os
from asposecellscloud.apis.cells_api import CellsApi

CLIENT_ID     = os.getenv("CellsCloudClientId")     # or hard-code  get from https://dashboard.aspose.cloud/#/applications
CLIENT_SECRET = os.getenv("CellsCloudClientSecret")

api = CellsApi(CLIENT_ID, CLIENT_SECRET)
```

### Excel → PDF (Local Conversion)

```python

from asposecellscloud.requests import ConvertSpreadsheetRequest

api.convert_spreadsheet(ConvertSpreadsheetRequest("input.xlsx", "pdf"), local_outpath="output.pdf")

```

### Upload a File to Cloud Storage

```python
from asposecellscloud.requests import UploadFileRequest

api.upload_file( UploadFileRequest("input.xlsx", "ExcelFiles/input.xlsx"))

```

### Create a Blank Workbook

```python
from asposecellscloud.requests import CreateSpreadsheetRequest

api.create_spreadsheet(CreateSpreadsheetRequest(format= 'xlsx'))
```

### Search Data in Spreadsheet

```python
from asposecellscloud.models import PutCellValueRequest

api.search_spreadsheet_content(SearchSpreadsheetContentRequest( 'TestData/'BookText.xlsx , 'Bike',ignoring_case= False))
```

## Supported Formats

|**Format**|**Description**|**Load**|**Save**|
| :- | :- | :- | :- |
|[XLS](https://docs.fileformat.com/spreadsheet/xls/)|Excel 95/5.0 - 2003 Workbook.|&radic;|&radic;|
|[XLSX](https://docs.fileformat.com/spreadsheet/xlsx/)|Office Open XML SpreadsheetML Workbook or template file, with or without macros.|&radic;|&radic;|
|[XLSB](https://docs.fileformat.com/spreadsheet/xlsb/)|Excel Binary Workbook.|&radic;|&radic;|
|[XLSM](https://docs.fileformat.com/spreadsheet/xlsm/)|Excel Macro-Enabled Workbook.|&radic;|&radic;|
|[XLT](https://docs.fileformat.com/spreadsheet/xlt/)|Excel 97 - Excel 2003 Template.|&radic;|&radic;|
|[XLTX](https://docs.fileformat.com/spreadsheet/xltx/)|Excel Template.|&radic;|&radic;|
|[XLTM](https://docs.fileformat.com/spreadsheet/xltm/)|Excel Macro-Enabled Template.|&radic;|&radic;|
|[XLAM](https://docs.fileformat.com/spreadsheet/xlam/)|An Excel Macro-Enabled Add-In file that's used to add new functions to Excel.| |&radic;|
|[CSV](https://docs.fileformat.com/spreadsheet/csv/)|CSV (Comma Separated Value) file.|&radic;|&radic;|
|[TSV](https://docs.fileformat.com/spreadsheet/tsv/)|TSV (Tab-separated values) file.|&radic;|&radic;|
|[TXT](https://docs.fileformat.com/word-processing/txt/)|Delimited plain text file.|&radic;|&radic;|
|[HTML](https://docs.fileformat.com/web/html/)|HTML format.|&radic;|&radic;|
|[MHTML](https://docs.fileformat.com/web/mhtml/)|MHTML file.|&radic;|&radic;|
|[ODS](https://docs.fileformat.com/spreadsheet/ods/)|ODS (OpenDocument Spreadsheet).|&radic;|&radic;|
|[Numbers](https://docs.fileformat.com/spreadsheet/numbers/)|The document is created by Apple's "Numbers" application which forms part of Apple's iWork office suite, a set of applications which run on the Mac OS X and iOS operating systems.|&radic;||
|[JSON](https://docs.fileformat.com/web/json/)|JavaScript Object Notation|&radic;|&radic;|
|[DIF](https://docs.fileformat.com/spreadsheet/dif/)|Data Interchange Format.| |&radic;|
|[PDF](https://docs.fileformat.com/pdf/)|Adobe Portable Document Format.| |&radic;|
|[XPS](https://docs.fileformat.com/page-description-language/xps/)|XML Paper Specification Format.| |&radic;|
|[SVG](https://docs.fileformat.com/page-description-language/svg/)|Scalable Vector Graphics Format.| |&radic;|
|[TIFF](https://docs.fileformat.com/image/tiff/)|Tagged Image File Format| |&radic;|
|[PNG](https://docs.fileformat.com/image/png/)|Portable Network Graphics Format| |&radic;|
|[BMP](https://docs.fileformat.com/image/bmp/)|Bitmap Image Format| |&radic;|
|[EMF](https://docs.fileformat.com/image/emf/)|Enhanced metafile Format| |&radic;|
|[JPEG](https://docs.fileformat.com/image/jpeg/)|JPEG is a type of image format that is saved using the method of lossy compression.| |&radic;|
|[GIF](https://docs.fileformat.com/image/gif/)|Graphical Interchange Format| |&radic;|
|[MARKDOWN](https://docs.fileformat.com/word-processing/md/)|Represents a markdown document.| |&radic;|
|[SXC](https://docs.fileformat.com/spreadsheet/sxc/)|An XML based format used by OpenOffice and StarOffice|&radic;|&radic;|
|[FODS](https://docs.fileformat.com/spreadsheet/fods/)|This is an Open Document format stored as flat XML.|&radic;|&radic;|
|[DOCX](https://docs.fileformat.com/word-processing/docx/)|A well-known format for Microsoft Word documents that is a combination of XML and binary files.||&radic;|
|[PPTX](https://docs.fileformat.com/presentation/pptx/)|The PPTX format is based on the Microsoft PowerPoint open XML presentation file format.||&radic;|
|[OTS](https://docs.fileformat.com/spreadsheet/ots/)|OTS (OpenDocument Spreadsheet).|&radic;|&radic;|
|[XML](https://docs.fileformat.com/web/xml/)|XML file.|&radic;|&radic;|
|[HTM](https://docs.fileformat.com/web/htm/)|HTM file.|&radic;|&radic;|
|[TIF](https://docs.fileformat.com/image/tiff/)|Tagged Image File Format| |&radic;|
|[WMF](https://docs.fileformat.com/image/wmf/)|WMF Image Format| |&radic;|
|[PCL](https://docs.fileformat.com/page-description-language/pcl/)|Printer Command Language Format| |&radic;|
|[AZW3](https://docs.fileformat.com/ebook/azw3/)|AZ3/KF8 File Format| |&radic;|
|[EPUB](https://docs.fileformat.com/ebook/epub/)|EPUB File Format| |&radic;|
|[DBF](https://docs.fileformat.com/ebook/epub/)|DBF File Format| |&radic;|
|[EPUB](https://docs.fileformat.com/database/dbf/)|database file| |&radic;|
|[XHTML](https://docs.fileformat.com/web/xhtml/)|XHTML File Format| |&radic;|

---

## Debugging & Error Handling

- Enable SDK logging:  
  `logging.basicConfig(level=logging.DEBUG)`  
- Catch `ApiException` for detailed error codes and messages.

---

## 6️⃣ Further Reading

- **Official Docs**: <https://docs.aspose.cloud/cells/>
- **Code Samples**: <https://github.com/aspose-cells-cloud/aspose-cells-cloud-python/examples>  
- **Live API Explorer**: <https://apireference.aspose.cloud/cells>

Combine the snippets above to start processing Excel in the cloud within minutes.
