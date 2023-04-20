CREATE TABLE
    IF NOT EXISTS IS601_Cart(
        id int AUTO_INCREMENT PRIMARY KEY,
        quantity int DEFAULT 0,
        cost int DEFAULT 99999,
        product_id int,
        user_id int,
        created TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        modified TIMESTAMP DEFAULT CURRENT_TIMESTAMP on update CURRENT_TIMESTAMP,
        check (quantity >= 0),
        -- don't allow negative stock; I don't allow backorders
        check (cost >= 0),
        -- don't allow negative costs
        FOREIGN KEY (user_id) REFERENCES IS601_Users(id),
        FOREIGN KEY(product_id) REFERENCES IS601_Products(id),
        UNIQUE KEY (product_id, user_id)
    )