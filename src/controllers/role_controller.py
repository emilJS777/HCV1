from flask import request
from src.services import role_service
from src.middlewares import permission_middleware, auth_middleware


# CREATE NEW ROLE
@auth_middleware.check_authorize
@permission_middleware.check_permission("create_role")
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
