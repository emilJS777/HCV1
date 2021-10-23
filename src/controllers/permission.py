from flask import request
from src.services import permission
from src.middleware import auth


# CREATE NEW PERMISSION _FOR DEVELOPER
def permission_post():
    req = request.get_json()
    res = permission.permission_create(permission_name=req['name'])
    return res


# GET PERMISSION BY ID
def permission_get_by_id(permission_id):
    res = permission.permission_get_by_id(permission_id=permission_id)
    return res


# GET ALL PERMISSIONS
@auth.check_authorize
def permission_get():
    res = permission.permission_get_all()
    return res


# UPDATE PERMISSION BY ID
def permission_update():
    req = request.get_json()
    res = permission.permission_update(permission_id=req['id'], permission_name=req['name'])
    return res


# DELETE PERMISSION BY ID
def permission_delete():
    req = request.get_json()
    res = permission.permission_delete(permission_id=req['id'])
    return res
