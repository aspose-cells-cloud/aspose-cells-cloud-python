"""Integration tests for AddText (generated from TestingData)."""

import os

import pytest

from aspose.cells.cloud import CellsCloudClient
from aspose.cells.cloud.request import AddTextRequest


def test_add_text(client):
    """Test for trim local spreadsheet file.."""
    request = AddTextRequest(
        text="New",
        position="AtTheBeginning",
        select_text="text",
        spreadsheet="testdata/BookText.xlsx",
    )

    response = client.do(request)
    assert response is not None


def test_add_text_skip_empty_cells(client):
    """Test for trim local spreadsheet file.."""
    request = AddTextRequest(
        text="New",
        position="AtTheBeginning",
        skip_empty_cells=True,
        worksheet="Bikes",
        spreadsheet="testdata/BookText.xlsx",
    )

    response = client.do(request)
    assert response is not None


def test_add_text_in_range(client):
    """Test for trim local spreadsheet file.."""
    request = AddTextRequest(
        text="New",
        position="AtTheBeginning",
        skip_empty_cells=True,
        worksheet="Bikes",
        range_="A1:B15",
        spreadsheet="testdata/BookText.xlsx",
    )

    response = client.do(request)
    assert response is not None


def test_add_text_before_text(client):
    """Test for trim local spreadsheet file.."""
    request = AddTextRequest(
        text="New",
        position="BeforeText",
        worksheet="Bikes",
        select_text="bike",
        spreadsheet="testdata/BookText.xlsx",
    )

    response = client.do(request)
    assert response is not None
