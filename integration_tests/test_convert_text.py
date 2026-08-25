"""Integration tests for ConvertText (generated from TestingData)."""

import os

import pytest

from aspose.cells.cloud import CellsCloudClient
from aspose.cells.cloud.request import ConvertTextRequest


def test_convert_text(client):
    """Test for update word case local spreadsheet file.."""
    request = ConvertTextRequest(
        convert_text_type="ConvertNumberToText",
        spreadsheet="testdata/BookText.xlsx",
    )

    response = client.do(request)
    assert response is not None


def test_convert_text_with_convert_characters(client):
    """Test for update word case local spreadsheet file.."""
    request = ConvertTextRequest(
        convert_text_type="ConvertCharacters",
        source_characters="Bikes",
        target_characters="MOTO",
        spreadsheet="testdata/BookText.xlsx",
    )

    response = client.do(request)
    assert response is not None


def test_convert_text_with_convert_write_space(client):
    """Test for update word case local spreadsheet file.."""
    request = ConvertTextRequest(
        convert_text_type="ConvertWriteSpace",
        target_characters="MOTO",
        worksheet="Bikes",
        spreadsheet="testdata/BookText.xlsx",
    )

    response = client.do(request)
    assert response is not None
