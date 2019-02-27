        """
        Test case for cells_page_breaks_put_vertical_page_break
        
        """
        name ='Book1.xlsx'
        sheet_name ='Sheet1'
        cellname = 'A1'     
        row = 1  
        column = 1  
        startRow = 1  
        endRow = 1      
        folder = "Temp"
        AuthUtil.Ready(name, folder)
        result = self.api.cells_page_breaks_put_vertical_page_break(name, sheet_name, cellname=cellname,column=column, row=row ,start_row=startRow,end_row=endRow,folder=folder)
        pass