-- overall sales performance
SELECT
SUM(revenue) as total_revenue,
SUM(profit_amount) as total_profit,
AVG(profit_amount/revenue)*100 as profit_margin_pct
FROM sales_data;

-- monthly revenue trend
SELECT
DATE_TRUNC('month', order_dt) as month,
SUM(revenue) as monthly_revenue
FROM sales_data
GROUP BY 1
ORDER BY 1;
