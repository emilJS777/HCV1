from flask import request, g
from . import FirmService, FirmValidator
from src.Auth import AuthMiddleware
from src.Permission import PermissionMiddleware
from src.Client import ClientMiddleware
from flask_expects_json import expects_json


# CREATE NEW FIRM
@AuthMiddleware.check_authorize
@ClientMiddleware.check_client(required=True)
@PermissionMiddleware.check_permission("firm_edit")
@expects_json(FirmValidator.firm_schema)
def firm_post():
    req_body = request.get_json()
    res = FirmService.firm_create(req_body=req_body)
    return res


# GET FIRM BY ID
@AuthMiddleware.check_authorize
@ClientMiddleware.check_client(required=True)
@PermissionMiddleware.check_permission("firm_get")
def firm_get_by_id(firm_id):
    res = FirmService.firm_get_by_id(firm_id=firm_id)
    return res


# GET ALL FIRM
@AuthMiddleware.check_authorize
@ClientMiddleware.check_client(required=True)
@PermissionMiddleware.check_permission("firm_get")
def firm_get():
    res = FirmService.firm_get_all(
        page=int(request.args.get('page')),
        per_page=int(request.args.get('per_page'))
    )
    return res


# UPDATE FIRM BY ID
@AuthMiddleware.check_authorize
@ClientMiddleware.check_client(required=True)
@PermissionMiddleware.check_permission("firm_edit")
@expects_json(FirmValidator.firm_schema)
def firm_update(firm_id):
    req_body = request.get_json()
    res = FirmService.firm_update(firm_id=firm_id, req_body=req_body)
    return res


# DELETE FIRM BY ID
@AuthMiddleware.check_authorize
@ClientMiddleware.check_client(required=True)
@PermissionMiddleware.check_permission("firm_edit")
def firm_delete(firm_id):
    res = FirmService.firm_delete(firm_id=firm_id)
    return res
