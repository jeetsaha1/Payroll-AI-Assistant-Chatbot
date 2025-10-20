from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Sample employee database
employees = {
    "101": {"name": "John", "salary": 45000, "tax": 5000, "bonus": 2000},
    "102": {"name": "Rahul", "salary": 50000, "tax": 6000, "bonus": 3000}
}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chatbot", methods=["POST"])
def chatbot():
    user_msg = request.json.get("message", "").lower()
    response = "🤖 I'm not sure how to respond to that."

    # Greeting
    if "hi" in user_msg or "hello" in user_msg:
        response = "👋 Hello! I’m your Payroll Assistant. You can ask me about employees or payslips."

    # Add new employee
    elif user_msg.startswith("add employee"):
        try:
            parts = user_msg.split()
            emp_id = parts[2]
            emp_name = parts[3]
            salary = int(parts[4]) if len(parts) > 4 else 0
            employees[emp_id] = {"name": emp_name, "salary": salary, "tax": 0, "bonus": 0}
            response = f"✅ Employee {emp_name} (ID: {emp_id}) added successfully with salary ₹{salary}."
        except:
            response = "⚠️ Please provide details correctly — e.g. 'add employee 103 Ankit 55000'."

    # Show employee details
    elif "show employee" in user_msg:
        emp_id = user_msg.split()[-1]
        if emp_id in employees:
            emp = employees[emp_id]
            response = (f"👤 <b>Employee ID:</b> {emp_id}<br>"
                        f"<b>Name:</b> {emp['name']}<br>"
                        f"<b>Salary:</b> ₹{emp['salary']}<br>"
                        f"<b>Tax:</b> ₹{emp['tax']}<br>"
                        f"<b>Bonus:</b> ₹{emp['bonus']}")
        else:
            response = "❌ Employee not found."

    # Show payslip
    elif "payslip" in user_msg:
        emp_id = user_msg.split()[-1]
        if emp_id in employees:
            emp = employees[emp_id]
            net_salary = emp['salary'] - emp['tax'] + emp['bonus']
            response = (f"📑 <b>Payslip for {emp['name']} (ID: {emp_id})</b><br>"
                        f"💰 <b>Gross Salary:</b> ₹{emp['salary']}<br>"
                        f"💸 <b>Tax Deduction:</b> ₹{emp['tax']}<br>"
                        f"🎁 <b>Bonus:</b> ₹{emp['bonus']}<br>"
                        f"----------------------------------<br>"
                        f"✅ <b>Net Salary:</b> ₹{net_salary}")
        else:
            response = "❌ Payslip not found. Please check the Employee ID."

    # List all employees
    elif "list employees" in user_msg or "show all" in user_msg:
        if employees:
            response = "<b>📋 Employee List:</b><br>"
            for emp_id, emp in employees.items():
                response += f"{emp_id}: {emp['name']} (₹{emp['salary']})<br>"
        else:
            response = "⚠️ No employees found."

    # Help command
    elif "help" in user_msg:
        response = ("💡 You can try:<br>"
                    "- add employee 103 Ankit 55000<br>"
                    "- show employee 101<br>"
                    "- show payslip for 101<br>"
                    "- list employees")

    return jsonify({"reply": response})

if __name__ == "__main__":
    app.run(debug=True)