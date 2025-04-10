CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  full_name TEXT NOT NULL,
  email VARCHAR(100) UNIQUE NOT NULL,
  birth_date DATE NOT NULL,
  is_active BOOLEAN DEFAULT TRUE
);

-- Verify the table structure
SELECT * FROM users;


-- all one them

-- Creating a table
CREATE TABLE products (
    product_id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Verify the table
SELECT * FROM products;

-- Dropping a table
DROP TABLE IF EXISTS products;

-- Verify by trying to select from the table (should give an error)
SELECT * FROM products;

-- Altering a table - Adding a column
ALTER TABLE users ADD COLUMN phone_number VARCHAR(20);

-- Verify the structure
SELECT phone_number FROM users;

-- Altering a table - Removing a column
ALTER TABLE users DROP COLUMN phone_number;

-- Verify by trying to select the column (should give an error)
SELECT phone_number FROM users;

-- Altering a table - Renaming a column
ALTER TABLE users RENAME COLUMN full_name TO name;

-- Verify the column name change
SELECT name FROM users;

-- Altering a table - Changing a column data type
ALTER TABLE products ALTER COLUMN price TYPE INTEGER;

-- Verify the change
SELECT price FROM products;

