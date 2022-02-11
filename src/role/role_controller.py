from flask import request
from . import role_service, role_validator
from ..middlewares import permission_middleware, auth_middleware
from flask_expects_json import expects_json


# CREATE NEW ROLE
@auth_middleware.check_authorize
@permission_middleware.check_permission("create_role")
@expects_json(role_validator.role_schema)
def role_post():
    req = request.get_json()
    res = role_service.role_create(role_name=req['name'])
    return res


# GET ROLE BY ID
@auth_middleware.check_authorize
@permission_middleware.check_permission("get_role_by_id")
def role_get_by_id(role_id):
    res = role_service.role_get_by_id(role_id=role_id)
    return res


# GET ALL ROLE
@auth_middleware.check_authorize
@permission_middleware.check_permission("get_roles")
def role_get():
    res = role_service.role_get_all()
    return res


# UPDATE ROLE BY ID
@auth_middleware.check_authorize
@permission_middleware.check_permission("update_role")
@expects_json(role_validator.role_schema)
def role_update():
    req = request.get_json()
    res = role_service.role_update(role_id=req['id'], role_name=req['name'])
    return res


# DELETE ROLE BY ID
@auth_middleware.check_authorize
@permission_middleware.check_permission("delete_role")
def role_delete():
    req = request.get_json()
    res = role_service.role_delete(role_id=req['id'])
    return res
