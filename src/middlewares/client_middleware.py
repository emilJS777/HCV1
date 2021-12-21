from flask import g
from src._response import response
from functools import wraps
from src.models.client_model import Client
from src.models.user_model import User


# CHECk CLIENT
# MIDDLEWARE FOR ASSIGNMENT g.client_id
def check_client(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):

        # FIND CLIENT ID BY g.user_id
        # IF NOT CLIENT ID OR NOT CLIENT RETURN NOT FOUND
        client_id = User.query.filter_by(id=g.user_id).first().client_id
        if not client_id or not Client.query.filter_by(id=client_id).first():
            return response(False, {'msg': 'client not found'}, 404)

        # IF CLIENT ID FOUND g.client_id ASSIGN CLIENT ID
        g.client_id = client_id
        return f(*args, **kwargs)

    return decorated_function
