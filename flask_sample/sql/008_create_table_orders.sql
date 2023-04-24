CREATE TABLE 
    IS601_Orders (
        id INT AUTO_INCREMENT PRIMARY KEY,
        user_id INT NOT NULL,
        created TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        total_price DECIMAL(10, 2) NOT NULL,
        address VARCHAR(255) NOT NULL,
        payment_method ENUM('Cash', 'Visa', 'MasterCard', 'Amex') NOT NULL,
        money_received DECIMAL(10, 2) NOT NULL,
        FOREIGN KEY (user_id) REFERENCES IS601_Users(id)
    )
