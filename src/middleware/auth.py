from flask import g, request
from src._response import response
from functools import wraps
from flask_jwt_extended import jwt_required, get_jwt_identity
from src.models import Auth


# CHECk AUTHORIZE BY TOKEN
def check_authorize(f):
    @wraps(f)
    @jwt_required()
    def decorated_function(*args, **kwargs):
        # FIND USER AUTH FROM DB & CHECK IS A ACCESS_TOKEN
        # IF TOKENS MATCH, ASSIGN g.user_id user_id
        user_auth = Auth.query.filter_by(user_id=get_jwt_identity()).first()
        if user_auth.access_token == request.headers['authorization'].split(' ')[1]:
            g.user_id = get_jwt_identity()
            return f(*args, **kwargs)

        # IF THEY DON`T MATCH SEND A RESPONSE INVALID TOKEN UNAUTHORIZED
        return response(False, {'msg': 'invalid token'}, 401)

    return decorated_function
