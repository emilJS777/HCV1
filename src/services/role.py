from src.models import Role, RolePermission, UserRole
from src._response import response
from flask import g


# CREATE NEW ROLE
def role_create(role_name):
    # IF FIND THIS ROLE NAME RETURN RESPONSE CONFLICT
    if Role.query.filter_by(name=role_name).first():
        return response(False, {'msg': 'role name is taken'}, 409)

    # ELSE ROLE BY THIS NAME SAVE
    new_role = Role(name=role_name, creator_id=g.user_id)
    new_role.save_db()
    return response(True, {'msg': 'new role successfully created'}, 200)


# ROLE GET BY ID
def role_get_by_id(role_id):
    # GET ROLE BY ID END VERIFY DOES IT EXIST
    # IF NO RETURN NOT FOUND
    role = Role.query.filter_by(id=role_id).first()
    if not role:
        return response(False, {'msg': 'role by this id not found'}, 404)

    # ELSE RETURN THIS ROLE AND STATUS OK
    return response(True, {'name': role.name}, 200)


# GET ALL ROLE
def role_get_all():
    arr = []
    # GET ALL ROLE
    roles = Role.query.all()

    # ITERATE OVER ONE AT A TIME AND INSERT THE ROLE OBJECT INTO THE ARRAY
    for role in roles:
        arr.append({'id': role.id, 'name': role.name})
    return response(True, arr, 200)


# UPDATE ROLE
def role_update(role_id, role_name):
    # GET ROLE BY ID AND VERIFY DOES IT EXIST
    # IF NO RETURN NOT FOUND
    role = Role.query.filter_by(id=role_id).first()
    if not role:
        return response(False, {'msg': 'role by this id not found'}, 404)

    # ELSE CHANGE AND UPDATE DB
    # AND RETURN RESPONSE OK
    role.name = role_name
    role.update_db()
    return response(True, {'msg': 'role successfully update'}, 200)


# DELETE ROLE BY ID
def role_delete(role_id):
    # GET ROLE BY ID AND VERIFY DIES EXIST
    # IF NO RETURN NOT FOUND
    role = Role.query.filter_by(id=role_id).first()
    if not role:
        return response(False, {"msg": "role by this id not found"}, 404)

    # GETS ALL CONNECTIONS WITH PERMISSIONS AND REMOVE
    role_permissions = RolePermission.query.filter_by(role_id=role_id).all()
    for role_permission in role_permissions:
        role_permission.delete_db()

    # GETS ALL CONNECTIONS WITH USERS AND REMOVE
    user_roles = UserRole.query.filter_by(role_id=role_id).all()
    for user_role in user_roles:
        user_role.delete_db()

    # ELSE REMOVE THIS ROLE FROM DB
    role.delete_db()
    return response(True, {'msg': "this role successfully deleted"}, 200)

