from src.services_db import role_service_db, role_permission_service_db, user_role_service_db
from src._response import response
from flask import g


# CREATE NEW ROLE
def role_create(role_name):
    # IF FIND THIS ROLE NAME RETURN RESPONSE CONFLICT
    if role_service_db.get_by_name_creator_id(name=role_name, creator_id=g.user_id):
        return response(False, {'msg': 'role name is taken'}, 409)

    # ELSE ROLE BY THIS NAME SAVE
    role_service_db.create(name=role_name, creator_id=g.user_id)
    return response(True, {'msg': 'new role successfully created'}, 200)


# ROLE GET BY ID
def role_get_by_id(role_id):
    # GET ROLE BY ID END VERIFY DOES IT EXIST. IF NO RETURN NOT FOUND
    role = role_service_db.get_by_id_creator_id(role_id=role_id, creator_id=g.user_id)
    if not role:
        return response(False, {'msg': 'role by this id not found'}, 404)

    # ELSE RETURN THIS ROLE AND STATUS OK
    return response(True, {'name': role.name}, 200)


# GET ALL ROLE
def role_get_all():
    # GET ALL ROLES BY CREATOR ID ASSIGN id: name:
    roles = role_service_db.get_all_by_creator_id(creator_id=g.user_id)
    return response(True, roles, 200)


# UPDATE ROLE
def role_update(role_id, role_name):
    # GET ROLE BY ID AND VERIFY DOES IT EXIST. IF NO RETURN NOT FOUND
    if not role_service_db.get_by_id_creator_id(role_id=role_id, creator_id=g.user_id):
        return response(False, {'msg': 'role by this id not found'}, 404)

    # IF FIND THIS ROLE NAME RETURN RESPONSE CONFLICT
    if role_service_db.get_by_name_creator_id(name=role_name, creator_id=g.user_id):
        return response(False, {'msg': 'role name is taken'}, 409)

    # ELSE CHANGE AND UPDATE DB. AND RETURN RESPONSE OK
    role_service_db.update(role_id=role_id, creator_id=g.user_id, name=role_name)
    return response(True, {'msg': 'role successfully update'}, 200)


# DELETE ROLE BY ID
def role_delete(role_id):
    # GET ROLE BY ID AND VERIFY DIES EXIST IF NO RETURN NOT FOUND
    if not role_service_db.get_by_id_creator_id(role_id=role_id, creator_id=g.user_id):
        return response(False, {"msg": "role by this id not found"}, 404)

    # GETS ALL CONNECTIONS WITH PERMISSIONS AND REMOVE
    role_permission_service_db.delete_all_by_role_id(role_id=role_id)

    # GETS ALL CONNECTIONS WITH USERS AND REMOVE
    user_role_service_db.delete_all_by_role_id(role_id=role_id)

    # REMOVE THIS ROLE FROM DB
    role_service_db.delete(role_id=role_id)
    return response(True, {'msg': "this role successfully deleted"}, 200)

