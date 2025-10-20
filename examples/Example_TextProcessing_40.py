import os

from asposecellscloud.apis.cells_api import CellsApi
from asposecellscloud.models import *
from asposecellscloud.requests import *

# If no environment variables are configured, please obtain the ClientId and ClientSecret from https://dashboard.aspose.cloud/#/applications and replace the following values:
# instance  = CellsApi('YourClientId','YourClientSecret')
instance  = CellsApi(os.getenv('CellsCloudClientId'),os.getenv('CellsCloudClientSecret'))

# The default value of the trim character is a blank space. Specify a specific location.   Remove excess spaces between words.
instance.trim_character(TrimCharacterRequest("BookText.xlsx", worksheet = "HumanResources", range ="A1:C12" , trim_space_between_word_to1 = True) ,local_outpath = "out1.xlsx")
# The default value of the trim character is a blank space. Specify a specific location.   Remove excess spaces between words. Only remove leading spaces.
instance.trim_character(TrimCharacterRequest("BookText.xlsx", worksheet = "Text", range ="J6:J6" ,trim_trailing = False, trim_space_between_word_to1 = True) ,local_outpath = "out2.xlsx")
# The default value of the trim character is a blank space. Specify a specific location.   Remove excess spaces between words. Only remove leading spaces. Remove all line breaks.
instance.trim_character(TrimCharacterRequest("BookText.xlsx", worksheet = "Text", range ="J7:J7" ,trim_trailing = False, trim_space_between_word_to1 = True,remove_all_line_breaks =True) ,local_outpath = "out3.xlsx")
# Uppercase every string in the selected range.
instance.update_word_case(UpdateWordCaseRequest("BookText.xlsx", "UpperCase", worksheet = "Text", range ="J7:J7" ) , local_outpath = "out4.xlsx")
# Lowercase every string in the selected range.
instance.update_word_case(UpdateWordCaseRequest("out4.xlsx", "LowerCase", worksheet = "Text", range ="J7:J7" ) , local_outpath = "out5.xlsx")
# ProperCase every string in the selected range.
instance.update_word_case(UpdateWordCaseRequest("out5.xlsx", "ProperCase", worksheet = "Text", range ="J7:J7" ) , local_outpath = "out6.xlsx")
# SentenceCase every string in the selected range.
instance.update_word_case(UpdateWordCaseRequest("out5.xlsx", "SentenceCase", worksheet = "Text", range ="J7:J7" ) , local_outpath = "out7.xlsx")

# Prefix every string in the selected range with "Aspose.Cells".
instance.add_text( AddTextRequest("BookText.xlsx", "Aspose.Cells", "AtTheBeginning", "") , local_outpath = "out8.xlsx"  )
# Insert an exclamation mark immediately after the specified substring within every string in the selected range.
instance.add_text( AddTextRequest("BookText.xlsx", "!", "AfterText", "hellow  word") , local_outpath = "out9.xlsx"  )
# Append an exclamation mark to every string in the selected range.
instance.add_text( AddTextRequest("BookText.xlsx", "!", "AtTheEnd", "", worksheet = "Text", range ="A1:J7" ,skip_empty_cells=False ) , local_outpath = "out10.xlsx"  )

# convert_text_type: ConvertNumberToText,ConvertCharacters,ConvertLinebreak,ConvertWriteSpace,ConvertAccentedChars
# Convert all numbers in the selected range to text.  If worksheet and range are empty, the entire workbook is processed.
instance.convert_text(ConvertTextRequest("BookText.xlsx", "ConvertNumberToText", "", ""), local_outpath = "out11.xlsx")
# Replace every '1' in the selected range with 'Aspose.Cells'. If worksheet and range are empty, the entire workbook is processed.
instance.convert_text(ConvertTextRequest("out11.xlsx", "ConvertCharacters", "1", "Aspose.Cells" , worksheet="Text", range="C9:F13"), local_outpath = "out12.xlsx")
# Replace all line breaks in the selected range with the specified character.
instance.convert_text(ConvertTextRequest("out12.xlsx", "ConvertLinebreak", "", "Linebreak"), local_outpath = "out13.xlsx")
# Replace all blank space in the selected range with the specified character.
instance.convert_text(ConvertTextRequest("out13.xlsx", "ConvertWriteSpace", "", "WriteSpace"), local_outpath = "out14.xlsx")

# ExtractTextType: ExtractFirstCharacter, ExtractFirstWord, ExtractLastCharacter, ExtractLastWord, ExtractTextBefore, ExtractTextAfter, ExtractBetweenSpecifiedCharacters, ExtractAllNumbers, GetTextFromAnyPosition
# 
# instance.extract_text(ExtractTextRequest("BookText.xlsx", "ExtractTextBefore", ";","","","","I2:I11" ,worksheet= "HumanResources",range="G2:G11" ) , local_outpath = "out15.xlsx")
