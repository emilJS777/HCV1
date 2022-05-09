from flask import request
from . import ClientUserService, ClientUserValidator
from src.Auth import AuthMiddleware
from src.Permission import PermissionMiddleware
from flask_expects_json import expects_json
from src.Client import ClientMiddleware


# GET USER IDS BY CLIENT ID
@AuthMiddleware.check_authorize
@ClientMiddleware.check_client(required=True)
@PermissionMiddleware.check_permission("user_get")
@PermissionMiddleware.check_permission("client_get")
def get_users_by_client_id():
    res = ClientUserService.get_users_by_client_id(
        page=int(request.args.get('page')),
        per_page=int(request.args.get('per_page')),
        client_id=int(request.args.get('client_id'))
    )
    return res


# BIND LINK CLIENT AND USER BY ID
@AuthMiddleware.check_authorize
@ClientMiddleware.check_client(required=True)
@PermissionMiddleware.check_permission("user_edit")
@PermissionMiddleware.check_permission("client_edit")
@expects_json(ClientUserValidator.client_user_schema)
def bind_client_user():
    req = request.get_json()
    res = ClientUserService.bind_client_user(client_id=req['client_id'], user_id=req['user_id'])
    return res


# UNBIND CLIENT USER
@AuthMiddleware.check_authorize
@ClientMiddleware.check_client(required=True)
@PermissionMiddleware.check_permission("user_edit")
@PermissionMiddleware.check_permission("client_edit")
@expects_json(ClientUserValidator.client_user_schema)
def unbind_client_user():
    req = request.get_json()
    res = ClientUserService.unbind_client_user(client_id=req['client_id'], user_id=req['user_id'])
    return res
