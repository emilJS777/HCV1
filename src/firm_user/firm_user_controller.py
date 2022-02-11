from flask import request
from . import firm_user_service
from ..middlewares import permission_middleware, client_middleware, auth_middleware


# GET USER IDS BY FIRM ID
@auth_middleware.check_authorize
@permission_middleware.check_permission("get_user_ids_by_firm_id")
@client_middleware.check_client
def get_user_ids_by_firm_id(firm_id):
    res = firm_user_service.get_user_ids_by_firm_id(firm_id=firm_id)
    return res


# BIND LINK FIRM AND USER BY ID
@auth_middleware.check_authorize
@permission_middleware.check_permission("bind_firm_user")
@client_middleware.check_client
def bind_firm_user():
    req = request.get_json()
    res = firm_user_service.bind_firm_user(firm_id=req['firm_id'], user_id=req['user_id'])
    return res


# UNBIND FIRM USER
@auth_middleware.check_authorize
@permission_middleware.check_permission("unbind_firm_user")
@client_middleware.check_client
def unbind_firm_user():
    req = request.get_json()
    res = firm_user_service.unbind_firm_user(firm_id=req['firm_id'], user_id=req['user_id'])
    return res
