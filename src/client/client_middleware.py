from flask import g
from src._response import response
from functools import wraps
from . import client_service_db
from src.user import user_service_db


# CHECk CLIENT
# MIDDLEWARE FOR ASSIGNMENT g.client_id
def check_client(required: bool):
    def decoration(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            # GET CLIENT ID FROM G USER ID
            client_id: int = user_service_db.get_by_id(user_id=g.user_id).client_id

            # VERIFY IF CHECK CLIEnt ARG REQUIRED IS TRUE AND CLIENT ID NOT FOUND RETURN FORBIDDEN
            if required and not client_id or client_id and not client_service_db.get_by_id(client_id=client_id):
                return response(False, {'msg': 'client not found'}, 403)

            # ELSE ASSIGN G CLIENT ID OR ASSIGN NONE AND NEXT
            else:
                g.client_id = client_id or None

            return f(*args, **kwargs)

        return decorated_function
    return decoration
