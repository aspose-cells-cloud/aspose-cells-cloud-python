        """
        Test case for cells_ole_objects_put_worksheet_ole_object
        Add OLE object
        """
        name ='Book1.xlsx'
        sheet_name ='Sheet6'
        ole = None
        upperLeftRow = 1         
        upperLeftColumn = 1  
        height = 100  
        width = 80  
        oleFile = 'OLEDoc.docx'  
        imageFile = 'word.jpg'  
        folder = "Temp"
        AuthUtil.Ready(name, folder)
        result = self.api.cells_ole_objects_put_worksheet_ole_object(name, sheet_name, ole_object=ole,upper_left_row=upperLeftRow,upper_left_column=upperLeftColumn,height=height,width=width,ole_file=oleFile, image_file=imageFile,folder=folder)