"""Integration tests for TrimSpreadsheet (generated from TestingData)."""

import os

import pytest

from aspose.cells.cloud import CellsCloudClient
from aspose.cells.cloud.request import TrimCharacterRequest


def test_trim_character(client):
    """Test for trim local spreadsheet file.."""
    request = TrimCharacterRequest(
        trim_leading=True,
        trim_trailing=True,
        trim_space_between_word_to1=True,
        trim_non_breaking_spaces=True,
        remove_extra_line_breaks=True,
        remove_all_line_breaks=True,
        spreadsheet="testdata/BookText.xlsx",
    )

    response = client.do(request)
    assert response is not None


def test_start_trim_character(client):
    """Test for trim local spreadsheet file.."""
    request = TrimCharacterRequest(
        trim_leading=True,
        trim_trailing=False,
        trim_space_between_word_to1=False,
        trim_non_breaking_spaces=True,
        remove_extra_line_breaks=True,
        remove_all_line_breaks=True,
        spreadsheet="testdata/BookText.xlsx",
    )

    response = client.do(request)
    assert response is not None


def test_trim_worksheet(client):
    pytest.skip("API TrimWorksheetRange is not defined in the specification")


def test_trim_range(client):
    pytest.skip("API TrimWorksheetRange is not defined in the specification")
