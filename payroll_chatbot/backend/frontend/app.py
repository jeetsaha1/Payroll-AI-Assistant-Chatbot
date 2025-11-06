# from flask import Flask, render_template, request, jsonify, send_file
# from datetime import datetime
# from reportlab.lib.pagesizes import A4
# from reportlab.pdfgen import canvas
# import io
# app = Flask(__name__)

# # Sample employee database
# employees = {
#     "101": {"name": "John", "salary": 45000, "tax": 5000, "bonus": 2000},
#     "102": {"name": "Rahul", "salary": 50000, "tax": 6000, "bonus": 3000}
# }

# @app.route("/")
# def home():
#     return render_template("index.html")

# @app.route("/chatbot", methods=["POST"])
# def chatbot():
#     data = request.get_json()
#     user_msg = data.get("message", "").lower()
#     print("Received:", user_msg)

#     response = "🤖 I'm not sure how to respond to that."

#     # Greeting
#     if "hi" in user_msg or "hello" in user_msg:
#         response = "👋 Hello! I’m your Payroll Assistant. You can ask me about employees or payslips."

#     # Add new employee
#     elif user_msg.startswith("add employee"):
#         try:
#             parts = user_msg.split()
#             emp_id = parts[2]
#             emp_name = parts[3]
#             salary = int(parts[4]) if len(parts) > 4 else 0
#             employees[emp_id] = {"name": emp_name, "salary": salary, "tax": 0, "bonus": 0}
#             response = f"✅ Employee {emp_name} (ID: {emp_id}) added successfully with salary ₹{salary}."
#         except:
#             response = "⚠️ Please provide details correctly — e.g. 'add employee 103 Ankit 55000'."

#     # Show employee details
#     elif "show employee" in user_msg:
#         emp_id = user_msg.split()[-1]
#         if emp_id in employees:
#             emp = employees[emp_id]
#             response = (f"👤 Employee ID: {emp_id}<br>"
#                         f"Name: {emp['name']}<br>"
#                         f"Salary: ₹{emp['salary']}<br>"
#                         f"Tax: ₹{emp['tax']}<br>"
#                         f"Bonus: ₹{emp['bonus']}")
#         else:
#             response = "❌ Employee not found."

#     # Show payslip
#     elif "payslip" in user_msg:
#         emp_id = user_msg.split()[-1]
#         if emp_id in employees:
#             emp = employees[emp_id]
#             net_salary = emp['salary'] - emp['tax'] + emp['bonus']
#             response = (f"📑 Payslip for {emp['name']} (ID: {emp_id})<br>"
#                         f"Gross Salary: ₹{emp['salary']}<br>"
#                         f"Tax Deduction: ₹{emp['tax']}<br>"
#                         f"Bonus: ₹{emp['bonus']}<br>"
#                         f"----------------------------------<br>"
#                         f"Net Salary: ₹{net_salary}")
#         else:
#             response = "❌ Payslip not found. Please check the Employee ID."

#     # List all employees
#     elif "list employees" in user_msg or "show all" in user_msg:
#         if employees:
#             response = "📋 Employee List:<br>"
#             for emp_id, emp in employees.items():
#                 response += f"{emp_id}: {emp['name']} (₹{emp['salary']})<br>"
#         else:
#             response = "⚠️ No employees found."

#     # Help command
#     elif "help" in user_msg:
#         response = ("💡 You can try:<br>"
#                     "- add employee 103 Ankit 55000<br>"
#                     "- show employee 101<br>"
#                     "- show payslip for 101<br>"
#                     "- list employees")
        
#         # 👋 Greeting
#     if any(word in user_msg for word in ["hi", "hello", "hey"]):
#         response = (
#             "👋 Hello! I’m your Payroll AI Assistant. You can ask me things like:<br>"
#             "• Show payslip for 101<br>"
#             "• Add employee 103 Ankit 55000<br>"
#             "• Update bonus for 101 3000<br>"
#             "• Check leave balance for 102<br>"
#         )

