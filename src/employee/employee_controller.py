from flask import request
from ..middlewares import auth_middleware, role_middleware, firm_middleware
from . import employee_service, employee_validator
from flask_expects_json import expects_json


# CREATE NEW EMPLOYEE
@auth_middleware.check_authorize
@firm_middleware.check_firm
@role_middleware.check_roles(["director", "accountant"])
@expects_json(employee_validator.employee_schema)
def employee_create():
    req = request.get_json()
    res = employee_service.employee_create(first_name=req['first_name'],
                                           last_name=req['last_name'],
                                           date_birth=req['date_birth'],
                                           passport_id=req['passport_id'])
    return res


# UPDATE EMPLOYEE BY ID
@auth_middleware.check_authorize
@firm_middleware.check_firm
@role_middleware.check_roles(["director", "accountant"])
@expects_json(employee_validator.employee_schema)
def employee_update(employee_id):
    req = request.get_json()
    res = employee_service.employee_update(employee_id=employee_id,
                                           first_name=req['first_name'],
                                           last_name=req['last_name'],
                                           date_birth=req['date_birth'],
                                           passport_id=req['passport_id'])
    return res


# DELETE EMPLOYEE BY ID
@auth_middleware.check_authorize
@firm_middleware.check_firm
@role_middleware.check_roles(["director", "accountant"])
def employee_delete(employee_id):
    res = employee_service.employee_delete(employee_id=employee_id)
    return res


# GET EMPLOYEE BY ID
@auth_middleware.check_authorize
@firm_middleware.check_firm
@role_middleware.check_roles(["director", "accountant"])
def employee_get_by_id(employee_id):
    res = employee_service.employee_get_by_id(employee_id=employee_id)
    return res


# GET ALL EMPLOYEE
@auth_middleware.check_authorize
@firm_middleware.check_firm
@role_middleware.check_roles(["director", "accountant"])
def employee_get():
    res = employee_service.employee_get_all()
    return res
