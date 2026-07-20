# **Spreadsheet Cloud API: reportAIAnalysis**

Intelligently analyzes spreadsheet data, identifies business scenarios, and generates professional data analysis reports. 


## **Quick Start**

- **Base URL**: `http://api.aspose.cloud/v4.0`
- **Authentication Method**: `JWT (OAuth2, application)`  **Token URL**: `https://api.aspose.cloud/connect/token`
## **Interface Details**

### **Endpoint** 

```
PUT http://api.aspose.cloud/v4.0/cells/ai/report/analysis
```
### **Function Description**
This endpoint serves as an enterprise-grade engine for intelligent business scenario recognition and data analysis. It leverages AI to automatically infer and output professional analytical reports by processing underlying structured metadata from Excel files.Core Processing Logic:1. Precise Business Classification: Automatically categorizes the input spreadsheet data into one of 12 core enterprise management domains    (including HR Administration, Attendance, Financial Management, Inventory, Project Management, etc.).2. Multi-dimensional Data Insights: Extracts core business objectives, Key Performance Indicators (KPIs), and current business status summaries    based on headers, sample values, and chart/pivot-table logic.3. Data Architecture Evaluation: Assesses the rationality of data organization (e.g., pivot table associations) and provides professional    improvement suggestions for data visualization effects.Input Specification:SpreadsheetOutput Specification:Returns a structured report strictly formatted in Markdown, divided into three main modules: "Business Scenario Recognition", "Core Data Insights", and "Structural and Visual Assessment".

### The request parameters of **reportAIAnalysis** API are: 

| Parameter Name | Type | Path/Query String/HTTPBody | Description | 
| :- | :- | :- |:- | 
|Spreadsheet|File|FormData|Upload spreadsheet file.|
|region|String|Query|Spreadsheet region/language setting (e.g., `en-US`, `fr-FR`). Influences number formatting, date parsing, and locale‑specific behavior.|
|password|String|Query|The password for opening spreadsheet file.|

### **Response Description**
```json
{
Void
}
```


## OpenAPI Specification

The [OpenAPI Specification](https://reference.aspose.cloud/cells/#/AIController/ReportAIAnalysis) defines a publicly accessible programming interface and lets you carry out REST interactions directly from a web browser.

[[Back to API list]](../DeveloperGuide.md#api-reference)  
[[Back to README]](../../README.md)