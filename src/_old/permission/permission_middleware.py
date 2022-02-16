from functools import wraps
from src._response import response
from src._old.permission import permission_service_db
from src.user_role import user_role_service_db
from src._old.role_permission import role_permission_service_db
from flask import g


# CHECK PERMISSION
def check_permission(allowed_permission):
    def decoration(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            # RUN AND GET ID RESOLUTION FROM ROLE
            for role_id in user_role_service_db.get_role_ids_by_user_id(user_id=g.user_id):

                # LOOSE ALL ROLES AND GET ID PERMISSION FROM THE ROLE
                for permission_id in role_permission_service_db.get_permission_ids_by_role_id(role_id=role_id):

                    # CHECK WHETHER THE PERMISSION IS INCLUDED WITH THIS PERMISSION BY NAME
                    if permission_service_db.get_by_id(permission_id=permission_id).name == allowed_permission:
                        return f(*args, **kwargs)

                # IF NO PERMISSION WAS FOUND FROM THE LIST,
                # SEE A MESSAGE ABOUT NOT PERMISSION AND INTERRUPT THE ROUTE
            return response(False, {'msg': 'you have no rights'}, 403)
        return decorated_function
    return decoration
