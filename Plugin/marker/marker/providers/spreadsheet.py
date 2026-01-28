import os
import tempfile
import logging
import uuid
from pathlib import Path

from marker.providers.pdf import PdfProvider

from asposecellscloud import  GetWorksheetsRequest, UploadFileRequest, ConvertWorksheetToHtmlTableRequest

css = '''
@page {
    size: A4 landscape;
    margin: 1.5cm;
}

table {
    width: 100%;
    border-collapse: collapse;
    break-inside: auto;
    font-size: 10pt;
}

tr {
    break-inside: avoid;
    page-break-inside: avoid;
}

td {
    border: 0.75pt solid #000;
    padding: 6pt;
}
'''


class SpreadSheetProvider(PdfProvider):
    def __init__(self, filepath: str, config=None):
        temp_pdf = tempfile.NamedTemporaryFile(delete=False, suffix=f".pdf")
        self.temp_pdf_path = temp_pdf.name
        temp_pdf.close()

        # Convert XLSX to PDF
        try:
            self.convert_xlsx_to_pdf(filepath)
        except Exception as e:
            raise RuntimeError(f"Failed to convert {filepath} to PDF: {e}")

        # Initialize the PDF provider with the temp pdf path
        super().__init__(self.temp_pdf_path, config)

    def __del__(self):
        if os.path.exists(self.temp_pdf_path):
            os.remove(self.temp_pdf_path)

    def convert_xlsx_to_pdf(self, filepath: str):
        from weasyprint import CSS, HTML
        from asposecellscloud.apis.cells_api import CellsApi
        instance = CellsApi(os.getenv('CellsCloudClientId'), os.getenv('CellsCloudClientSecret'))
        # request = ConvertSpreadsheetRequest(filepath, 'pdf')
        # result = instance.convert_spreadsheet(request)
        filename = str(uuid.uuid4()) + Path(filepath).suffix
        instance.upload_file(UploadFileRequest(filepath, filename))
        worksheets =  instance.get_worksheets( GetWorksheetsRequest(filename) ).worksheets.worksheet_list
        html = ""
        for worksheet in worksheets:
            sheetname = worksheet.link.href[1:]
            response = instance.convert_table_to_html( ConvertWorksheetToHtmlTableRequest( filepath, sheetname)  )
            with open(response, "r", encoding="utf-8") as f:
                content = f.read()
                html += f'<div><h1>{sheetname}</h1>' + content + '</div>'

        # We convert the HTML into a PDF
        HTML(string=html).write_pdf(
            self.temp_pdf_path,
            stylesheets=[CSS(string=css), self.get_font_css()]
        )


 