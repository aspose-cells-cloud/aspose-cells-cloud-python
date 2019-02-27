        """
        Test case for cells_charts_put_worksheet_chart_title
        Add chart title / Set chart title visible
        """
        name ='myDocument.xlsx'
        sheet_name ='Sheet3'
        chartIndex = 0  
        title = Title()
        title.text = "test"
        folder = "Temp"
        AuthUtil.Ready(name, folder)
        result = self.api.cells_charts_put_worksheet_chart_title(name, sheet_name, chartIndex ,title=title, folder=folder)