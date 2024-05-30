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

class TestPropertiesControllerApi(unittest.TestCase):
    def setUp(self):
        warnings.simplefilter('ignore', ResourceWarning)
        global global_api
        if global_api is None:
           global_api = CellsApi(AuthUtil.GetClientId(),AuthUtil.GetClientSecret(),"v3.0",AuthUtil.GetBaseUrl())
        self.api = global_api

    def tearDown(self):
        pass

    def test_get_document_properties(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  GetDocumentPropertiesRequest( remote_name,type= 'All',folder= remote_folder,storage_name= '')
        self.api.get_document_properties(request)
        time.sleep(1)

    def test_get_document_property(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  GetDocumentPropertyRequest( remote_name, 'Author',folder= remote_folder,storage_name= '')
        self.api.get_document_property(request)
        time.sleep(1)

    def test_put_document_property(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        property = CellsDocumentProperty(name= 'Author' ,value= 'cells developer' )
        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PutDocumentPropertyRequest( remote_name, property,folder= remote_folder,storage_name= '')
        self.api.put_document_property(request)
        time.sleep(1)

    def test_delete_document_property(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  DeleteDocumentPropertyRequest( remote_name, 'Author',type= 'All',folder= remote_folder,storage_name= '')
        self.api.delete_document_property(request)
        time.sleep(1)

    def test_delete_document_properties(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  DeleteDocumentPropertiesRequest( remote_name,folder= remote_folder,storage_name= '')
        self.api.delete_document_properties(request)
        time.sleep(1)

if __name__ == '__main__':
    unittest.main()