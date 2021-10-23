from functools import wraps
from src._response import response
from src.models import Permission, UserRole, RolePermission
from flask import g


# CHECK PERMISSION
def check_permission(allowed_permission):
    def decoration(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            # GET ID OF ALL ROLE WHICH THE USER HAS
            user_roles = UserRole.query.filter_by(user_id=g.user_id).all()

            # RUN AND GET ID RESOLUTION FROM ROLE
            for user_role in user_roles:
                role_permissions = RolePermission.query.filter_by(role_id=user_role.role_id).all()

                # LOOSE ALL ROLES AND GET ID PERMISSION FROM THE ROLE
                for role_permission in role_permissions:
                    permission = Permission.query.filter_by(id=role_permission.permission_id).first()

                    # CHECK WHETHER THE PERMISSION IS INCLUDED WITH THIS PERMISSION BY NAME
                    if permission.name == allowed_permission:
                        return f(*args, **kwargs)

                # IF NO PERMISSION WAS FOUND FROM THE LIST,
                # SEE A MESSAGE ABOUT NOT PERMISSION AND INTERRUPT THE ROUTE
            return response(False, {'msg': 'you have no rights'}, 403)
        return decorated_function
    return decoration
