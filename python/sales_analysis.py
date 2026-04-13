import pandas as pd

df = pd.read_csv('data/cleaned_sales_data.csv')

# monthly revenue
monthly_sales = df.groupby(df['order_dt'].dt.to_period('M'))['revenue'].sum()

# revenue by category
category_sales = df.groupby('product_category')['revenue'].sum()

# profit by region
region_profit = df.groupby('region')['profit_amount'].sum()

print("Monthly revenue")
print(monthly_sales.head())

print("Category sales")
print(category_sales.head())

print("Region profit")
print(region_profit.head())
