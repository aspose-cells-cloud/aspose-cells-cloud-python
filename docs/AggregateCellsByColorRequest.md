# **Spreadsheet Cloud API: aggregateCellsByColor**

The Aggregate by Color API provides a convenient way to perform calculations on cells that share the same fill or font color. This API supports a range of aggregate operations, including count, sum, maximum value, minimum value, and average value, enabling you to analyze and summarize data based on color distinctions. 


## **Quick Start**

- **Base URL**: `http://api.aspose.cloud/v4.0`
- **Authentication Method**: `JWT (OAuth2, application)`  **Token URL**: `https://api.aspose.cloud/connect/token`
- **Example** 

## **Interface Details**

### **Endpoint** 

```
PUT http://api.aspose.cloud/v4.0/cells/calculate/aggergate/color
```
### **Function Description**
The Aggregate by Color API is a powerful tool for data analysis, allowing you to perform color-based aggregations efficiently. Whether you need to count, sum, find the max or min value, or calculate the average, this API provides the flexibility to handle various aggregate operations based on cell colors.- Color-Based Aggregation: Perform calculations on cells grouped by their fill or font color.- Aggregate Operations:- Count: Determine the number of cells with the same color.- Sum: Calculate the total value of cells with the same color.- Max Value: Identify the highest value among cells with the same color.- Min Value: Find the lowest value among cells with the same color.- Average Value: Compute the mean value of cells with the same color.**Example Use Case**Suppose you have a spreadsheet where different categories of data are highlighted with different colors. You can use the Aggregate by Color API to quickly summarize the data for each color category. For instance, you can calculate the total sales for cells highlighted in green or the average cost for cells highlighted in red.

### The request parameters of **aggregateCellsByColor** API are: 

| Parameter Name | Type | Path/Query String/HTTPBody | Description | 
| :- | :- | :- |:- | 
|Spreadsheet|File|FormData|Upload spreadsheet file.|
|worksheet|String|Query||
|range|String|Query||
|operation|String|Query||
|colorPosition|String|Query||
|regoin|String|Query|The spreadsheet region setting.|
|password|String|Query|The password for opening spreadsheet file.|

### **Response Description**
```json
{
  "Name": "AggregateResultByColorResponse",
  "Type": "Class",
  "ParentName": "CellsCloudResponse",
  "IsAbstract": false,
  "Properties": [
    {
      "Name": "AggregateResults",
      "Nullable": true,
      "ReadOnly": false,
      "IsInherit": false,
      "DataType": {
        "Identifier": "Container",
        "Reference": "AggregateResultByColor",
        "ElementDataType": {
          "Identifier": "Class",
          "Reference": "AggregateResultByColor",
          "Name": "class:aggregateresultbycolor"
        },
        "Name": "container"
      }
    },
    {
      "Name": "Code",
      "Nullable": true,
      "ReadOnly": false,
      "IsInherit": true,
      "DataType": {
        "Identifier": "Integer",
        "Name": "integer"
      }
    },
    {
      "Name": "Status",
      "Nullable": true,
      "ReadOnly": false,
      "IsInherit": true,
      "DataType": {
        "Identifier": "String",
        "Name": "string"
      }
    }
  ]
}
```


## OpenAPI Specification

The [OpenAPI Specification](https://reference.aspose.cloud/cells/#/CalculateController/AggregateCellsByColor) defines a publicly accessible programming interface and lets you carry out REST interactions directly from a web browser.
