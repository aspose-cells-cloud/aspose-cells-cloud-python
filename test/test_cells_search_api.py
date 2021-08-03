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
class TestCellsSearchApi(unittest.TestCase):
    """ CellsApi unit test stubs """
    
    def setUp(self):
        warnings.simplefilter('ignore', ResourceWarning)
        global global_api
        if global_api is None:
           global_api = asposecellscloud.apis.lite_cells_api.LiteCellsApi(AuthUtil.GetClientId(),AuthUtil.GetClientSecret(),"v3.0",AuthUtil.GetBaseUrl())
        self.api = global_api

    def tearDown(self):
        pass

    def test_cells_search(self):
        assemblytest = os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" + "assemblytest.xlsx"
        datasource = os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" + "datasource.xlsx"
        result = self.api.post_search({ "assemblytest.xlsx" :assemblytest,  "datasource.xlsx":datasource},"png")
        # print(result)
        pass
    def test_cells_search_sheet(self):
        assemblytest = os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" + "assemblytest.xlsx"
        datasource = os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" + "datasource.xlsx"
        result = self.api.post_search({ "assemblytest.xlsx" :assemblytest,  "datasource.xlsx":datasource},"png",sheetname='Shhet1')
        # print(result)
        pass

if __name__ == '__main__':
    unittest.main()
