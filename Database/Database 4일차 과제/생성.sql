-- USE classicmodels;
-- 1. 생성(CREATE)
INSERT INTO customers(customerNumber, customerName, contactLastName, phone, addressLine1, city, country) 
VALUES (1001, 'Heesu', 'KIM', '010-1234-5678', '이 동네 어딘가', '이 도시 어딘가', '대한민국'),
 	(1002, 'Maroo', 'KIM', '010-0987-6543', '이 동네 어딘가', '이 도시 어딘가', '대한민국')
INSERT INTO products(productCode,productName,productLine,productScale,productVendor,productDescription,quantityInStock,buyPrice,MSRP)
VALUES (9001, '뛰뛰', 'Classic Cars', '1:900', 'studio', '저세상 자동차', 9999, '99.00', '122.73');
INSERT INTO employees(employeeNumber,lastName,firstName,extension,email,officeCode,reportsTo,jobTitle)
VALUES (2025, 'KIM', 'Marie', 'x808', 'mariene@classicmodelcars.com', '4', '1102', 'Sales Rep');
INSERT INTO offices(officeCode,city,phone,addressLine1,addressLine2,state,country,postalCode,territory)
VALUES ('9','Seoul','+02 123 4567','Seoul Station','NULL','NULL','Korea','8282','Korea')
INSERT INTO orders(orderNumber,orderDate,requiredDate,shippedDate,status,comments,customerNumber) 
VALUES (11101,'2025-01-06','2025-01-13','2025-01-10','Shipped',NULL,1001),
 		(11102,'2025-01-09','2025-01-18','2025-01-11','Shipped','Check on availability.',1002);
INSERT INTO orderdetails(orderNumber,productCode,quantityOrdered,priceEach,orderLineNumber)
VALUES (11101,'9001',24,'99.00',1),(11102,'9001',36,'99.00',1);
INSERT INTO productlines(productLine,textDescription,htmlDescription,image)
VALUES ('Classic','환상의 자동차, 당신의 것',NULL,NULL);
INSERT INTO customers(customerNumber, customerName, contactLastName, phone, addressLine1, city, country) 
VALUES (1003, 'hiie', 'KIM', '010-0000-0000', '저 동네 어딘가', '저 도시 어딘가', '대한민국');
INSERT INTO products(productCode,productName,productLine,productScale,productVendor,productDescription,quantityInStock,buyPrice,MSRP)
VALUES (9002, '빵빵', 'Classic', '1:900', 'studio', '이세상 자동차', 9999, '99.00', '122.73');
