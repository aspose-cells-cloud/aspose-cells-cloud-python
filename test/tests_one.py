# coding: utf-8

from __future__ import absolute_import

import os
import sys
import time
import unittest
import warnings

ABSPATH = os.path.abspath(os.path.realpath(os.path.dirname(__file__)) + "/..")
sys.path.append(ABSPATH)

import AuthUtil

from asposecellscloud.apis.cells_api import CellsApi
from asposecellscloud.models import *
from asposecellscloud.requests import *
from asposecellscloud.rest import ApiException

global_api = None

class TestOneCase(unittest.TestCase):
    def setUp(self):
        warnings.simplefilter('ignore', ResourceWarning)
        global global_api
        if global_api is None:
           global_api = CellsApi(AuthUtil.GetClientId(),AuthUtil.GetClientSecret(),"v3.0",AuthUtil.GetBaseUrl())
        self.api = global_api
    def test_one_case(self):
        remote_folder = 'TestData/In'

        local_name = 'TestCase.xlsx'
        remote_name = 'TestCase.xlsx'
        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 

        top10Filter = Top10Filter(items= 1 ,is_percent= True ,field_index =0  )
        filter_column = FilterColumn(filter_type='Top10Filter' , top10_filter = top10Filter )
        autoFilter = AutoFilter(filter_columns= [filter_column] )
        filter = PivotFilter(field_index= 0 ,filter_type= 'Count' ,auto_filter = autoFilter )

        request =  PutWorksheetPivotTableFilterRequest( remote_name, 'Sheet4', 0, filter,need_re_calculate= True,folder= remote_folder,storage_name= '')
        self.api.put_worksheet_pivot_table_filter(request)
        
        
    def tearDown(self):
        pass

   
if __name__ == '__main__':
    unittest.main()