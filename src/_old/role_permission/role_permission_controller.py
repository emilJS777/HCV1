from flask import request
from . import role_permission_service
from src.middlewares import auth_middleware
from ..permission import permission_middleware


# GET PERMISSION IDS BY ROLE ID
@auth_middleware.check_authorize
@permission_middleware.check_permission("get_permission_ids_by_role_id")
def get_permission_ids_by_role_id(role_id):
    res = role_permission_service.get_permission_ids_by_role_id(role_id=role_id)
    return res


# BIND LINK ROLE AND PERMISSION BY IDS
@auth_middleware.check_authorize
@permission_middleware.check_permission("bind_role_permission")
def bind_role_permission():
    req = request.get_json()
    res = role_permission_service.bind_role_permission(role_id=req['role_id'], permission_id=req['permission_id'])
    return res


# UNBIND ROLE PERMISSION
@auth_middleware.check_authorize
@permission_middleware.check_permission("unbind_role_permission")
def unbind_role_permission():
    req = request.get_json()
    res = role_permission_service.unbind_role_permission(role_id=req['role_id'], permission_id=req['permission_id'])
    return res
