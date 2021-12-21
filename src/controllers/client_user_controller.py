from flask import request
from src.services import client_user_service
from src.middlewares import permission_middleware, auth_middleware


# GET USER IDS BY CLIENT ID
@auth_middleware.check_authorize
@permission_middleware.check_permission("get_user_ids_by_client_id")
def get_user_ids_by_client_id(client_id):
    res = client_user_service.get_user_ids_by_client_id(client_id=client_id)
    return res


# BIND LINK CLIENT AND USER BY ID
@auth_middleware.check_authorize
@permission_middleware.check_permission("bind_client_user")
def bind_client_user():
    req = request.get_json()
    res = client_user_service.bind_client_user(client_id=req['client_id'], user_id=req['user_id'])
    return res


# UNBIND CLIENT USER
@auth_middleware.check_authorize
@permission_middleware.check_permission("unbind_client_user")
def unbind_client_user():
    req = request.get_json()
    res = client_user_service.unbind_client_user(client_id=req['client_id'], user_id=req['user_id'])
    return res
