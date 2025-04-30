-- DB 생성
CREATE DATABASE db3day;
USE db3day;
-- employees 테이블 생성
CREATE TABLE employees(
	id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    position VARCHAR(100),
    salary DECIMAL(10,2)
);
-- employees 직원데이터 추가
INSERT INTO employees (name, position, salary) VALUES
	('혜린', 'PM', 90000),
    ('은우', 'Frontend', 80000),
    ('가을', 'Backend', 92000),
    ('지수', 'Frontend', 78000),
    ('민혁', 'Frontend', 96000),
    ('하온', 'Backend', 130000);
-- 모든 직원 이름, 연봉조회
SELECT * FROM db3day.employees;
-- Frontend, 연봉 9000 이하
SELECT name, salary FROM employees WHERE position = 'Frontend' AND salary <= 90000;
-- PM 직원 연봉 10% 인상, 결과 확인
SET SQL_SAFE_UPDATES = 0;
UPDATE employees SET salary = salary * 1.10 WHERE position = 'PM' AND id IS NOT NULL;
SELECT * FROM db3day.employees;
-- Backend 직원 연봉 5% 인상
UPDATE employees SET salary = salary * 1.05 WHERE position = 'Backend';
-- 사원 민혁, 데이터 삭제
DELETE FROM employees WHERE name = '민혁'; 
-- position별 그룹화, 각 직책의 평균 연봉 계산
SELECT position, AVG(salary) AS average_salary FROM employees GROUP BY position;
-- employees 테이블 삭제
DROP TABLE employees;