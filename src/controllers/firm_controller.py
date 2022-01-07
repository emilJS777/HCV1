from flask import request
from src.services import firm_service
from src.middlewares import permission_middleware, auth_middleware, client_middleware
from flask_expects_json import expects_json
from src.validators import firm_validator


# CREATE NEW FIRM
@auth_middleware.check_authorize
@permission_middleware.check_permission("create_firm")
@client_middleware.check_client
@expects_json(firm_validator.firm_schema)
def firm_post():
    req_body = request.get_json()
    res = firm_service.firm_create(req_body=req_body)
    return res


# GET FIRM BY ID
@auth_middleware.check_authorize
@permission_middleware.check_permission("get_firm_by_id")
@client_middleware.check_client
def firm_get_by_id(firm_id):
    res = firm_service.firm_get_by_id(firm_id=firm_id)
    return res


# GET ALL FIRM
@auth_middleware.check_authorize
@permission_middleware.check_permission("get_firms")
@client_middleware.check_client
def firm_get():
    res = firm_service.firm_get_all()
    return res


# UPDATE FIRM BY ID
@auth_middleware.check_authorize
@permission_middleware.check_permission("update_firm")
@client_middleware.check_client
@expects_json(firm_validator.firm_schema)
def firm_update(firm_id):
    req_body = request.get_json()
    res = firm_service.firm_update(firm_id=firm_id, req_body=req_body)
    return res


# DELETE FIRM BY ID
@auth_middleware.check_authorize
@permission_middleware.check_permission("delete_firm")
@client_middleware.check_client
def firm_delete(firm_id):
    res = firm_service.firm_delete(firm_id=firm_id)
    return res
