from flask import request, g
from . import UserService
from src.Auth import AuthMiddleware
from flask_expects_json import expects_json
from src.User import UserValidator
from src.Permission import PermissionMiddleware
from src.Client import ClientMiddleware


# CREATE NEW USER OR REGISTRATION
@expects_json(UserValidator.user_schema)
def create_user() -> dict:
    req = request.get_json()
    res = UserService.create_user(ticket=req['ticket'], user_name=req['name'], password=req['password'])
    return res


# CREATE USER TICKET
@AuthMiddleware.check_authorize
@ClientMiddleware.check_client(required=True)
@PermissionMiddleware.check_permission("user_edit")
@expects_json(UserValidator.user_ticket_schema)
def create_user_ticket() -> dict:
    req: dict = request.get_json()
    res = UserService.create_user_ticket(creator_id=g.user_id, full_name=req['full_name'], client_id=g.client_id)
    return res


# GET USER BY ID
@AuthMiddleware.check_authorize
@ClientMiddleware.check_client(required=True)
@PermissionMiddleware.check_permission("user_get")
def user_get_by_id(user_id) -> dict:
    res = UserService.user_get_by_id(user_id=user_id)
    return res


# GET ALL USER
@AuthMiddleware.check_authorize
@ClientMiddleware.check_client(required=True)
@PermissionMiddleware.check_permission("user_get")
def user_get() -> dict:
    res = UserService.user_get_all()
    return res


# UPDATE USER BY ID (set full name)
@AuthMiddleware.check_authorize
@ClientMiddleware.check_client(required=True)
@PermissionMiddleware.check_permission("user_edit")
def user_update(user_id: int) -> dict:
    req = request.get_json()
    res = UserService.user_update(user_id=user_id, full_name=req['full_name'].title())
    return res


# DELETE USER BY ID
@AuthMiddleware.check_authorize
@ClientMiddleware.check_client(required=True)
@PermissionMiddleware.check_permission("user_edit")
def user_delete(user_id) -> dict:
    res = UserService.user_delete(user_id=user_id)
    return res
