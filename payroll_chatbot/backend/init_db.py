import sqlite3

DB_PATH = "../database/payroll.db"

# Connect (will create file if not exists)
conn = sqlite3.connect(DB_PATH)
c = conn.cursor()

# Create employees table
c.execute("""
CREATE TABLE IF NOT EXISTS employees (
    emp_id INTEGER PRIMARY KEY,
    name TEXT,
    password TEXT
)
""")

# Create payroll table
c.execute("""
CREATE TABLE IF NOT EXISTS payroll (
    emp_id INTEGER,
    basic INTEGER,
    hra INTEGER,
    allowance INTEGER,
    deductions INTEGER,
    FOREIGN KEY (emp_id) REFERENCES employees(emp_id)
)
""")

# Insert sample data
c.execute("INSERT OR IGNORE INTO employees VALUES (1, 'Jeet Saha', '1234')")
c.execute("INSERT OR IGNORE INTO payroll VALUES (1, 30000, 10000, 5000, 3000)")

conn.commit()
conn.close()

print("Database initialized ✅")
