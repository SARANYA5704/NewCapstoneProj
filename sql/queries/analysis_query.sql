-- Total orders placed by each customer
SELECT
    ec.full_name,
    COUNT(o.order_id) AS total_orders
FROM ecommerce_customers ec
LEFT JOIN orders o ON ec.customer_id = o.customer_id
GROUP BY ec.full_name;

-- Total revenue generated per product
SELECT
    p.name,
    SUM(o.quantity * p.price) AS total_revenue
FROM orders o
JOIN products p ON o.product_id = p.product_id
GROUP BY p.name;

-- Aggregate Queries
-- Total number of customers
SELECT COUNT(*) AS total_customers
FROM ecommerce_customers;

-- Total number of products
SELECT COUNT(*) AS total_products
FROM products;

-- Total orders placed
SELECT COUNT(*) AS total_orders
FROM orders;

-- Total quantity of products sold
SELECT SUM(quantity) AS total_quantity_sold
FROM orders;

-- Total revenue generated per product
SELECT p.name AS product_name, SUM(o.quantity * p.price) AS total_revenue
FROM orders o
JOIN products p ON o.product_id = p.product_id
GROUP BY p.name;

-- Average price of products
SELECT AVG(price) AS avg_product_price
FROM products;

-- Maximum and minimum order quantity
SELECT MAX(quantity) AS max_order_quantity,
       MIN(quantity) AS min_order_quantity
FROM orders;
