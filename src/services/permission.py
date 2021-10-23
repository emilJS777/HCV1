from src.models import Permission, RolePermission, UserRole
from src._response import response
from flask import g


# CREATE NEW PERMISSION SERVICE
def permission_create(permission_name):
    # IF FIND THIS PERMISSION NAME RETURN RESPONSE CONFLICT
    if Permission.query.filter_by(name=permission_name).first():
        return response(False, {'msg': 'permission name is taken'}, 409)

    # ELSE PERMISSION BY THIS NAME SAVE
    new_permission = Permission(name=permission_name)
    new_permission.save_db()
    return response(True, {'msg': 'new permission successfully created'}, 200)


# GET PERMISSION BY ID
def permission_get_by_id(permission_id):
    # GET PERMISSION BY ID END VERIFY DOES IT EXIST
    # IF NO RETURN NOT FOUND
    permission = Permission.query.filter_by(id=permission_id).first()
    if not permission:
        return response(False, {'msg': 'permission by this id not found'}, 404)

    # ELSE RETURN THIS PERMISSION AND STATUS OK
    return response(True, {'name': permission.name}, 200)


# GET ALL PERMISSION
def permission_get_all():
    arr = []

    # GET ALL ROLES OF THIS USER
    user_roles = UserRole.query.filter_by(user_id=g.user_id).all()

    # GET ALL PERMISSIONS
    for user_role in user_roles:
        role_permissions = RolePermission.query.filter_by(role_id=user_role.role_id).all()

        # OVERRIDE AND INSERT PERMISSION ID INTO ARRAY
        for role_permission in role_permissions:
            arr.append(role_permission.permission_id)

    return response(True, arr, 200)


# UPDATE PERMISSION
def permission_update(permission_id, permission_name):
    # GET PERMISSION BY ID AND VERIFY DOES IT EXIST
    # IF NO RETURN NOT FOUND
    permission = Permission.query.filter_by(id=permission_id).first()
    if not permission:
        return response(False, {'msg': 'permission by this id not found'}, 404)

    # ELSE CHANGE AND UPDATE DB
    # AND RETURN RESPONSE OK
    permission.name = permission_name
    permission.update_db()
    return response(True, {'msg': 'permission successfully update'}, 200)


# DELETE PERMISSION BY ID
def permission_delete(permission_id):
    # GET PERMISSION BY ID AND VERIFY DIES EXIST
    # IF NO RETURN NOT FOUND
    permission = Permission.query.filter_by(id=permission_id).first()
    if not permission:
        return response(False, {"msg": "permission by this id not found"}, 404)

    # GETS ALL CONNECTIONS WITH ROLES AND REMOVE
    role_permissions = RolePermission.query.filter_by(permission_id=permission_id).all()
    for role_permission in role_permissions:
        role_permission.delete_db()

    # ELSE REMOVE THIS PERMISSION FROM DB
    permission.delete_db()
    return response(True, {'msg': "this permission successfully deleted"}, 200)

