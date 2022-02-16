from flask import request, g
from . import firm_service, firm_validator
from ..middlewares import client_middleware, auth_middleware, role_middleware
from flask_expects_json import expects_json


# CREATE NEW FIRM
@auth_middleware.check_authorize
@client_middleware.check_client
@role_middleware.check_roles(["owner"])
@expects_json(firm_validator.firm_schema)
def firm_post():
    req_body = request.get_json()
    res = firm_service.firm_create(req_body=req_body, client_id=g.client_id)
    return res


# GET FIRM BY ID
@auth_middleware.check_authorize
@client_middleware.check_client
@role_middleware.check_roles(["owner"])
def firm_get_by_id(firm_id):
    res = firm_service.firm_get_by_id(firm_id=firm_id, client_id=g.client_id)
    return res


# GET ALL FIRM
@auth_middleware.check_authorize
@client_middleware.check_client
@role_middleware.check_roles(["owner"])
def firm_get():
    res = firm_service.firm_get_all(client_id=g.client_id)
    return res


# UPDATE FIRM BY ID
@auth_middleware.check_authorize
@client_middleware.check_client
@role_middleware.check_roles(["owner"])
@expects_json(firm_validator.firm_schema)
def firm_update(firm_id):
    req_body = request.get_json()
    res = firm_service.firm_update(firm_id=firm_id, req_body=req_body, client_id=g.client_id)
    return res


# DELETE FIRM BY ID
@auth_middleware.check_authorize
@client_middleware.check_client
@role_middleware.check_roles(["owner"])
def firm_delete(firm_id):
    res = firm_service.firm_delete(firm_id=firm_id, client_id=g.client_id)
    return res
