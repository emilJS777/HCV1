from src.services_db import user_db, user_role_db
from src._response import response
from flask import g


# CREATE NEW USER
def user_create(user_name, password):
    # IF FIND THIS USER NAME RETURN RESPONSE CONFLICT
    if user_db.get_by_name(name=user_name):
        return response(False, {'msg': 'user name is taken'}, 409)

    # ELSE USER BY THIS NAME SAVE
    new_user = user_db.create(name=user_name, password=password, creator_id=g.user_id)
    return response(True, {'msg': 'new user by id {} successfully created'.format(new_user.id)}, 200)


# USER GET BY ID
def user_get_by_id(user_id):
    # GET USER BY ID END VERIFY USER DOES IT EXIST. IF NO RETURN NOT FOUND
    user = user_db.get_by_id_creator_id(user_id=user_id, creator_id=g.user_id)
    if not user:
        return response(False, {'msg': 'user by this id not found'}, 404)

    # ELSE RETURN THIS USER AND STATUS OK
    return response(True, {'name': user.name}, 200)


# GET ALL USER
def user_get_all():
    # GET AND RETURN USERS BY CREATOR ID
    users = user_db.get_all_by_creator_id(creator_id=g.user_id)
    return response(True, users, 200)


# UPDATE USER
def user_update(user_id, user_name):
    # GET USER BY ID AND VERIFY DOES IT EXIST. IF NO RETURN NOT FOUND
    user = user_db.get_by_id_creator_id(user_id=user_id, creator_id=g.user_id)
    if not user:
        return response(False, {'msg': 'user by this id not found'}, 404)

    # IF USER BY ThiS NAME FOUND RETURN CONFLICT
    if user_db.get_by_name(name=user_name):
        return response(False, {'msg': 'user name is taken'}, 409)

    # ELSE CHANGE AND UPDATE DB AND RETURN RESPONSE OK
    user_db.update(user_id=user_id, creator_id=g.user_id, user_name=user_name)
    return response(True, {'msg': 'user successfully update'}, 200)


# DELETE USER BY ID
def user_delete(user_id):
    # GET USER BY ID AND VERIFY DIES EXIST IF NO RETURN NOT FOUND
    if not user_db.get_by_id_creator_id(user_id=user_id, creator_id=g.user_id):
        return response(False, {"msg": "user by this id not found"}, 404)

    # GETS ALL CONNECTIONS WITH ROLE AND REMOVE
    user_role_db.delete_all_by_user_id(user_id=user_id)

    # REMOVE THIS USER FROM DB
    user_db.delete(user_id=user_id, creator_id=g.user_id)
    return response(True, {'msg': "this user successfully deleted"}, 200)
