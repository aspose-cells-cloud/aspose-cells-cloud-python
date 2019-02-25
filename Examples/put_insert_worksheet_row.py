"""
        Test case for cells_put_insert_worksheet_row
        Insert new worksheet row.
        """
        name ='Book1.xlsx'
        sheet_name ='Sheet1'
        rowIndex = 1
        folder = "Temp"
        AuthUtil.Ready(name, folder)
        self.api.cells_put_insert_worksheet_row(name, sheet_name, rowIndex , folder = folder)