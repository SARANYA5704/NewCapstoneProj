SELECT
    ec.full_name,
    p.name AS product_name,
    o.quantity,
    o.order_date
FROM orders o
JOIN ecommerce_customers ec ON o.customer_id = ec.customer_id
JOIN products p ON o.product_id = p.product_id;

SELECT
    ec.full_name,
    ec.city,
    p.name,
    p.price
FROM orders o
JOIN ecommerce_customers ec ON o.customer_id = ec.customer_id
JOIN products p ON o.product_id = p.product_id
WHERE p.price > 20000;

