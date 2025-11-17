INSERT INTO ecommerce_customers (full_name, email, phone, city, created_at)
VALUES
('Priya S', 'priya@gmail.com', '9000011111', 'Chennai', '2024-03-02'),
('Kumar R', 'kumar@gmail.com', '9000022222', 'Coimbatore', '2024-04-01'),
('John Mathew', 'john@gmail.com', '9000033333', 'Bangalore', '2024-04-20'),
('Meenakshi L', 'meenakshi@gmail.com', '9000044444', 'Hyderabad', '2024-03-14');

INSERT INTO products (name, price, stock)
VALUES
('Laptop', 55000, 10),
('Smartphone', 25000, 20),
('Headphones', 1500, 50),
('Keyboard', 900, 40);

INSERT INTO orders (customer_id, product_id, quantity, order_date)
VALUES
(1, 1, 1, '2024-05-01'),
(2, 2, 2, '2024-06-10'),
(3, 3, 3, '2024-06-15'),
(4, 1, 1, '2024-06-20');
