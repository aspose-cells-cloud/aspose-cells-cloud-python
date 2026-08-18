# **Spreadsheet Cloud API: categorizeSpreadsheet**

AI-powered data categorization: Automatically classifies spreadsheet column data into logical groups. 


## **Quick Start**

- **Base URL**: `http://api.aspose.cloud/v4.0`
- **Authentication Method**: `JWT (OAuth2, application)`  **Token URL**: `https://api.aspose.cloud/connect/token`
## **Interface Details**

### **Endpoint** 

```
PUT http://api.aspose.cloud/v4.0/cells/ai/categorize/spreadsheet
```
### **Function Description**
This endpoint analyzes the specified column data and uses AI to categorize each entry into logical groups.The results are added as a new column in the spreadsheet.            ## Use Cases            - Expense Categorization: Classify expenses as Food/Transportation/Office/HR etc.- Product Classification: Group products by type or category- Customer Segmentation: Segment customers by industry or behavior            ## Processing Pipeline            1. Data Extraction: Reads all values from the specified column2. AI Analysis: Sends data to AI for intelligent categorization3. Result Integration: Adds categorization results as a new column4. File Output: Returns the categorized spreadsheet            ## Error Handling            - 400 Bad Request: targetColumn parameter is missing- 500 Server Error: Worksheet not found, column not found, no data to process, or AI service failure

### The request parameters of **categorizeSpreadsheet** API are: 

| Parameter Name | Type | Path/Query String/HTTPBody | Description | 
| :- | :- | :- |:- | 
|Spreadsheet|File|FormData|Upload spreadsheet file.|
|targetColumn|String|Query|The column name to categorize (e.g., "Expense Item", "Product Name"). Required.|
|sheetName|String|Query|Optional: The worksheet name to process. If not specified, all worksheets will be processed.|
|newColumnName|String|Query|Optional: Name for the new categorization column (default: "AI Category").|
|region|String|Query|Spreadsheet region/language setting (e.g., `en-US`, `fr-FR`). Influences number formatting, date parsing, and locale‑specific behavior.|
|password|String|Query|The password for opening spreadsheet file.|

### **Response Description**
```json
{
File
}
```


## OpenAPI Specification

The [OpenAPI Specification](https://reference.aspose.cloud/cells/#/AIController/CategorizeSpreadsheet) defines a publicly accessible programming interface and lets you carry out REST interactions directly from a web browser.

[[Back to API list]](../DeveloperGuide.md#api-reference)  
[[Back to README]](../../README.md)