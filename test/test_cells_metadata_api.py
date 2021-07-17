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
from asposecellscloud.models import CellsDocumentProperty
import AuthUtil

global_api = None
class TestCellsMetadatApi(unittest.TestCase):
    """ CellsApi unit test stubs """
    
    def setUp(self):
        warnings.simplefilter('ignore', ResourceWarning)
        global global_api
        if global_api is None:
           global_api = asposecellscloud.apis.lite_cells_api.LiteCellsApi(AuthUtil.GetClientId(),AuthUtil.GetClientSecret(),"v3.0",AuthUtil.GetBaseUrl())
        self.api = global_api

    def tearDown(self):
        pass

    def test_cells_update_metadata(self):
        assemblytest = os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" + "assemblytest.xlsx"
        datasource = os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" + "datasource.xlsx"
        documentProperty = CellsDocumentProperty()
        documentProperty.name = 'test'
        documentProperty.value = 'test'
        documentProperties = [documentProperty]
        result = self.api.post_metadata({ "assemblytest.xlsx" :assemblytest,  "datasource.xlsx":datasource},documentProperties)
        # print(result)
        pass

    def test_cells_get_metadata(self):
        assemblytest = os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" + "assemblytest.xlsx"
        datasource = os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" + "datasource.xlsx"
        result = self.api.get_metadata({ "assemblytest.xlsx" :assemblytest,  "datasource.xlsx":datasource})
        # print(result)
        pass
    def test_cells_delete_metadata(self):
        assemblytest = os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" + "assemblytest.xlsx"
        datasource = os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" + "datasource.xlsx"
        result = self.api.delete_metadata({ "assemblytest.xlsx" :assemblytest,  "datasource.xlsx":datasource})
        # print(result)
        pass
if __name__ == '__main__':
    unittest.main()
