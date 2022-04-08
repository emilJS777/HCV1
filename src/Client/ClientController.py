from flask import request
from . import ClientService, ClientValidator
from src.Auth import AuthMiddleware
from src.Permission import PermissionMiddleware
from flask_expects_json import expects_json
from src.Client import ClientMiddleware


# CREATE NEW CLIENT
@AuthMiddleware.check_authorize
@ClientMiddleware.check_client(required=True)
@PermissionMiddleware.check_permission("client_edit")
@expects_json(ClientValidator.client_schema)
def client_post():
    req = request.get_json()
    res = ClientService.client_create(name=req['name'],
                                       description=req["description"],
                                       max_count_firms=req['max_count_firms']
                                       )
    return res


# UPDATE CLIENT BY ID
@AuthMiddleware.check_authorize
@ClientMiddleware.check_client(required=True)
@PermissionMiddleware.check_permission("client_edit")
@expects_json(ClientValidator.client_schema)
def client_update(client_id):
    req: dict = request.get_json()
    res: dict = ClientService.client_update(client_id=client_id,
                                            name=req['name'],
                                            description=req["description"],
                                            max_count_firms=req['max_count_firms'])
    return res


# DELETE CLIENT BY ID
@AuthMiddleware.check_authorize
@ClientMiddleware.check_client(required=True)
@PermissionMiddleware.check_permission("client_edit")
def client_delete(client_id: int):
    res = ClientService.client_delete(client_id=client_id)
    return res


# GET CLIENT BY ID
@AuthMiddleware.check_authorize
@ClientMiddleware.check_client(required=True)
@PermissionMiddleware.check_permission("client_get")
def client_get_by_id(client_id):
    res = ClientService.client_get_by_id(client_id=client_id)
    return res


# GET ALL CLIENT
@AuthMiddleware.check_authorize
@ClientMiddleware.check_client(required=True)
@PermissionMiddleware.check_permission("client_get")
def client_get():
    res = ClientService.client_get_all()
    return res



