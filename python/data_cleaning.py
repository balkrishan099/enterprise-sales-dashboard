import pandas as pd

df = pd.read_csv('data/client_sales_data.csv')

df['order_dt'] = pd.to_datetime(df['order_dt'])

df['profit_margin_pct'] = (df['profit_amount'] / df['revenue']) * 100

print(df.head())
