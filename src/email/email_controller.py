from . import email_service, email_validator
from flask import request
from ..middlewares import auth_middleware, role_middleware
from flask_expects_json import expects_json


# CREATE EMAIL
@auth_middleware.check_authorize
@role_middleware.check_roles(["super_admin", "owner", "director", "accountant"])
@expects_json(email_validator.email_schema)
def email_create():
    req = request.get_json()
    res = email_service.email_create(address=req['address'])
    return res


# UPDATE EMAIL
@auth_middleware.check_authorize
@role_middleware.check_roles(["super_admin", "owner", "director", "accountant"])
@expects_json(email_validator.email_schema)
def email_update():
    req = request.get_json()
    res = email_service.email_update(address=req['address'])
    return res


# DELETE EMAIL
@auth_middleware.check_authorize
@role_middleware.check_roles(["super_admin", "owner", "director", "accountant"])
def email_delete():
    res = email_service.email_delete()
    return res


# GET BY USER ID EMAIL
@auth_middleware.check_authorize
@role_middleware.check_roles(["super_admin", "owner", "director", "accountant"])
def email_get_by_user_id():
    user_id = request.args['user_id']
    res = email_service.email_get_by_user_id(user_id=user_id)
    return res
