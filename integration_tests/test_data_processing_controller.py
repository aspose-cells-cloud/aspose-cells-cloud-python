"""Integration tests for DataProcessingController (generated from TestingData)."""

import os

import pytest

from aspose.cells.cloud import CellsCloudClient
from aspose.cells.cloud.request import PostDataTransformationRequest
from aspose.cells.cloud.request import PostWorkbookDataCleansingRequest
from aspose.cells.cloud.request import PostWorkbookDataDeduplicationRequest
from aspose.cells.cloud.request import PostWorkbookDataFillRequest

from aspose.cells.cloud.model import AppliedStep
from aspose.cells.cloud.model import DataCleansing
from aspose.cells.cloud.model import DataFill
from aspose.cells.cloud.model import DataFillValue
from aspose.cells.cloud.model import DataItem
from aspose.cells.cloud.model import DataQuery
from aspose.cells.cloud.model import DataSource
from aspose.cells.cloud.model import DataTransformationRequest
from aspose.cells.cloud.model import DeduplicationRegion
from aspose.cells.cloud.model import LoadData
from aspose.cells.cloud.model import LoadTo
from aspose.cells.cloud.model import Range
from aspose.cells.cloud.model import UnpivotColumn


def test_post_workbook_data_cleansing(client):
    """Test for PostWorkbookDataCleansing of DataProcessingController.."""
    client.upload_file("testdata/BookCsvDuplicateData.csv", "TestData/In/BookCsvDuplicateData.csv", storage_name=None)

    request = PostWorkbookDataCleansingRequest(
        name="BookCsvDuplicateData.csv",
        data_cleansing=DataCleansing(need_fill_data=True, data_fill=DataFill(data_fill_default_value=DataFillValue(default_date='2024-01-01', default_number=0, default_boolean=False))),
        folder="TestData/In",
    )

    response = client.do(request)
    assert response is not None


def test_post_workbook_data_deduplication(client):
    """Test for PostWorkbookDataDeduplication of DataProcessingController.."""
    client.upload_file("testdata/BookCsvDuplicateData.csv", "TestData/In/BookCsvDuplicateData.csv", storage_name=None)

    request = PostWorkbookDataDeduplicationRequest(
        name="BookCsvDuplicateData.csv",
        deduplication_region=DeduplicationRegion(ranges=[]),
        folder="TestData/In",
    )

    response = client.do(request)
    assert response is not None


def test_post_workbook_data_fill(client):
    """Test for PostWorkbookDataFill of DataProcessingController.."""
    client.upload_file("testdata/BookCsvDuplicateData.csv", "TestData/In/BookCsvDuplicateData.csv", storage_name=None)

    request = PostWorkbookDataFillRequest(
        name="BookCsvDuplicateData.csv",
        data_fill=DataFill(data_fill_default_value=DataFillValue(default_date='2024-01-01', default_number=0, default_boolean=False)),
        folder="TestData/In",
    )

    response = client.do(request)
    assert response is not None


def test_post_data_transformation(client):
    """Test for PostDataTransformation of DataProcessingController.."""
    client.upload_file("testdata/BookTableL2W.xlsx", "TestData/In/BookTableL2W.xlsx", storage_name=None)

    request = PostDataTransformationRequest(
        data_transformation_request=DataTransformationRequest(load_data=LoadData(load_to=LoadTo(begin_column_index=2, begin_row_index=3, worksheet='L2W'), data_query=DataQuery(name='DataQuery', data_item=DataItem(data_item_type='Table', value='Table1'), data_source=DataSource(data_source_type='CloudFileSystem', data_path='TestData/In/BookTableL2W.xlsx'), data_source_data_type='ListObject')), applied_steps=[AppliedStep(step_name='UnpivotColumn', applied_operate=UnpivotColumn(applied_operate_type='UnpivotColumn', value_map_name='Count', column_map_name='Date', unpivot_column_names=['2017', '2018', '2019']))]),
    )

    response = client.do(request)
    assert response is not None
