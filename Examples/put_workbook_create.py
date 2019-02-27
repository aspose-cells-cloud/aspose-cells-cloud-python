      """
        Test case for cells_workbook_put_workbook_create
        Create new workbook using deferent methods.
        """
        templateFile ='Book1.xlsx'       
        folder = "Temp"
        name = "NewBook" + datetime.now().strftime("%Y%m%d%H%M%S") + ".xlsx"    
        dataFile = "ReportData.xml"  
        AuthUtil.Ready(templateFile, folder)
        AuthUtil.Ready(dataFile, folder)
        template_file = folder + "/" + templateFile
        data_file = folder + "/" + dataFile
        result = self.api.cells_workbook_put_workbook_create(name, template_file=template_file, data_file=data_file,  folder=folder)