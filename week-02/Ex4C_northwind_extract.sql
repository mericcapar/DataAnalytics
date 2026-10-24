/*
a) The table that holds the items Northwind sells is products.
b) The table that holds the categories of the items is categories.
*/

USE northwind;

SELECT * FROM employees;
-- The employee whose name makes her look like a bird is Margaret Peacock.

SELECT * FROM products;
-- The query returns 77 records. To return only 10 rows, use the "Limit to" dropdown in the query toolbar and select "Limit to 10 rows".
-- BONUS: Add LIMIT 10 at the end of the query: SELECT * FROM products LIMIT 10;
-- Source: MySQL documentation (dev.mysql.com), SELECT statement, LIMIT clause.

SELECT * FROM categories;
-- The category id of Seafood is 8.

SELECT OrderID, OrderDate, ShipName, ShipCountry
FROM orders
LIMIT 50;