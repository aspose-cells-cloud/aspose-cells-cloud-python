"""
        Test case for cells_auto_filter_put_worksheet_color_filter
        
        """
        name ='Book1.xlsx'
        sheet_name ='Sheet1'
        range ='A1:C10'
        fieldIndex = 0  
        colorFilter = ColorFilterRequest()
        color = Color(0, 255, 0, 0)
        cellColor = CellsColor()
        cellColor.color = color
        colorFilter.foreground_color = cellColor
        colorFilter.pattern = 'Solid'
        matchBlanks = True
        refresh = True
        folder = "Temp"
        AuthUtil.Ready(name, folder)
        result = self.api.cells_auto_filter_put_worksheet_color_filter(name, sheet_name,range ,fieldIndex, color_filter = colorFilter , match_blanks = matchBlanks, refresh = refresh, folder = folder)