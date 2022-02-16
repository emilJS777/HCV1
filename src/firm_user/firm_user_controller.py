from flask import request
from . import firm_user_service
from ..middlewares import client_middleware, auth_middleware, role_middleware


# GET USER IDS BY FIRM ID
@auth_middleware.check_authorize
@client_middleware.check_client
@role_middleware.check_roles(["owner"])
def get_user_ids_by_firm_id(firm_id):
    res = firm_user_service.get_user_ids_by_firm_id(firm_id=firm_id)
    return res


# BIND LINK FIRM AND USER BY ID
@auth_middleware.check_authorize
@client_middleware.check_client
@role_middleware.check_roles(["owner"])
def bind_firm_user():
    req = request.get_json()
    res = firm_user_service.bind_firm_user(firm_id=req['firm_id'], user_id=req['user_id'])
    return res


# UNBIND FIRM USER
@auth_middleware.check_authorize
@client_middleware.check_client
@role_middleware.check_roles(["owner"])
def unbind_firm_user():
    req = request.get_json()
    res = firm_user_service.unbind_firm_user(firm_id=req['firm_id'], user_id=req['user_id'])
    return res
