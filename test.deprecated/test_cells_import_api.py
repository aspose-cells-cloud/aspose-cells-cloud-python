# coding: utf-8

from __future__ import absolute_import

import os
import sys
import unittest
import warnings
import base64

from asposecellscloud.models import ImportIntArrayOption
from asposecellscloud.models import ImportPictureOption
ABSPATH = os.path.abspath(os.path.realpath(os.path.dirname(__file__)) + "/..")
sys.path.append(ABSPATH)
import asposecellscloud
from asposecellscloud.rest import ApiException
from asposecellscloud.apis.light_cells_api import LightCellsApi
import AuthUtil

global_api = None
class TestCellsImportApi(unittest.TestCase):
    """ CellsApi unit test stubs """
    
    def setUp(self):
        warnings.simplefilter('ignore', ResourceWarning)
        global global_api
        if global_api is None:
           global_api = asposecellscloud.apis.light_cells_api.LightCellsApi(AuthUtil.GetClientId(),AuthUtil.GetClientSecret(),"v3.0",AuthUtil.GetBaseUrl())
        self.api = global_api

    def tearDown(self):
        pass

    def test_cells_import_intarray(self):
        assemblytest = os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" + "assemblytest.xlsx"
        datasource = os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" + "datasource.xlsx"

        data = ImportIntArrayOption()
        data.destination_worksheet = 'Sheet1'
        data.first_column = 1
        data.first_row = 3
        data.import_data_type = 'IntArray'
        data.is_vertical = True
        data.data = [1, 2, 3, 4]

        result = self.api.post_import({ "assemblytest.xlsx" :assemblytest,  "datasource.xlsx":datasource},data)
        # print(result)
        pass
    def test_cells_import_picture(self):
        assemblytest = os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" + "assemblytest.xlsx"
        datasource = os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" + "datasource.xlsx"

        data = ImportPictureOption()
        data.destination_worksheet = 'Sheet1'
        data.upper_left_row = 1
        data.upper_left_column = 3
        data.lower_right_row = 11
        data.lower_right_column = 13
        data.import_data_type = 'Picture'
        fullfilename = os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" + "WaterMark.png"
        f = open(fullfilename, 'rb')
        png = f.read()
        f.close()      
        data.data =base64.b64encode(png).decode('ascii')
        # base64_bytes = base64.b64encode(png)       
        # data.data = base64.b64encode(base64_bytes.decode('ascii') )

        result = self.api.post_import({ "assemblytest.xlsx" :assemblytest,  "datasource.xlsx":datasource},data)
        # print(result)
        pass
if __name__ == '__main__':
    unittest.main()
