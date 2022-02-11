from .employee_model import Employee


def create(first_name, last_name, date_birth, passport_id, firm_id):
    # CREATE EMPLOYEE SAVE DB AND RETURN
    employee = Employee(first_name=first_name, last_name=last_name, date_birth=date_birth,
                        passport_id=passport_id, firm_id=firm_id)
    employee.save_db()
    return employee


def update(employee_id, first_name, last_name, date_birth, passport_id):
    # GET EMPLOYEE BY ID AND FIRM ID AND UPDATE & RETURN
    employee = Employee.query.filter_by(id=employee_id).first()
    employee.first_name = first_name
    employee.last_name = last_name
    employee.date_birth = date_birth
    employee.passport_id = passport_id
    employee.update_db()
    return employee


def delete(employee_id):
    # GET EMPLOYEE BY ID AND DELETE
    employee = Employee.query.filter_by(id=employee_id).first()
    employee.delete_db()
    return employee


def get_by_id(employee_id, firm_id):
    # GET EMPLOYEE BY ID
    employee = Employee.query.filter_by(id=employee_id, firm_id=firm_id).first()
    return employee


def get_employee_ids_by_firm_id(firm_id):
    # GET ALL EMPLOYEE IDS BY FIRM ID
    employee_ids = []
    for employee in Employee.query.filter_by(firm_id=firm_id).all():
        employee_ids.append(employee.id)
    return employee_ids


def get_by_passport_id(passport_id):
    # GET EMPLOYEE BY PASSPORT ID AND RETURN
    employee = Employee.query.filter_by(passport_id=passport_id).first()
    return employee

