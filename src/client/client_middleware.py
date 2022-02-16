from flask import g
from src._response import response
from functools import wraps
from . import client_service_db
from src.user import user_service_db


# CHECk CLIENT
# MIDDLEWARE FOR ASSIGNMENT g.client_id
def check_client(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        # FIND CLIENT ID BY g.user_id
        # IF NOT CLIENT ID OR NOT CLIENT RETURN NOT FOUND
        user = user_service_db.get_by_id(user_id=g.user_id)
        if not user or not client_service_db.get_by_id(client_id=user.client_id):
            return response(False, {'msg': 'client not found'}, 404)

        # IF CLIENT ID FOUND g.client_id ASSIGN CLIENT ID
        g.client_id = user.client_id
        return f(*args, **kwargs)

    return decorated_function
