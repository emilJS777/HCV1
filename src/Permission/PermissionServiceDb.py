from .PermissionModel import Permission
from flask import g
from typing import List


def create(permission_name, permission_title, category_id: int = None, client_id: int = None, firm: bool or None = None):
    # CREATE NEW PERMISSION BY NAME AND RETURN
    permission = Permission(name=permission_name, title=permission_title)
    permission.category_id = category_id
    permission.client_id = client_id
    permission.firm = firm
    permission.save_db()
    return permission


def update(permission_id, permission_name, permission_title, category_id: int = None):
    # GET PERMISSION BY ID AND UPDATE NAME AND RETURN
    permission = Permission.query.filter_by(id=permission_id).first()
    permission.name = permission_name
    permission.title = permission_title
    permission.category_id = category_id
    permission.update_db()
    return permission


def get_by_name(permission_name, client_id: int = None):
    # GET AND RETURN PERMISSION BY NAME
    client_id = client_id or g.client_id
    permission = Permission.query.filter_by(name=permission_name, client_id=client_id).first()
    return permission


def get_by_id(permission_id):
    # GET PERMISSION BY ID AND RETURN
    permission = Permission.query.filter_by(id=permission_id).first()
    return permission


def delete(permission_id):
    # GET PERMISSION BY ID AND DELETE
    permission = Permission.query.filter_by(id=permission_id).first()
    permission.delete_db()
    return permission


def get_all_by_self_client(firm: bool) -> List[Permission]:
    # GET PERMISSIONS BY SELF CLIENT AND FIRM
    permissions: List[Permission] = Permission.query.filter_by(firm=firm, client_id=g.client_id).all()
    return permissions