#     # ➕ Add new employee
#     elif user_msg.startswith("add employee"):
#         try:
#             parts = user_msg.split()
#             emp_id = parts[2]
#             emp_name = parts[3]
#             salary = int(parts[4]) if len(parts) > 4 else 0
#             employees[emp_id] = {"name": emp_name, "salary": salary, "tax": 0, "bonus": 0, "leaves": 0}
#             response = f"✅ Employee {emp_name} (ID: {emp_id}) added successfully with salary ₹{salary}."
#         except:
#             response = "⚠️ Please provide details correctly — e.g. 'add employee 103 Ankit 55000'."

#     # 📋 Show employee details
#     elif "show employee" in user_msg:
#         emp_id = user_msg.split()[-1]
#         if emp_id in employees:
#             emp = employees[emp_id]
#             response = (f"👤 Employee ID: {emp_id}<br>"
#                         f"Name: {emp['name']}<br>"
#                         f"Salary: ₹{emp['salary']}<br>"
#                         f"Tax: ₹{emp['tax']}<br>"
#                         f"Bonus: ₹{emp['bonus']}<br>"
#                         f"Leaves Taken: {emp['leaves']}")
#         else:
#             response = "❌ Employee not found."

#     # 💵 Update bonus
#     elif "update bonus" in user_msg:
#         try:
#             parts = user_msg.split()
#             emp_id = parts[-2]
#             bonus = int(parts[-1])
#             if emp_id in employees:
#                 employees[emp_id]["bonus"] = bonus
#                 response = f"🎁 Bonus for {employees[emp_id]['name']} updated to ₹{bonus}."
#             else:
#                 response = "❌ Employee not found."
#         except:
#             response = "⚠️ Use format: update bonus for 101 3000"

#     # 💸 Update tax
#     elif "update tax" in user_msg:
#         try:
#             parts = user_msg.split()
#             emp_id = parts[-2]
#             tax = int(parts[-1])
#             if emp_id in employees:
#                 employees[emp_id]["tax"] = tax
#                 response = f"🧾 Tax for {employees[emp_id]['name']} updated to ₹{tax}."
#             else:
#                 response = "❌ Employee not found."
#         except:
#             response = "⚠️ Use format: update tax for 101 5000"

#     # 🏖️ Leave balance
#     elif "leave" in user_msg or "leaves" in user_msg:
#         emp_id = user_msg.split()[-1]
#         if emp_id in employees:
#             emp = employees[emp_id]
#             response = f"🌴 {emp['name']} has taken {emp['leaves']} leaves this month."
#         else:
#             response = "❌ Employee not found."


#     # 📊 Payslip details
#     elif "payslip" in user_msg and "generate" not in user_msg:
#         emp_id = user_msg.split()[-1]
#         if emp_id in employees:
#             emp = employees[emp_id]
#             net_salary = emp['salary'] - emp['tax'] + emp['bonus']
#             response = (f"📑 Payslip for {emp['name']} (ID: {emp_id})<br>"
#                         f"Gross Salary: ₹{emp['salary']}<br>"
#                         f"Tax Deduction: ₹{emp['tax']}<br>"
#                         f"Bonus: ₹{emp['bonus']}<br>"
#                         f"----------------------------------<br>"
#                         f"Net Salary: ₹{net_salary}")
#         else:
#             response = "❌ Payslip not found. Please check the Employee ID."

#     # 🧾 Generate payslip PDF
#     elif "generate payslip" in user_msg:
#         emp_id = user_msg.split()[-1]
#         if emp_id in employees:
#             buffer = io.BytesIO()
#             emp = employees[emp_id]
#             c = canvas.Canvas(buffer, pagesize=A4)
#             c.setFont("Helvetica-Bold", 16)
#             c.drawString(200, 800, "Company XYZ Pvt. Ltd.")
#             c.setFont("Helvetica", 12)
#             c.drawString(50, 760, f"Payslip for: {emp['name']} (ID: {emp_id})")
#             c.drawString(50, 740, f"Date: {datetime.now().strftime('%d-%m-%Y')}")
#             c.drawString(50, 700, f"Gross Salary: ₹{emp['salary']}")
#             c.drawString(50, 680, f"Tax Deduction: ₹{emp['tax']}")
#             c.drawString(50, 660, f"Bonus: ₹{emp['bonus']}")
#             c.drawString(50, 640, f"Net Salary: ₹{emp['salary'] - emp['tax'] + emp['bonus']}")
#             c.showPage()
#             c.save()
#             buffer.seek(0)
#             return send_file(buffer, as_attachment=True, download_name=f"payslip_{emp_id}.pdf", mimetype="application/pdf")
#         else:
#             response = "❌ Employee not found."

