from flask import request
from src.services import role_permission
from src.middleware import permission, auth


# GET PERMISSION IDS BY ROLE ID
@auth.check_authorize
@permission.check_permission("get_permission_ids_by_role_id")
def get_permission_ids_by_role_id(role_id):
    res = role_permission.get_permission_ids_by_role_id(role_id=role_id)
    return res


# BIND LINK ROLE AND PERMISSION BY IDS
@auth.check_authorize
@permission.check_permission("bind_role_permission")
def bind_role_permission():
    req = request.get_json()
    res = role_permission.bind_role_permission(role_id=req['role_id'], permission_id=req['permission_id'])
    return res


# UNBIND ROLE PERMISSION
@auth.check_authorize
@permission.check_permission("unbind_role_permission")
def unbind_role_permission():
    req = request.get_json()
    res = role_permission.unbind_role_permission(role_id=req['role_id'], permission_id=req['permission_id'])
    return res
