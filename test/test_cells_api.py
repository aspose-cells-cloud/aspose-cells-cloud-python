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
import AuthUtil
from asposecellscloud.models import CalculationOptions
from asposecellscloud.models import FontSetting
from asposecellscloud.models import Font
from asposecellscloud.models import Style
global_api = None
class TestCellsApi(unittest.TestCase):
    """ CellsApi unit test stubs """
    
    def setUp(self):
        global global_api
        if global_api is None:
           global_api = asposecellscloud.apis.cells_api.CellsApi(AuthUtil.GetAPPSID(),AuthUtil.GetAPPKey(),"v3.0",'https://api-qa.aspose.cloud')
        self.api = global_api

    def tearDown(self):
        pass

    def test_cells_delete_worksheet_columns(self):
        """
        Test case for cells_delete_worksheet_columns

        Delete worksheet columns.
        """
        name ='Book1.xlsx'
        sheet_name ='Sheet1'
        column_index = 1 
        columns = 2
        update_reference = True
        folder = "PythonTest"
        result = AuthUtil.Ready(self.api, name, folder)
        self.assertTrue(len(result.uploaded)>0)        
        result = self.api.cells_delete_worksheet_columns(name, sheet_name, column_index, columns, update_reference, folder = folder)
        self.assertEqual(result.code,200)
        pass

    def test_cells_delete_worksheet_row(self):
        """
        Test case for cells_delete_worksheet_row

        Delete worksheet row.
        """
        name ='Book1.xlsx'
        sheet_name ='Sheet1'
        row_index = 1  
        folder = "PythonTest"
        result = AuthUtil.Ready(self.api, name, folder)
        self.assertTrue(len(result.uploaded)>0)
        
        result = self.api.cells_delete_worksheet_row(name, sheet_name, row_index, folder = folder)
        self.assertEqual(result.code,200)
        pass

    def test_cells_delete_worksheet_rows(self):
        """
        Test case for cells_delete_worksheet_rows

        Delete several worksheet rows.
        """
        name ='Book1.xlsx'
        sheet_name ='Sheet1'
        startrow = 1  
        total_rows =2
        update_reference = True
        folder = "PythonTest"
        result = AuthUtil.Ready(self.api, name, folder)
        self.assertTrue(len(result.uploaded)>0)
        
        result = self.api.cells_delete_worksheet_rows(name, sheet_name, startrow, total_rows = total_rows, update_reference = update_reference, folder = folder)
        self.assertEqual(result.code,200)
        pass

    def test_cells_get_worksheet_cell(self):
        """
        Test case for cells_get_worksheet_cell

        Read cell data by cell's name.
        """
        name ='Book1.xlsx'
        sheet_name ='Sheet1'
        cell_or_method_name = 'C1'  
        folder = "PythonTest"
        result = AuthUtil.Ready(self.api, name, folder)
        self.assertTrue(len(result.uploaded)>0)
        
        result = self.api.cells_get_worksheet_cell(name, sheet_name, cell_or_method_name, folder = folder)
        # self.assertEqual(result.Code,200)
        pass

    def test_cells_get_worksheet_cell_style(self):
        """
        Test case for cells_get_worksheet_cell_style

        Read cell's style info.
        """
        name ='Book1.xlsx'
        sheet_name ='Sheet1'
        cellName = 'C1'  
        folder = "PythonTest"
        result = AuthUtil.Ready(self.api, name, folder)
        self.assertTrue(len(result.uploaded)>0)
        
        result = self.api.cells_get_worksheet_cell_style(name, sheet_name, cellName, folder = folder)
        self.assertEqual(result.code,200)
        pass

    def test_cells_get_worksheet_cells(self):
        """
        Test case for cells_get_worksheet_cells

        Get cells info.
        """
        name ='Book1.xlsx'
        sheet_name ='Sheet1'
        offest = 2  
        count =10
        folder = "PythonTest"
        result = AuthUtil.Ready(self.api, name, folder)
        self.assertTrue(len(result.uploaded)>0)
        
        result = self.api.cells_get_worksheet_cells(name, sheet_name, offest = offest, count = count, folder = folder)
        self.assertEqual(result.code,200)
        pass

    def test_cells_get_worksheet_column(self):
        """
        Test case for cells_get_worksheet_column

        Read worksheet column data by column's index.
        """
        name ='Book1.xlsx'
        sheet_name ='Sheet1'
        columnIndex = 2  
        folder = "PythonTest"
        result = AuthUtil.Ready(self.api, name, folder)
        self.assertTrue(len(result.uploaded)>0)
        
        result = self.api.cells_get_worksheet_column(name, sheet_name, columnIndex, folder = folder)
        self.assertEqual(result.code,200)
        pass

    def test_cells_get_worksheet_columns(self):
        """
        Test case for cells_get_worksheet_columns

        Read worksheet columns info.
        """
        name ='Book1.xlsx'
        sheet_name ='Sheet1'
        folder = "PythonTest"
        result = AuthUtil.Ready(self.api, name, folder)
        self.assertTrue(len(result.uploaded)>0)
        
        result = self.api.cells_get_worksheet_columns(name, sheet_name, folder = folder)
        self.assertEqual(result.code,200)
        pass

    def test_cells_get_worksheet_row(self):
        """
        Test case for cells_get_worksheet_row

        Read worksheet row data by row's index.
        """
        name ='Book1.xlsx'
        sheet_name ='Sheet1'
        rowIndex = 1  
        folder = "PythonTest"
        result = AuthUtil.Ready(self.api, name, folder)
        self.assertTrue(len(result.uploaded)>0)
        
        result = self.api.cells_get_worksheet_row(name, sheet_name, rowIndex,folder=folder)
        self.assertEqual(result.code,200)
        pass

    def test_cells_get_worksheet_rows(self):
        """
        Test case for cells_get_worksheet_rows

        Read worksheet rows info.
        """
        name ='Book1.xlsx'
        sheet_name ='Sheet1'
        folder = "PythonTest"
        result = AuthUtil.Ready(self.api, name, folder)
        self.assertTrue(len(result.uploaded)>0)
        
        result = self.api.cells_get_worksheet_rows(name, sheet_name, folder = folder)
        self.assertEqual(result.code,200)
        pass

    def test_cells_post_cell_calculate(self):
        """
        Test case for cells_post_cell_calculate

        Cell calculate formula
        """
        name ='Book1.xlsx'
        sheet_name ='Sheet1'
        cellName = 'C1'  
        options = CalculationOptions()
        options.recursive = True
        options.ignore_error = True
        folder = "PythonTest"
        result = AuthUtil.Ready(self.api, name, folder)
        self.assertTrue(len(result.uploaded)>0)
        
        result = self.api.cells_post_cell_calculate(name, sheet_name,cellName, options = options, folder = folder)
        self.assertEqual(result.code,200)
        pass

    # def test_cells_post_cell_characters(self):
    #     """
    #     Test case for cells_post_cell_characters

    #     Set cell characters 
    #     """
    #     name ='Book1.xlsx'
    #     sheet_name ='Sheet2'
    #     cellName = 'G8'
    #     font = Font()
    #     font.size = 10.0
    #     fs1 = FontSetting(font, 2, 0)
    #     options = [fs1]
    #     folder = "PythonTest"
    #     result = AuthUtil.Ready(self.api, name, folder)
    #     self.assertTrue(len(result.uploaded)>0)
        
    #     result = self.api.cells_post_cell_characters(name, sheet_name, cellName, options=options, folder=folder)
    #     self.assertEqual(result.code,200)
    #     pass

    def test_cells_post_clear_contents(self):
        """
        Test case for cells_post_clear_contents

        Clear cells contents.
        """
        name ='Book1.xlsx'
        sheet_name ='Sheet1'
        range = 'A1:C10'  
        startRow = 1
        startColumn =1
        endRow = 3
        endColumn = 3
        folder = "PythonTest"
        result = AuthUtil.Ready(self.api, name, folder)
        self.assertTrue(len(result.uploaded)>0)
        
        result = self.api.cells_post_clear_contents(name, sheet_name, range = range, start_row = startRow,start_column = startColumn,end_row=endRow,end_column=endColumn,folder=folder)
        self.assertEqual(result.code,200)
        pass

    def test_cells_post_clear_formats(self):
        """
        Test case for cells_post_clear_formats

        Clear cells contents.
        """
        name ='Book1.xlsx'
        sheet_name ='Sheet1'
        range = 'A1:C10'  
        startRow = 1
        startColumn =1
        endRow = 3
        endColumn = 3
        folder = "PythonTest"
        result = AuthUtil.Ready(self.api, name, folder)
        self.assertTrue(len(result.uploaded)>0)
        
        result = self.api.cells_post_clear_formats(name, sheet_name, range=range, start_row=startRow,start_column=startColumn,end_row=endRow,end_column=endColumn,folder=folder)
        self.assertEqual(result.code,200)
        pass

    def test_cells_post_column_style(self):
        """
        Test case for cells_post_column_style

        Set column style
        """
        name ='Book1.xlsx'
        sheet_name ='Sheet1'
        columnIndex = 1  
        style = Style()
        font = Font()
        font.is_bold = True
        font.size = 10
        style.font = font
        folder = "PythonTest"
        result = AuthUtil.Ready(self.api, name, folder)
        self.assertTrue(len(result.uploaded)>0)
        
        result = self.api.cells_post_column_style(name, sheet_name, columnIndex, style=style,folder=folder)
        self.assertEqual(result.code,200)
        pass

    def test_cells_post_copy_cell_into_cell(self):
        """
        Test case for cells_post_copy_cell_into_cell

        Copy cell into cell
        """
        name ='Book1.xlsx'
        sheet_name ='Sheet1'
        destCellName = 'C1'  
        worksheet = 'Sheet2'
        cellName ='B1' 
        row =1
        column =2       
        folder = "PythonTest"
        result = AuthUtil.Ready(self.api, name, folder)
        self.assertTrue(len(result.uploaded)>0)
        
        result = self.api.cells_post_copy_cell_into_cell(name, cellName,sheet_name, worksheet, cellname=cellName,row=row,column=column,folder=folder)
        self.assertEqual(result.code,200)
        pass

    def test_cells_post_copy_worksheet_columns(self):
        """
        Test case for cells_post_copy_worksheet_columns

        Copy worksheet columns.
        """
        name ='Book1.xlsx'
        sheet_name ='Sheet1'
        sourceColumnIndex = 1  
        destinationColumnIndex = 21
        columnNumber =1 
        worksheet ='Sheet2'       
        folder = "PythonTest"
        result = AuthUtil.Ready(self.api, name, folder)
        self.assertTrue(len(result.uploaded)>0)
        
        result = self.api.cells_post_copy_worksheet_columns(name, sheet_name, sourceColumnIndex, destinationColumnIndex,columnNumber,worksheet=worksheet,folder=folder)
        self.assertEqual(result.code,200)
        pass

    def test_cells_post_copy_worksheet_rows(self):
        """
        Test case for cells_post_copy_worksheet_rows

        Copy worksheet rows.
        """
        name ='Book1.xlsx'
        sheet_name ='Sheet1'
        sourceRowIndex = 1  
        destinationRowIndex = 21
        rowNumber =1 
        worksheet ='Sheet2'       
        folder = "PythonTest"
        result = AuthUtil.Ready(self.api, name, folder)
        self.assertTrue(len(result.uploaded)>0)
        
        result = self.api.cells_post_copy_worksheet_rows(name, sheet_name, sourceRowIndex, destinationRowIndex,rowNumber,worksheet=worksheet,folder=folder)
        self.assertEqual(result.code,200)
        pass

    def test_cells_post_group_worksheet_columns(self):
        """
        Test case for cells_post_group_worksheet_columns

        Group worksheet columns.
        """
        name ='Book1.xlsx'
        sheet_name ='Sheet1'
        firstIndex = 1  
        lastIndex = 21
        hide ='true'       
        folder = "PythonTest"
        result = AuthUtil.Ready(self.api, name, folder)
        self.assertTrue(len(result.uploaded)>0)
        
        result = self.api.cells_post_group_worksheet_columns(name, sheet_name, firstIndex, lastIndex,hide=hide,folder=folder)
        self.assertEqual(result.code,200)
        pass

    def test_cells_post_group_worksheet_rows(self):
        """
        Test case for cells_post_group_worksheet_rows

        Group worksheet rows.
        """
        name ='Book1.xlsx'
        sheet_name ='Sheet1'
        firstIndex = 1  
        lastIndex = 21
        hide ='true'       
        folder = "PythonTest"
        result = AuthUtil.Ready(self.api, name, folder)
        self.assertTrue(len(result.uploaded)>0)
        
        result = self.api.cells_post_group_worksheet_rows(name, sheet_name, firstIndex, lastIndex,hide=hide,folder=folder)
        self.assertEqual(result.code,200)
        pass

    def test_cells_post_hide_worksheet_columns(self):
        """
        Test case for cells_post_hide_worksheet_columns

        Hide worksheet columns.
        """
        name ='Book1.xlsx'
        sheet_name ='Sheet1'
        startColumn = 1  
        totalColumns = 21
        folder = "PythonTest"
        result = AuthUtil.Ready(self.api, name, folder)
        self.assertTrue(len(result.uploaded)>0)
        
        result = self.api.cells_post_hide_worksheet_columns(name, sheet_name, startColumn, totalColumns,folder=folder)
        self.assertEqual(result.code,200)
        pass

    def test_cells_post_hide_worksheet_rows(self):
        """
        Test case for cells_post_hide_worksheet_rows

        Hide worksheet rows.
        """
        name ='Book1.xlsx'
        sheet_name ='Sheet1'
        startrow = 1  
        totalRows = 21
        folder = "PythonTest"
        result = AuthUtil.Ready(self.api, name, folder)
        self.assertTrue(len(result.uploaded)>0)
        
        result = self.api.cells_post_hide_worksheet_rows(name, sheet_name, startrow, totalRows,folder=folder)
        self.assertEqual(result.code,200)
        pass

    def test_cells_post_row_style(self):
        """
        Test case for cells_post_row_style

        Set row style.
        """
        name ='Book1.xlsx'
        sheet_name ='Sheet1'
        rowIndex = 1  
        style = Style()
        font = Font()
        font.is_bold = True
        font.size = 10
        style.font = font
        folder = "PythonTest"
        result = AuthUtil.Ready(self.api, name, folder)
        self.assertTrue(len(result.uploaded)>0)
        
        result = self.api.cells_post_row_style(name, sheet_name, rowIndex, style=style,folder=folder)
        self.assertEqual(result.code,200)
        pass

    def test_cells_get_cell_html_string(self):
        """
        Test case for cells_get_cell_html_string

        Set htmlstring value into cell
        """
        name ='Book1.xlsx'
        sheet_name ='Sheet1'
        cellName = 'C1' 
        folder = "PythonTest"
        result = AuthUtil.Ready(self.api, name, folder)
        self.assertTrue(len(result.uploaded)>0)
        
        result = self.api.cells_get_cell_html_string(name, sheet_name, cellName,folder=folder)
        self.assertIsNotNone(result)
        pass

    def test_cells_post_set_cell_html_string(self):
        """
        Test case for cells_post_set_cell_html_string

        Set htmlstring value into cell
        """
        name ='Book1.xlsx'
        sheet_name ='Sheet1'
        cellName = 'C1'
        html_string = "http://api.aspose.cloud/v3.0/cells" 
        folder = "PythonTest"
        result = AuthUtil.Ready(self.api, name, folder)
        self.assertTrue(len(result.uploaded)>0)
        
        result = self.api.cells_post_set_cell_html_string(name, sheet_name, cellName,html_string,folder=folder)
        self.assertEqual(result.code,200)
        pass

    def test_cells_post_set_cell_range_value(self):
        """
        Test case for cells_post_set_cell_range_value

        Set cell range value 
        """
        name ='Book1.xlsx'
        sheet_name ='Sheet1'
        cellarea = 'A1:C10' 
        value = '12345' 
        type = 'String' 
        folder = "PythonTest"
        result = AuthUtil.Ready(self.api, name, folder)
        self.assertTrue(len(result.uploaded)>0)
        
        result = self.api.cells_post_set_cell_range_value(name, sheet_name, cellarea, value, type, folder = folder)
        self.assertEqual(result.code,200)
        pass

    def test_cells_post_set_worksheet_column_width(self):
        """
        Test case for cells_post_set_worksheet_column_width

        Set worksheet column width.
        """
        name ='Book1.xlsx'
        sheet_name ='Sheet1'
        columnIndex = 1 
        width = '10'
        folder = "PythonTest"
        result = AuthUtil.Ready(self.api, name, folder)
        self.assertTrue(len(result.uploaded)>0)
        
        result = self.api.cells_post_set_worksheet_column_width(name, sheet_name, columnIndex, width, folder = folder)
        self.assertEqual(result.code,200)
        pass

    def test_cells_post_ungroup_worksheet_columns(self):
        """
        Test case for cells_post_ungroup_worksheet_columns

        Ungroup worksheet columns.
        """
        name ='Book1.xlsx'
        sheet_name ='Sheet1'
        firstIndex = 1 
        lastIndex = 10
        folder = "PythonTest"
        result = AuthUtil.Ready(self.api, name, folder)
        self.assertTrue(len(result.uploaded)>0)
        
        result = self.api.cells_post_ungroup_worksheet_columns(name, sheet_name, firstIndex, lastIndex, folder=folder)
        self.assertEqual(result.code,200)
        pass

    def test_cells_post_ungroup_worksheet_rows(self):
        """
        Test case for cells_post_ungroup_worksheet_rows

        Ungroup worksheet rows.
        """
        name ='Book1.xlsx'
        sheet_name ='Sheet1'
        firstIndex = 1 
        lastIndex = 10
        isAll = True
        folder = "PythonTest"
        result = AuthUtil.Ready(self.api, name, folder)
        self.assertTrue(len(result.uploaded)>0)
        
        result = self.api.cells_post_ungroup_worksheet_rows(name, sheet_name, firstIndex, lastIndex,is_all=isAll, folder=folder)
        self.assertEqual(result.code,200)
        pass

    def test_cells_post_unhide_worksheet_columns(self):
        """
        Test case for cells_post_unhide_worksheet_columns

        Unhide worksheet columns.
        """
        name ='Book1.xlsx'
        sheet_name ='Sheet1'
        startcolumn = 1 
        totalColumns = 10
        width =20.0
        folder = "PythonTest"
        result = AuthUtil.Ready(self.api, name, folder)
        self.assertTrue(len(result.uploaded)>0)
        
        result = self.api.cells_post_unhide_worksheet_columns(name, sheet_name, startcolumn, totalColumns,width=width, folder=folder)
        self.assertEqual(result.code,200)
        pass

    def test_cells_post_unhide_worksheet_rows(self):
        """
        Test case for cells_post_unhide_worksheet_rows

        Unhide worksheet rows.
        """
        name ='Book1.xlsx'
        sheet_name ='Sheet1'
        startrow = 1 
        totalRows = 10
        height =20.0
        folder = "PythonTest"
        result = AuthUtil.Ready(self.api, name, folder)
        self.assertTrue(len(result.uploaded)>0)
        
        result = self.api.cells_post_unhide_worksheet_rows(name, sheet_name, startrow, totalRows, height = height, folder=folder)
        self.assertEqual(result.code,200)
        pass

    def test_cells_post_update_worksheet_cell_style(self):
        """
        Test case for cells_post_update_worksheet_cell_style

        Update cell's style.
        """
        name ='Book1.xlsx'
        sheet_name ='Sheet1'
        cellName = 'C1' 
        style = Style()
        font = Font()
        font.is_bold = True
        font.size = 10
        style.font = font
        folder = "PythonTest"
        result = AuthUtil.Ready(self.api, name, folder)
        self.assertTrue(len(result.uploaded)>0)
        
        result = self.api.cells_post_update_worksheet_cell_style(name, sheet_name, cellName, style=style, folder = folder)
        self.assertEqual(result.code,200)
        pass

    def test_cells_post_update_worksheet_range_style(self):
        """
        Test case for cells_post_update_worksheet_range_style

        Update cell's range style.
        """
        name ='Book1.xlsx'
        sheet_name ='Sheet1'
        range = 'C1:F10' 
        style = Style()
        font = Font()
        font.is_bold = True
        font.size = 10
        style.font = font
        folder = "PythonTest"
        result = AuthUtil.Ready(self.api, name, folder)
        self.assertTrue(len(result.uploaded)>0)
        
        result = self.api.cells_post_update_worksheet_range_style(name, sheet_name, range, style=style, folder=folder)
        self.assertEqual(result.code,200)
        pass

    def test_cells_post_update_worksheet_row(self):
        """
        Test case for cells_post_update_worksheet_row

        Update worksheet row.
        """
        name ='Book1.xlsx'
        sheet_name ='Sheet1'
        rowIndex = 1 
        height = 10.0
        folder = "PythonTest"
        result = AuthUtil.Ready(self.api, name, folder)
        self.assertTrue(len(result.uploaded)>0)
        
        result = self.api.cells_post_update_worksheet_row(name, sheet_name, rowIndex, height=height, folder=folder)
        self.assertEqual(result.code,200)
        pass

    def test_cells_post_worksheet_cell_set_value(self):
        """
        Test case for cells_post_worksheet_cell_set_value

        Set cell value.
        """
        name ='Book1.xlsx'
        sheet_name ='Sheet1'
        cellName = 'C1' 
        folder = "PythonTest"
        result = AuthUtil.Ready(self.api, name, folder)
        self.assertTrue(len(result.uploaded)>0)
        
        result = self.api.cells_post_worksheet_cell_set_value(name, sheet_name, cellName, value="1", type="String", folder=folder)
        result = self.api.cells_post_worksheet_cell_set_value(name, sheet_name, cellName, value="1", type="int", folder=folder)
        result = self.api.cells_post_worksheet_cell_set_value(name, sheet_name, cellName, value="2018/10/09", type="DateTime", formula='=Now()', folder=folder)
        self.assertEqual(result.code,200)
        pass

    def test_cells_post_worksheet_merge(self):
        """
        Test case for cells_post_worksheet_merge

        Merge cells.
        """
        name ='Book1.xlsx'
        sheet_name ='Sheet1'
        startRow = 1 
        startColumn = 1
        totalRows =10
        totalColumns = 2
        folder = "PythonTest"
        result = AuthUtil.Ready(self.api, name, folder)
        self.assertTrue(len(result.uploaded)>0)
        
        result = self.api.cells_post_worksheet_merge(name, sheet_name, startRow, startColumn,totalRows ,totalColumns , folder = folder)
        self.assertEqual(result.code,200)
        pass

    def test_cells_post_worksheet_unmerge(self):
        """
        Test case for cells_post_worksheet_unmerge

        Unmerge cells.
        """
        name ='Book1.xlsx'
        sheet_name ='Sheet1'
        startRow = 1 
        startColumn = 1
        totalRows =10
        totalColumns = 2
        folder = "PythonTest"
        result = AuthUtil.Ready(self.api, name, folder)
        self.assertTrue(len(result.uploaded)>0)        
        result = self.api.cells_post_worksheet_unmerge(name, sheet_name, startRow, startColumn,totalRows ,totalColumns , folder = folder)
        self.assertEqual(result.code,200)
        pass

    def test_cells_put_insert_worksheet_columns(self):
        """
        Test case for cells_put_insert_worksheet_columns

        Insert worksheet columns.
        """
        name ='Book1.xlsx'
        sheet_name ='Sheet1'
        columnIndex = 1 
        columns = 11
        updateReference = True
        folder = "PythonTest"
        result = AuthUtil.Ready(self.api, name, folder)
        self.assertTrue(len(result.uploaded)>0)        
        result = self.api.cells_put_insert_worksheet_columns(name, sheet_name, columnIndex, columns,update_reference = updateReference , folder = folder)
        self.assertEqual(result.code,200)
        pass

    def test_cells_put_insert_worksheet_row(self):
        """
        Test case for cells_put_insert_worksheet_row

        Insert new worksheet row.
        """
        name ='Book1.xlsx'
        sheet_name ='Sheet1'
        rowIndex = 1
        folder = "PythonTest"
        result = AuthUtil.Ready(self.api, name, folder)
        self.assertTrue(len(result.uploaded)>0)
        result = self.api.cells_put_insert_worksheet_row(name, sheet_name, rowIndex , folder = folder)
        self.assertEqual(result.code,200)
        pass

    def test_cells_put_insert_worksheet_rows(self):
        """
        Test case for cells_put_insert_worksheet_rows

        Insert several new worksheet rows.
        """
        name ='Book1.xlsx'
        sheet_name ='Sheet1'
        startrow = 1
        totalRows = 11
        updateReference = True
        folder = "PythonTest"
        result = AuthUtil.Ready(self.api, name, folder)
        self.assertTrue(len(result.uploaded)>0)
        
        result = self.api.cells_put_insert_worksheet_rows(name, sheet_name, startrow , total_rows = totalRows, update_reference = updateReference, folder = folder)
        self.assertEqual(result.code,200)
        pass


if __name__ == '__main__':
    unittest.main()
