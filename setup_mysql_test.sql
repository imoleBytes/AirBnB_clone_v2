-- Do same for test database and test user

--Create the database
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- Creates a  test user
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

-- Grants all privileges to test user on the db
GRANT ALL PRIVILEGE ON hbnb_test_db.* TO 'hbnb_test'@'localhost';

-- Grants select privilege on performance_schema to test user
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
