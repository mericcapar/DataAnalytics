USE northwind;
SELECT database();

-- 1. Write a query to find the price of the cheapest item that Northwind sells. Then write a
-- second query to find the name of the product that has that price.

SELECT MIN(UnitPrice) AS CheapestPrice
FROM products;

SELECT ProductName 
FROM products
WHERE UnitPrice = 2.50;

-- 2. Write a query to find the average price of all items that Northwind sells.
-- (Bonus: Once you have written a working query, try asking Claude or ChatGPT for help
-- using the ROUND function to round the average price to the nearest cent.

SELECT ROUND(AVG(UnitPrice), 2) AS AveragePrice
FROM products;

-- 3.Write a query to find the price of the most expensive item that Northwind sells. Then
-- write a second query to find the name of the product with that price, plus the name of
-- the supplier for that product.

SELECT MAX(UnitPrice) AS HighestPrice
from products;

SELECT p.ProductName, p.UnitPrice, s.CompanyName AS SupplierName
FROM products p
JOIN suppliers s ON p.SupplierID = s.SupplierID
WHERE p.UnitPrice = 263.50;

-- 4.Write a query to find total monthly payroll (the sum of all the employees’ monthly
-- salaries)

SELECT SUM(Salary) AS TotalMonthlyPayroll
FROM employees;

-- 5. Write a query to identify the highest salary and the lowest salary amounts which any
-- employee makes. (Just the amounts, not the specific employees!)

SELECT MAX(Salary) AS HighestSalary, MIN(SALARY) AS LowestSalary
FROM employees;

-- 6. Write a query to find the name and supplier ID of each supplier and the number of
-- items they supply. Hint: Join is your friend here.

SELECT s.SupplierID, s.CompanyName, COUNT(p.ProductID) AS ItemCount
FROM suppliers s
JOIN products p ON s.SupplierID = p.SupplierID
GROUP BY s.SupplierID, s.CompanyName;