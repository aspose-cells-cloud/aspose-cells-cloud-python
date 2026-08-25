"""Integration tests for Conversion (generated from TestingData)."""

import os

import pytest

from aspose.cells.cloud import CellsCloudClient
from aspose.cells.cloud.request import ConvertChartToImageRequest
from aspose.cells.cloud.request import ConvertChartToPdfRequest
from aspose.cells.cloud.request import ConvertRangeToCsvRequest
from aspose.cells.cloud.request import ConvertRangeToHtmlRequest
from aspose.cells.cloud.request import ConvertRangeToImageRequest
from aspose.cells.cloud.request import ConvertRangeToJsonRequest
from aspose.cells.cloud.request import ConvertRangeToPdfRequest
from aspose.cells.cloud.request import ConvertSpreadsheetRequest
from aspose.cells.cloud.request import ConvertSpreadsheetToCsvRequest
from aspose.cells.cloud.request import ConvertSpreadsheetToJsonRequest
from aspose.cells.cloud.request import ConvertSpreadsheetToPdfRequest
from aspose.cells.cloud.request import ConvertTableToCsvRequest
from aspose.cells.cloud.request import ConvertTableToHtmlRequest
from aspose.cells.cloud.request import ConvertTableToImageRequest
from aspose.cells.cloud.request import ConvertTableToJsonRequest
from aspose.cells.cloud.request import ConvertTableToPdfRequest
from aspose.cells.cloud.request import ConvertWorksheetToCsvRequest
from aspose.cells.cloud.request import ConvertWorksheetToHtmlRequest
from aspose.cells.cloud.request import ConvertWorksheetToHtmlTableRequest
from aspose.cells.cloud.request import ConvertWorksheetToImageRequest
from aspose.cells.cloud.request import ConvertWorksheetToPdfRequest
from aspose.cells.cloud.request import ExportChartAsFormatRequest
from aspose.cells.cloud.request import ExportRangeAsFormatRequest
from aspose.cells.cloud.request import ExportSpreadsheetAsFormatRequest
from aspose.cells.cloud.request import ExportTableAsFormatRequest
from aspose.cells.cloud.request import ExportWorksheetAsFormatRequest
from aspose.cells.cloud.request import SaveSpreadsheetAsRequest

from aspose.cells.cloud.model import SaveOptionsData


def test_workbook_save_as_0(client):
    """Test for save workbook as one of the available formats. (parameter set 1 of 2)."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = SaveSpreadsheetAsRequest(
        name="Book1.xlsx",
        format_="csv",
        save_options_data=SaveOptionsData(filename='OutResult/PostExcelSaveAs.csv'),
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200


def test_workbook_save_as_1(client):
    """Test for save workbook as one of the available formats. (parameter set 2 of 2)."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = SaveSpreadsheetAsRequest(
        name="Book1.xlsx",
        format_="pdf",
        save_options_data=SaveOptionsData(filename='OutResult/PostExcelSaveAs.pdf'),
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200


def test_convert_workbook_0(client):
    """Test for get workbook as one of the available formats. (parameter set 1 of 2)."""
    request = ConvertSpreadsheetRequest(
        spreadsheet="testdata/Book1.xlsx",
        format_="png",
    )

    response = client.do(request)
    assert response is not None


def test_convert_workbook_1(client):
    """Test for get workbook as one of the available formats. (parameter set 2 of 2)."""
    request = ConvertSpreadsheetRequest(
        spreadsheet="testdata/Book1.xlsx",
        format_="sql",
    )

    response = client.do(request)
    assert response is not None


def test_convert_spreadsheet_to_pdf(client):
    """Test for get workbook as one of the available formats.."""
    request = ConvertSpreadsheetToPdfRequest(
        spreadsheet="testdata/Book1.xlsx",
    )

    response = client.do(request)
    assert response is not None


def test_convert_spreadsheet_to_csv(client):
    """Test for get workbook as one of the available formats.."""
    request = ConvertSpreadsheetToCsvRequest(
        spreadsheet="testdata/Book1.xlsx",
    )

    response = client.do(request)
    assert response is not None


def test_convert_spreadsheet_to_json(client):
    """Test for get workbook as one of the available formats.."""
    request = ConvertSpreadsheetToJsonRequest(
        spreadsheet="testdata/Book1.xlsx",
    )

    response = client.do(request)
    assert response is not None


def test_convert_workbook_save_cloud(client):
    """Test for converting workbook to one of the available formats.."""
    request = ConvertSpreadsheetRequest(
        format_="csv",
        out_path="OutResult/ConvertWorkbook.csv",
        spreadsheet="testdata/Book1.xlsx",
    )

    response = client.do(request)
    assert response is not None


