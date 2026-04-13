import pandas as pd

df = pd.read_csv('data/cleaned_sales_data.csv')

# ensure date format
df['order_dt'] = pd.to_datetime(df['order_dt'])

# monthly revenue
monthly_sales = df.groupby(df['order_dt'].dt.to_period('M'))['revenue'].sum()

# revenue by category
category_sales = df.groupby('product_category')['revenue'].sum()

# profit by region
region_profit = df.groupby('region')['profit_amount'].sum()

print("\nMonthly revenue")
print(monthly_sales)

print("\nRevenue by category")
print(category_sales)

print("\nProfit by region")
print(region_profit)
