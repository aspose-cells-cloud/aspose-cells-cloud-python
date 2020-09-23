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
from asposecellscloud.apis.cells_api import CellsApi
import AuthUtil
global_api = None

class TestCellsAutoshapesApi(unittest.TestCase):
    """ CellsAutoshapesApi unit test stubs """

    def setUp(self):
        global global_api
        if global_api is None:
           global_api = asposecellscloud.apis.cells_api.CellsApi(AuthUtil.GetAPPSID(),AuthUtil.GetAPPKey(),"v3.0",AuthUtil.GetBaseUrl())
        self.api = global_api

    def tearDown(self):
        pass

    def test_cells_autoshapes_get_worksheet_autoshape(self):
        """
        Test case for cells_autoshapes_get_worksheet_autoshape

        Get autoshape info.
        """
        name ='myDocument.xlsx'
        sheet_name ='Sheet2'
        autoshapeNumber = 4  
        folder = "PythonTest"
        result = AuthUtil.Ready(self.api, name, folder)
        self.assertTrue(len(result.uploaded)>0)
        result = self.api.cells_autoshapes_get_worksheet_autoshape(name, sheet_name,autoshapeNumber, folder=folder)
        # self.assertEqual(result.code,200)
        pass

    def test_cells_autoshapes_get_worksheet_autoshape_format(self):
        """
        Test case for cells_autoshapes_get_worksheet_autoshape with format

        Get autoshape info.
        """
        name ='myDocument.xlsx'
        sheet_name ='Sheet2'
        autoshapeNumber = 4  
        folder = "PythonTest"
        result = AuthUtil.Ready(self.api, name, folder)
        self.assertTrue(len(result.uploaded)>0)
        result = self.api.cells_autoshapes_get_worksheet_autoshape(name, sheet_name,autoshapeNumber, format="png", folder=folder)
        # self.assertEqual(result.code,200)
        pass

    def test_cells_autoshapes_get_worksheet_autoshapes(self):
        """
        Test case for cells_autoshapes_get_worksheet_autoshapes

        Get worksheet autoshapes info.
        """
        name ='myDocument.xlsx'
        sheet_name ='Sheet2'
        folder = "PythonTest"
        result = AuthUtil.Ready(self.api, name, folder)
        self.assertTrue(len(result.uploaded)>0)
        result = self.api.cells_autoshapes_get_worksheet_autoshapes(name, sheet_name, folder=folder)
        self.assertEqual(result.code,200)
        pass


if __name__ == '__main__':
    unittest.main()
