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

class TestBatchControllerApi(unittest.TestCase):
    def setUp(self):
        warnings.simplefilter('ignore', ResourceWarning)
        global global_api
        if global_api is None:
           global_api = CellsApi(AuthUtil.GetClientId(),AuthUtil.GetClientSecret(),"v3.0",AuthUtil.GetBaseUrl())
        self.api = global_api

    def tearDown(self):
        pass

    def test_post_batch_convert(self):
        remote_folder = 'TestData/In'

        local_book1 = 'Book1.xlsx'
        remote_book1 = 'Book1.xlsx'
        local_my_doc = 'myDocument.xlsx'
        remote_my_doc = 'myDocument.xlsx'

        batchConvertRequestMatchCondition = MatchConditionRequest(regex_pattern= '(^Book)(.+)(xlsx$)' )
        batchConvertRequest = BatchConvertRequest(source_folder= remote_folder ,format= 'pdf' ,out_folder= 'OutResult' ,match_condition= batchConvertRequestMatchCondition )
        result = AuthUtil.Ready(self.api, local_book1, remote_folder + '/' + remote_book1 ,  '')
        self.assertTrue(len(result.uploaded)>0) 
        result = AuthUtil.Ready(self.api, local_my_doc, remote_folder + '/' + remote_my_doc ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PostBatchConvertRequest( batchConvertRequest)
        self.api.post_batch_convert(request)
        time.sleep(1)

    def test_post_batch_protect(self):
        remote_folder = 'TestData/In'

        local_book1 = 'Book1.xlsx'
        remote_book1 = 'Book1.xlsx'
        local_my_doc = 'myDocument.xlsx'
        remote_my_doc = 'myDocument.xlsx'

        batchProtectRequestMatchCondition = MatchConditionRequest(regex_pattern= '(^Book)(.+)(xlsx$)' )
        batchProtectRequest = BatchProtectRequest(source_folder= remote_folder ,protection_type= 'All' ,password= '123456' ,out_folder= 'OutResult' ,match_condition= batchProtectRequestMatchCondition )
        result = AuthUtil.Ready(self.api, local_book1, remote_folder + '/' + remote_book1 ,  '')
        self.assertTrue(len(result.uploaded)>0) 
        result = AuthUtil.Ready(self.api, local_my_doc, remote_folder + '/' + remote_my_doc ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PostBatchProtectRequest( batchProtectRequest)
        self.api.post_batch_protect(request)
        time.sleep(1)

    def test_post_batch_lock(self):
        remote_folder = 'TestData/In'

        local_book1 = 'Book1.xlsx'
        remote_book1 = 'Book1.xlsx'
        local_my_doc = 'myDocument.xlsx'
        remote_my_doc = 'myDocument.xlsx'

        batchLockRequestMatchCondition = MatchConditionRequest(regex_pattern= '(^Book)(.+)(xlsx$)' )
        batchLockRequest = BatchLockRequest(source_folder= remote_folder ,password= '123456' ,out_folder= 'OutResult' ,match_condition= batchLockRequestMatchCondition )
        result = AuthUtil.Ready(self.api, local_book1, remote_folder + '/' + remote_book1 ,  '')
        self.assertTrue(len(result.uploaded)>0) 
        result = AuthUtil.Ready(self.api, local_my_doc, remote_folder + '/' + remote_my_doc ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PostBatchLockRequest( batchLockRequest)
        self.api.post_batch_lock(request)
        time.sleep(1)

    def test_post_batch_unlock(self):
        remote_folder = 'TestData/In'

        local_book1 = 'Book1.xlsx'
        remote_book1 = 'Book1.xlsx'
        local_my_doc = 'myDocument.xlsx'
        remote_my_doc = 'myDocument.xlsx'

        batchLockRequestMatchCondition = MatchConditionRequest(regex_pattern= '(^Book)(.+)(xlsx$)' )
        batchLockRequest = BatchLockRequest(source_folder= remote_folder ,password= '123456' ,out_folder= 'OutResult' ,match_condition= batchLockRequestMatchCondition )
        result = AuthUtil.Ready(self.api, local_book1, remote_folder + '/' + remote_book1 ,  '')
        self.assertTrue(len(result.uploaded)>0) 
        result = AuthUtil.Ready(self.api, local_my_doc, remote_folder + '/' + remote_my_doc ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PostBatchUnlockRequest( batchLockRequest)
        self.api.post_batch_unlock(request)
        time.sleep(1)

if __name__ == '__main__':
    unittest.main()