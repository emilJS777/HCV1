from flask import request
from src.services import firm_user
from src.middleware import permission, auth


# GET USER IDS BY FIRM ID
@auth.check_authorize
@permission.check_permission("get_user_ids_by_firm_id")
def get_user_ids_by_firm_id(firm_id):
    res = firm_user.get_user_ids_by_firm_id(firm_id=firm_id)
    return res


# BIND LINK FIRM AND USER BY ID
@auth.check_authorize
@permission.check_permission("bind_firm_user")
def bind_firm_user():
    req = request.get_json()
    res = firm_user.bind_firm_user(firm_id=req['firm_id'], user_id=req['user_id'])
    return res


# UNBIND FIRM USER
@auth.check_authorize
@permission.check_permission("unbind_firm_user")
def unbind_firm_user():
    req = request.get_json()
    res = firm_user.unbind_firm_user(firm_id=req['firm_id'], user_id=req['user_id'])
    return res
