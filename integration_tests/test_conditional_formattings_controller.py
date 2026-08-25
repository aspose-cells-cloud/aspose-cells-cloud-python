"""Integration tests for ConditionalFormattingsController (generated from TestingData)."""

import os

import pytest

from aspose.cells.cloud import CellsCloudClient
from aspose.cells.cloud.request import DeleteWorksheetConditionalFormattingAreaRequest
from aspose.cells.cloud.request import DeleteWorksheetConditionalFormattingRequest
from aspose.cells.cloud.request import DeleteWorksheetConditionalFormattingsRequest
from aspose.cells.cloud.request import GetWorksheetConditionalFormattingRequest
from aspose.cells.cloud.request import GetWorksheetConditionalFormattingsRequest
from aspose.cells.cloud.request import PutWorksheetConditionalFormattingRequest
from aspose.cells.cloud.request import PutWorksheetFormatConditionAreaRequest
from aspose.cells.cloud.request import PutWorksheetFormatConditionConditionRequest
from aspose.cells.cloud.request import PutWorksheetFormatConditionRequest

from aspose.cells.cloud.model import FormatCondition


def test_get_worksheet_conditional_formattings(client):
    """Test for GetWorksheetConditionalFormattings of ConditionalFormattingsController.."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = GetWorksheetConditionalFormattingsRequest(
        name="Book1.xlsx",
        sheet_name="Sheet1",
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200


def test_get_worksheet_conditional_formatting(client):
    """Test for GetWorksheetConditionalFormatting of ConditionalFormattingsController.."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = GetWorksheetConditionalFormattingRequest(
        name="Book1.xlsx",
        sheet_name="Sheet1",
        index=0,
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200


def test_put_worksheet_conditional_formatting(client):
    """Test for PutWorksheetConditionalFormatting of ConditionalFormattingsController.."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = PutWorksheetConditionalFormattingRequest(
        name="Book1.xlsx",
        sheet_name="Sheet1",
        formatcondition=FormatCondition(type_='CellValue', operator='Between', formula1='v1', formula2='v2'),
        cell_area="A1:C10",
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200


def test_put_worksheet_format_condition(client):
    """Test for PutWorksheetFormatCondition of ConditionalFormattingsController.."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = PutWorksheetFormatConditionRequest(
        name="Book1.xlsx",
        sheet_name="Sheet1",
        index=0,
        cell_area="A1:C10",
        type_="CellValue",
        operator_type="Between",
        formula1="v1",
        formula2="v2",
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200


def test_put_worksheet_format_condition_area(client):
    """Test for PutWorksheetFormatConditionArea of ConditionalFormattingsController.."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = PutWorksheetFormatConditionAreaRequest(
        name="Book1.xlsx",
        sheet_name="Sheet1",
        index=0,
        cell_area="A1:C10",
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200


def test_put_worksheet_format_condition_condition(client):
    """Test for PutWorksheetFormatConditionCondition of ConditionalFormattingsController.."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = PutWorksheetFormatConditionConditionRequest(
        name="Book1.xlsx",
        sheet_name="Sheet1",
        index=0,
        type_="CellValue",
        operator_type="Between",
        formula1="v1",
        formula2="v2",
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200


def test_delete_worksheet_conditional_formattings(client):
    """Test for DeleteWorksheetConditionalFormattings of ConditionalFormattingsController.."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = DeleteWorksheetConditionalFormattingsRequest(
        name="Book1.xlsx",
        sheet_name="Sheet1",
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200


def test_delete_worksheet_conditional_formatting(client):
    """Test for DeleteWorksheetConditionalFormatting of ConditionalFormattingsController.."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = DeleteWorksheetConditionalFormattingRequest(
        name="Book1.xlsx",
        sheet_name="Sheet1",
        index=0,
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200


def test_delete_worksheet_conditional_formatting_area(client):
    """Test for DeleteWorksheetConditionalFormattingArea of ConditionalFormattingsController.."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = DeleteWorksheetConditionalFormattingAreaRequest(
        name="Book1.xlsx",
        sheet_name="Sheet1",
        start_row=1,
        start_column=1,
        total_rows=4,
        total_columns=6,
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200
