from . import UserPermissionServiceDb
from src.User import UserServiceDb
from src.Firm import FirmServiceDb
from src._response import response
from typing import List
from flask import g


# CREATE BIND
def create_bind(user_id: int, permission_id: int, firm_id: int = None) -> dict:
    # GET FIRM AND OR USER IF NOT FOUND RETURN NOT FOUND
    if not UserServiceDb.get_by_id(user_id) or firm_id and not FirmServiceDb.get_by_id(firm_id):
        return response(False, {'msg': 'user and/or firm not found'}, 404)

    if not UserPermissionServiceDb.get_by_user_id_permission_id_firm_id(
        user_id=g.user_id,
        permission_id=permission_id,
        firm_id=firm_id
    ):
        return response(False, {'msg': 'permission not found'}, 403)

    if UserPermissionServiceDb.get_by_user_id_permission_id_firm_id(
            user_id=user_id,
            permission_id=permission_id,
            firm_id=firm_id
    ):
        return response(False, {'msg': 'binding already exists'}, 409)

    UserPermissionServiceDb.create(
        user_id=user_id,
        permission_id=permission_id,
        client_id=g.client_id,
        firm_id=firm_id
    )
    return response(True, {'msg': 'permission user successfully binding'}, 200)


# DELETE BIND
def delete_bind(user_id: int, permission_id: int, firm_id: int = None) -> dict:
    # GET FIRM AND OR USER IF NOT FOUND RETURN NOT FOUND
    if not UserServiceDb.get_by_id(user_id) or firm_id and not FirmServiceDb.get_by_id(firm_id):
        return response(False, {'msg': 'user and/or firm not found'}, 404)

    if not UserPermissionServiceDb.get_by_user_id_permission_id_firm_id(
        user_id=g.user_id,
        permission_id=permission_id,
        firm_id=firm_id
    ):
        return response(False, {'msg': 'permission not found'}, 403)

    if not UserPermissionServiceDb.get_by_user_id_permission_id_firm_id(
            user_id=user_id,
            permission_id=permission_id,
            firm_id=firm_id
    ):
        return response(False, {'msg': 'binding not found'}, 404)

    UserPermissionServiceDb.delete(
        user_id=user_id,
        permission_id=permission_id,
        firm_id=firm_id
    )

    return response(True, {'msg': 'binding successfully deleted'}, 200)


# GET PERMISSIONS BY USER ID
def get_permissions_by_user_id(user_id: int, firm_id: int = None) -> dict:
    # GET USER BY ID IF NOT FOUND RETURN NOT FOUND
    if not UserServiceDb.get_by_id(user_id):
        return response(False, {'msg': 'user not found'}, 404)

    permission_ids: List[int] = UserPermissionServiceDb.get_permission_ids_by_user_id_firm_id(
        user_id=user_id,
        firm_id=firm_id
    )
    return response(True, permission_ids, 200)
