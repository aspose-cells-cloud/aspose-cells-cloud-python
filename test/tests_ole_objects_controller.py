# coding: utf-8

from __future__ import absolute_import

import os
import sys
import unittest
import warnings

ABSPATH = os.path.abspath(os.path.realpath(os.path.dirname(__file__)) + "/..")
sys.path.append(ABSPATH)

from asposecellscloud.rest import ApiException
from asposecellscloud.apis.cells_api import CellsApi
import AuthUtil
from asposecellscloud.models import *
from asposecellscloud.requests import *

global_api = None

class TestOleObjectsControllerApi(unittest.TestCase):
    def setUp(self):
        warnings.simplefilter('ignore', ResourceWarning)
        global global_api
        if global_api is None:
           global_api = CellsApi(AuthUtil.GetClientId(),AuthUtil.GetClientSecret(),"v3.0",AuthUtil.GetBaseUrl())
        self.api = global_api

    def tearDown(self):
        pass

    def test_get_worksheet_ole_objects(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  GetWorksheetOleObjectsRequest( remote_name, 'Sheet6',folder= remote_folder,storage_name= '')
        self.api.get_worksheet_ole_objects(request)


    def test_get_worksheet_ole_object(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  GetWorksheetOleObjectRequest( remote_name, 'Sheet6', 0,format= 'png',folder= remote_folder,storage_name= '')
        self.api.get_worksheet_ole_object(request)


    def test_delete_worksheet_ole_objects(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  DeleteWorksheetOleObjectsRequest( remote_name, 'Sheet6',folder= remote_folder,storage_name= '')
        self.api.delete_worksheet_ole_objects(request)


    def test_delete_worksheet_ole_object(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  DeleteWorksheetOleObjectRequest( remote_name, 'Sheet6', 0,folder= remote_folder,storage_name= '')
        self.api.delete_worksheet_ole_object(request)


    def test_post_update_worksheet_ole_object(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        ole = OleObject(left= 10 ,right= 10 ,height= 90 ,width= 78 )
        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PostUpdateWorksheetOleObjectRequest( remote_name, 'Sheet6', 0, ole,folder= remote_folder,storage_name= '')
        self.api.post_update_worksheet_ole_object(request)


    def test_put_worksheet_ole_object(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        ole_doc = 'OLEDoc.docx'
        word_jpg = 'word.jpg'
        remote_name = 'Book1.xlsx'

        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
        result = AuthUtil.Ready(self.api, ole_doc, 'OLEDoc.docx' ,  '')
        self.assertTrue(len(result.uploaded)>0) 
        result = AuthUtil.Ready(self.api, word_jpg, 'word.jpg' ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PutWorksheetOleObjectRequest( remote_name, 'Sheet6',upper_left_row= 1,upper_left_column= 1,height= 100,width= 80,ole_file= 'OLEDoc.docx',image_file= 'word.jpg',folder= remote_folder,storage_name= '')
        self.api.put_worksheet_ole_object(request)


if __name__ == '__main__':
    unittest.main()