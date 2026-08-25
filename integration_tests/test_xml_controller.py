"""Integration tests for XmlController (generated from TestingData)."""

import os

import pytest

from aspose.cells.cloud import CellsCloudClient
from aspose.cells.cloud.request import PostWorkbookExportXMLRequest
from aspose.cells.cloud.request import PostWorkbookImportXMLRequest

from aspose.cells.cloud.model import DataSource
from aspose.cells.cloud.model import ImportPosition
from aspose.cells.cloud.model import ImportXMLRequest


def test_post_workbook_export_xml(client):
    """Test for PostWorkbookExportXML of XmlController.."""
    client.upload_file("testdata/Template.xlsx", "TestData/In/Template.xlsx", storage_name=None)

    request = PostWorkbookExportXMLRequest(
        name="Template.xlsx",
        folder="TestData/In",
    )

    response = client.do(request)
    assert response is not None


def test_post_workbook_import_xml(client):
    """Test for PostWorkbookImortXML of XmlController.."""
    client.upload_file("testdata/Template.xlsx", "TestData/In/Template.xlsx", storage_name=None)

    client.upload_file("testdata/data.xml", "TestData/In/data.xml", storage_name=None)

    request = PostWorkbookImportXMLRequest(
        name="Template.xlsx",
        import_xml_request=ImportXMLRequest(xml_file_source=DataSource(data_source_type='CloudFileSystem', data_path='TestData/In/data.xml'), import_position=ImportPosition(sheet_name='Sheet1', row_index=3, column_index=4)),
        folder="TestData/In",
    )

    response = client.do(request)
    assert response is not None
