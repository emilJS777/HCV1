from src.models.user_role import UserRole


def create_bind(user_id, role_id):
    # CREATE NEW BIND USER_ROLE AND RETURN
    new_bind_user_role = UserRole(user_id=user_id, role_id=role_id)
    new_bind_user_role.save_db()
    return new_bind_user_role


def delete_bind(user_id, role_id):
    # GET USER ROLE LINK AND DELETE
    user_role = UserRole.query.filter_by(user_id=user_id, role_id=role_id).first()
    user_role.delete_db()
    return user_role


def get_by_user_id_role_id(user_id, role_id):
    # GET USER_ROLE BY USER ID ROLE ID AND RETURN
    user_role = UserRole.query.filter_by(user_id=user_id, role_id=role_id).first()
    return user_role


def get_role_ids_by_user_id(user_id):
    arr = []
    # GET AND RETURN ALL ROLE ID BY USER ID
    for user_role in UserRole.query.filter_by(user_id=user_id).all():
        arr.append(user_role.role_id)
    return arr


def delete_all_by_role_id(role_id):
    # GETS ALL CONNECTIONS WITH USERS AND REMOVE
    for user_role in UserRole.query.filter_by(role_id=role_id).all():
        user_role.delete_db()


def delete_all_by_user_id(user_id):
    # GEtS ALL CONNECTIONS WITH ROLES AND REMOVE
    for user_role in UserRole.query.filter_by(user_id=user_id).all():
        user_role.delete_db()
