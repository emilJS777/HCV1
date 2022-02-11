from flask import request
from . import user_role_service
from ..middlewares import permission_middleware, auth_middleware


# GET ROLE IDS BY USER ID
@auth_middleware.check_authorize
@permission_middleware.check_permission("get_role_ids_by_user_id")
def get_role_ids_by_user_id(user_id):
    res = user_role_service.get_role_ids_by_user_id(user_id=user_id)
    return res


# BIND LINK USER AND ROLE BY IDS
@auth_middleware.check_authorize
@permission_middleware.check_permission("bind_user_role")
def bind_user_role():
    req = request.get_json()
    res = user_role_service.bind_user_role(user_id=req['user_id'], role_id=req['role_id'])
    return res


# UNBIND USER ROLE
@auth_middleware.check_authorize
@permission_middleware.check_permission("unbind_user_role")
def unbind_user_role():
    req = request.get_json()
    res = user_role_service.unbind_user_role(user_id=req['user_id'], role_id=req['role_id'])
    return res
