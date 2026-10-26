USE northwind;

-- 1.List the ProductID, ProductName and UnitPrice.
SELECT ProductID, ProductName, UnitPrice
FROM products;

-- 2. Write a query to identify the products where the unit price is $7.50 or less.
SELECT ProductID, ProductName, UnitPrice
FROM products
WHERE UnitPrice  <= 7.50;

-- 3.What are the products that we carry where we have no units on hand, but 1 or more units are on backorder? 
SELECT ProductID, ProductName, UnitPrice,UnitsInStock, UnitsOnOrder
FROM products
WHERE UnitsInStock = 0 AND UnitsOnOrder >= 1;

-- 4. How does the products table identify the category? Where is the list of categories?
--    Products use CategoryID, which links to the categories table.
SELECT * FROM categories;
-- SeaFood Category is 8

SELECT ProductID, ProductName
FROM products
WHERE CategoryID=8;

-- 5. How do you know each product's supplier? Where is supplier info?
--    Products use SupplierID, which links to the suppliers table.
SELECT SupplierID, CompanyName
FROM suppliers
WHERE CompanyName = 'Tokyo Traders';
-- SupplierID is 4.

SELECT ProductID, ProductName
FROM products
WHERE SupplierID =4;

-- Question 6
SELECT COUNT(*) AS EmployeeCount
FROM employees;

-- Question 6.2
SELECT EmployeeID, FirstName, LastName, Title
FROM employees
WHERE Title  LIKE '%Manager%'



