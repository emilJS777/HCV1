from src._response import response
from src.models import RolePermission, Role, Permission, UserRole
from flask import g


# GET PERMISSION IDS BY ROLE ID
def get_permission_ids_by_role_id(role_id):
    arr = []
    # GET ROLE PERMISSION BY ROLE ID
    role_permissions = RolePermission.query.filter_by(role_id=role_id).all()

    # AND ASSIGN ARR PERMISSION ID
    for role_permission in role_permissions:
        arr.append(role_permission.permission_id)

    return response(True, arr, 200)


# BIND ROLE PERMISSION
def bind_role_permission(role_id, permission_id):
    # CHECK THE USER HAS THE PERMISSION
    # THAT WANTS TO ASSOCIATE THE ROLE
    user_roles = UserRole.query.filter_by(user_id=g.user_id).all()
    for user_role in user_roles:
        role_permissions = RolePermission.query.filter_by(role_id=user_role.role_id).all()

        for role_permission in role_permissions:
            if role_permission.permission_id == permission_id:
                # VERIFY EXISTS PERMISSION AND ROLE BY THIS ID
                # IF NO RETURN NOT FOUND
                role = Role.query.filter_by(id=role_id).first()
                permission = Permission.query.filter_by(id=permission_id).first()
                if not role or not permission:
                    return response(False, {'msg': 'role and/or permission by this id not found'}, 404)

                # CHECK IF THIS CONNECTION EXISTS
                # IF EXISTING RETURN CONFLICT
                role_permission = RolePermission.query.filter_by(role_id=role_id,
                                                                 permission_id=permission_id).first()
                if role_permission:
                    return response(False, {'msg': 'such a connection already exists'}, 409)

                # IF NOT EXISTING CREATE LINK AND SAVE
                new_bind_role_permission = RolePermission(role_id=role_id, permission_id=permission_id)
                new_bind_role_permission.save_db()
                return response(True, {'msg': 'new link role permission successfully created'}, 200)

    # IF THE USER DOESN'T HAVE SUCH PERMISSION RETURN ANSWER
    return response(False, {'msg': 'you do not have such permission'}, 403)


# UNBIND ROLE PERMISSION
def unbind_role_permission(role_id, permission_id):
    # GET AND CHECK WHETHER THIS COMMUNICATION EXISTS
    # IF NO RETURN NOT FOUND
    role_permission = RolePermission.query.filter_by(role_id=role_id, permission_id=permission_id).first()
    if not role_permission:
        return response(False, {'msg': 'this connection does not exist'}, 404)

    # IF EXIST DELETE FROM DB AND RESPONSE
    role_permission.delete_db()
    return response(True, {'msg': 'role permission link successfully deleted'}, 200)
