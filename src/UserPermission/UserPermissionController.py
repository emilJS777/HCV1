from . import UserPermissionService
from flask import request
from src.Auth import AuthMiddleware
from src.Client import ClientMiddleware
from src.Permission import PermissionMiddleware


# CREATE BIND
@AuthMiddleware.check_authorize
@ClientMiddleware.check_client(required=True)
@PermissionMiddleware.check_permission("user_edit")
def create_bind() -> dict:
    req: dict = request.get_json()
    res: dict = UserPermissionService.create_bind(
        user_id=req['user_id'],
        permission_id=req['permission_id'],
        firm_id=req['firm_id']
    )
    return res


# DELETE BIND
@AuthMiddleware.check_authorize
@ClientMiddleware.check_client(required=True)
@PermissionMiddleware.check_permission("user_edit")
def delete_bind() -> dict:
    req: dict = request.get_json()
    res: dict = UserPermissionService.delete_bind(
        user_id=req['user_id'],
        permission_id=req['permission_id'],
        firm_id=req['firm_id']
    )
    return res


# GET PERMISSION IDS BY USER ID FIRM ID
@AuthMiddleware.check_authorize
@ClientMiddleware.check_client(required=True)
def get_permission_ids_by_user_firm() -> dict:
    res: dict = UserPermissionService.get_permissions_by_user_id(
        user_id=request.args.get('user_id'),
        firm_id=request.args.get('firm_id')
    )
    return res

