def calculate_salary(emp_row):
    # Example payroll structure
    basic = emp_row["basic"]
    hra = emp_row["hra"]
    allowance = emp_row["allowance"]
    deductions = emp_row["deductions"]

    gross = basic + hra + allowance
    net = gross - deductions

    return {
        "emp_id": emp_row["emp_id"],
        "basic": basic,
        "hra": hra,
        "allowance": allowance,
        "deductions": deductions,
        "gross": gross,
        "net": net
    }
