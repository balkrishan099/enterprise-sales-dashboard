import pandas as pd

# load dataset
df = pd.read_csv('data/client_sales_data.csv')

# convert date column
df['order_dt'] = pd.to_datetime(df['order_dt'])

# remove duplicate rows
df = df.drop_duplicates()

# create new metric
df['profit_margin_pct'] = (df['profit_amount'] / df['revenue']) * 100

# save cleaned data
df.to_csv('data/cleaned_sales_data.csv', index=False)

print("data cleaned successfully")
print(df.head())
