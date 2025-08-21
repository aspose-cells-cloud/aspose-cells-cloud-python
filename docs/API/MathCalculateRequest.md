# **Spreadsheet Cloud API: mathCalculate**

The Math Calculate API enables you to perform a variety of mathematical operations on a selected range of cells. You can add or subtract a specific number from all selected cells, as well as multiply or divide individual cells and entire columns. This API simplifies complex calculations and enhances data manipulation capabilities. 


## **Quick Start**

- **Base URL**: `http://api.aspose.cloud/v4.0`
- **Authentication Method**: `JWT (OAuth2, application)`  **Token URL**: `https://api.aspose.cloud/connect/token`
- **Example** 

## **Interface Details**

### **Endpoint** 

```
PUT http://api.aspose.cloud/v4.0/cells/calculate/math
```
### **Function Description**
The API provides a flexible and efficient solution for performing arithmetic operations on a range of cells. Whether you need to add, subtract, multiply, or divide, this API allows you to apply the same operation uniformly across the selected range, enhancing your data manipulation capabilities.**Key Features**- **Add and Subtract**: Add or subtract a specific number from all selected cells.- **Multiply and Divide**: Multiply or divide individual cells and entire columns.- **Uniform Application**: Apply the same operation uniformly across the selected range.

### The request parameters of **mathCalculate** API are: 

| Parameter Name | Type | Path/Query String/HTTPBody | Description | 
| :- | :- | :- |:- | 
|Spreadsheet|File|FormData|Upload spreadsheet file.|
|operation|String|Query||
|value|String|Query||
|worksheet|String|Query||
|range|String|Query||
|regoin|String|Query|The spreadsheet region setting.|
|password|String|Query|The password for opening spreadsheet file.|

### **Response Description**
```json
{
File
}
```


## OpenAPI Specification

The [OpenAPI Specification](https://reference.aspose.cloud/cells/#/CalculateController/MathCalculate) defines a publicly accessible programming interface and lets you carry out REST interactions directly from a web browser.
