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
from asposecellscloud.models import SparklineGroups
import AuthUtil
global_api = None

class TestSparklineGroupsApi(unittest.TestCase):
    """ CellsAutoshapesApi unit test stubs """

    def setUp(self):
        global global_api
        if global_api is None:
           global_api = asposecellscloud.apis.cells_api.CellsApi(AuthUtil.GetAPPSID(),AuthUtil.GetAPPKey(),"v3.0",AuthUtil.GetBaseUrl())
        self.api = global_api

    def tearDown(self):
        pass

    def test_cells_sparklinegroups_gppd(self):
        """
        Test case for test_cells_sparklinegroups_gppd

        """
        name ='TestCase.xlsx'
        sheet_name ='Sheet1'
        index = 0  
        folder = "PythonTest"
        result = AuthUtil.Ready(self.api, name, folder)
        self.assertTrue(len(result.uploaded)>0)
        
        gets_result = self.api.cells_sparkline_groups_get_worksheet_sparkline_groups(name, sheet_name, folder=folder)
        self.assertEqual(gets_result.code,200)
        
        put_result = self.api.cells_sparkline_groups_put_worksheet_sparkline_group(name, sheet_name,"Line","C6:E13",'false', "G6:G13", folder=folder)
        self.assertEqual(put_result.code,200)

        get_result = self.api.cells_sparkline_groups_get_worksheet_sparkline_group(name, sheet_name,index, folder=folder)
        self.assertEqual(get_result.code,200)
        
        sparkline_group = SparklineGroups()
        post_result = self.api.cells_sparkline_groups_post_worksheet_sparkline_group(name, sheet_name,index,sparkline_group, folder=folder)
        self.assertEqual(post_result.code,200)      

        del_result = self.api.cells_sparkline_groups_delete_worksheet_sparkline_group(name, sheet_name,index, folder=folder)
        self.assertEqual(del_result.code,200) 

        dels_result = self.api.cells_sparkline_groups_delete_worksheet_sparkline_groups(name, sheet_name, folder=folder)
        self.assertEqual(dels_result.code,200) 
        pass
 

if __name__ == '__main__':
    unittest.main()
    