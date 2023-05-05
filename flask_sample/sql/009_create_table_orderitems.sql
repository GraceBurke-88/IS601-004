CREATE TABLE
    IS601_OrderItems (
        id INT AUTO_INCREMENT PRIMARY KEY,
        order_id INT NOT NULL,
        product_id INT NOT NULL,
        quantity INT NOT NULL,
        unit_price DECIMAL(10, 2) NOT NULL,
        FOREIGN KEY (order_id) REFERENCES IS601_Orders(id),
        FOREIGN KEY (product_id) REFERENCES IS601_Products(id)
    )
