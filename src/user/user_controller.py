from flask import request
from . import user_service
from ..middlewares import permission_middleware, auth_middleware
from flask_expects_json import expects_json
from src.user import user_validator


# CREATE NEW USER
@auth_middleware.check_authorize
@permission_middleware.check_permission("create_user")
@expects_json(user_validator.user_schema)
def user_post():
    req = request.get_json()
    res = user_service.user_create(user_name=req['name'], password=req['password'],
                                   first_name=req["first_name"], last_name=req["last_name"])
    return res


# GET USER BY ID
@auth_middleware.check_authorize
@permission_middleware.check_permission("get_user_by_id")
def user_get_by_id(user_id):
    res = user_service.user_get_by_id(user_id=user_id)
    return res


# GET ALL USER
@auth_middleware.check_authorize
@permission_middleware.check_permission("get_users")
def user_get():
    res = user_service.user_get_all()
    return res


# UPDATE USER BY ID
@auth_middleware.check_authorize
@permission_middleware.check_permission("update_user")
@expects_json(user_validator.user_schema)
def user_update():
    req = request.get_json()
    res = user_service.user_update(user_id=req['id'], user_name=req['name'],
                                   first_name=req["first_name"], last_name=req["last_name"])
    return res


# DELETE USER BY ID
@auth_middleware.check_authorize
@permission_middleware.check_permission("delete_user")
def user_delete():
    req = request.get_json()
    res = user_service.user_delete(user_id=req['id'])
    return res
