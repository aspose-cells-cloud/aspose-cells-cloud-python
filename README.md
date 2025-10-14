![](https://img.shields.io/badge/aspose.cells%20Cloud%20SDK-25.10-green?style=for-the-badge&logo=python) [![Product Page](https://img.shields.io/badge/Product-0288d1?style=for-the-badge&logo=Google-Chrome&logoColor=white)](https://products.aspose.cloud/cells/python/) [![Documentation](https://img.shields.io/badge/Documentation-388e3c?style=for-the-badge&logo=Hugo&logoColor=white)](https://docs.aspose.cloud/cells/) [![API Ref](https://img.shields.io/badge/Reference-f39c12?style=for-the-badge&logo=html5&logoColor=white)](https://reference.aspose.cloud/cells/) [![Examples](https://img.shields.io/badge/Examples-1565c0?style=for-the-badge&logo=Github&logoColor=white)](https://github.com/aspose-cells-cloud/aspose-cells-cloud-perl/tree/master/Examples) [![Blog](https://img.shields.io/badge/Blog-d32f2f?style=for-the-badge&logo=WordPress&logoColor=white)](https://blog.aspose.cloud/categories/aspose.cells-cloud-product-family/) [![Support](https://img.shields.io/badge/Support-7b1fa2?style=for-the-badge&logo=Discourse&logoColor=white)](https://forum.aspose.cloud/c/cells/7) [![PyPI](https://img.shields.io/pypi/v/asposecellscloud?style=for-the-badge)](https://pypi.org/project/asposecellscloud/) [![PyPI - Python Version](https://img.shields.io/pypi/pyversions/asposecellscloud?style=for-the-badge)](https://www.python.org/) [![PyPI - Downloads](https://img.shields.io/pypi/dm/asposecellscloud?style=for-the-badge)](https://pypi.org/project/asposecellscloud/)  [![GitHub license](https://img.shields.io/github/license/aspose-cells-cloud/aspose-cells-cloud-python?style=for-the-badge)](https://github.com/aspose-cells-cloud/aspose-cells-cloud-python/blob/master/LICENSE) ![GitHub commits since latest release (by date)](https://img.shields.io/github/commits-since/aspose-cells-cloud/aspose-cells-cloud-python/25.10?style=for-the-badge)

[Aspose.Cells Cloud SDK for Python](https://products.aspose.cloud/cells/python) is a cloud-first REST API that lets Python applications create, read, edit, convert, and repair [Excel, ODS, CSV, JSON, and other spreadsheet files](https://docs.aspose.cloud/cells/supported-file-formats/) without installing Microsoft Office. It supports advanced features, including cell formatting, formulas, pivot tables, conditional styling, charts, hyperlinks, comments, data validation, document splitting, and merging, and runs on AWS, Azure, and Google Cloud, while ensuring data integrity.

## Quick Start Guide

To begin with Aspose.Cells Cloud, here's what you need to do:

1. Sign up for an account at [Aspose for Cloud](https://dashboard.aspose.cloud/#/apps) to obtain your client id and secret.
2. Install the Aspose.Cells Cloud Python package from the [pypi](https://pypi.org/).

```bash
   pip install asposecellscloud
```

3. Use the conversion code provided below as a reference to add or modify your application.

## Convert Excel to PDF Using Python

```python
from asposecellscloud.apis.cells_api import CellsApi
from asposecellscloud.models import *
from asposecellscloud.requests import *

CellsCloudClientId = "...."     # get from https://dashboard.aspose.cloud/#/applications
CellsCloudClientSecret = "...." # get from https://dashboard.aspose.cloud/#/applications

cellsApi = CellsApi(CellsCloudClientId,CellsCloudClientSecret)
cellsApi.convert_spreadsheet(ConvertSpreadsheetRequest( 'EmployeeSalesSummary.xlsx', 'pdf') , local_outpath = "EmployeeSalesSummary.pdf")
```

## Support file format

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

## Manipulate Excel and other spreadsheet files in the Cloud

- **File Manipulation**: Users can upload, download, delete, and manage Excel files stored in the cloud.
- **File Formatting**: Supports formatting of cells, fonts, colors, and alignment modes in Excel files to cater to users' specific requirements.
- **Data Processing**: Powerful functions for data processing including reading, writing, modifying cell data, performing formula calculations, and formatting data.
- **Formula Calculation**: Built-in formula engine handles complex formula calculations in Excel and returns accurate results.
- **Chart Manipulation**: Users can create, edit, and delete charts from Excel files for data analysis and visualization needs.
- **Table Processing**: Offers robust processing capabilities for various form operations such as creation, editing, formatting, and conversion, meeting diverse form processing needs.
- **Data Verification**: Includes data verification function to set cell data type, range, uniqueness, ensuring data accuracy and integrity.
- **Batch Processing**: Supports batch processing of multiple Excel documents, such as batch format conversion, data extraction, and style application..
- **Import/Export Data**: Facilitates importing data from various sources into spreadsheets and exporting spreadsheet data to other formats.
- **Security Management**: Offers a range of security features like data encryption, access control, and permission management to safeguard the security and integrity of spreadsheet data.

## Feature & Enhancements in Version v25.10

Full list of issues covering all changes in this release:

|**ID**|**Summary**|**Category**|
| :- | :- | :- |
| 57421 | Optimize data Transform API: replace delete with remove. | Improvement  |
| 57574 | Support to update the spreadsheet content words case in Cells Cloud 4.0. | Improvement  |
| 57575 | Support to remove characters from spreadsheet content in Cells Cloud 4.0. | Improvement  |
| 57576 | Support to add text for spreadsheet content in Cells Cloud 4.0. | Improvement  |
| 57577 | Support to convert text for spreadsheet content in Cells Cloud 4.0. | Improvement  |
| 57578 | Support to extract text for spreadsheet content in Cells Cloud 4.0. | Improvement  |
| 57579 | Support to extract text for spreadsheet content in Cells Cloud 4.0. | Improvement  |
| 57580 | Support to split text for spreadsheet content in Cells Cloud 4.0. | Improvement  |

## Available SDKs

The Aspose.Cells Cloud SDK is available in multiple popular programming languages, enabling developers to integrate spreadsheet processing capabilities across various development environments.

[![Go](https://img.shields.io/badge/Go-00ADD8.svg?style=for-the-badge&logo=go&logoColor=white)](https://github.com/aspose-cells-cloud/aspose-cells-cloud-go) [![Go](https://img.shields.io/badge/Go-asposecellscloud-%2300ADD8?logo=go&style=for-the-badge)](https://pkg.go.dev/github.com/aspose-cells-cloud/aspose-cells-cloud-go/v25)

[![Java](https://img.shields.io/badge/Java-red?logo=openjdk&style=for-the-badge&logoColor=white)](https://github.com/aspose-cells-cloud/aspose-cells-cloud-java) [![Java](https://img.shields.io/badge/Maven-Aspose.Cells.Cloud.pom.xml-red?logo=apache-maven&style=for-the-badge)](https://github.com/aspose-cells-cloud/aspose-cells-cloud-java/blob/master/Aspose.Cells.Cloud.pom.xml)

[![C#](https://img.shields.io/badge/.NET-%23512BD4?style=for-the-badge&logo=dotnet&logoColor=white)](https://github.com/aspose-cells-cloud/aspose-cells-cloud-dotnet) [![.NET](https://img.shields.io/badge/NuGet-Aspose.Cells--Cloud-%23512BD4?logo=nuget&style=for-the-badge)](https://www.nuget.org/packages/Aspose.cells-Cloud/#readme-body-tab)

[![Node.js](https://img.shields.io/badge/Node.js-43853D.svg?style=for-the-badge&logo=node.js&logoColor=white)](https://github.com/aspose-cells-cloud/aspose-cells-cloud-node) [![Node.js](https://img.shields.io/badge/npm-asposecellscloud-orange?logo=npm&style=for-the-badge)](https://www.npmjs.com/package/asposecellscloud)

[![Perl](https://img.shields.io/badge/Perl-39457E.svg?style=for-the-badge&logo=perl&logoColor=white)](https://github.com/aspose-cells-cloud/aspose-cells-cloud-perl) [![Perl](https://img.shields.io/badge/CPAN-AsposeCellsCloud--CellsApi-blue?logo=perl&style=for-the-badge)](https://metacpan.org/dist/AsposeCellsCloud-CellsApi)

[![PHP](https://img.shields.io/badge/PHP-777BB4.svg?style=for-the-badge&logo=php&logoColor=white)](https://github.com/aspose-cells-cloud/aspose-cells-cloud-php) [![PHP](https://img.shields.io/badge/Composer-aspose/cells--sdk--php-8892BF?logo=php&style=for-the-badge)](https://packagist.org/packages/aspose/cells-sdk-php)

[![Python](https://img.shields.io/badge/Python-14354C.svg?style=for-the-badge&logo=python&logoColor=white)](https://github.com/aspose-cells-cloud/aspose-cells-cloud-python) [![Python](https://img.shields.io/badge/pip-asposecellscloud-blue?logo=pypi&style=for-the-badge)](https://pypi.org/project/asposecellscloud/)

[![Ruby](https://img.shields.io/badge/Ruby-CC342D.svg?style=for-the-badge&logo=ruby&logoColor=white)](https://github.com/aspose-cells-cloud/aspose-cells-cloud-ruby) [![Ruby](https://img.shields.io/badge/Gem-aspose__cells__cloud-red?logo=ruby&style=for-the-badge)](https://rubygems.org/gems/aspose_cells_cloud)

## [Release history version](CHANGELOG.md)
