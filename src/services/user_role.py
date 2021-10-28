from src.services_db import user_db, user_role_db, role_db
from src._response import response
from flask import g


# GET ROLE IDS BY USER ID
def get_role_ids_by_user_id(user_id):
    # IF USER NOT FOUND RETURN RESPONSE 404 CODE
    if not user_db.get_by_id_creator_id(user_id=user_id, creator_id=g.user_id):
        return response(False, {'msg': 'user not found'}, 404)

    # GET USER ROLE BY USER ID
    role_ids = user_role_db.get_role_ids_by_user_id(user_id=user_id)
    return response(True, role_ids, 200)


# BIND USER ROLE
def bind_user_role(user_id, role_id):
    # VERIFY EXISTS USER AND ROLE BY THIS ID. IF NO RETURN NOT FOUND
    user = user_db.get_by_id_creator_id(user_id=user_id, creator_id=g.user_id)
    role = role_db.get_by_id_creator_id(role_id=role_id, creator_id=g.user_id)
    if not user or not role:
        return response(False, {'msg': 'user and/or role by this id not found'}, 404)

    # CHECK IF THIS CONNECTION EXISTS. IF EXISTING RETURN CONFLICT
    if user_role_db.get_by_user_id_role_id(user_id=user_id, role_id=role_id):
        return response(False, {'msg': 'such a connection already exists'}, 409)

    # IF NOT EXISTING CREATE LINK AND SAVE
    user_role_db.create_bind(user_id=user_id, role_id=role_id)
    return response(True, {'msg': 'new link user role successfully created'}, 200)


# UNBIND USER ROLE
def unbind_user_role(user_id, role_id):
    # IF USER Not FOUND RETURN 404 CODE
    if not user_db.get_by_id_creator_id(user_id=user_id, creator_id=g.user_id):
        return response(False, {'msg': "user not found"}, 404)

    # GET AND CHECK WHETHER THIS COMMUNICATION EXISTS. IF NO RETURN NOT FOUND
    if not user_role_db.get_by_user_id_role_id(user_id=user_id, role_id=role_id):
        return response(False, {'msg': 'this connection does not exist'}, 404)

    # IF EXIST DELETE FROM DB AND RESPONSE
    user_role_db.delete_bind(user_id=user_id, role_id=role_id)
    return response(True, {'msg': 'user role link successfully deleted'}, 200)
