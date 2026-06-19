# **Spreadsheet Cloud API: summarizeSpreadsheet**

Summarizes spreadsheet content using AI and returns the summary as a downloadable text file. 


## **Quick Start**

- **Base URL**: `http://api.aspose.cloud/v4.0`
- **Authentication Method**: `JWT (OAuth2, application)`  **Token URL**: `https://api.aspose.cloud/connect/token`
## **Interface Details**

### **Endpoint** 

```
PUT http://api.aspose.cloud/v4.0/cells/ai/summarize/spreadsheet
```
### **Function Description**
This endpoint accepts an Excel spreadsheet file upload via multipart/form-data, extracts all text content from every worksheet,and uses AI to generate a comprehensive summary in English. The summary is returned as a downloadable TXT file.            The method processes the entire workbook, including all worksheets, to provide a complete analysis of the data.            ## **Supported Input Methods**            - **File Upload**: Send an Excel file (.xlsx, .xls, .xlsm, .xlsb, .csv, .ods) as multipart/form-data            ## **Processing Pipeline**            1. **Content Extraction**: Extracts content from every worksheet using intelligent sampling2. **Structured Context**: Builds structured markdown context with proper hierarchy3. **AI Analysis**: Sends the structured context to AI for comprehensive analysis4. **Summary Generation**: AI generates a summary covering key data points, trends, insights, and anomalies5. **File Output**: Returns the summary as a downloadable TXT file            ## **Intelligent Sampling**            - Small sheets (≤50 rows): Full content included- Large sheets (&gt;50 rows): Head + uniform sampling + tail- Summary tables prioritized over raw data            ## **Error Handling**            - **400 Bad Request**: Empty workbook or no text content to summarize- **401 Unauthorized**: Authentication failed for AI service- **500 Server Error**: AI service unavailable, workbook processing error, or internal processing failure            ## **Key Features and Benefits**            - **Smart Sampling**: Handles large datasets without exceeding AI token limits- **AI-Powered Summarization**: Uses advanced AI for intelligent data analysis- **Multi-Format Support**: Supports various Excel formats- **Automatic File Naming**: Generates output filename with "_summary" suffix- **English Output**: Summary is always generated in English

### The request parameters of **summarizeSpreadsheet** API are: 

| Parameter Name | Type | Path/Query String/HTTPBody | Description | 
| :- | :- | :- |:- | 
|Spreadsheet|File|FormData|Upload spreadsheet file.|
|region|String|Query|Spreadsheet region/language setting (e.g., `en-US`, `fr-FR`). Influences number formatting, date parsing, and locale‑specific behavior.|
|password|String|Query|The password for opening spreadsheet file.|

### **Response Description**
```json
{
File
}
```


## OpenAPI Specification

The [OpenAPI Specification](https://reference.aspose.cloud/cells/#/AIController/SummarizeSpreadsheet) defines a publicly accessible programming interface and lets you carry out REST interactions directly from a web browser.

[[Back to API list]](../DeveloperGuide.md#api-reference)  
[[Back to README]](../../README.md)