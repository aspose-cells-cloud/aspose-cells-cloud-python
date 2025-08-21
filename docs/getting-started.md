# Aspose.Cells Cloud SDK for Python – Quick Start

> **In 3 minutes** you’ll have a working Python script that converts Excel → PDF and uploads files to Aspose Cloud Storage.

---

## Sign Up & Get API Keys

1. **Create a free account** → [Aspose ID Sign-Up](https://id.containerize.com/signup)  
2. **Grab your Client ID & Client Secret** → [Aspose Cloud Dashboard](https://dashboard.aspose.cloud/#/applications)

---

## Install the SDK from PyPI

```bash
pip install asposecellscloud
```

> Package page: [asposecellscloud on PyPI](https://pypi.org/project/asposecellscloud/)

---

## Minimal Code Examples

### 🔁 Convert Excel (XLSX) to PDF

```python
from asposecellscloud.apis.cells_api import CellsApi
from asposecellscloud.models import *
from asposecellscloud.requests import *

CellsCloudClientId = "...."     # get from https://dashboard.aspose.cloud/#/applications
CellsCloudClientSecret = "...." # get from https://dashboard.aspose.cloud/#/applications

cellsApi = CellsApi(CellsCloudClientId,CellsCloudClientSecret)
cellsApi.convert_spreadsheet(ConvertSpreadsheetRequest( 'EmployeeSalesSummary.xlsx', 'pdf') , local_outpath = "EmployeeSalesSummary.pdf")
```

### 📤 Upload File to Cloud Storage

```python
from asposecellscloud.apis.cells_api import CellsApi
from asposecellscloud.models import *
from asposecellscloud.requests import *

CellsCloudClientId = "...."     # get from https://dashboard.aspose.cloud/#/applications
CellsCloudClientSecret = "...." # get from https://dashboard.aspose.cloud/#/applications

cellsApi = CellsApi(CellsCloudClientId,CellsCloudClientSecret)
cellsApi.upload_file(UploadFileRequest("EmployeeSalesSummary.Xlsx", 'SDKPython/CellsCloud/EmployeeSalesSummary.Xlsx'))
```
