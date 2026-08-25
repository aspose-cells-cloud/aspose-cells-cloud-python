"""Integration tests for WorksheetValidationsController (generated from TestingData)."""

import os

import pytest

from aspose.cells.cloud import CellsCloudClient
from aspose.cells.cloud.request import DeleteWorksheetValidationRequest
from aspose.cells.cloud.request import DeleteWorksheetValidationsRequest
from aspose.cells.cloud.request import GetWorksheetValidationRequest
from aspose.cells.cloud.request import GetWorksheetValidationsRequest
from aspose.cells.cloud.request import PostWorksheetValidationRequest
from aspose.cells.cloud.request import PutWorksheetValidationRequest

from aspose.cells.cloud.model import Validation


def test_get_worksheet_validations(client):
    """Test for GetWorksheetValidations of WorksheetValidationsController.."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = GetWorksheetValidationsRequest(
        name="Book1.xlsx",
        sheet_name="Sheet1",
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200


def test_get_worksheet_validation(client):
    """Test for GetWorksheetValidation of WorksheetValidationsController.."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = GetWorksheetValidationRequest(
        name="Book1.xlsx",
        sheet_name="Sheet1",
        validation_index=0,
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200


def test_put_worksheet_validation(client):
    """Test for PutWorksheetValidation of WorksheetValidationsController.."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = PutWorksheetValidationRequest(
        name="Book1.xlsx",
        sheet_name="Sheet1",
        range_="A1:C10",
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200


def test_post_worksheet_validation(client):
    """Test for PostWorksheetValidation of WorksheetValidationsController.."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = PostWorksheetValidationRequest(
        name="Book1.xlsx",
        sheet_name="Sheet1",
        validation_index=0,
        validation=Validation(formula1='=A1', type_='Custom'),
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200


def test_delete_worksheet_validation(client):
    """Test for DeleteWorksheetValidation of WorksheetValidationsController.."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = DeleteWorksheetValidationRequest(
        name="Book1.xlsx",
        sheet_name="Sheet1",
        validation_index=0,
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200


def test_delete_worksheet_validations(client):
    """Test for DeleteWorksheetValidations of WorksheetValidationsController.."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = DeleteWorksheetValidationsRequest(
        name="Book1.xlsx",
        sheet_name="Sheet1",
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200
