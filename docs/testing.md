# Testing Guide

## Overview

The integration test suite contains **489 test functions across 46 test groups**, generated from JSON
configuration files in `TestingData/` and executed with pytest.

## Test Structure

```
integration_tests/
├── test_cells_controller.py             # 40 tests for CellsController
├── test_conversion.py                   # 32 tests for ConversionController
├── test_workbook_controller.py          # 32 tests for WorkbookController
├── test_worksheet_controller.py         # 39 tests for WorksheetsController
├── test_light_cells.py                  # 19 tests for LightCellsController
├── test_pivot_tables_controller.py      # 19 tests for PivotTablesController
├── test_charts_controller.py            # 14 tests for ChartsController
└── ...                                  # 39 more test files
```

## Test Configuration Format

Tests are defined in JSON files under `TestingData/` (same schema as the Go SDK):

```json
{
  "Name": "CellsController",
  "Folder": "CellsCloud30",
  "Variables": { "RemoteFolder": "TestData/In" },
  "Cases": [
    {
      "Name": "PostClearContents",
      "ApiMethod": "PostClearContents",
      "Description": ["Test for PostClearContents."],
      "Variables": { "LocalName": "Book1.xlsx", "RemoteName": "Book1.xlsx" },
      "Files": [
        { "LocalPath": "%LocalName%", "RemotePath": "%RemoteFolder%/%RemoteName%", "StorageName": "" }
      ],
      "Parameters": [
        { "Name": "name", "DataType": { "Identifier": "String" }, "Value": "%RemoteName%" }
      ],
      "Assertions": [
        { "Type": "EqualsInteger", "Expression": "Code", "Value": "200" }
      ]
    }
  ]
}
```

## Running Tests

### Prerequisites

1. Valid Aspose Cloud credentials.
2. Python 3.8+ and `pip install -e .`.
3. Test data files in `testdata/`.

### Setup

```bash
export CellsCloudClientId="your-client-id"
export CellsCloudClientSecret="your-client-secret"
export CellsCloudApiBaseUrl="https://api.aspose.cloud"
```

### Execute

```bash
# Run all integration tests
python -m pytest integration_tests

# Run a single controller's tests
python -m pytest integration_tests/test_cells_controller.py

# Run a single test function
python -m pytest integration_tests/test_cells_controller.py::test_post_clear_contents

# Run tests matching a substring
python -m pytest integration_tests -k post_clear_contents
```

### PowerShell runner (integration tests + report)

`run_integration_tests.ps1` wraps the pytest run, tallies results, and generates a report:

```powershell
.\run_integration_tests.ps1
.\run_integration_tests.ps1 -ClientId "..." -ClientSecret "..."
.\run_integration_tests.ps1 -BaseUrl "https://api.aspose.cloud" -ReportDir "test_report"
```

The script:

1. Locates Python and prints its version.
2. Exports `CellsCloudClientId`, `CellsCloudClientSecret`, and `CellsCloudApiBaseUrl`
   (tests are reported as *skipped* when credentials are absent).
3. Runs `python -m pytest integration_tests -q --junitxml=test_report/results.xml`.
4. Parses the JUnit XML and prints a summary (total / passed / failed / errored / skipped / pass
   rate).
5. Writes `test_report/report.md` (summary + per-module table + failure detail) and
   `test_report/results.xml` (raw JUnit).

Pass `-NoReport` to print the summary to the console without writing files.

## Generated Test Pattern

Each test case follows this structure:

```python
import os

import pytest

from aspose.cells.cloud import CellsCloudClient
from aspose.cells.cloud.request import PostClearContentsRequest


@pytest.fixture(scope="module")
def client():
    return CellsCloudClient(
        os.environ["CellsCloudClientId"],
        os.environ["CellsCloudClientSecret"],
        os.environ["CellsCloudApiBaseUrl"],
    )


def test_post_clear_contents(client):
    request = PostClearContentsRequest(
        name="Book1.xlsx",
        sheet_name="Sheet1",
        range="A1:C10",
        folder="TestData/In",
    )

    response = client.do(request)          # raises SDKError on failure

    assert response.status_code == 200
```

## Test Parameter Mapping

| Spec Parameter | Test Data Value | Keyword Argument |
|---------------|----------------|------------------|
| Required, Path, String | `"Book1.xlsx"` | `name="Book1.xlsx"` |
| Required, FormData, File | `"testdata/file.xlsx"` | `spreadsheet="testdata/file.xlsx"` |
| Optional, Query, Integer | `0` | `offset=0` |
| Optional, Query, String | `"value"` | `folder="value"` |
| Required, Body, Class | `{...}` | `options=Model()` (placeholder) |

## Variable Resolution

Test data uses `%VariableName%` placeholders resolved against group-level and case-level `Variables`.

## Known Limitations

1. **Complex object initialization**: Class/Container parameters are initialized with empty models;
   manual adjustment may be needed for tests requiring specific field values.
2. **Unresolved variables**: undefined variables produce empty strings.
3. **Unmatched APIs**: test cases referencing APIs not in the spec are skipped with a warning
   (`pytest.skip`).
4. **File uploads**: tests requiring pre-uploaded files need manual upload before execution.

## Adding New Tests

1. Create or update a JSON file in `TestingData/`.
2. Run `python generate_tests.py`.
3. Run `python -m pytest integration_tests`.
4. Add any required sample files to `testdata/`.

## Continuous Integration

Tests require credentials and network access. They are designed for local development, CI (service
principal credentials), and smoke runs (a subset of critical-path tests). In CI, set the three
environment variables and run `python -m pytest`.
