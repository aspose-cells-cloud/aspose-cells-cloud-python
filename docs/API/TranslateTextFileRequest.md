# **Spreadsheet Cloud API: translateTextFile**

Translates text file content to the specified target language. 


## **Quick Start**

- **Base URL**: `http://api.aspose.cloud/v4.0`
- **Authentication Method**: `JWT (OAuth2, application)`  **Token URL**: `https://api.aspose.cloud/connect/token`
## **Interface Details**

### **Endpoint** 

```
PUT http://api.aspose.cloud/v4.0/cells/ai/translate/text-file
```
### **Function Description**
This method supports two modes of operation:1. **File Upload Mode**: Accepts a text file upload via multipart/form-data and returns the translated text as a downloadable file2. **Direct Content Mode**: Accepts raw text content in the request body and returns the translated text directly            The method uses AI translation services to accurately translate the text content while preserving the original formatting and line structure.            ## **Supported Input Methods**            - **File Upload**: Send a text file as multipart/form-data with form field name "file"- **Direct Text**: Send raw text content directly in the request body            ## **Error Handling**            - **400 Bad Request**: Empty content or missing translation text- **401 Unauthorized**: Authentication failed for translation service- **500 Server Error**: Translation service unavailable or internal processing error            ## **Key Features and Benefits**            - **Flexible Input**: Accepts both file uploads and raw text content- **AI-Powered Translation**: Uses advanced AI for natural and accurate translations- **Format Preservation**: Maintains original text formatting, line breaks, and structure- **Automatic File Handling**: When uploading files, automatically generates translated filename with "_translated" suffix

### The request parameters of **translateTextFile** API are: 

| Parameter Name | Type | Path/Query String/HTTPBody | Description | 
| :- | :- | :- |:- | 
|Spreadsheet|File|FormData|Upload spreadsheet file.|
|targetLanguage|String|Query|The target language code for translation (e.g., "es", "fr", "de").|
|customEndpoint|String|Query||
|customApiKey|String|Query||
|customModel|String|Query||
|region|String|Query|Spreadsheet region/language setting (e.g., `en-US`, `fr-FR`). Influences number formatting, date parsing, and locale‑specific behavior.|
|password|String|Query|The password for opening spreadsheet file.|

### **Response Description**
```json
{
Void
}
```


## OpenAPI Specification

The [OpenAPI Specification](https://reference.aspose.cloud/cells/#/AIController/TranslateTextFile) defines a publicly accessible programming interface and lets you carry out REST interactions directly from a web browser.

[[Back to API list]](../DeveloperGuide.md#api-reference)  
[[Back to README]](../../README.md)