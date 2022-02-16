from flask import request
from . import client_service, client_validator
from src.middlewares import auth_middleware, role_middleware
from flask_expects_json import expects_json


# CREATE NEW CLIENT
@auth_middleware.check_authorize
@role_middleware.check_roles(["super_admin"])
@expects_json(client_validator.client_schema)
def client_post():
    req = request.get_json()
    res = client_service.client_create(client_name=req['name'], client_description=req["description"],
                                       max_count_firms=req['max_count_firms'])
    return res


# GET CLIENT BY ID
@auth_middleware.check_authorize
@role_middleware.check_roles(["super_admin"])
def client_get_by_id(client_id):
    res = client_service.client_get_by_id(client_id=client_id)
    return res


# GET ALL CLIENT
@auth_middleware.check_authorize
@role_middleware.check_roles(["super_admin"])
def client_get():
    res = client_service.client_get_all()
    return res


# UPDATE CLIENT BY ID
@auth_middleware.check_authorize
@role_middleware.check_roles(["super_admin"])
@expects_json(client_validator.client_schema)
def client_update(client_id):
    req = request.get_json()
    res = client_service.client_update(client_id=client_id,
                                       client_name=req['name'],
                                       client_description=req["description"],
                                       max_count_firms=req['max_count_firms'])
    return res


# DELETE CLIENT BY ID
@auth_middleware.check_authorize
@role_middleware.check_roles(["super_admin"])
def client_delete(client_id):
    res = client_service.client_delete(client_id=client_id)
    return res
