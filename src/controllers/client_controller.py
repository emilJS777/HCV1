from flask import request
from src.services import client_service
from src.middlewares import permission_middleware, auth_middleware
from flask_expects_json import expects_json
from src.validators import client_validator


# CREATE NEW CLIENT
@auth_middleware.check_authorize
@permission_middleware.check_permission("create_client")
@expects_json(client_validator.client_schema)
def client_post():
    req = request.get_json()
    res = client_service.client_create(client_name=req['name'], client_description=req["description"],
                                       max_count_firms=req['max_count_firms'])
    return res


# GET CREATE BY ID
@auth_middleware.check_authorize
@permission_middleware.check_permission("get_client_by_id")
def client_get_by_id(client_id):
    res = client_service.client_get_by_id(client_id=client_id)
    return res


# GET ALL CLIENT
@auth_middleware.check_authorize
@permission_middleware.check_permission("get_clients")
def client_get():
    res = client_service.client_get_all()
    return res


# UPDATE CLIENT BY ID
@auth_middleware.check_authorize
@permission_middleware.check_permission("update_client")
@expects_json(client_validator.client_schema)
def client_update():
    req = request.get_json()
    res = client_service.client_update(client_id=req['id'], client_name=req['name'],
                                       client_description=req["description"], max_count_firms=req['max_count_firms'])
    return res


# DELETE CLIENT BY ID
@auth_middleware.check_authorize
@permission_middleware.check_permission("delete_client")
def client_delete():
    req = request.get_json()
    res = client_service.client_delete(client_id=req['id'])
    return res
