# API Reference

## Overview

The Aspose.Cells Cloud SDK for Python exposes **461 API operations across 42 controllers** through a
single `aspose.cells.cloud.CellsCloudClient`.

## Client

### Initialization

```python
from aspose.cells.cloud import CellsCloudClient

client = CellsCloudClient(
    "your-client-id",             # Aspose Cloud Client ID
    "your-client-secret",         # Aspose Cloud Client Secret
    "https://api.aspose.cloud",   # base URL (optional; defaults to production)
)

client.configuration.timeout = 30            # seconds (default 30)
client.configuration.retries = 3             # default 0
client.configuration.add_default_header("X-Custom", "value")
```

### Executing Requests

```python
from aspose.cells.cloud import CellsCloudClient, SDKError
from aspose.cells.cloud.request import PostCellCharactersRequest

request = PostCellCharactersRequest(
    name="Book1.xlsx",
    sheet_name="Sheet1",
    cell_name="D4",
    folder="TestData/In",        # optional
    options=[font_setting],      # optional
)

try:
    response = client.do(request)           # raises SDKError on failure
    print(response.status_code)
    print(response)                         # __str__() => body
except SDKError as e:
    print(f"SDK error: {e}", file=sys.stderr)
```

`do(request)` executes a single request and returns a `RichResponse`. To run several requests at once,
use `do_batch(*requests)`, which returns a `List[RichResponse]`.

### Response

```python
class RichResponse:
    status_code: int                  # HTTP status code
    headers: Dict[str, str]           # response headers
    body: bytes                       # raw body

    def __str__(self) -> str          # body decoded as UTF-8
    def to_bytes(self) -> bytes       # body as bytes
    def get_json(self, cls=None)      # decode JSON; optionally hydrate a model
```

## Controllers

Operations are grouped by controller. Each operation maps to a request class under
`aspose/cells/cloud/request/` (snake_case module, `PascalCase` class).

### CellsController (40 operations)

Cell-level operations on worksheets.

| Operation | Method | Path |
|-----------|--------|------|
| `PostClearContents` | POST | `/cells/{name}/worksheets/{sheetName}/cells/clearcontents` |
| `PostClearFormats` | POST | `/cells/{name}/worksheets/{sheetName}/cells/clearformats` |
| `PostCopyCellIntoCell` | POST | `/cells/{name}/worksheets/{sheetName}/cells/{cellName}/copy` |
| `PostSetCellHtmlString` | POST | `/cells/{name}/worksheets/{sheetName}/cells/{cellName}/htmlstring` |
| `PostSetCellRangeValue` | POST | `/cells/{name}/worksheets/{sheetName}/cells` |
| `PostUpdateWorksheetRangeStyle` | POST | `/cells/{name}/worksheets/{sheetName}/cells/style` |
| `PostWorksheetMerge` | POST | `/cells/{name}/worksheets/{sheetName}/cells/merge` |
| `PostWorksheetUnmerge` | POST | `/cells/{name}/worksheets/{sheetName}/cells/unmerge` |
| `PostCellCharacters` | POST | `/cells/{name}/worksheets/{sheetName}/cells/{cellName}/characters` |
| `GetWorksheetColumns` | GET | `/cells/{name}/worksheets/{sheetName}/columns` |
| `GetWorksheetRows` | GET | `/cells/{name}/worksheets/{sheetName}/cells/rows` |
| `GetWorksheetCell` | GET | `/cells/{name}/worksheets/{sheetName}/cells/{cellName}` |
| `GetWorksheetCellStyle` | GET | `/cells/{name}/worksheets/{sheetName}/cells/{cellName}/style` |

### WorkbookController (25 operations)

| Operation | Method | Path |
|-----------|--------|------|
| `PostWorkbookSaveAs` | POST | `/cells/{name}/saveAs` |
| `PostWorkbookMerge` | POST | `/cells/{name}/merge` |
| `PostWorkbookSplit` | POST | `/cells/{name}/split` |
| `PostWorkbookProtect` | POST | `/cells/{name}/protection` |
| `PostWorkbookEncrypt` | POST | `/cells/{name}/encryption` |
| `PostWorkbookDecrypt` | POST | `/cells/{name}/decryption` |
| `PostWorkbookSettings` | POST | `/cells/{name}/settings` |
| `GetWorkbook` | GET | `/cells/{name}` |
| `GetWorkbookSettings` | GET | `/cells/{name}/settings` |
| `CreateWorkbook` | PUT | `/cells/{name}` |

### WorksheetsController (39 operations)