def test_convert_worksheet_to_svg(client):
    """Test for converting worksheet to image file.."""
    request = ConvertWorksheetToImageRequest(
        worksheet="Sheet2",
        format_="svg",
        spreadsheet="testdata/TestTables.xlsx",
    )

    response = client.do(request)
    assert response is not None


def test_convert_worksheet_to_png(client):
    """Test for converting worksheet to image file.."""
    request = ConvertWorksheetToImageRequest(
        worksheet="Sheet2",
        format_="png",
        spreadsheet="testdata/TestTables.xlsx",
    )

    response = client.do(request)
    assert response is not None


def test_convert_worksheet_to_tiff(client):
    """Test for converting worksheet to image file.."""
    request = ConvertWorksheetToImageRequest(
        worksheet="Sheet2",
        format_="tiff",
        spreadsheet="testdata/TestTables.xlsx",
    )

    response = client.do(request)
    assert response is not None


def test_convert_worksheet_to_pdf(client):
    """Test for converting worksheet to pdf file.."""
    request = ConvertWorksheetToPdfRequest(
        worksheet="Sheet2",
        spreadsheet="testdata/TestTables.xlsx",
    )

    response = client.do(request)
    assert response is not None


def test_convert_worksheet_to_csv(client):
    """Test for converting worksheet to pdf file.."""
    request = ConvertWorksheetToCsvRequest(
        worksheet="Sheet2",
        spreadsheet="testdata/TestTables.xlsx",
    )

    response = client.do(request)
    assert response is not None


def test_convert_worksheet_to_html(client):
    """Test for converting worksheet to pdf file.."""
    request = ConvertWorksheetToHtmlRequest(
        worksheet="Sheet2",
        spreadsheet="testdata/TestTables.xlsx",
    )

    response = client.do(request)
    assert response is not None


def test_convert_worksheet_to_table(client):
    pytest.skip("API ConvertWorksheetToTable is not defined in the specification")


def test_convert_worksheet_to_html_table(client):
    """Test for converting worksheet to pdf file.."""
    request = ConvertWorksheetToHtmlTableRequest(
        worksheet="Sheet2",
        spreadsheet="testdata/TestTables.xlsx",
    )

    response = client.do(request)
    assert response is not None


def test_convert_table_to_svg(client):
    """Test for converting table to image file.."""
    request = ConvertTableToImageRequest(
        worksheet="Sheet2",
        table_name="Table13",
        format_="svg",
        spreadsheet="testdata/TestTables.xlsx",
    )

    response = client.do(request)
    assert response is not None


def test_convert_table_to_png(client):
    """Test for converting table to image file.."""
    request = ConvertTableToImageRequest(
        worksheet="Sheet2",
        table_name="Table13",
        format_="png",
        spreadsheet="testdata/TestTables.xlsx",
    )

    response = client.do(request)
    assert response is not None


def test_convert_table_to_pdf(client):
    """Test for converting table to pdf file.."""
    request = ConvertTableToPdfRequest(
        worksheet="Sheet2",
        table_name="Table13",
        spreadsheet="testdata/TestTables.xlsx",
    )

    response = client.do(request)
    assert response is not None


def test_convert_table_to_csv(client):
    """Test for converting table to csv file.."""
    request = ConvertTableToCsvRequest(
        worksheet="Sheet2",
        table_name="Table13",
        spreadsheet="testdata/TestTables.xlsx",
    )

    response = client.do(request)
    assert response is not None


def test_convert_table_to_html(client):
    """Test for converting table to html file.."""
    request = ConvertTableToHtmlRequest(
        worksheet="Sheet2",
        table_name="Table13",
        spreadsheet="testdata/TestTables.xlsx",
    )

    response = client.do(request)
    assert response is not None


def test_convert_table_to_json(client):
    """Test for converting table to json file.."""
    request = ConvertTableToJsonRequest(
        worksheet="Sheet2",
        table_name="Table13",
        spreadsheet="testdata/TestTables.xlsx",
    )

    response = client.do(request)
    assert response is not None


def test_convert_range_to_image(client):
    """Test for converting range to image file.."""
    request = ConvertRangeToImageRequest(
        worksheet="Sheet2",
        range_="B2:F10",
        format_="svg",
        spreadsheet="testdata/TestTables.xlsx",
    )

    response = client.do(request)
    assert response is not None


