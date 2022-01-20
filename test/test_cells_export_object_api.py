# coding: utf-8

from __future__ import absolute_import

import os
import sys
import unittest
import warnings

ABSPATH = os.path.abspath(os.path.realpath(os.path.dirname(__file__)) + "/..")
sys.path.append(ABSPATH)
import asposecellscloud
from asposecellscloud.rest import ApiException
from asposecellscloud.apis.light_cells_api import LightCellsApi
import AuthUtil

global_api = None
class TestCellsExportObjectApi(unittest.TestCase):
    """ CellsApi unit test stubs """
    
    def setUp(self):
        warnings.simplefilter('ignore', ResourceWarning)
        global global_api
        if global_api is None:
           global_api = asposecellscloud.apis.light_cells_api.LightCellsApi(AuthUtil.GetClientId(),AuthUtil.GetClientSecret(),"v3.0",AuthUtil.GetBaseUrl())
        self.api = global_api

    def tearDown(self):
        pass

    def test_cells_export_chart_pdf(self):
        Book1 = os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" + "Book1.xlsx"
        myDocument = os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" + "myDocument.xlsx"
        result = self.api.post_export({ "Book1.xlsx" :Book1,  "myDocument.xlsx":myDocument},"chart","pdf")
        self.assertIsNotNone(result)
        pass
    def test_cells_export_chart_tiff(self):
        Book1 = os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" + "Book1.xlsx"
        myDocument = os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" + "myDocument.xlsx"
        result = self.api.post_export({ "Book1.xlsx" :Book1,  "myDocument.xlsx":myDocument},"chart","tiff")
        self.assertIsNotNone(result)
        pass    
    def test_cells_export_chart_png(self):
        Book1 = os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" + "Book1.xlsx"
        myDocument = os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" + "myDocument.xlsx"
        result = self.api.post_export({ "Book1.xlsx" :Book1,  "myDocument.xlsx":myDocument},"chart","png")
        self.assertIsNotNone(result)
        pass    
    def test_cells_export_picture_png(self):
        Book1 = os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" + "Book1.xlsx"
        myDocument = os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" + "myDocument.xlsx"
        result = self.api.post_export({ "Book1.xlsx" :Book1,  "myDocument.xlsx":myDocument},"picture","png")
        self.assertIsNotNone(result)
        pass
    def test_cells_export_shape_png(self):
        Book1 = os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" + "Book1.xlsx"
        myDocument = os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" + "myDocument.xlsx"
        result = self.api.post_export({ "Book1.xlsx" :Book1,  "myDocument.xlsx":myDocument},"shape","png")
        self.assertIsNotNone(result)
        pass

    def test_cells_export_sheet_png(self):
        Book1 = os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" + "Book1.xlsx"
        myDocument = os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" + "myDocument.xlsx"
        result = self.api.post_export({ "Book1.xlsx" :Book1,  "myDocument.xlsx":myDocument},"sheet","png")
        self.assertIsNotNone(result)
        pass
    def test_cells_export_sheet_pdf(self):
        Book1 = os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" + "Book1.xlsx"
        myDocument = os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" + "myDocument.xlsx"
        result = self.api.post_export({ "Book1.xlsx" :Book1,  "myDocument.xlsx":myDocument},"sheet","pdf")
        self.assertIsNotNone(result)
        pass    
    def test_cells_export_sheet_xlsx(self):
        Book1 = os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" + "Book1.xlsx"
        myDocument = os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" + "myDocument.xlsx"
        result = self.api.post_export({ "Book1.xlsx" :Book1,  "myDocument.xlsx":myDocument},"sheet","xlsx")
        self.assertIsNotNone(result)
        pass
    def test_cells_export_workbook_png(self):
        Book1 = os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" + "Book1.xlsx"
        myDocument = os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" + "myDocument.xlsx"
        result = self.api.post_export({ "Book1.xlsx" :Book1,  "myDocument.xlsx":myDocument},"workbook", "png")
        self.assertIsNotNone(result)
        pass
    def test_cells_export_workbook_pdf(self):
        Book1 = os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" + "Book1.xlsx"
        myDocument = os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" + "myDocument.xlsx"
        result = self.api.post_export({ "Book1.xlsx" :Book1,  "myDocument.xlsx":myDocument},"workbook", "pdf")
        self.assertIsNotNone(result)
        pass
    def test_cells_export_workbook_md(self):
        Book1 = os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" + "Book1.xlsx"
        myDocument = os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" + "myDocument.xlsx"
        result = self.api.post_export({ "Book1.xlsx" :Book1,  "myDocument.xlsx":myDocument},"workbook", "md")
        self.assertIsNotNone(result)
        pass
    def test_cells_export_workbook_ods(self):
        Book1 = os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" + "Book1.xlsx"
        myDocument = os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" + "myDocument.xlsx"
        result = self.api.post_export({ "Book1.xlsx" :Book1,  "myDocument.xlsx":myDocument},"workbook", "ods")
        self.assertIsNotNone(result)
        pass
if __name__ == '__main__':
    unittest.main()
