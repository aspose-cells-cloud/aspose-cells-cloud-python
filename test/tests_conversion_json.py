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

class TestConversionJsonApi(unittest.TestCase):
    def setUp(self):
        warnings.simplefilter('ignore', ResourceWarning)
        global global_api
        if global_api is None:
           global_api = CellsApi(AuthUtil.GetClientId(),AuthUtil.GetClientSecret(),"v3.0",AuthUtil.GetBaseUrl())
        self.api = global_api

    def tearDown(self):
        pass

    def test_convert_workbook_csv(self):
        remote_folder = 'TestData/In'

        local_name = 'codegen-spec.json'
        remote_name = 'codegen-spec.json'

        format = 'csv'

        mapFiles = { 
            local_name: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +local_name             
        }
        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PutConvertWorkbookRequest( mapFiles,format= format)
        self.api.put_convert_workbook(request)
        time.sleep(1)

    def test_convert_workbook_xls(self):
        remote_folder = 'TestData/In'

        local_name = 'codegen-spec.json'
        remote_name = 'codegen-spec.json'

        format = 'xls'

        mapFiles = { 
            local_name: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +local_name             
        }
        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PutConvertWorkbookRequest( mapFiles,format= format)
        self.api.put_convert_workbook(request)
        time.sleep(1)

    def test_convert_workbook_html(self):
        remote_folder = 'TestData/In'

        local_name = 'codegen-spec.json'
        remote_name = 'codegen-spec.json'

        format = 'html'

        mapFiles = { 
            local_name: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +local_name             
        }
        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PutConvertWorkbookRequest( mapFiles,format= format)
        self.api.put_convert_workbook(request)
        time.sleep(1)

    def test_convert_workbook_mhtml(self):
        remote_folder = 'TestData/In'

        local_name = 'codegen-spec.json'
        remote_name = 'codegen-spec.json'

        format = 'mhtml'

        mapFiles = { 
            local_name: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +local_name             
        }
        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PutConvertWorkbookRequest( mapFiles,format= format)
        self.api.put_convert_workbook(request)
        time.sleep(1)

    def test_convert_workbook_ods(self):
        remote_folder = 'TestData/In'

        local_name = 'codegen-spec.json'
        remote_name = 'codegen-spec.json'

        format = 'ods'

        mapFiles = { 
            local_name: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +local_name             
        }
        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PutConvertWorkbookRequest( mapFiles,format= format)
        self.api.put_convert_workbook(request)
        time.sleep(1)

    def test_convert_workbook_pdf(self):
        remote_folder = 'TestData/In'

        local_name = 'codegen-spec.json'
        remote_name = 'codegen-spec.json'

        format = 'pdf'

        mapFiles = { 
            local_name: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +local_name             
        }
        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PutConvertWorkbookRequest( mapFiles,format= format)
        self.api.put_convert_workbook(request)
        time.sleep(1)

    def test_convert_workbook_xml(self):
        remote_folder = 'TestData/In'

        local_name = 'codegen-spec.json'
        remote_name = 'codegen-spec.json'

        format = 'xml'

        mapFiles = { 
            local_name: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +local_name             
        }
        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PutConvertWorkbookRequest( mapFiles,format= format)
        self.api.put_convert_workbook(request)
        time.sleep(1)

    def test_convert_workbook_txt(self):
        remote_folder = 'TestData/In'

        local_name = 'codegen-spec.json'
        remote_name = 'codegen-spec.json'

        format = 'txt'

        mapFiles = { 
            local_name: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +local_name             
        }
        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PutConvertWorkbookRequest( mapFiles,format= format)
        self.api.put_convert_workbook(request)
        time.sleep(1)

    def test_convert_workbook_xlsb(self):
        remote_folder = 'TestData/In'

        local_name = 'codegen-spec.json'
        remote_name = 'codegen-spec.json'

        format = 'xlsb'

        mapFiles = { 
            local_name: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +local_name             
        }
        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PutConvertWorkbookRequest( mapFiles,format= format)
        self.api.put_convert_workbook(request)
        time.sleep(1)

    def test_convert_workbook_xps(self):
        remote_folder = 'TestData/In'

        local_name = 'codegen-spec.json'
        remote_name = 'codegen-spec.json'

        format = 'xps'

        mapFiles = { 
            local_name: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +local_name             
        }
        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PutConvertWorkbookRequest( mapFiles,format= format)
        self.api.put_convert_workbook(request)
        time.sleep(1)

    def test_convert_workbook_md(self):
        remote_folder = 'TestData/In'

        local_name = 'codegen-spec.json'
        remote_name = 'codegen-spec.json'

        format = 'md'

        mapFiles = { 
            local_name: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +local_name             
        }
        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PutConvertWorkbookRequest( mapFiles,format= format)
        self.api.put_convert_workbook(request)
        time.sleep(1)

    def test_convert_workbook_numbers(self):
        remote_folder = 'TestData/In'

        local_name = 'codegen-spec.json'
        remote_name = 'codegen-spec.json'

        format = 'numbers'

        mapFiles = { 
            local_name: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +local_name             
        }
        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PutConvertWorkbookRequest( mapFiles,format= format)
        self.api.put_convert_workbook(request)
        time.sleep(1)

    def test_convert_workbook_svg(self):
        remote_folder = 'TestData/In'

        local_name = 'codegen-spec.json'
        remote_name = 'codegen-spec.json'

        format = 'svg'

        mapFiles = { 
            local_name: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +local_name             
        }
        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PutConvertWorkbookRequest( mapFiles,format= format)
        self.api.put_convert_workbook(request)
        time.sleep(1)

    def test_convert_workbook_docx(self):
        remote_folder = 'TestData/In'

        local_name = 'codegen-spec.json'
        remote_name = 'codegen-spec.json'

        format = 'docx'

        mapFiles = { 
            local_name: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +local_name             
        }
        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PutConvertWorkbookRequest( mapFiles,format= format)
        self.api.put_convert_workbook(request)
        time.sleep(1)

    def test_convert_workbook_pptx(self):
        remote_folder = 'TestData/In'

        local_name = 'codegen-spec.json'
        remote_name = 'codegen-spec.json'

        format = 'pptx'

        mapFiles = { 
            local_name: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +local_name             
        }
        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PutConvertWorkbookRequest( mapFiles,format= format)
        self.api.put_convert_workbook(request)
        time.sleep(1)

    def test_convert_workbook_json(self):
        remote_folder = 'TestData/In'

        local_name = 'codegen-spec.json'
        remote_name = 'codegen-spec.json'

        format = 'json'

        mapFiles = { 
            local_name: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +local_name             
        }
        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PutConvertWorkbookRequest( mapFiles,format= format)
        self.api.put_convert_workbook(request)
        time.sleep(1)

    def test_convert_workbook_sql(self):
        remote_folder = 'TestData/In'

        local_name = 'codegen-spec.json'
        remote_name = 'codegen-spec.json'

        format = 'sql'

        mapFiles = { 
            local_name: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +local_name             
        }
        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PutConvertWorkbookRequest( mapFiles,format= format)
        self.api.put_convert_workbook(request)
        time.sleep(1)

if __name__ == '__main__':
    unittest.main()