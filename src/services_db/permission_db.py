from src.models.permission import Permission


def create(permission_name):
    # CREATE NEW PERMISSION BY NAME AND RETURN
    permission = Permission(name=permission_name)
    permission.save_db()
    return permission


def update(permission_id, permission_name):
    # GET PERMISSION BY ID AND UPDATE NAME AND RETURN
    permission = Permission.query.filter_by(id=permission_id).first()
    permission.name = permission_name
    permission.update_db()
    return permission


def get_by_name(permission_name):
    # GET AND RETURN PERMISSION BY NAME
    permission = Permission.query.filter_by(name=permission_name).first()
    return permission


def get_by_id(permission_id):
    # GET PERMISSION BY ID AND RETURN
    permission = Permission.query.filter_by(id=permission_id).first()
    return permission


def delete(permission_id):
    # GET PERMISSION BY ID AND DELETE
    permission = Permission.query.filter_by(id=permission_id).first()
    permission.delete_db()
    return permission
