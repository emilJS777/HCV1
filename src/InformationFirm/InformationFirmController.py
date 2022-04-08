from . import InformationFirmService, InformationFirmValidator
from flask import request
from src.Auth import AuthMiddleware
from src.Client import ClientMiddleware
from src.Permission import PermissionMiddleware
from flask_expects_json import expects_json


# CREATE BIND INFORMATION FIRM
@AuthMiddleware.check_authorize
@ClientMiddleware.check_client(required=True)
@PermissionMiddleware.check_permission("firm_edit")
@expects_json(InformationFirmValidator.information_firm_schema)
def bind_information_firm():
    req = request.get_json()
    res = InformationFirmService.bind_information_firm(information_id=req['information_id'], firm_id=req['firm_id'])
    return res


# DELETE BIND INFORMATION FIRM
@AuthMiddleware.check_authorize
@ClientMiddleware.check_client(required=True)
@PermissionMiddleware.check_permission("firm_edit")
@expects_json(InformationFirmValidator.information_firm_schema)
def unbind_information_firm():
    req = request.get_json()
    res = InformationFirmService.unbind_information_firm(information_id=req['information_id'], firm_id=req['firm_id'])
    return res


# GET FIRM IDS BY INFORMATION ID
@AuthMiddleware.check_authorize
@ClientMiddleware.check_client(required=True)
@PermissionMiddleware.check_permission("firm_get")
def get_firm_ids_by_information_id(information_id: int):
    res = InformationFirmService.get_firm_ids_by_information_id(information_id=information_id)
    return res
