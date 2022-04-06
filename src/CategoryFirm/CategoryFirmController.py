from . import CategoryFirmService, CategoryFirmValidator
from flask import request
from src.Auth import AuthMiddleware
from src.Client import ClientMiddleware
from src.Permission import PermissionMiddleware
from flask_expects_json import expects_json


# CREATE BIND CATEGORY FIRM
@AuthMiddleware.check_authorize
@ClientMiddleware.check_client(required=True)
@PermissionMiddleware.check_permission("firm_edit")
@expects_json(CategoryFirmValidator.category_firm_schema)
def bind_category_firm():
    req = request.get_json()
    res = CategoryFirmService.bind_category_firm(category_id=req['category_id'], firm_id=req['firm_id'])
    return res


# DELETE BIND CATEGORY FIRM
@AuthMiddleware.check_authorize
@ClientMiddleware.check_client(required=True)
@PermissionMiddleware.check_permission("firm_edit")
@expects_json(CategoryFirmValidator.category_firm_schema)
def unbind_category_firm():
    req = request.get_json()
    res = CategoryFirmService.unbind_category_firm(category_id=req['category_id'], firm_id=req['firm_id'])
    return res


# GET FIRM IDS BY CATEGORY ID
@AuthMiddleware.check_authorize
@ClientMiddleware.check_client(required=True)
@PermissionMiddleware.check_permission("firm_get")
def get_firm_ids_by_category_id(category_id: int):
    res = CategoryFirmService.get_firm_ids_by_category_id(category_id=category_id)
    return res
