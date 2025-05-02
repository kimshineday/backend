-- USE classicmodels;
-- 3. 갱신(UPDATE)
UPDATE customers SET addressline2 = '여기는 어딘가' WHERE customerNumber = '1002';
UPDATE products SET buyprice = 97.00 WHERE productCode = '9002';
UPDATE employees SET jobTitle = 'VP Marketing' WHERE employeeNumber = 2025;
UPDATE offices SET phone = '+82 02-123-4567' WHERE officeCode = '9';
UPDATE orders SET status = 'Shipped' WHERE orderNumber = 10414;
UPDATE orderdetails SET quantityOrdered = 35 WHERE orderNumber = '10100';
UPDATE payments SET amount = 700 WHERE customerNumber = '398' AND checkNumber = 'JPMR4544';
UPDATE productlines SET textDescription = '환상의 자동차, 과연 당신의 것일까?' WHERE productLine = 'Classic';
-- 고객님 이메일이 없어요..대신 직원 이메일 수정.
UPDATE employees SET email = 'marie@classicmodelcars.com' WHERE employeeNumber = 2025;
UPDATE products SET buyprice = 800 WHERE productCode = '9001' AND '9002';