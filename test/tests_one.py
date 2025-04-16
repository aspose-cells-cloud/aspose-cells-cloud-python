# coding: utf-8

from __future__ import absolute_import

import base64
import os
import shutil
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
        cellsApi = CellsApi(AuthUtil.GetClientId(),AuthUtil.GetClientSecret())
        convertOption = ConvertWorkbookOptions ()
        convertOption.convert_format = 'png'
        convertOption.file_info = FileInfo()
        convertOption.file_info.filename = "Book1.xlsx"          
        with open("TestData/Book1.xlsx", "rb") as excel_file:
            convertOption.file_info.file_content = base64.b64encode(excel_file.read()).decode("utf-8") 
        convertOption.page_setup = PageSetup()
        convertOption.page_setup.print_headings = True
        convertWorkbookRequest = PostConvertWorkbookRequest(convertOption)
        fileInfo = cellsApi.post_convert_workbook(convertWorkbookRequest)
        file_bytes = base64.b64decode(fileInfo.file_content)
        
        with open(fileInfo.filename, "wb") as f:
            f.write(file_bytes)
        # remote_folder = 'TestData/In'


        # local_name = 'Book1.xlsx'
        # remote_name = 'Book1.xlsx'

        # with open("../TestData/" + local_name, 'rb') as f:
        #     filename = os.path.basename(f.name)
        #     filedata = f.read()
        #     request = PutConvertWorkbookRequest({filename:filedata}, format='pdf')
        #     response = self.api.put_convert_workbook(request)
        #     shutil.move(response, 'ExampleData3.pdf')

        # with open("../TestData/" + local_name, 'rb') as f:
        #     filename = os.path.basename(f.name)
        #     filedata = f.read()
        #     request = PutConvertWorkbookRequest(filedata, format='pdf')
        #     response = self.api.put_convert_workbook(request)
        #     shutil.move(response, 'ExampleData3.pdf')

        # mapFiles = {
        #     local_name:  "../TestData/" + local_name
        # }
        # request = PutConvertWorkbookRequest(mapFiles, format= 'pdf')


        # request = PutConvertWorkbookRequest("../TestData/" + local_name, format='pdf')
        # response = self.api.put_convert_workbook(request)
        # shutil.move(response, 'ExampleData2.pdf')
        # request =  UploadFileRequest( mapFiles, remote_folder + '/' + remote_name,storage_name= '')
        # self.api.upload_file(request)
        #
        # image_or_print_options =  ImageOrPrintOptions(one_page_per_sheet= True)
        # page_setup = PageSetup( black_and_white= True, bottom_margin=0,left_margin=0,top_margin=0,right_margin=0,print_headings= False )
        # range_operate_source = Range(column_count= 28 ,first_column= 1 ,first_row= 1 ,row_count= 42 )
        #
        # range_convert = RangeConvertRequest(source= range_operate_source ,image_or_print_options= image_or_print_options ,page_setup= page_setup , image_type= 'Png' )
        #
        # request =  PostWorksheetCellsRangeToImageRequest( remote_name, 'Retention Analysis', range_convert,folder= remote_folder,storage_name= '')
        # print(request.name)
        # response = self.api.post_worksheet_cells_range_to_image(request)
        # print(response)
        # # os.rename(response, 'ExampleData.png')
        # shutil.move(response, 'ExampleData.png')
        # source_name = 'Book1.xlsx'
        # target_name = 'myDocument.xlsx'

        # source_name = 'Book1.xlsx'
        # result = AuthUtil.Ready(self.api, source_name, remote_folder + '/' + source_name ,  '')
        # self.assertTrue(len(result.uploaded)>0) 

        # rangeOperateSource = Range(column_count= 3 ,first_column= 8 ,first_row= 4 ,row_count= 2, worksheet="Sheet1" )
        # rangeOperateTarget = Range(column_count= 3 ,first_column= 1,first_row= 1 ,row_count= 2 , worksheet="Sheet4")
        # rangeOperate = RangeCopyRequest(operate= 'CopyTo' ,source= rangeOperateSource ,target= rangeOperateTarget,target_workbook = remote_folder + '/' + target_name )

        # request =  PostWorksheetCellsRangesCopyRequest( source_name, 'Sheet1', rangeOperate,   folder= remote_folder,storage_name= '')
        # self.api.post_worksheet_cells_ranges_copy(request)        

        # remote_folder = 'TestData/In'

        # local_name = 'TestCase.xlsx'
        # remote_name = 'TestCase.xlsx'
        # result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        # self.assertTrue(len(result.uploaded)>0) 

        # top10Filter = Top10Filter(items= 1 ,is_percent= True ,field_index =0  )
        # filter_column = FilterColumn(filter_type='Top10Filter' , top10_filter = top10Filter )
        # autoFilter = AutoFilter(filter_columns= [filter_column] )
        # filter = PivotFilter(field_index= 0 ,filter_type= 'Count' ,auto_filter = autoFilter )

        # request =  PutWorksheetPivotTableFilterRequest( remote_name, 'Sheet4', 0, filter,need_re_calculate= True,folder= remote_folder,storage_name= '')
        # self.api.put_worksheet_pivot_table_filter(request)
        
        
    def tearDown(self):
        pass

   
if __name__ == '__main__':
    unittest.main()