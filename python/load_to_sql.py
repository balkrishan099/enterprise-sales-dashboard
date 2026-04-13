import pandas as pd
import sqlite3

# read csv
df = pd.read_csv('data/client_sales_data.csv')

# connect database
conn = sqlite3.connect('data/sales.db')

# store table
df.to_sql('sales_data', conn, if_exists='replace', index=False)

print("data loaded into SQL database")

conn.close()
