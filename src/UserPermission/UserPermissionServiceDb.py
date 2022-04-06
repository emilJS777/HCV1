from .UserPermissionModel import UserPermission
from typing import List
from flask import g


# CREATE
def create(user_id: int, permission_id: int, client_id: int, firm_id: int = None) -> UserPermission:
    user_permission: UserPermission = UserPermission(
        user_id=user_id,
        permission_id=permission_id,
        firm_id=firm_id,
        client_id=client_id
    )
    user_permission.save_db()
    return user_permission


# DELETE
def delete(user_id: int, permission_id: int, firm_id: int) -> UserPermission:
    user_permission: UserPermission = UserPermission.query.filter_by(
        user_id=user_id,
        permission_id=permission_id,
        firm_id=firm_id
    ).first()
    user_permission.delete_db()
    return user_permission


# GET PERMISSION ID FIRM ID LIST BY USER ID
def get_permission_firm_ids_by_user_id(user_id: int) -> List[dict]:
    user_permissions: List[UserPermission] = UserPermission.query.filter_by(
        user_id=user_id
    ).all()

    user_permission_list: List[dict] = []
    for user_permission in user_permissions:
        user_permission_list.append({'permission_id': user_permission.permission_id, 'firm_id': user_permission.firm_id})

    return user_permission_list


# GET BY FIRM ID PERMISSION ID USER ID
def get_by_user_id_permission_id_firm_id(user_id: int, permission_id: int, firm_id: int) -> UserPermission:
    user_permission: UserPermission = UserPermission.query.filter_by(
        user_id=user_id,
        permission_id=permission_id,
        firm_id=firm_id,
        client_id=g.client_id
    ).first()

    return user_permission


# GET PERMISSION IDS BY FIRM ID USER ID
def get_permission_ids_by_user_id_firm_id(user_id: int, firm_id: int) -> List[int]:
    user_permissions: List[UserPermission] = UserPermission.query.filter_by(client_id=g.client_id,
                                                                            user_id=user_id,
                                                                            firm_id=firm_id).all()
    permission_ids: List[int] = []
    for user_permission in user_permissions:
        permission_ids.append(user_permission.permission_id)

    return permission_ids

