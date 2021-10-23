from flask import request
from src.services import user
from src.middleware import permission, auth


# CREATE NEW USER
@auth.check_authorize
@permission.check_permission("create_user")
def user_post():
    req = request.get_json()
    res = user.user_create(user_name=req['name'], password=req['password'])
    return res


# GET USER BY ID
@auth.check_authorize
@permission.check_permission("get_user_by_id")
def user_get_by_id(user_id):
    res = user.user_get_by_id(user_id=user_id)
    return res


# GET ALL USER
@auth.check_authorize
@permission.check_permission("get_users")
def user_get():
    res = user.user_get_all()
    return res


# UPDATE USER BY ID
@auth.check_authorize
@permission.check_permission("update_user")
def user_update():
    req = request.get_json()
    res = user.user_update(user_id=req['id'], user_name=req['name'])
    return res


# DELETE USER BY ID
@auth.check_authorize
@permission.check_permission("delete_user")
def user_delete():
    req = request.get_json()
    res = user.user_delete(user_id=req['id'])
    return res
