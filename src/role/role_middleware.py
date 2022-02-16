from functools import wraps
from src._response import response
from src.user_role import user_role_service_db
from . import role_service_db
from flask import g


# CHECK ROLES
def check_roles(allowed_roles):
    def decoration(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            # RUN AND GET ID RESOLUTION FROM ROLE
            for role_id in user_role_service_db.get_role_ids_by_user_id(user_id=g.user_id):

                # GET ROLE BY ID AND VERIFY NAME IN ALLOWED ROLES
                role = role_service_db.get_by_id(role_id=role_id)
                if role.name in allowed_roles:
                    return f(*args, **kwargs)

                # IF NO PERMISSION WAS FOUND FROM THE LIST,
                # SEE A MESSAGE ABOUT NOT PERMISSION AND INTERRUPT THE ROUTE
            return response(False, {'msg': 'you have no rights'}, 403)
        return decorated_function
    return decoration
