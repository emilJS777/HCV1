from src.services_db import employee_service_db
from flask import g
from src._response import response


# CREATE NEW EMPLOYEE
def employee_create(first_name, last_name, date_birth, passport_id):
    # VERIFY IF EMPLOYEE BY PASSPORT ID EXIST RETURN CONFLICT
    if employee_service_db.get_by_passport_id(passport_id=passport_id):
        return response(False, {'msg': f'employee by passport id {passport_id} exist'}, 409)

    # ELSE CREATE NEW EMPLOYEE AND RETURN OK
    employee = employee_service_db.create(first_name=first_name, last_name=last_name, date_birth=date_birth,
                                          passport_id=passport_id, firm_id=g.firm_id)
    return response(True, {'msg': f'new employee by id {employee.id} successfully created'}, 200)


# UPDATE EMPLOYEE
def employee_update(employee_id, first_name, last_name, date_birth, passport_id):
    # GET AND VERIFY IF EMPLOYEE BY ID AND FIRM ID NOT FOUND RETURN NOT FOUND
    if not employee_service_db.get_by_id(employee_id=employee_id, firm_id=g.firm_id):
        return response(False, {'msg': f'employee by id {employee_id} not found'}, 404)

    # ELSE UPDATE EMPLOYEE BY ID AND FIRM ID AND RETURN OK
    employee = employee_service_db.update(employee_id=employee_id, first_name=first_name,
                                          last_name=last_name, date_birth=date_birth, passport_id=passport_id)
    return response(True, {'msg': f'employee by id {employee.id} successfully updated'}, 200)


# DELETE EMPLOYEE
def employee_delete(employee_id):
    # GET AND VERIFY IF EMPLOYEE BY ID AND FIRM ID NOT FOUND RETURN NOT FOUND
    if not employee_service_db.get_by_id(employee_id=employee_id, firm_id=g.firm_id):
        return response(False, {'msg': f'employee by id {employee_id} not found'}, 404)

    # ELSE DELETE EMPLOYEE BY ID AND RETURN OK
    employee = employee_service_db.delete(employee_id=employee_id)
    return response(True, {'msg': f'employee by id {employee.id} successfully deleted'}, 200)


# GET ALL IDS BY FIRM ID
def employee_get_all():
    # GET ALL EMPLOYEE IDS BY FIRM ID
    employee_ids = employee_service_db.get_employee_ids_by_firm_id(firm_id=g.firm_id)
    return response(True, employee_ids, 200)


# GET EMPLOYEE BY ID AND FIRM ID
def employee_get_by_id(employee_id):
    # GET EMPLOYEE BY ID AND FIRM ID AND VERIFY. IF NOT FOUND RETURN NOT FOUND
    employee = employee_service_db.get_by_id(employee_id=employee_id, firm_id=g.firm_id)
    if not employee:
        return response(False, {'msg': f'employee by id {employee_id} not found'}, 404)

    # ELSE RETURN EMPLOYEE FIELDS
    return response(True, {'first_name': employee.first_name, 'last_name': employee.last_name,
                           'date_birth': employee.date_birth, 'passport_id': employee.passport_id}, 200)
