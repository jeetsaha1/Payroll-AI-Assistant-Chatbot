from datetime import datetime
from models.employee import Employee
from utils.security import encrypt_data


class PayrollService:
    def __init__(self, db_session):
        self.db_session = db_session

    def calculate_net_salary(self, employee_id, month, year):
        employee = self.db_session.query(Employee).filter_by(id=employee_id).first()
        if not employee:
            return None
        
        basic_salary = employee.salary_structure['basic']
        hra = employee.salary_structure['hra']
        allowances = employee.salary_structure['allowances']
        deductions = self.calculate_deductions(employee_id, month, year)

        net_salary = basic_salary + hra + allowances - deductions
        return net_salary

    def calculate_deductions(self, employee_id, month, year):
        # Placeholder for actual deduction calculations
        pf_deduction = 0.12 * self.db_session.query(Employee).filter_by(id=employee_id).first().salary_structure['basic']
        esi_deduction = 0.0075 * self.db_session.query(Employee).filter_by(id=employee_id).first().salary_structure['basic']
        # Add other deductions as necessary
        return pf_deduction + esi_deduction

    def generate_payslip(self, employee_id, month, year):
        employee = self.db_session.query(Employee).filter_by(id=employee_id).first()
        if not employee:
            return None
        
        net_salary = self.calculate_net_salary(employee_id, month, year)
        payslip_data = {
            'employee_name': employee.name,
            'employee_id': employee.id,
            'month': month,
            'year': year,
            'net_salary': net_salary,
            'generated_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        
        # Here you would generate a PDF or other format for the payslip
        # For now, we will just return the data
        return payslip_data

    def save_employee_salary_record(self, employee_id, salary_record):
        # Placeholder for saving salary record to the database
        encrypted_record = encrypt_data(salary_record)
        # Save encrypted_record to the database
        pass

    def get_salary_expense_report(self, department):
        # Placeholder for generating salary expense report for a department
        total_expense = 0
        employees = self.db_session.query(Employee).filter_by(department=department).all()
        for employee in employees:
            total_expense += self.calculate_net_salary(employee.id, datetime.now().month, datetime.now().year)
        return total_expense