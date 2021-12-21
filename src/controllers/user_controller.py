from flask import request
from src.services import user_service
from src.middlewares import permission_middleware, auth_middleware


# CREATE NEW USER
@auth_middleware.check_authorize
@permission_middleware.check_permission("create_user")
def user_post():
    req = request.get_json()
    res = user_service.user_create(user_name=req['name'], password=req['password'])
    return res


# GET USER BY ID
@auth_middleware.check_authorize
@permission_middleware.check_permission("get_user_by_id")
def user_get_by_id(user_id):
    res = user_service.user_get_by_id(user_id=user_id)
    return res


# GET ALL USER
@auth_middleware.check_authorize
@permission_middleware.check_permission("get_users")
def user_get():
    res = user_service.user_get_all()
    return res


# UPDATE USER BY ID
@auth_middleware.check_authorize
@permission_middleware.check_permission("update_user")
def user_update():
    req = request.get_json()
    res = user_service.user_update(user_id=req['id'], user_name=req['name'])
    return res


# DELETE USER BY ID
@auth_middleware.check_authorize
@permission_middleware.check_permission("delete_user")
def user_delete():
    req = request.get_json()
    res = user_service.user_delete(user_id=req['id'])
    return res
