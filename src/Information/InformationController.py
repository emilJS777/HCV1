from . import InformationService, InformationValidator
from flask import request
from src.Auth import AuthMiddleware
from src.Client import ClientMiddleware
from src.Permission import PermissionMiddleware
from flask_expects_json import expects_json


# CREATE information
@AuthMiddleware.check_authorize
@ClientMiddleware.check_client(required=True)
@PermissionMiddleware.check_permission("firm_edit")
@expects_json(InformationValidator.information_schema)
def information_create():
    req = request.get_json()
    res = InformationService.create_information(
        title=req['title'],
        description=req['description'],
        unit_id=req['unit_id']
    )
    return res


# DELETE information
@AuthMiddleware.check_authorize
@ClientMiddleware.check_client(required=True)
@PermissionMiddleware.check_permission("firm_edit")
def information_delete(information_id: int):
    res = InformationService.delete_information(information_id=information_id)
    return res


# UPDATE information
@AuthMiddleware.check_authorize
@ClientMiddleware.check_client(required=True)
@PermissionMiddleware.check_permission("firm_edit")
@expects_json(InformationValidator.information_schema)
def information_update(information_id: int):
    req = request.get_json()
    res = InformationService.update_information(
        information_id=information_id,
        title=req['title'],
        description=req['description'],
        unit_id=req['unit_id']
    )
    return res


# GET ALL information
@AuthMiddleware.check_authorize
@ClientMiddleware.check_client(required=True)
@PermissionMiddleware.check_permission("firm_get")
def information_get_all():
    res = InformationService.get_all_information()
    return res


# GET information BY ID
@AuthMiddleware.check_authorize
@ClientMiddleware.check_client(required=True)
@PermissionMiddleware.check_permission("firm_get")
def information_get_by_id(information_id: int):
    res = InformationService.get_information_by_id(information_id=information_id)
    return res


# GET UNIT BY ID
@AuthMiddleware.check_authorize
@ClientMiddleware.check_client(required=True)
def get_unit_by_id(unit_id: int):
    res = InformationService.get_unit_by_id(unit_id)
    return res


# GET UNITS ALL
@AuthMiddleware.check_authorize
@ClientMiddleware.check_client(required=True)
def get_unit_all():
    res = InformationService.get_unit_all()
    return res

