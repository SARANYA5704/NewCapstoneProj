-- Get all e-commerce customers
SELECT * FROM ecommerce_customers;

-- Get all products
SELECT * FROM products;

-- Get all orders
SELECT * FROM orders;

-- Search customer by email
SELECT * FROM ecommerce_customers
WHERE email = 'priya@gmail.com';

-- Reduce stock of a product after sale
UPDATE products
SET stock = stock - 2
WHERE product_id = 1;

-- Delete a specific order
DELETE FROM orders
WHERE order_id = 4;
