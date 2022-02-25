from flask import request
from . import client_user_service
from src.auth import auth_middleware
from src.permission import permission_middleware


# GET USER IDS BY CLIENT ID
@auth_middleware.check_authorize
@permission_middleware.check_permission("bind_user_client")
def get_user_ids_by_client_id(client_id):
    res = client_user_service.get_user_ids_by_client_id(client_id=client_id)
    return res


# BIND LINK CLIENT AND USER BY ID
@auth_middleware.check_authorize
@permission_middleware.check_permission("bind_user_client")
def bind_client_user():
    req = request.get_json()
    res = client_user_service.bind_client_user(client_id=req['client_id'], user_id=req['user_id'])
    return res


# UNBIND CLIENT USER
@auth_middleware.check_authorize
@permission_middleware.check_permission("bind_user_client")
def unbind_client_user():
    req = request.get_json()
    res = client_user_service.unbind_client_user(client_id=req['client_id'], user_id=req['user_id'])
    return res
