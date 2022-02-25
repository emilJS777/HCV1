from .user_permission_model import UserPermission


def create_bind(user_id, permission_id):
    # CREATE NEW USER PERMISSION LINK AND RETURN
    new_bind_user_permission = UserPermission(user_id=user_id, permission_id=permission_id)
    new_bind_user_permission.save_db()
    return new_bind_user_permission


def delete_bind(user_id, permission_id):
    # GET USER PERMISSION LINK AND DELETE
    user_permission = UserPermission.query.filter_by(user_id=user_id, permission_id=permission_id).first()
    user_permission.delete_db()
    return user_permission


def get_by_user_id_permission_id(user_id, permission_id):
    # GET AND RETURN ROLE_PERMISSION BY ROLE ID AND PERMISSION ID
    user_permission = UserPermission.query.filter_by(user_id=user_id, permission_id=permission_id).first()
    return user_permission


def delete_all_by_permission_id(permission_id):
    # GETS ALL CONNECTIONS WITH ROLE AND DELETE
    for user_permission in UserPermission.query.filter_by(permission_id=permission_id).all():
        user_permission.delete_db()


def delete_all_by_user_id(user_id):
    # GETS ALL CONNECTIONS WITH PERMISSION AND DELETE
    for user_permission in UserPermission.query.filter_by(user_id=user_id).all():
        user_permission.delete_db()


def get_permission_ids_by_user_id(user_id):
    arr = []
    # OVERRIDE AND INSERT PERMISSION ID INTO ARRAY
    for user_permission in UserPermission.query.filter_by(user_id=user_id).all():
        arr.append(user_permission.permission_id)
    return arr