| Operation | Method | Path |
|-----------|--------|------|
| `PutAddNewWorksheet` | PUT | `/cells/{name}/worksheets/{sheetName}` |
| `DeleteWorksheet` | DELETE | `/cells/{name}/worksheets/{sheetName}` |
| `PostCopyWorksheet` | POST | `/cells/{name}/worksheets/{sheetName}/copy` |
| `PostRenameWorksheet` | POST | `/cells/{name}/worksheets/{sheetName}/rename` |
| `PostMoveWorksheet` | POST | `/cells/{name}/worksheets/{sheetName}/move` |
| `PostHideWorksheet` | POST | `/cells/{name}/worksheets/{sheetName}/hide` |
| `PostUnhideWorksheet` | POST | `/cells/{name}/worksheets/{sheetName}/unhide` |
| `GetWorksheet` | GET | `/cells/{name}/worksheets/{sheetName}` |
| `GetWorksheets` | GET | `/cells/{name}/worksheets` |

### ConversionController (42 operations)

| Operation | Method | Path |
|-----------|--------|------|
| `PostWorkbookSaveAs` | POST | `/cells/{name}/saveAs` |
| `PutConvertWorkbook` | PUT | `/cells/convert` |
| `GetWorksheetWithFormat` | GET | `/cells/{name}/worksheets/{sheetName}` |
| `PostWorkbookExportAs` | POST | `/cells/{name}/export` |
| `PostWorkbookToPdf` | POST | `/cells/{name}/toPdf` |
| `PostWorkbookToHtml` | POST | `/cells/{name}/toHtml` |

### ChartsController (24 operations)

| Operation | Method | Path |
|-----------|--------|------|
| `PutWorksheetAddChart` | PUT | `/cells/{name}/worksheets/{sheetName}/charts` |
| `DeleteWorksheetChart` | DELETE | `/cells/{name}/worksheets/{sheetName}/charts/{chartIndex}` |
| `GetWorksheetChart` | GET | `/cells/{name}/worksheets/{sheetName}/charts/{chartIndex}` |
| `GetWorksheetCharts` | GET | `/cells/{name}/worksheets/{sheetName}/charts` |
| `PostWorksheetChart` | POST | `/cells/{name}/worksheets/{sheetName}/charts/{chartIndex}` |

### DataProcessingController (23 operations)

| Operation | Method | Path |
|-----------|--------|------|
| `PostWorkbookMerge` | POST | `/cells/{name}/merge` |
| `PostWorkbookSplit` | POST | `/cells/{name}/split` |
| `PostImportData` | POST | `/cells/{name}/importdata` |
| `PostWorkbookProtect` | POST | `/cells/{name}/protection` |

### File & Storage Controllers

| Operation | Method | Path |
|-----------|--------|------|
| `UploadFile` | PUT | `/cells/storage/file/{path}` |
| `DownloadFile` | GET | `/cells/storage/file/{path}` |
| `CopyFile` | PUT | `/cells/storage/file/copy/{path}` |
| `MoveFile` | PUT | `/cells/storage/file/move/{path}` |
| `DeleteFile` | DELETE | `/cells/storage/file/{path}` |
| `CreateFolder` | PUT | `/cells/storage/folder/{path}` |
| `DeleteFolder` | DELETE | `/cells/storage/folder/{path}` |
| `GetFilesList` | GET | `/cells/storage/folder/{path}` |
| `GetDiscUsage` | GET | `/cells/storage/disc` |

### Other Notable Controllers

| Controller | Operations | Key Features |
|-----------|-----------|-------------|
| `TextProcessingController` | 24 | Add/extract/convert/trim text, word case |
| `PivotTablesController` | 21 | Pivot table CRUD and filtering |
| `LightCellsController` | 15 | Lightweight batch operations |
| `SearchController` | 14 | Text search and replace |
| `RangesController` | 14 | Named range operations |
| `AutoFilterController` | 13 | AutoFilter and date/custom filters |
| `ListObjectsController` | 13 | List objects (tables) management |
| `ConditionalFormattingsController` | 9 | Format conditions, data bars |
| `ShapesController` | 8 | Shape management |
| `PicturesController` | 7 | Picture insert/update/delete |
| `SparklineGroupsController` | 6 | Sparkline management |
| `AIController` | 5 | AI translation, summarization |
| `BatchController` | 5 | Batch convert/protect/lock/split |

## Common Parameters

Available across most operations (as optional keyword arguments):

| Keyword | Python type | Description |
|---------|-------------|-------------|
| `folder` | `Optional[str]` | Remote folder path |
| `storage_name` | `Optional[str]` | Storage name (default: empty) |
| `password` | `Optional[str]` | File password for encrypted files |
| `region` | `Optional[str]` | Locale setting (e.g. `en-US`) |

## Error Handling

All request/HTTP failures raise an `SDKError` (a `Exception` subclass):

```python
try:
    response = client.do(request)
except SDKError as e:
    print(f"SDK Error [{e.code}]: {e}", file=sys.stderr)
```
