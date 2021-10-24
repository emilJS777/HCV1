from flask import request
from src.services import client_user
from src.middleware import permission, auth


# GET USER IDS BY CLIENT ID
@auth.check_authorize
@permission.check_permission("get_user_ids_by_client_id")
def get_user_ids_by_client_id(client_id):
    res = client_user.get_user_ids_by_client_id(client_id=client_id)
    return res


# BIND LINK CLIENT AND USER BY ID
@auth.check_authorize
@permission.check_permission("bind_client_user")
def bind_client_user():
    req = request.get_json()
    res = client_user.bind_client_user(client_id=req['client_id'], user_id=req['user_id'])
    return res


# UNBIND CLIENT USER
@auth.check_authorize
@permission.check_permission("unbind_client_user")
def unbind_client_user():
    req = request.get_json()
    res = client_user.unbind_client_user(client_id=req['client_id'], user_id=req['user_id'])
    return res
