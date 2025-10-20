from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Employee(Base):
    __tablename__ = 'employees'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    department = Column(String, nullable=False)
    basic_salary = Column(Float, nullable=False)
    hra = Column(Float, nullable=False)
    allowances = Column(Float, nullable=True)
    bonuses = Column(Float, nullable=True)
    deductions = Column(Float, nullable=True)

    def __init__(self, name, department, basic_salary, hra, allowances=0, bonuses=0, deductions=0):
        self.name = name
        self.department = department
        self.basic_salary = basic_salary
        self.hra = hra
        self.allowances = allowances
        self.bonuses = bonuses
        self.deductions = deductions

    def calculate_net_salary(self):
        return (self.basic_salary + self.hra + self.allowances + self.bonuses) - self.deductions

    @classmethod
    def get_all_employees(cls, session):
        return session.query(cls).all()

    @classmethod
    def get_employee_by_id(cls, session, employee_id):
        return session.query(cls).filter(cls.id == employee_id).first()

    def update_employee(self, session):
        session.commit()

    def delete_employee(self, session):
        session.delete(self)
        session.commit()