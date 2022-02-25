from src.user import user_service_db
from src.permission import permission_service_db
from . import user_permission_service_db
from src._response import response
from flask import g


# GET PERMISSION IDS BY USER ID
def get_permission_ids_by_user_id(user_id):
    # IF NOT USER BY ID RETURN NOT FOUND
    if not user_service_db.get_by_id(user_id=user_id):
        return response(False, {'msg': 'user not found'}, 404)

    # GET PERMISSION IDS BY USER ID
    permission_ids = user_permission_service_db.get_permission_ids_by_user_id(user_id=user_id)
    return response(True, permission_ids, 200)


# BIND USER PERMISSION
def bind_user_permission(user_id, permission_id):
    # VERIFY IF REQUESTER ID EXIST THIS PERMISSION NOT FOUND RETURN FORBIDDEN
    if not user_permission_service_db.get_by_user_id_permission_id(user_id=g.user_id, permission_id=permission_id):
        return response(False, {'msg': 'forbidden'}, 403)

    # IF USER OR PERMISSION NOT FIND RETURN 404 NOT FOUND
    if not user_service_db.get_by_id(user_id=user_id) or not permission_service_db.get_by_id(permission_id=permission_id):
        return response(False, {'msg': 'user or permission not found'}, 404)

    # GET BY USER ID AND PERMISSION ID, IF EXIST RETURN CONFLICT
    if user_permission_service_db.get_by_user_id_permission_id(user_id=user_id, permission_id=permission_id):
        return response(False, {'msg': 'bind exist'}, 409)

    # CREATE BIND AND RETURN OK
    user_permission_service_db.create_bind(user_id=user_id, permission_id=permission_id)
    return response(False, {'msg': 'binding done'}, 200)


# UNBIND USER PERMISSION
def unbind_user_permission(user_id, permission_id):
    # CHECK WHETHER THE USER HAS SUCH ROLE IF NO ISSUE
    if not user_service_db.get_by_id(user_id=user_id):
        return response(False, {'msg': 'user not found'}, 404)

    # VERIFY IF REQUESTER ID EXIST THIS PERMISSION NOT FOUND RETURN FORBIDDEN
    if not user_permission_service_db.get_by_user_id_permission_id(user_id=g.user_id, permission_id=permission_id):
        return response(False, {'msg': 'forbidden'}, 403)

    # GET AND CHECK WHETHER THIS COMMUNICATION EXISTS. IF NO RETURN NOT FOUND
    if not user_permission_service_db.get_by_user_id_permission_id(user_id, permission_id):
        return response(False, {'msg': 'this link not found'}, 404)

    # IF EXIST DELETE FROM DB AND RESPONSE
    user_permission_service_db.delete_bind(user_id=user_id, permission_id=permission_id)
    return response(True, {'msg': 'user permission link successfully deleted'}, 200)
