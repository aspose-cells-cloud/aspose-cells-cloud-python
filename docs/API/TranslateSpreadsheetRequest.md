# **Spreadsheet Cloud API: translateSpreadsheet**

Translates the entire spreadsheet to the specified target language. 


## **Quick Start**

- **Base URL**: `http://api.aspose.cloud/v4.0`
- **Authentication Method**: `JWT (OAuth2, application)`  **Token URL**: `https://api.aspose.cloud/connect/token`
## **Interface Details**

### **Endpoint** 

```
PUT http://api.aspose.cloud/v4.0/cells/ai/translate/spreadsheet
```
### **Function Description**
This method reads all text content from the spreadsheet workbook, translates it to the target language using AI translation services, and returns the translated spreadsheet file. The translation process preserves the original spreadsheet structure and formatting.            ## **Custom AI Configuration (Optional)**            You can provide your own AI endpoint by passing the following query parameters:            - `customEndpoint`: Full Chat Completions URL (e.g., https://api.deepseek.com/v1/chat/completions)- `customApiKey`: Your API key- `customModel`: Model name (e.g., deepseek-chat)            If these parameters are omitted, the default Aspose AI service will be used.            ## **Error Handling**            - **400 Bad Request**: Invalid target language parameter or invalid custom AI configuration.- **401 Unauthorized**: Authentication failed for translation service.- **500 Server Error**: Translation service unavailable or spreadsheet processing error.            ## **Key Features and Benefits**            - **AI-Powered Translation**: Uses advanced AI for accurate translations.- **Structure Preservation**: Maintains original spreadsheet layout and formulas.- **Multi-Sheet Support**: Translates content across all worksheets automatically.- **Bring Your Own AI**: Support custom OpenAI-compatible endpoints.

### The request parameters of **translateSpreadsheet** API are: 

| Parameter Name | Type | Path/Query String/HTTPBody | Description | 
| :- | :- | :- |:- | 
|Spreadsheet|File|FormData|Upload spreadsheet file.|
|targetLanguage|String|Query|The target language code for translation (e.g., "es", "fr", "de").|
|customEndpoint|String|Query|Optional. Full Chat Completions endpoint URL.|
|customApiKey|String|Query|Optional. API key for the custom AI service.|
|customModel|String|Query|Optional. Model name to use.|
|region|String|Query|Spreadsheet region/language setting (e.g., `en-US`, `fr-FR`). Influences number formatting, date parsing, and locale‑specific behavior.|
|password|String|Query|The password for opening spreadsheet file.|

### **Response Description**
```json
{
File
}
```


## OpenAPI Specification

The [OpenAPI Specification](https://reference.aspose.cloud/cells/#/AIController/TranslateSpreadsheet) defines a publicly accessible programming interface and lets you carry out REST interactions directly from a web browser.

[[Back to API list]](../DeveloperGuide.md#api-reference)  
[[Back to README]](../../README.md)