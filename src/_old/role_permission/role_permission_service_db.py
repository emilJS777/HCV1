from .role_permission_model import RolePermission


def create_bind(role_id, permission_id):
    # CREATE NEW ROLE PERMISSION LINK AND RETURN
    new_bind_role_permission = RolePermission(role_id=role_id, permission_id=permission_id)
    new_bind_role_permission.save_db()
    return new_bind_role_permission


def delete_bind(role_id, permission_id):
    # GET ROLE PERMISSION LINK AND DELETE
    role_permission = RolePermission.query.filter_by(role_id=role_id, permission_id=permission_id).first()
    role_permission.delete_db()
    return role_permission


def get_by_role_id_permission_id(role_id, permission_id):
    # GET AND RETURN ROLE_PERMISSION BY ROLE ID AND PERMISSION ID
    role_permission = RolePermission.query.filter_by(role_id=role_id, permission_id=permission_id).first()
    return role_permission


def delete_all_by_permission_id(permission_id):
    # GETS ALL CONNECTIONS WITH ROLE AND DELETE
    for role_permission in RolePermission.query.filter_by(permission_id=permission_id).all():
        role_permission.delete_db()


def delete_all_by_role_id(role_id):
    # GETS ALL CONNECTIONS WITH PERMISSION AND DELETE
    for role_permission in RolePermission.query.filter_by(role_id=role_id).all():
        role_permission.delete_db()


def get_permission_ids_by_role_id(role_id):
    arr = []
    # OVERRIDE AND INSERT PERMISSION ID INTO ARRAY
    for role_permission in RolePermission.query.filter_by(role_id=role_id).all():
        arr.append(role_permission.permission_id)
    return arr
