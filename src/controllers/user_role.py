from flask import request
from src.services import user_role
from src.middleware import permission, auth


# GET ROLE IDS BY USER ID
@auth.check_authorize
@permission.check_permission("get_role_ids_by_user_id")
def get_role_ids_by_user_id(user_id):
    res = user_role.get_role_ids_by_user_id(user_id=user_id)
    return res


# BIND LINK USER AND ROLE BY IDS
@auth.check_authorize
@permission.check_permission("bind_user_role")
def bind_user_role():
    req = request.get_json()
    res = user_role.bind_user_role(user_id=req['user_id'], role_id=req['role_id'])
    return res


# UNBIND USER ROLE
@auth.check_authorize
@permission.check_permission("unbind_user_role")
def unbind_user_role():
    req = request.get_json()
    res = user_role.unbind_user_role(user_id=req['user_id'], role_id=req['role_id'])
    return res
