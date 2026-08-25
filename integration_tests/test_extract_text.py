"""Integration tests for ExtractText (generated from TestingData)."""

import os

import pytest

from aspose.cells.cloud import CellsCloudClient
from aspose.cells.cloud.request import ExtractTextRequest


def test_extract_text(client):
    """Test for update word case local spreadsheet file.."""
    request = ExtractTextRequest(
        extract_text_type="ExtractFirstCharacter",
        before_position=10,
        after_position=0,
        out_position_range="F1:F10",
        worksheet="Bikes",
        range_="A1:A10",
        spreadsheet="testdata/BookText.xlsx",
    )

    response = client.do(request)
    assert response is not None


def test_extract_text_with_extract_last_character(client):
    """Test for update word case local spreadsheet file.."""
    request = ExtractTextRequest(
        extract_text_type="ExtractLastCharacter",
        before_position=0,
        after_position=10,
        out_position_range="F1:F10",
        worksheet="Bikes",
        range_="A1:A10",
        spreadsheet="testdata/BookText.xlsx",
    )

    response = client.do(request)
    assert response is not None


def test_extract_text_with_extract_text_after(client):
    """Test for update word case local spreadsheet file.."""
    request = ExtractTextRequest(
        extract_text_type="ExtractTextAfter",
        before_position=0,
        after_position=0,
        after_text="bikes",
        out_position_range="F1:F10",
        worksheet="Bikes",
        range_="A1:A10",
        spreadsheet="testdata/BookText.xlsx",
    )

    response = client.do(request)
    assert response is not None
