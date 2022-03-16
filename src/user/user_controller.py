from flask import request, g
from . import user_service
from src.auth import auth_middleware
from flask_expects_json import expects_json
from src.user import user_validator
from src.permission import permission_middleware
from src.client import client_middleware
from src.firm import firm_middleware


# CREATE NEW USER OR REGISTRATION
@expects_json(user_validator.user_schema)
def create_user() -> dict:
    req = request.get_json()
    res = user_service.create_user(ticket=req['ticket'], user_name=req['name'], password=req['password'])
    return res


# CREATE USER TICKET
@auth_middleware.check_authorize
@permission_middleware.check_permission("user_edit")
@client_middleware.check_client(required=False)
@firm_middleware.check_firm(required=False)
def create_user_ticket() -> dict:
    res = user_service.create_user_ticket(creator_id=g.user_id, client_id=g.client_id, firm_id=g.firm_id)
    return res


# GET USER BY ID
@auth_middleware.check_authorize
@permission_middleware.check_permission("user_get")
@client_middleware.check_client(required=False)
@firm_middleware.check_firm(required=False)
def user_get_by_id(user_id) -> dict:
    res = user_service.user_get_by_id(user_id=user_id)
    return res


# GET ALL USER
@auth_middleware.check_authorize
@permission_middleware.check_permission("user_get")
@client_middleware.check_client(required=False)
@firm_middleware.check_firm(required=False)
def user_get() -> dict:
    res = user_service.user_get_all()
    return res


# UPDATE USER BY ID (set full name)
@auth_middleware.check_authorize
@permission_middleware.check_permission("user_edit")
@client_middleware.check_client(required=False)
@firm_middleware.check_firm(required=False)
def user_update(user_id: int) -> dict:
    req = request.get_json()
    res = user_service.user_update(user_id=user_id, full_name=req['full_name'].title())
    return res


# DELETE USER BY ID
@auth_middleware.check_authorize
@permission_middleware.check_permission("user_edit")
@client_middleware.check_client(required=False)
@firm_middleware.check_firm(required=False)
def user_delete(user_id) -> dict:
    res = user_service.user_delete(user_id=user_id)
    return res
