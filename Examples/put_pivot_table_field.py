        """
        Test case for cells_pivot_tables_put_pivot_table_field
        Add pivot field into into pivot table
        """
        name ='TestCase.xlsx'
        sheet_name ='Sheet4'
        pivotTableIndex = 0
        pivotFieldType = "row"
        request = PivotTableFieldRequest()
        request.data = [1]
        folder = "Temp"
        AuthUtil.Ready(name, folder)
        result = self.api.cells_pivot_tables_put_pivot_table_field(name, sheet_name, pivotTableIndex, pivotFieldType,request=request,need_re_calculate=True,folder=folder)