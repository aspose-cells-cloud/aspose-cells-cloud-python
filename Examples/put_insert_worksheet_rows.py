  """
        Test case for cells_put_insert_worksheet_rows
        Insert several new worksheet rows.
        """
        name ='Book1.xlsx'
        sheet_name ='Sheet1'
        startrow = 1
        totalRows = 11
        updateReference = True
        folder = "Temp"
        AuthUtil.Ready(name, folder)
        self.api.cells_put_insert_worksheet_rows(name, sheet_name, startrow , total_rows = totalRows, update_reference = updateReference, folder = folder)