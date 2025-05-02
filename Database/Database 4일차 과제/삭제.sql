-- USE classicmodels;
-- 3. 삭제(DELETE)
DELETE FROM customers WHERE customerNumber = 10000;
DELETE FROM products WHERE productCode = '9002';
DELETE FROM employees WHERE employeeNumber = 2025;
DELETE FROM offices WHERE officeCode = '9';
DELETE FROM orders WHERE orderNumber = 11102;
DELETE FROM orderdetails WHERE orderNumber = '10205';
DELETE FROM payments WHERE customerNumber = 496 AND checkNumber = 'MN89921';
DELETE FROM productlines WHERE productLine = 'Classic';
DELETE FROM customers WHERE customerNumber = NULL AND city = '저 도시 어딘가';
DELETE FROM products WHERE productCode = 'Classic Cars';