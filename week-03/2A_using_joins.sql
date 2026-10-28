USE northwind;

-- 1. List the product id, product name, unit price and category name of all products.
--    Order by category name and within that, by product name
SELECT p.ProductID, p.ProductName, p.UnitPrice, c.CategoryName
FROM products p
JOIN categories c on p.CategoryID = c.CategoryID
ORDER BY c.CategoryName, p.ProductName;

-- 2. List the product id, product name, unit price and supplier name of all products
--    that cost more than $75. Order by product name.
SELECT p.ProductID, p.ProductName, p.UnitPrice, s.CompanyName as SupplierName
FROM products p
JOIN suppliers s ON p.SupplierID = s.SupplierID
WHERE p.UnitPrice > 75
ORDER BY p.ProductName;