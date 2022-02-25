from . import category_firm_service
from flask import request
from src.auth import auth_middleware
from src.client import client_middleware
from src.permission import permission_middleware


# CREATE BIND CATEGORY FIRM
@auth_middleware.check_authorize
@client_middleware.check_client(required=True)
@permission_middleware.check_permission("firm_edit")
def bind_category_firm():
    req = request.get_json()
    res = category_firm_service.bind_category_firm(category_id=req['category_id'], firm_id=req['firm_id'])
    return res


# DELETE BIND CATEGORY FIRM
@auth_middleware.check_authorize
@client_middleware.check_client(required=True)
@permission_middleware.check_permission("firm_edit")
def unbind_category_firm():
    req = request.get_json()
    res = category_firm_service.unbind_category_firm(category_id=req['category_id'], firm_id=req['firm_id'])
    return res


# GET FIRM IDS BY CATEGORY ID
@auth_middleware.check_authorize
@client_middleware.check_client(required=True)
@permission_middleware.check_permission("firm_get")
def get_firm_ids_by_category_id(category_id: int):
    res = category_firm_service.get_firm_ids_by_category_id(category_id=category_id)
    return res
