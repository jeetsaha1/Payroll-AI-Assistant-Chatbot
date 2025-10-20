import requests

url = "http://127.0.0.1:5000/payroll/generate_payslip"
data = {
    "employee_id": "E001",
    "month": "September",
    "year": "2025"
}

response = requests.post(url, json=data)
try:
    print("POST /chatbot =>", response.json())
except Exception:
    print("POST /chatbot =>", response.text)

