import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

# 1. Load the data with proper encoding
try:
    df = pd.read_csv('sales_data_sample.csv', encoding='cp949')  # Using Korean encoding
    print("✅ Data loaded successfully!\n")
    
# 2. Display basic info
    print("📊 Data Overview:")
    print(df.head(3))
    
    print("\n📝 Data Structure:")
    print(df.info())
    
# 3. Clean and transform data
    df['ORDERDATE'] = pd.to_datetime(df['ORDERDATE'])
    df['YEAR_MONTH'] = df['ORDERDATE'].dt.to_period('M')
    
# 4. Generate key metrics
    print("\n🔑 Key Metrics:")
    metrics = {
        'Time Period': f"{df['ORDERDATE'].min().date()} to {df['ORDERDATE'].max().date()}",
        'Total Sales': f"${df['SALES'].sum():,.2f}",
        'Avg. Order Value': f"${df['SALES'].mean():,.2f}",
        'Unique Customers': df['CUSTOMERNAME'].nunique()
    }
    print(pd.DataFrame.from_dict(metrics, orient='index', columns=['Value']))
    
# 5. Create visualizations
    print("\n📈 Sales Performance:")
    plt.figure(figsize=(12, 6))
    monthly_sales = df.groupby('YEAR_MONTH')['SALES'].sum()
    monthly_sales.plot(kind='bar', color='skyblue')
    plt.title('Monthly Sales Trend', fontsize=14)
    plt.ylabel('Sales (USD)')
    plt.xlabel('Month')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
    
    print("\n🏷️ Product Category Performance:")
    plt.figure(figsize=(10, 6))
    category_sales = df.groupby('PRODUCTLINE')['SALES'].sum().sort_values()
    category_sales.plot(kind='barh', color='lightgreen')
    plt.title('Sales by Product Category', fontsize=14)
    plt.xlabel('Total Sales (USD)')
    plt.tight_layout()
    plt.show()
    
except Exception as e:
    print(f"❌ Error: {str(e)}")
    print("\nTroubleshooting Tips:")
    print("1. Verify file path and encoding")
    print("2. Check for file corruption")
    print("3. Try opening in Excel and re-saving as UTF-8 CSV")