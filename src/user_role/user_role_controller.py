from flask import request
from . import user_role_service
from ..middlewares import auth_middleware, role_middleware


# GET ROLE IDS BY USER ID
@auth_middleware.check_authorize
@role_middleware.check_roles(["super_admin", "owner", "director"])
def get_role_ids_by_user_id(user_id):
    res = user_role_service.get_role_ids_by_user_id(user_id=user_id)
    return res


# BIND LINK USER AND ROLE BY IDS
@auth_middleware.check_authorize
@role_middleware.check_roles(["super_admin", "owner", "director"])
def bind_user_role():
    req = request.get_json()
    res = user_role_service.bind_user_role(user_id=req['user_id'], role_id=req['role_id'])
    return res


# UNBIND USER ROLE
@auth_middleware.check_authorize
@role_middleware.check_roles(["super_admin", "owner", "director"])
def unbind_user_role():
    req = request.get_json()
    res = user_role_service.unbind_user_role(user_id=req['user_id'], role_id=req['role_id'])
    return res
