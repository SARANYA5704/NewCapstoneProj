-- All Orders with Customer and Product Details
SELECT
    ec.full_name,
    p.name AS product_name,
    o.quantity,
    o.order_date
FROM orders o
JOIN ecommerce_customers ec ON o.customer_id = ec.customer_id
JOIN products p ON o.product_id = p.product_id;


-- Orders with Products Costing More Than ₹20,000
SELECT
    ec.full_name,
    ec.city,
    p.name,
    p.price
FROM orders o
JOIN ecommerce_customers ec ON o.customer_id = ec.customer_id
JOIN products p ON o.product_id = p.product_id
WHERE p.price > 20000;

-- Customers Who Haven’t Ordered Anything
SELECT
    ec.full_name,
    ec.city
FROM ecommerce_customers ec
LEFT JOIN orders o ON ec.customer_id = o.customer_id
WHERE o.order_id IS NULL;

-- Total Spending by Each Customer
SELECT
    ec.full_name,
    SUM(p.price * o.quantity) AS total_spent
FROM orders o
JOIN ecommerce_customers ec ON o.customer_id = ec.customer_id
JOIN products p ON o.product_id = p.product_id
GROUP BY ec.full_name;


