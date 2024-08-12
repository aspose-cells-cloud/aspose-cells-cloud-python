# coding: utf-8

from __future__ import absolute_import

import os
import sys
import unittest
import warnings
import time

ABSPATH = os.path.abspath(os.path.realpath(os.path.dirname(__file__)) + "/..")
sys.path.append(ABSPATH)

from asposecellscloud.rest import ApiException
from asposecellscloud.apis.cells_api import CellsApi
import AuthUtil
from asposecellscloud.models import *
from asposecellscloud.requests import *

global_api = None

class TestChartsControllerApi(unittest.TestCase):
    def setUp(self):
        warnings.simplefilter('ignore', ResourceWarning)
        global global_api
        if global_api is None:
           global_api = CellsApi(AuthUtil.GetClientId(),AuthUtil.GetClientSecret(),"v3.0",AuthUtil.GetBaseUrl())
        self.api = global_api

    def tearDown(self):
        pass

    def test_get_worksheet_charts(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  GetWorksheetChartsRequest( remote_name, 'Sheet4',folder= remote_folder,storage_name= '')
        self.api.get_worksheet_charts(request)
        

    def test_get_worksheet_chart(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  GetWorksheetChartRequest( remote_name, 'Sheet4', 0,format= 'png',folder= remote_folder,storage_name= '')
        self.api.get_worksheet_chart(request)
        

    def test_put_worksheet_chart(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PutWorksheetChartRequest( remote_name, 'Sheet4', 'Pie',upper_left_row= 5,upper_left_column= 5,lower_right_row= 10,lower_right_column= 10,area= 'C7:D11',is_vertical= True,title= 'Aspose Chart',folder= remote_folder,storage_name= '')
        self.api.put_worksheet_chart(request)
        

    def test_delete_worksheet_chart(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  DeleteWorksheetChartRequest( remote_name, 'Sheet4', 0,folder= remote_folder,storage_name= '')
        self.api.delete_worksheet_chart(request)
        

    def test_post_worksheet_chart(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        chart = Chart(show_legend= True ,show_data_table= True )
        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PostWorksheetChartRequest( remote_name, 'Sheet4', 0, chart,folder= remote_folder,storage_name= '')
        self.api.post_worksheet_chart(request)
        

    def test_get_worksheet_chart_legend(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  GetWorksheetChartLegendRequest( remote_name, 'Sheet4', 0,folder= remote_folder,storage_name= '')
        self.api.get_worksheet_chart_legend(request)
        

    def test_post_worksheet_chart_legend(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        legend = Legend(position= 'Top' )
        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PostWorksheetChartLegendRequest( remote_name, 'Sheet4', 0, legend,folder= remote_folder,storage_name= '')
        self.api.post_worksheet_chart_legend(request)
        

    def test_put_worksheet_chart_legend(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PutWorksheetChartLegendRequest( remote_name, 'Sheet4', 0,folder= remote_folder,storage_name= '')
        self.api.put_worksheet_chart_legend(request)
        

    def test_delete_worksheet_chart_legend(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  DeleteWorksheetChartLegendRequest( remote_name, 'Sheet4', 0,folder= remote_folder,storage_name= '')
        self.api.delete_worksheet_chart_legend(request)
        

    def test_delete_worksheet_charts(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  DeleteWorksheetChartsRequest( remote_name, 'Sheet4',folder= remote_folder,storage_name= '')
        self.api.delete_worksheet_charts(request)
        

    def test_get_worksheet_chart_title(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  GetWorksheetChartTitleRequest( remote_name, 'Sheet4', 0,folder= remote_folder,storage_name= '')
        self.api.get_worksheet_chart_title(request)
        

    def test_post_worksheet_chart_title(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        title = Title(is_visible= True )
        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PostWorksheetChartTitleRequest( remote_name, 'Sheet4', 0, title,folder= remote_folder,storage_name= '')
        self.api.post_worksheet_chart_title(request)
        

    def test_put_worksheet_chart_title(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        title = Title(is_visible= True )
        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PutWorksheetChartTitleRequest( remote_name, 'Sheet4', 0,title= title,folder= remote_folder,storage_name= '')
        self.api.put_worksheet_chart_title(request)
        

    def test_delete_worksheet_chart_title(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  DeleteWorksheetChartTitleRequest( remote_name, 'Sheet4', 0,folder= remote_folder,storage_name= '')
        self.api.delete_worksheet_chart_title(request)
        

if __name__ == '__main__':
    unittest.main()