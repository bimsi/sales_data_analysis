# Sales Data Analysis Project  

## 1. Project Overview  
**Objective:**  
To analyze sales performance, identify trends, and evaluate product category performance using historical sales data.  

**Scope:**  
- Time period covered in the dataset  
- Key metrics such as total sales, average order value, and customer count  
- Monthly sales trends and product category performance  

**Outcome:**  
- Clear understanding of sales patterns  
- Identification of top-performing product categories  
- Data-driven insights for business decision-making  

## 2. Key Components  

### A. Data Collection  
**Sources:**  
- Sales data extracted from a CSV file (`sales_data_sample.csv`)  

**Metrics Tracked:**  
- Total sales  
- Average order value  
- Number of unique customers  
- Monthly sales trends  
- Sales by product category  

### B. Analysis Framework  
**Quantitative Analysis:**  
- Aggregation of sales by month and product category  
- Calculation of key performance indicators (KPIs)  

**Qualitative Analysis:**  
- Interpretation of trends in monthly sales  
- Comparison of product category performance  

**Tools Used:**  
- Python (Pandas for data manipulation, Matplotlib & Seaborn for visualization)  

### C. Key Findings  
- The dataset covers sales from [start date] to [end date].  
- Total sales amounted to [total sales value].  
- The average order value was [average order value].  
- [Number] unique customers were recorded in the dataset.  
- Monthly sales trends showed [increasing/declining/stable] performance.  
- The top-performing product category was [category name].  

### D. Recommendations  
- Focus on promoting high-performing product categories.  
- Investigate fluctuations in monthly sales to identify underlying causes.  
- Enhance customer engagement strategies to increase order value.  

## 3. Implementation  
- Data was loaded and cleaned, ensuring correct date formatting.  
- Key metrics were calculated and visualized using bar charts for trends and horizontal bar charts for category performance.  

## 4. Results & Impact  
- The analysis provided actionable insights into sales performance.  
- Visualizations helped quickly identify trends and top performers.  

## 5. Visual Aids  
- **Monthly Sales Trend:** Bar chart showing sales over time.
![Monthly Sales Trend](https://github.com/user-attachments/assets/c1097eeb-4f0b-4276-81f4-e242a5898b4a)

- **Sales by Product Category:** Horizontal bar chart ranking categories by total sales.
![Sales by Product Category](https://github.com/user-attachments/assets/125a98d7-7613-453a-acd3-a3373b7e342b)


## 6. Lessons Learned  
- Proper data encoding is crucial when handling datasets with special characters.  
- Visualizations significantly improve the interpretability of sales trends.  
- Regular analysis of sales data can help in proactive decision-making.


Here’s a structured breakdown of the provided Python code for sales data analysis:

### **1. Importing Libraries**
![Importing Libraries](https://github.com/user-attachments/assets/16cbcb30-4078-45c1-a6d5-c5bd84c4ecc1)

- **Purpose**:  
  - `pandas`: Data manipulation and analysis.  
  - `matplotlib.pyplot` and `seaborn`: Data visualization.  
  - `datetime`: Handling date-time conversions.  

### **2. Loading the Data**
![Loading the Data](https://github.com/user-attachments/assets/af5feb52-c48e-4a25-88ce-93376e74c9fe)

- **Key Actions**:  
  - Attempts to read a CSV file named `sales_data_sample.csv` with Korean encoding (`cp949`).  
  - Uses a `try-except` block to handle potential errors (e.g., file not found, encoding issues).  
  - Prints a success message if loaded correctly.  

### **3. Displaying Basic Data Info**
![Displaying Basic Data Info](https://github.com/user-attachments/assets/40c89887-f0f2-468e-9ace-f5ae8fbd08a9)

- **Outputs**:  
  - **Data Overview**: Shows a snapshot of the first 3 rows.  
  - **Data Structure**: Summary of columns, data types, and missing values.  

### **4. Data Cleaning & Transformation**
![Data Cleaning   Transformation](https://github.com/user-attachments/assets/a9f82924-fa51-4995-a5ed-75fce465653d)

- **Purpose**:  
  - Converts `ORDERDATE` to a datetime format for time-based analysis.  
  - Creates a new column `YEAR_MONTH` to aggregate sales by month.  

### **5. Generating Key Metrics**
![Generating Key Metrics](https://github.com/user-attachments/assets/8b51ee7f-8393-45b1-bf87-540ce88561c2)

- **Metrics Calculated**:  
  - **Time Period**: Date range of the dataset.  
  - **Total Sales**: Sum of all sales.  
  - **Avg. Order Value**: Mean sales per order.  
  - **Unique Customers**: Count of distinct customer names.  

### **6. Data Visualizations**
#### **A. Monthly Sales Trend**
![Monthly Sales Trend](https://github.com/user-attachments/assets/f2120631-8f26-4c4e-96b5-2ad8669c3af3)

- **Steps**:  
  1. Groups data by `YEAR_MONTH` and sums `SALES`.  
  2. Plots a bar chart with formatted labels/titles.  

#### **B. Product Category Performance**
![Product Category Performance](https://github.com/user-attachments/assets/b8864d27-edcb-4d85-962a-b4e091229146)

- **Steps**:  
  1. Groups sales by `PRODUCTLINE`, sorts values in ascending order.  
  2. Plots a horizontal bar chart for easy comparison.  

### **7. Error Handling**
![Error Handling](https://github.com/user-attachments/assets/b18a790b-8bea-46c3-b93c-7d7e362ecb59)

- **Purpose**:  
  - Catches and displays errors (e.g., file not found, encoding issues).  
  - Provides troubleshooting steps for common problems.  


### **Key Takeaways**
1. **Data Loading**: Explicit encoding handling for non-ASCII characters (e.g., Korean).  
2. **Transformations**: Date parsing and period extraction for time-based analysis.  
3. **Metrics**: Focus on sales performance and customer engagement.  
4. **Visualizations**: Bar charts for trends, horizontal bars for categorical comparisons.  
5. **Robustness**: Error handling to guide debugging. 
