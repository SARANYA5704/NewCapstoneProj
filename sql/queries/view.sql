-- View for all customer orders
CREATE VIEW customer_orders AS
SELECT
    ec.full_name,
    p.name AS product_name,
    o.quantity,
    o.order_date
FROM orders o
JOIN ecommerce_customers ec ON o.customer_id = ec.customer_id
JOIN products p ON o.product_id = p.product_id;

-- View for most ordered products
CREATE VIEW top_selling_products AS
SELECT
    p.name,
    SUM(o.quantity) AS total_sold
FROM orders o
JOIN products p ON o.product_id = p.product_id
GROUP BY p.name
ORDER BY total_sold DESC;