def test_convert_range_to_pdf(client):
    """Test for converting range to pdf file.."""
    request = ConvertRangeToPdfRequest(
        worksheet="Sheet2",
        range_="A1:F10",
        spreadsheet="testdata/TestTables.xlsx",
    )

    response = client.do(request)
    assert response is not None


def test_convert_range_to_csv(client):
    """Test for converting range to csv file.."""
    request = ConvertRangeToCsvRequest(
        worksheet="Sheet2",
        range_="A1:F10",
        spreadsheet="testdata/TestTables.xlsx",
    )

    response = client.do(request)
    assert response is not None


def test_convert_range_to_html(client):
    """Test for converting range to html file.."""
    request = ConvertRangeToHtmlRequest(
        worksheet="Sheet2",
        range_="A1:F10",
        spreadsheet="testdata/TestTables.xlsx",
    )

    response = client.do(request)
    assert response is not None


def test_convert_range_to_json(client):
    """Test for converting range to json file.."""
    request = ConvertRangeToJsonRequest(
        worksheet="Sheet2",
        range_="A1:F10",
        spreadsheet="testdata/TestTables.xlsx",
    )

    response = client.do(request)
    assert response is not None


def test_convert_chart_to_image(client):
    """Test for converting workbook to one of the available formats.."""
    request = ConvertChartToImageRequest(
        worksheet="Sales",
        chart_index=0,
        format_="svg",
        spreadsheet="testdata/EmployeeSalesSummary.xlsx",
    )

    response = client.do(request)
    assert response is not None


def test_convert_chart_to_pdf(client):
    """Test for converting chart to pdf file.."""
    request = ConvertChartToPdfRequest(
        worksheet="Sales",
        chart_index=0,
        spreadsheet="testdata/EmployeeSalesSummary.xlsx",
    )

    response = client.do(request)
    assert response is not None


def test_export_spreadsheet_as_format_0(client):
    """Test for get workbook as one of the available formats. (parameter set 1 of 3)."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = ExportSpreadsheetAsFormatRequest(
        name="Book1.xlsx",
        format_="pdf",
        folder="TestData/In",
    )

    response = client.do(request)
    assert response is not None


def test_export_spreadsheet_as_format_1(client):
    """Test for get workbook as one of the available formats. (parameter set 2 of 3)."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = ExportSpreadsheetAsFormatRequest(
        name="Book1.xlsx",
        format_="pptx",
        folder="TestData/In",
    )

    response = client.do(request)
    assert response is not None


def test_export_spreadsheet_as_format_2(client):
    """Test for get workbook as one of the available formats. (parameter set 3 of 3)."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = ExportSpreadsheetAsFormatRequest(
        name="Book1.xlsx",
        format_="json",
        folder="TestData/In",
    )

    response = client.do(request)
    assert response is not None


def test_export_worksheet_as_format(client):
    """Test for export worksheet to one of the available formats.."""
    client.upload_file("testdata/EmployeeSalesSummary.xlsx", "TestData/In/EmployeeSalesSummary.xlsx", storage_name=None)

    request = ExportWorksheetAsFormatRequest(
        name="EmployeeSalesSummary.xlsx",
        worksheet="Sales",
        format_="svg",
        folder="TestData/In",
    )

    response = client.do(request)
    assert response is not None


def test_export_chart_as_format(client):
    """Test for converting workbook to one of the available formats.."""
    client.upload_file("testdata/EmployeeSalesSummary.xlsx", "TestData/In/EmployeeSalesSummary.xlsx", storage_name=None)

    request = ExportChartAsFormatRequest(
        name="EmployeeSalesSummary.xlsx",
        worksheet="Sales",
        chart_index=0,
        format_="svg",
        folder="TestData/In",
    )

    response = client.do(request)
    assert response is not None


def test_export_table_as_format(client):
    """Test for converting table to one of the available formats.."""
    client.upload_file("testdata/TestTables.xlsx", "TestData/In/TestTables.xlsx", storage_name=None)

    request = ExportTableAsFormatRequest(
        name="TestTables.xlsx",
        worksheet="Sheet2",
        table_name="Table13",
        format_="svg",
        folder="TestData/In",
    )

    response = client.do(request)
    assert response is not None


def test_export_range_as_format(client):
    """Test for converting range to one of the available formats.."""
    client.upload_file("testdata/EmployeeSalesSummary.xlsx", "TestData/In/EmployeeSalesSummary.xlsx", storage_name=None)

    request = ExportRangeAsFormatRequest(
        name="EmployeeSalesSummary.xlsx",
        worksheet="Sales",
        range_="A1:F16",
        format_="svg",
        folder="TestData/In",
    )

    response = client.do(request)
    assert response is not None
