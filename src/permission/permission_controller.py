from flask import request
from . import permission_service, permission_middleware
from ..middlewares import auth_middleware


# CREATE NEW PERMISSION _FOR DEVELOPER
@auth_middleware.check_authorize
@permission_middleware.check_permission("create_permission")
def permission_post():
    req = request.get_json()
    res = permission_service.permission_create(permission_name=req['name'])
    return res


# GET PERMISSION BY ID
def permission_get_by_id(permission_id):
    res = permission_service.permission_get_by_id(permission_id=permission_id)
    return res


# GET ALL PERMISSIONS
@auth_middleware.check_authorize
def permission_get():
    res = permission_service.permission_get_all()
    return res


# UPDATE PERMISSION BY ID _FOR DEVELOPER
@auth_middleware.check_authorize
@permission_middleware.check_permission("update_permission")
def permission_update():
    req = request.get_json()
    res = permission_service.permission_update(permission_id=req['id'], permission_name=req['name'])
    return res


# DELETE PERMISSION BY ID _FOR DEVELOPER
@auth_middleware.check_authorize
@permission_middleware.check_permission("delete_permission")
def permission_delete():
    req = request.get_json()
    res = permission_service.permission_delete(permission_id=req['id'])
    return res
