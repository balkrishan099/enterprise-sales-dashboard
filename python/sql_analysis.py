import sqlite3
import pandas as pd

conn = sqlite3.connect('data/sales.db')

# SQL query
query = """
SELECT
product_category,
SUM(revenue) as revenue
FROM sales_data
GROUP BY product_category
"""

df = pd.read_sql(query, conn)

print(df)

conn.close()
