-- USE classicmodels;
-- 2. 읽기(READ)
SELECT * FROM customers;
SELECT * FROM products;
SELECT lastName, firstName, jobTitle FROM employees;
SELECT city, addressLine1, addressLine2, state, country FROM offices;
SELECT * FROM orders ORDER BY orderDate DESC LIMIT 10;
SELECT * FROM orderdetails WHERE orderNumber = 10418;
SELECT * FROM payments WHERE customerNumber = 128;
SELECT productLine, textDescription FROM productlines;
SELECT * FROM customers WHERE city = '이 도시 어딘가';
SELECT * FROM products WHERE buyprice BETWEEN 99 AND 100;
