from flask import request, g
from . import user_service
from ..middlewares import auth_middleware, role_middleware
from flask_expects_json import expects_json
from src.user import user_validator


# CREATE NEW USER OR REGISTRATION
@expects_json(user_validator.user_schema)
def create_user():
    req = request.get_json()
    res = user_service.create_user(ticket=req['ticket'], user_name=req['name'], password=req['password'],
                                   first_name=req["first_name"], last_name=req["last_name"])
    return res


# CREATE USER TICKET
@auth_middleware.check_authorize
@role_middleware.check_roles(["super_admin", "owner", "director"])
def create_user_ticket():
    res = user_service.create_user_ticket(creator_id=g.user_id)
    return res


# GET USER BY ID
@auth_middleware.check_authorize
@role_middleware.check_roles(["super_admin", "owner", "director"])
def user_get_by_id(user_id):
    res = user_service.user_get_by_id(user_id=user_id)
    return res


# GET ALL USER
@auth_middleware.check_authorize
@role_middleware.check_roles(["super_admin", "owner", "director"])
def user_get():
    res = user_service.user_get_all()
    return res


# UPDATE USER BY ID
@auth_middleware.check_authorize
@role_middleware.check_roles(["super_admin", "owner", "director", "accountant"])
@expects_json(user_validator.user_schema)
def user_update():
    req = request.get_json()
    res = user_service.user_update(user_id=g.user_id, user_name=req['name'],
                                   first_name=req["first_name"], last_name=req["last_name"])
    return res


# DELETE USER BY ID
@auth_middleware.check_authorize
@role_middleware.check_roles(["super_admin", "owner", "director", "accountant"])
def user_delete():
    res = user_service.user_delete(user_id=g.user_id)
    return res
