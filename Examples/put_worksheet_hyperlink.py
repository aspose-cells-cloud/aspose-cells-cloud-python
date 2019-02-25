        """
        Test case for cells_hypelinks_put_worksheet_hyperlink
        Add worksheet hyperlink.
        """
        name ='Book1.xlsx'
        sheet_name ='Sheet1'
        firstRow = 1      
        firstColumn =1 
        totalRows = 2 
        totalColumns = 3 
        address = 'http://www.aspose.com'    
        folder = "Temp"
        AuthUtil.Ready(name, folder)
        result = self.api.cells_hypelinks_put_worksheet_hyperlink(name, sheet_name,firstRow,firstColumn,totalRows,totalColumns,address,folder=folder)