from functools import wraps
from src._response import response
from . import permission_service_db
from .permission_service_db import Permission
from src.user_permission import user_permission_service_db
from flask import g


# CHECK PERMISSION
def check_permission(allowed_permission: str):
    def decoration(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            # GET PERMISSIONS BY USER ID AND VERIFY
            permission: Permission = permission_service_db.get_by_name(permission_name=allowed_permission)
            if not user_permission_service_db.get_by_user_id_permission_id(user_id=g.user_id,
                                                                           permission_id=permission.id):
                return response(False, {'msg': 'you have no rights'}, 403)

                # IF NO PERMISSION WAS FOUND FROM THE LIST,
                # SEE A MESSAGE ABOUT NOT PERMISSION AND INTERRUPT THE ROUTE
            return f(*args, **kwargs)
        return decorated_function
    return decoration
