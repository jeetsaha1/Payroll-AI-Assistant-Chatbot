DROP TABLE IF EXISTS employees;
CREATE TABLE employees (
    emp_id INTEGER PRIMARY KEY,
    name TEXT,
    password TEXT
);

DROP TABLE IF EXISTS payroll;
CREATE TABLE payroll (
    emp_id INTEGER,
    basic INTEGER,
    hra INTEGER,
    allowance INTEGER,
    deductions INTEGER,
    FOREIGN KEY (emp_id) REFERENCES employees(emp_id)
);

-- Sample data
INSERT INTO employees (emp_id, name, password) VALUES (1, 'Jeet Saha', '1234');
INSERT INTO payroll (emp_id, basic, hra, allowance, deductions) VALUES (1, 30000, 10000, 5000, 3000);