#     # 📃 List all employees
#     elif "list employees" in user_msg or "show all" in user_msg:
#         if employees:
#             response = "📋 Employee List:<br>"
#             for emp_id, emp in employees.items():
#                 response += f"{emp_id}: {emp['name']} (₹{emp['salary']})<br>"
#         else:
#             response = "⚠️ No employees found."

#     # ❓ Help section
#     elif "help" in user_msg:
#         response = ("💡 You can try:<br>"
#                     "- add employee 103 Ankit 55000<br>"
#                     "- show employee 101<br>"
#                     "- update bonus for 101 3000<br>"
#                     "- update tax for 102 4500<br>"
#                     "- check leave balance for 101<br>"
#                     "- generate payslip for 101<br>"
#                     "- show payday<br>"
#                     "- list employees")

#     # 💬 Small talk
#     elif "thank" in user_msg:
#         response = "😊 You’re welcome! Always happy to assist with your payroll queries."
#     elif "how are you" in user_msg:
#         response = "🤖 I'm great! Ready to process payrolls and keep employees happy 😄"
#     elif "bye" in user_msg:
#         response = "👋 Goodbye! Have a productive day ahead!"

#     return jsonify({"reply": response})

# if __name__ == "__main__":
#     app.run(debug=True)















from flask import Flask, render_template, request, jsonify, send_file
from datetime import datetime
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
import io

app = Flask(__name__)

