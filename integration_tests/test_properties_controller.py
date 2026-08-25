"""Integration tests for PropertiesController (generated from TestingData)."""

import os

import pytest

from aspose.cells.cloud import CellsCloudClient
from aspose.cells.cloud.request import DeleteDocumentPropertiesRequest
from aspose.cells.cloud.request import DeleteDocumentPropertyRequest
from aspose.cells.cloud.request import GetDocumentPropertiesRequest
from aspose.cells.cloud.request import GetDocumentPropertyRequest
from aspose.cells.cloud.request import PutDocumentPropertyRequest

from aspose.cells.cloud.model import CellsDocumentProperty


def test_get_document_properties(client):
    """Test for GetDocumentProperties of PropertiesController.."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = GetDocumentPropertiesRequest(
        name="Book1.xlsx",
        type_="All",
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200


def test_get_document_property(client):
    """Test for GetDocumentProperty of PropertiesController.."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = GetDocumentPropertyRequest(
        name="Book1.xlsx",
        property_name="Author",
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200


def test_put_document_property(client):
    """Test for PutDocumentProperty of PropertiesController.."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = PutDocumentPropertyRequest(
        name="Book1.xlsx",
        property_=CellsDocumentProperty(name='Author', value='cells developer'),
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200


def test_delete_document_property(client):
    """Test for DeleteDocumentProperty of PropertiesController.."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = DeleteDocumentPropertyRequest(
        name="Book1.xlsx",
        property_name="Author",
        type_="All",
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200


def test_delete_document_properties(client):
    """Test for DeleteDocumentProperties of PropertiesController.."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = DeleteDocumentPropertiesRequest(
        name="Book1.xlsx",
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200
