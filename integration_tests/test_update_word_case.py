"""Integration tests for UpdateWordCase (generated from TestingData)."""

import os

import pytest

from aspose.cells.cloud import CellsCloudClient
from aspose.cells.cloud.request import UpdateWordCaseRequest


def test_update_word_case(client):
    """Test for update word case local spreadsheet file.."""
    request = UpdateWordCaseRequest(
        word_case_type="ProperCase",
        worksheet="Bikes",
        spreadsheet="testdata/BookText.xlsx",
    )

    response = client.do(request)
    assert response is not None


def test_update_word_case_in_range(client):
    """Test for update word case local spreadsheet file.."""
    request = UpdateWordCaseRequest(
        word_case_type="ProperCase",
        worksheet="Bikes",
        range_="A1:B15",
        spreadsheet="testdata/BookText.xlsx",
    )

    response = client.do(request)
    assert response is not None


def test_update_word_case_in_spreadsheet(client):
    """Test for update word case local spreadsheet file.."""
    request = UpdateWordCaseRequest(
        word_case_type="ProperCase",
        spreadsheet="testdata/BookText.xlsx",
    )

    response = client.do(request)
    assert response is not None
