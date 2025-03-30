CREATE DATABASE employee_db;
USE employee_db;

CREATE TABLE employees (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    designation VARCHAR(100) NOT NULL,
    mandal VARCHAR(100) NOT NULL,
    opening_balance DECIMAL(10,2) NOT NULL,
    subscription_april DECIMAL(10,2), subscription_may DECIMAL(10,2), subscription_june DECIMAL(10,2),
    subscription_july DECIMAL(10,2), subscription_august DECIMAL(10,2), subscription_september DECIMAL(10,2),
    subscription_october DECIMAL(10,2), subscription_november DECIMAL(10,2), subscription_december DECIMAL(10,2),
    subscription_january DECIMAL(10,2), subscription_february DECIMAL(10,2), subscription_march DECIMAL(10,2),
    reductions_april DECIMAL(10,2), reductions_may DECIMAL(10,2), reductions_june DECIMAL(10,2),
    reductions_july DECIMAL(10,2), reductions_august DECIMAL(10,2), reductions_september DECIMAL(10,2),
    reductions_october DECIMAL(10,2), reductions_november DECIMAL(10,2), reductions_december DECIMAL(10,2),
    reductions_january DECIMAL(10,2), reductions_february DECIMAL(10,2), reductions_march DECIMAL(10,2),
    closing_balance DECIMAL(10,2) NOT NULL
);
