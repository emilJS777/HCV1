from . import category_service, category_validator
from flask import request
from src.auth import auth_middleware
from src.client import client_middleware
from src.permission import permission_middleware
from flask_expects_json import expects_json


# CREATE CATEGORY
@auth_middleware.check_authorize
@permission_middleware.check_permission("firm_edit")
@client_middleware.check_client(required=True)
@expects_json(category_validator.category_schema)
def category_create():
    req = request.get_json()
    res = category_service.create_category(title=req['title'], description=req['description'])
    return res


# DELETE CATEGORY
@auth_middleware.check_authorize
@permission_middleware.check_permission("firm_edit")
@client_middleware.check_client(required=True)
def category_delete(category_id: int):
    res = category_service.delete_category(category_id=category_id)
    return res


# UPDATE CATEGORY
@auth_middleware.check_authorize
@permission_middleware.check_permission("firm_edit")
@client_middleware.check_client(required=True)
@expects_json(category_validator.category_schema)
def category_update(category_id: int):
    req = request.get_json()
    res = category_service.update_category(category_id=category_id, title=req['title'], description=req['description'])
    return res


# GET ALL CATEGORIES
@auth_middleware.check_authorize
@permission_middleware.check_permission("firm_get")
@client_middleware.check_client(required=True)
def category_get_all():
    res = category_service.get_all_category()
    return res


# GET CATEGORY BY ID
@auth_middleware.check_authorize
@permission_middleware.check_permission("firm_get")
@client_middleware.check_client(required=True)
def category_get_by_id(category_id: int):
    res = category_service.get_category_by_id(category_id=category_id)
    return res
