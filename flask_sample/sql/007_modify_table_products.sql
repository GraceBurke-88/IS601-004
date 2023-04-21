
-- 1. Add missing columns (created, modified, unit_price, visibility)
ALTER TABLE IS601_Products
ADD COLUMN visibility BOOLEAN DEFAULT TRUE;

-- 3. Remove the 'color' column ALTER TABLE IS601_Products DROP COLUMN color;


-- 4. Modify the 'category' column data type to match the desired specifications
ALTER TABLE IS601_Products MODIFY category VARCHAR(30);