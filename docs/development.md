# Development Guide

## Project Overview

This SDK is generated from `aspose.cells.cloud.specification.json` (461 operations, 42 controllers,
483 data models) and mirrors the structure of the Aspose.Cells Cloud SDK for Go, translated to Python.

## Directory Structure

```
cells-cloud-sdk-python/
├── pyproject.toml                      # packaging + dependencies
├── run_integration_tests.ps1           # PowerShell integration runner + report
├── aspose/cells/cloud/                 # the package
│   ├── __init__.py
│   ├── version.py
│   ├── cells_cloud_client.py
│   ├── configuration.py
│   ├── request_option.py               # abstract base class
│   ├── rich_response.py
│   ├── sdk_error.py
│   ├── model/                          # 483 model modules
│   └── request/                        # 461 request modules
├── tests/                              # offline unit tests (no credentials/network)
├── integration_tests/                  # integration tests (JSON-driven)
├── testdata/                           # sample XLSX / CSV files
├── generate_models.py                  # model generation script
├── generate_requests.py                # request generation script
├── generate_tests.py                   # test generation script
└── references/                         # generation rules (see ../references)
```

## Code Generation

### Prerequisites

- Python 3.8+ and `pip`.
- The API specification file: `aspose.cells.cloud.specification.json`.
- Generation scripts in the project root.

### Generate Models

```bash
python generate_models.py
```

Reads the `Models` array and generates one module per model under `aspose/cells/cloud/model/`. Each
model follows [references/model_generation_rules.md](../references/model_generation_rules.md).

### Generate Requests

```bash
python generate_requests.py
```

Reads the `Operations` array and generates one request class per operation under
`aspose/cells/cloud/request/`, following
[references/request_generation_rules.md](../references/request_generation_rules.md).

### Generate Tests

```bash
python generate_tests.py
```

Reads `TestingData/` JSON files and generates pytest cases under `integration_tests/`, following
[references/test_generation_rules.md](../references/test_generation_rules.md).

## Testing

Two test layers ship with the SDK:

- **Offline unit tests** (`tests/`) — model serialization, request building, configuration, and the
  (mocked) client pipeline. Run with `python -m pytest tests`; no credentials or network required.
- **Integration tests** (`integration_tests/`) — generated from `TestingData/`, exercise the live
  API, and require Aspose Cloud credentials. Run with
  `python -m pytest integration_tests`, or via the PowerShell runner:

  ```powershell
  .\run_integration_tests.ps1   # runs, tallies, and writes test_report/report.md
  ```

See [testing.md](testing.md) for the full test guide.

## Type Mapping

| Spec `DataType.Identifier` | Go type | Python type (type hint) |
|----------------------------|---------|-------------------------|
| `String` | `string` | `str` / `Optional[str]` |
| `Boolean` | `*bool` | `bool` / `Optional[bool]` |
| `Integer` | `*int32` | `int` / `Optional[int]` |
| `Long` | `*int64` | `int` / `Optional[int]` |
| `Floating` | `*float64` | `float` / `Optional[float]` |
| `DateTime` | `time.Time` | `datetime.datetime` (ISO 8601) |
| `Byte` | `[]byte` | `bytes` |
| `Class` (Reference) | `*Ref` | `Ref` / `Optional[Ref]` |
| `Container` (Reference) | `[]Ref` | `List[Ref]` |
| `Array` (ElementDataType) | `[]T` | `List[T]` |
| `Object` / `Any` | `map[string]interface{}` / `interface{}` | `Dict[str, Any]` / `Any` |

> **Nullability is free in Python.** `Optional[T]` (i.e. `T | None`) defaults to `None`, which is
> omitted from `to_dict()` output — reproducing the Go SDK's `omitempty` with no pointer helpers or
> boxing.

## Key Design Patterns

### Request Base Class

Every request class inherits from `RequestOption`, an `abc.ABC`:

```python
from abc import ABC, abstractmethod
from typing import Dict, Optional


class RequestOption(ABC):
    @abstractmethod
    def get_method(self) -> str:
        """GET / POST / PUT / DELETE."""

    @abstractmethod
    def get_path(self) -> str:
        """Path with {param} already substituted."""

    def get_query_parameters(self) -> Dict[str, str]:
        return {}

    def get_header_parameters(self) -> Dict[str, str]:
        return {}

    def get_json_body(self) -> Optional[dict]:
        return None

    def get_multipart_form(self) -> Optional[dict]:
        return None
```

### Required & Optional Parameters

Required parameters are required `__init__` arguments, validated there (the analog of the Go SDK
returning `nil` on a missing required arg). Optional parameters are keyword arguments defaulting to
`None`:

```python
request = PostClearContentsRequest(
    name="Book1.xlsx",        # required
    sheet_name="Sheet1",      # required
    range="A1:C10",           # optional
    folder="TestData/In",     # optional
)
```

This mirrors the Go SDK's `NewXxxRequest(required..., opts...)` / `WithCommonParameter` pattern with
Python's keyword-argument idiom — no fluent setter chain.

### Parameter Type Rules

| Parameter Type | Required | Optional |
|---------------|----------|----------|
| string | `str` (validated non-empty) | `Optional[str]` (None/empty = omitted) |
| integer / boolean / floating | `int` / `bool` / `float` (validated) | `Optional[...]` (None = omitted) |
| Class | `Type` (validated non-None) | `Optional[Type]` (None = omitted) |
| Container / Array | `List[T]` | `Optional[List[T]]` |

### Model Serialization

Models expose `to_dict()` mapping `snake_case` fields to their **PascalCase wire names**, skipping
`None` values, and `to_json()` delegates to it. See
[references/model_generation_rules.md](../references/model_generation_rules.md).

## Adding New APIs

1. Add the operation (and any new models) to `aspose.cells.cloud.specification.json`.
2. Run `python generate_models.py` to (re)generate model modules.
3. Run `python generate_requests.py` to (re)generate request classes.
4. Add test data to `TestingData/` and run `python generate_tests.py`.
5. Lint and test:

```bash
python -m compileall aspose          # syntax check
python -m ruff check                 # lint
python -m pytest                     # test
```

## Contributing

1. Follow the naming and layout conventions in `CLAUDE.md`.
2. Models use `@dataclass` + `Optional` fields + `to_dict()`/`to_json()`.
3. Requests inherit `RequestOption`; validate required args (raise `ValueError`).
4. Raise `SDKError` for HTTP failures, `ValueError` for bad local input — never a bare `Exception`.
5. Run `python -m compileall aspose` and `python -m pytest` before submitting changes.
