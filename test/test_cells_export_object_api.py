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
from asposecellscloud.apis.lite_cells_api import LiteCellsApi
import AuthUtil

global_api = None
class TestCellsExportObjectApi(unittest.TestCase):
    """ CellsApi unit test stubs """
    
    def setUp(self):
        warnings.simplefilter('ignore', ResourceWarning)
        global global_api
        if global_api is None:
           global_api = asposecellscloud.apis.lite_cells_api.LiteCellsApi(AuthUtil.GetClientId(),AuthUtil.GetClientSecret(),"v3.0",AuthUtil.GetBaseUrl())
        self.api = global_api

    def tearDown(self):
        pass

    def test_cells_export_chart(self):
        Book1 = os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" + "Book1.xlsx"
        myDocument = os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" + "myDocument.xlsx"
        result = self.api.post_export({ "Book1.xlsx" :Book1,  "myDocument.xlsx":myDocument},"chart","pdf")
        pass
    def test_cells_export_comment(self):
        Book1 = os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" + "Book1.xlsx"
        myDocument = os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" + "myDocument.xlsx"
        result = self.api.post_export({ "Book1.xlsx" :Book1,  "myDocument.xlsx":myDocument},"comment","png")
        pass

    def test_cells_export_picture(self):
        Book1 = os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" + "Book1.xlsx"
        myDocument = os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" + "myDocument.xlsx"
        result = self.api.post_export({ "Book1.xlsx" :Book1,  "myDocument.xlsx":myDocument},"picture","png")
        pass
    def test_cells_export_shape(self):
        Book1 = os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" + "Book1.xlsx"
        myDocument = os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" + "myDocument.xlsx"
        result = self.api.post_export({ "Book1.xlsx" :Book1,  "myDocument.xlsx":myDocument},"shape", "png")
        pass
if __name__ == '__main__':
    unittest.main()
