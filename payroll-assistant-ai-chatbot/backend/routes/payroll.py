from flask import Blueprint
from services.payroll_service import PayrollService
from database import db

payroll_bp = Blueprint('payroll', __name__)

payroll_service = PayrollService(db.session)  # Pass db.session here

# ...existing code...

@payroll_bp.route('/salary/<int:employee_id>', methods=['GET'])
def get_salary(employee_id):
    salary_details = payroll_service.calculate_salary(employee_id)
    return jsonify(salary_details)

@payroll_bp.route('/payslip/<int:employee_id>', methods=['GET'])
def generate_payslip(employee_id):
    payslip = payroll_service.generate_payslip(employee_id)
    return jsonify(payslip)

@payroll_bp.route('/compliance/report', methods=['GET'])
def compliance_report():
    report = payroll_service.generate_compliance_report()
    return jsonify(report)

@payroll_bp.route('/deductions/<int:employee_id>', methods=['GET'])
def get_deductions(employee_id):
    deductions = payroll_service.get_deductions(employee_id)
    return jsonify(deductions)