from flask import jsonify
from database import db
from services.payroll_service import PayrollService

class ChatbotService:
    def __init__(self, db_session):
        self.payroll_service = PayrollService(db_session)
        # ...other initialization...

    def get_response(self, message):
        # ...your chatbot logic...
        return "This is a mock chatbot response."
    

# Try to use OpenAI if available
try:
    from openai import OpenAI
    OPENAI_AVAILABLE = True
except ImportError:
    OPENAI_AVAILABLE = False


class ChatbotService:
    def __init__(self):
        self.payroll_service = PayrollService()

        if OPENAI_AVAILABLE:
            self.client = OpenAI()  # AI chatbot enabled
        else:
            self.client = None      # Fallback to rule-based chatbot

    def handle_query(self, user_query, user_id):
        """
        Main handler for chatbot queries
        """
        # If AI chatbot is available, try it first
        if self.client:
            try:
                response = self.client.chat.completions.create(
                    model="gpt-4o-mini",  # or "gpt-3.5-turbo"
                    messages=[{"role": "user", "content": user_query}]
                )
                return response.choices[0].message.content
            except Exception as e:
                return f"AI chatbot error: {str(e)}"

        # Otherwise use simple rule-based responses
        if "salary" in user_query.lower():
            return self.get_salary_info(user_id)
        elif "payslip" in user_query.lower():
            return self.get_payslip(user_id)
        elif "pf" in user_query.lower():
            return self.get_pf_deduction(user_id)
        else:
            return "Sorry, I can only answer payroll-related queries (salary, payslip, PF)."

    def get_salary_info(self, user_id):
        net_salary = self.payroll_service.calculate_net_salary(user_id)
        return f"Your net salary for this month is ₹{net_salary}."

    def get_payslip(self, user_id):
        payslip = self.payroll_service.generate_payslip(user_id)
        return f"Here is your payslip: {payslip}"  # could be URL or PDF data

    def get_pf_deduction(self, user_id):
        pf_deduction = self.payroll_service.get_pf_deduction(user_id)
        return f"Your PF deduction this year is ₹{pf_deduction}."

    def process_chatbot_response(self, response):
        return jsonify({"response": response})
