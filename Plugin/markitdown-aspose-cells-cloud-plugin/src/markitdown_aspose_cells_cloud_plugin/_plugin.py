import io
import os
from typing import Any, BinaryIO

from markitdown import (
    DocumentConverter,
    DocumentConverterResult,
    MarkItDown,
    StreamInfo,
)

from asposecellscloud.requests import ConvertSpreadsheetRequest
from asposecellscloud.apis import CellsApi

__plugin_interface_version__ = (
    1  # The version of the plugin interface that this plugin uses
)

ACCEPTED_MIME_TYPE_PREFIXES = [
    "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",  # .xlsx
    "application/vnd.ms-excel",                                           # .xls
    "application/vnd.oasis.opendocument.spreadsheet",                     # .ods
]

ACCEPTED_FILE_EXTENSIONS = [".xlsx",".xls",".ods"]


def register_converters(markitdown: MarkItDown, **kwargs):
    """
    Called during construction of MarkItDown instances to register converters provided by plugins.
    """
    markitdown.register_converter(AsposeCellsCloudConverter())

    # E,g. for Windows: Set CellsCloudClientId and CellsCloudClientSecret
    # PowerShell: $env:CellsCloudClientId = "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
    # PowerShell: $env:CellsCloudClientSecret = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
    # CDM:        set CellsCloudClientId="xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
    # CDM:        set CellsCloudClientSecret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"


class AsposeCellsCloudConverter(DocumentConverter):
    """
    Converts an Excel file to in the simplest possible way.
    """

    def accepts(
        self,
        file_stream: BinaryIO,
        stream_info: StreamInfo,
        **kwargs: Any,
    ) -> bool:
        mimetype = (stream_info.mimetype or "").lower()
        extension = (stream_info.extension or "").lower()

        if extension in ACCEPTED_FILE_EXTENSIONS:
            return True

        for prefix in ACCEPTED_MIME_TYPE_PREFIXES:
            if mimetype.startswith(prefix):
                return True

        return False

    def convert(
        self,
        file_stream: BinaryIO,
        stream_info: StreamInfo,
        **kwargs: Any,
    ) -> DocumentConverterResult:
        instance = CellsApi(os.getenv('CellsCloudClientId'), os.getenv('CellsCloudClientSecret'))
        binary_data: bytes  = file_stream.read()
        request = ConvertSpreadsheetRequest(binary_data, 'md')
        result = instance.convert_spreadsheet(request)
        # Set other properties
        # ...
        with open(result, "rb") as f:
            file_in_memory = io.BytesIO(f.read())
        textStr = file_in_memory.getvalue().decode('utf-8')
        return DocumentConverterResult(
            title=None,
            markdown=textStr,
        )

