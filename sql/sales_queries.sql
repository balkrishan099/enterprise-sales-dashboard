SELECT 
DATE_TRUNC('month', order_dt) as month,
SUM(revenue) as total_revenue
FROM sales_data
GROUP BY 1;
