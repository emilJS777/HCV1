from . import CategoryService, CategoryValidator
from flask import request
from src.Auth import AuthMiddleware
from src.Client import ClientMiddleware
from src.Permission import PermissionMiddleware
from flask_expects_json import expects_json


# CREATE CATEGORY
@AuthMiddleware.check_authorize
@PermissionMiddleware.check_permission("firm_edit")
@ClientMiddleware.check_client(required=True)
@expects_json(CategoryValidator.category_schema)
def category_create():
    req = request.get_json()
    res = CategoryService.create_category(title=req['title'], description=req['description'])
    return res


# DELETE CATEGORY
@AuthMiddleware.check_authorize
@PermissionMiddleware.check_permission("firm_edit")
@ClientMiddleware.check_client(required=True)
def category_delete(category_id: int):
    res = CategoryService.delete_category(category_id=category_id)
    return res


# UPDATE CATEGORY
@AuthMiddleware.check_authorize
@PermissionMiddleware.check_permission("firm_edit")
@ClientMiddleware.check_client(required=True)
@expects_json(CategoryValidator.category_schema)
def category_update(category_id: int):
    req = request.get_json()
    res = CategoryService.update_category(category_id=category_id, title=req['title'], description=req['description'])
    return res


# GET ALL CATEGORIES
@AuthMiddleware.check_authorize
@PermissionMiddleware.check_permission("firm_get")
@ClientMiddleware.check_client(required=True)
def category_get_all():
    res = CategoryService.get_all_category()
    return res


# GET CATEGORY BY ID
@AuthMiddleware.check_authorize
@PermissionMiddleware.check_permission("firm_get")
@ClientMiddleware.check_client(required=True)
def category_get_by_id(category_id: int):
    res = CategoryService.get_category_by_id(category_id=category_id)
    return res
