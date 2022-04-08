from functools import wraps
from src._response import response
from . import PermissionServiceDb
from .PermissionServiceDb import Permission
from src.UserPermission import UserPermissionServiceDb
from flask import g, request


# CHECK PERMISSION
def check_permission(allowed_permission: str):
    def decoration(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            # GET PERMISSIONS BY USER ID AND VERIFY
            permission: Permission = PermissionServiceDb.get_by_name(permission_name=allowed_permission)

            user_permission = UserPermissionServiceDb.get_by_user_id_permission_id_firm_id(
                user_id=g.user_id,
                permission_id=permission.id,
                firm_id=request.args.get('firm_id') or request.get_json()['firm_id'] if permission.firm else None

            )
            
            if not user_permission:
                return response(False, {'msg': 'you have no rights'}, 403)

                # IF NO PERMISSION WAS FOUND FROM THE LIST,
                # SEE A MESSAGE ABOUT NOT PERMISSION AND INTERRUPT THE ROUTE
            return f(*args, **kwargs)
        return decorated_function
    return decoration
