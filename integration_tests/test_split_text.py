"""Integration tests for SplitText (generated from TestingData)."""

import os

import pytest

from aspose.cells.cloud import CellsCloudClient
from aspose.cells.cloud.request import SplitTextRequest


def test_split_text(client):
    """Test for update word case local spreadsheet file.."""
    request = SplitTextRequest(
        delimiters="Comma",
        keep_delimiters_in_resulting_cells=True,
        keep_delimiters_position="BeforeText",
        how_to_split="SplitToColumns",
        worksheet="Bikes",
        range_="A1:A10",
        spreadsheet="testdata/BookText.xlsx",
    )

    response = client.do(request)
    assert response is not None
