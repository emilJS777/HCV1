from flask import request
from . import user_permission_service
from src.auth import auth_middleware
from src.permission import permission_middleware
from src.user import user_service_db


# GET PERMISSION IDS BY USER ID
@auth_middleware.check_authorize
@permission_middleware.check_permission("user_edit")
def get_permission_ids_by_user_id(user_id):
    res = user_permission_service.get_permission_ids_by_user_id(user_id=user_id)
    return res


# BIND LINK USER AND PERMISSION BY IDS
@auth_middleware.check_authorize
@permission_middleware.check_permission("user_edit")
def bind_user_permission():
    req = request.get_json()
    res = user_permission_service.bind_user_permission(user_id=req['user_id'], permission_id=req['permission_id'])
    return res


# UNBIND USER PERMISSION
@auth_middleware.check_authorize
@permission_middleware.check_permission("user_edit")
def unbind_user_permission():
    req = request.get_json()
    res = user_permission_service.unbind_user_permission(user_id=req['user_id'], permission_id=req['permission_id'])
    return res