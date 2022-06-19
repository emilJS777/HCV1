from . import UserPermissionServiceDb
from src.Permission import PermissionServiceDb
from src.User import UserServiceDb
from src.Firm import FirmServiceDb
from src._response import response
from typing import List
from flask import g


# CREATE BIND
def create_bind(user_id: int, permission_id: int, firm_id: int = None) -> dict:
    # GET FIRM AND OR USER IF NOT FOUND RETURN NOT FOUND
    if not UserServiceDb.get_by_id(user_id) or firm_id and not FirmServiceDb.get_by_id(firm_id):
        return response(False, {'msg': 'user and/or firm not found'}, 200)

    if not UserPermissionServiceDb.get_by_user_id_permission_id_firm_id(
        user_id=g.user_id,
        permission_id=permission_id,
        firm_id=firm_id
    ):
        return response(False, {'msg': 'permission not found'}, 200)

    if UserPermissionServiceDb.get_by_user_id_permission_id_firm_id(
            user_id=user_id,
            permission_id=permission_id,
            firm_id=firm_id
    ):
        return response(False, {'msg': 'binding already exists'}, 200)

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
        return response(False, {'msg': 'user and/or firm not found'}, 200)

    if not UserPermissionServiceDb.get_by_user_id_permission_id_firm_id(
        user_id=g.user_id,
        permission_id=permission_id,
        firm_id=firm_id
    ):
        return response(False, {'msg': 'permission not found'}, 200)

    if not UserPermissionServiceDb.get_by_user_id_permission_id_firm_id(
            user_id=user_id,
            permission_id=permission_id,
            firm_id=firm_id
    ):
        return response(False, {'msg': 'binding not found'}, 200)

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
        return response(False, {'msg': 'user not found'}, 200)

    permission_list: List[dict] = []

    for permission_id in UserPermissionServiceDb.get_permission_ids_by_user_id_firm_id(
        user_id=user_id,
        firm_id=firm_id
    ):
        permission: PermissionServiceDb.Permission = PermissionServiceDb.get_by_id(permission_id)
        permission_list.append({'id': permission.id, 'name': permission.name, 'title': permission.title})

    return response(True, permission_list, 200)
