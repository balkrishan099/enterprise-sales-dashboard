-- revenue by category
SELECT
product_category,
SUM(revenue) as revenue
FROM sales_data
GROUP BY product_category
ORDER BY revenue DESC;

-- profit by region
SELECT
region,
SUM(profit_amount) as profit
FROM sales_data
GROUP BY region
ORDER BY profit DESC;

-- top customers
SELECT
cust_id,
SUM(revenue) as revenue
FROM sales_data
GROUP BY cust_id
ORDER BY revenue DESC
LIMIT 10;
