"""Integration tests for TextProcessingController (generated from TestingData)."""

import os

import pytest

from aspose.cells.cloud import CellsCloudClient
from aspose.cells.cloud.request import PostAddTextContentRequest
from aspose.cells.cloud.request import PostTrimContentRequest
from aspose.cells.cloud.request import PostUpdateWordCaseRequest

from aspose.cells.cloud.model import AddTextOptions
from aspose.cells.cloud.model import DataSource
from aspose.cells.cloud.model import ScopeOptions
from aspose.cells.cloud.model import TrimContentOptions
from aspose.cells.cloud.model import WordCaseOptions


def test_post_add_text_content(client):
    """Test for PostAddTextContent of TextProcessingController.."""
    client.upload_file("testdata/BookText.xlsx", "TestData/In/BookText.xlsx", storage_name=None)

    request = PostAddTextContentRequest(
        add_text_options=AddTextOptions(data_source=DataSource(data_source_type='CloudFileSystem', data_path='TestData/In/BookText.xlsx'), text='Aspose.Cells Cloud is an excellent product.', scope_options=ScopeOptions(scope='Workbook'), select_poistion='AtTheBeginning', skip_empty_cells=True),
    )

    response = client.do(request)
    assert response is not None


def test_post_trim_content(client):
    """Test for PostTrimContent of TextProcessingController.."""
    client.upload_file("testdata/BookText.xlsx", "TestData/In/BookText.xlsx", storage_name=None)

    request = PostTrimContentRequest(
        trim_content_options=TrimContentOptions(data_source=DataSource(data_source_type='CloudFileSystem', data_path='TestData/In/BookText.xlsx'), trim_leading=True, trim_trailing=True, trim_space_between_word_to1=True, remove_all_line_breaks=True, scope_options=ScopeOptions(scope='EntireWorkbook')),
    )

    response = client.do(request)
    assert response is not None


def test_post_update_word_case(client):
    """Test for PostUpdateWordCase of TextProcessingController.."""
    client.upload_file("testdata/BookText.xlsx", "TestData/In/BookText.xlsx", storage_name=None)

    request = PostUpdateWordCaseRequest(
        word_case_options=WordCaseOptions(data_source=DataSource(data_source_type='CloudFileSystem', data_path='TestData/In/BookText.xlsx'), word_case_type='None', scope_options=ScopeOptions(scope='EntireWorkbook')),
    )

    response = client.do(request)
    assert response is not None
