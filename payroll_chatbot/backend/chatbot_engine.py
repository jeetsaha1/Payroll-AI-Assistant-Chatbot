import sqlite3

DB_PATH = "database/payroll.db"

def chatbot_response(message, emp_id=None):
    msg = message.lower()

    if "salary" in msg or "pay" in msg:
        if not emp_id:
            return "Please login to view your salary details."
        conn = sqlite3.connect(DB_PATH)
        conn.row_factory = sqlite3.Row
        emp = conn.execute("SELECT * FROM payroll WHERE emp_id=?", (emp_id,)).fetchone()
        conn.close()
        if not emp:
            return "No payroll data found."
        return f"Your net salary is ₹{emp['basic']+emp['hra']+emp['allowance']-emp['deductions']}."
    
    elif "payslip" in msg:
        return "Payslip feature coming soon! (PDF generation)"
    
    elif "leave" in msg:
        return "You have 5 casual leaves remaining."
    
    return "I can help with salary, payslip, leave balance, and payroll queries."
