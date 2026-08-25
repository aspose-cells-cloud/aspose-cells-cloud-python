"""Integration tests for PageSetupController (generated from TestingData)."""

import os

import pytest

from aspose.cells.cloud import CellsCloudClient
from aspose.cells.cloud.request import DeleteHeaderFooterRequest
from aspose.cells.cloud.request import GetFooterRequest
from aspose.cells.cloud.request import GetHeaderRequest
from aspose.cells.cloud.request import GetPageSetupRequest
from aspose.cells.cloud.request import PostFitTallToPagesRequest
from aspose.cells.cloud.request import PostFitWideToPagesRequest
from aspose.cells.cloud.request import PostFooterRequest
from aspose.cells.cloud.request import PostHeaderRequest
from aspose.cells.cloud.request import PostPageSetupRequest

from aspose.cells.cloud.model import PageSetup


def test_get_page_setup(client):
    """Test for GetPageSetup of PageSetupController.."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = GetPageSetupRequest(
        name="Book1.xlsx",
        sheet_name="Sheet1",
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200


def test_post_page_setup(client):
    """Test for PostPageSetup of PageSetupController.."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = PostPageSetupRequest(
        name="Book1.xlsx",
        sheet_name="Sheet1",
        page_setup=PageSetup(black_and_white=True, center_horizontally=True, center_vertically=True),
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200


def test_delete_header_footer(client):
    """Test for DeleteHeaderFooter of PageSetupController.."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = DeleteHeaderFooterRequest(
        name="Book1.xlsx",
        sheet_name="Sheet1",
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200


def test_get_header(client):
    """Test for GetHeader of PageSetupController.."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = GetHeaderRequest(
        name="Book1.xlsx",
        sheet_name="Sheet1",
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200


def test_post_header(client):
    """Test for PostHeader of PageSetupController.."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = PostHeaderRequest(
        name="Book1.xlsx",
        sheet_name="Sheet1",
        section=1,
        script="Update add header",
        is_first_page=True,
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200


def test_get_footer(client):
    """Test for GetFooter of PageSetupController.."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = GetFooterRequest(
        name="Book1.xlsx",
        sheet_name="Sheet1",
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200


def test_post_footer(client):
    """Test for PostFooter of PageSetupController.."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = PostFooterRequest(
        name="Book1.xlsx",
        sheet_name="Sheet1",
        section=1,
        script="add footer script",
        is_first_page=True,
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200


def test_post_fit_wide_to_pages(client):
    """Test for PostFitWideToPages of PageSetupController.."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = PostFitWideToPagesRequest(
        name="Book1.xlsx",
        sheet_name="Sheet1",
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200


def test_post_fit_tall_to_pages(client):
    """Test for PostFitTallToPages of PageSetupController.."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = PostFitTallToPagesRequest(
        name="Book1.xlsx",
        sheet_name="Sheet1",
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200