# Sample employee database
employees = {
    "101": {"name": "John", "salary": 45000, "tax": 5000, "bonus": 2000, "leaves": 2},
    "102": {"name": "Rahul", "salary": 50000, "tax": 6000, "bonus": 3000, "leaves": 1}
}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chatbot", methods=["POST"])
def chatbot():
    data = request.get_json()
    user_msg = data.get("message", "").lower().strip()
    print("Received:", user_msg)

    response = "🤖 I'm not sure how to respond to that."

    # 👋 Greeting
    if any(word in user_msg for word in ["hi", "hello", "hey"]):
        response = (
            "👋 Hello! I’m your Payroll AI Assistant.<br>"
            "You can try commands like:<br>"
            "• show employee 101<br>"
            "• add employee 103 Ankit 55000<br>"
            "• update bonus for 101 3000<br>"
            "• generate payslip for 101"
        )

    # ➕ Add new employee
    elif user_msg.startswith("add employee"):
        try:
            parts = user_msg.split()
            emp_id = parts[2]
            emp_name = parts[3]
            salary = int(parts[4])
            employees[emp_id] = {"name": emp_name, "salary": salary, "tax": 0, "bonus": 0, "leaves": 0}
            response = f"✅ Employee {emp_name} (ID: {emp_id}) added successfully with salary ₹{salary}."
        except:
            response = "⚠️ Please provide details correctly — e.g. 'add employee 103 Ankit 55000'."

    # 📋 Show employee details
    elif "show employee" in user_msg:
        emp_id = user_msg.split()[-1]
        if emp_id in employees:
            emp = employees[emp_id]
            response = (
                f"👤 Employee ID: {emp_id}<br>"
                f"Name: {emp['name']}<br>"
                f"Salary: ₹{emp['salary']}<br>"
                f"Tax: ₹{emp['tax']}<br>"
                f"Bonus: ₹{emp['bonus']}<br>"
                f"Leaves Taken: {emp['leaves']}"
            )
        else:
            response = "❌ Employee not found."

    # 💵 Update bonus
    elif "update bonus" in user_msg:
        try:
            parts = user_msg.split()
            emp_id = parts[-2]
            bonus = int(parts[-1])
            if emp_id in employees:
                employees[emp_id]["bonus"] = bonus
                response = f"🎁 Bonus for {employees[emp_id]['name']} updated to ₹{bonus}."
            else:
                response = "❌ Employee not found."
        except:
            response = "⚠️ Use format: update bonus for 101 3000"

    # 🧾 Update tax
    elif "update tax" in user_msg:
        try:
            parts = user_msg.split()
            emp_id = parts[-2]
            tax = int(parts[-1])
            if emp_id in employees:
                employees[emp_id]["tax"] = tax
                response = f"🧾 Tax for {employees[emp_id]['name']} updated to ₹{tax}."
            else:
                response = "❌ Employee not found."
        except:
            response = "⚠️ Use format: update tax for 101 5000"

    # 🌴 Check leave
    elif "leave" in user_msg or "leaves" in user_msg:
        emp_id = user_msg.split()[-1]
        if emp_id in employees:
            emp = employees[emp_id]
            response = f"🌴 {emp['name']} has taken {emp['leaves']} leaves this month."
        else:
            response = "❌ Employee not found."

    # 📄 Generate payslip link
    elif "generate payslip" in user_msg:
        emp_id = user_msg.split()[-1]
        if emp_id in employees:
            response = f"🧾 Payslip ready! 👉 <a href='/download_payslip/{emp_id}' target='_blank'>Click here to download</a>"
        else:
            response = "❌ Employee not found."

    # 📃 List all employees
    elif "list employees" in user_msg or "show all" in user_msg:
        if employees:
            response = "📋 Employee List:<br>"
            for emp_id, emp in employees.items():
                response += f"{emp_id}: {emp['name']} (₹{emp['salary']})<br>"
        else:
            response = "⚠️ No employees found."

    # 💡 Help section
    elif "help" in user_msg:
        response = (
            "💡 Commands you can use:<br>"
            "- add employee 103 Ankit 55000<br>"
            "- show employee 101<br>"
            "- update bonus for 101 3000<br>"
            "- update tax for 102 4500<br>"
            "- generate payslip for 101<br>"
            "- list employees"
        )
    elif "how are you" in user_msg:
        response = "🤖 I'm great! Ready to process payrolls and keep employees happy 😄"
# 

    elif "thank" in user_msg:
        response = "😊 You’re welcome! Always happy to help with your payroll queries."
    elif "bye" in user_msg:
        response = "👋 Goodbye! Have a productive day!"

    return jsonify({"reply": response})


# Separate route to generate & send PDF
@app.route("/download_payslip/<emp_id>")
def download_payslip(emp_id):
    if emp_id not in employees:
        return "❌ Employee not found.", 404

    emp = employees[emp_id]
    buffer = io.BytesIO()
    c = canvas.Canvas(buffer, pagesize=A4)
    c.setFont("Helvetica-Bold", 16)
    c.drawString(200, 800, "Company XYZ Pvt. Ltd.")
    c.setFont("Helvetica", 12)
    c.drawString(50, 760, f"Payslip for: {emp['name']} (ID: {emp_id})")
    c.drawString(50, 740, f"Date: {datetime.now().strftime('%d-%m-%Y')}")
    c.drawString(50, 700, f"Gross Salary: ₹{emp['salary']}")
    c.drawString(50, 680, f"Tax Deduction: ₹{emp['tax']}")
    c.drawString(50, 660, f"Bonus: ₹{emp['bonus']}")
    c.drawString(50, 640, f"Net Salary: ₹{emp['salary'] - emp['tax'] + emp['bonus']}")
    c.showPage()
    c.save()
    buffer.seek(0)

    return send_file(buffer, as_attachment=True, download_name=f"payslip_{emp_id}.pdf", mimetype="application/pdf")


if __name__ == "__main__":
    app.run(debug=True)
