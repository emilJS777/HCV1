from src._response import response
from src.models import UserRole, Role, User


# GET ROLE IDS BY USER ID
def get_role_ids_by_user_id(user_id):
    arr = []
    # GET USER ROLE BY USER ID
    user_roles = UserRole.query.filter_by(user_id=user_id).all()

    # AND ASSIGN ARR ROLE ID
    for user_role in user_roles:
        arr.append(user_role.role_id)

    return response(True, arr, 200)


# BIND USER ROLE
def bind_user_role(user_id, role_id):
    # VERIFY EXISTS USER AND ROLE BY THIS ID
    # IF NO RETURN NOT FOUND
    user = User.query.filter_by(id=user_id).first()
    role = Role.query.filter_by(id=role_id).first()
    if not user or not role:
        return response(False, {'msg': 'user and/or role by this id not found'}, 404)

    # CHECK IF THIS CONNECTION EXISTS
    # IF EXISTING RETURN CONFLICT
    user_role = UserRole.query.filter_by(user_id=user_id, role_id=role_id).first()
    if user_role:
        return response(False, {'msg': 'such a connection already exists'}, 409)

    # IF NOT EXISTING CREATE LINK AND SAVE
    new_bind_user_role = UserRole(user_id=user_id, role_id=role_id)
    new_bind_user_role.save_db()
    return response(True, {'msg': 'new link user role successfully created'}, 200)


# UNBIND USER ROLE
def unbind_user_role(user_id, role_id):
    # GET AND CHECK WHETHER THIS COMMUNICATION EXISTS
    # IF NO RETURN NOT FOUND
    user_role = UserRole.query.filter_by(user_id=user_id, role_id=role_id).first()
    if not user_role:
        return response(False, {'msg': 'this connection does not exist'}, 404)

    # IF EXIST DELETE FROM DB AND RESPONSE
    user_role.delete_db()
    return response(True, {'msg': 'user role link successfully deleted'}, 200)
