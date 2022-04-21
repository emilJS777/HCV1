from src.User import UserServiceDb
from . import AuthServiceDb
from flask_bcrypt import check_password_hash
from flask import request
from src._response import response
from flask_jwt_extended import get_jwt_identity


def login(user_name, password):
    # FIND THE USER BY NAME AND CHECK IF THE PASSWORD
    # IS INCORRECT OR THE USER IS NOT FOUND
    # RETURN RESPONSE UNAUTHORIZED
    user = UserServiceDb.get_by_name(name=user_name)
    if not user or not check_password_hash(user.password_hash, password):
        return response(False, {'msg': 'invalid User name and/or password'}, 401)

    # UPDATE AUTH PAIR TOKENS AND RETURN
    new_auth = AuthServiceDb.update_pair_tokens(user_id=user.id)
    return response(True, {'access_token': new_auth.access_token, "refresh_token": new_auth.refresh_token}, 200)


def get_profile(user_id: int) -> dict:
    # GET AUTH PROFILE AND RETURN OK
    user: UserServiceDb.User = UserServiceDb.get_by_id(user_id)
    return response(True, {'id': user.id, 'name': user.name, 'full_name': user.full_name, 'position_id': user.position_id}, 200)


def refresh_token():
    # GET AUTH BY USER ID AND CHECK
    # FOR COMPLIANCE WITH THE REFRESH TOKEN
    auth = AuthServiceDb.get_by_user_id(user_id=get_jwt_identity())
    if auth.refresh_token == request.headers['authorization'].split(' ')[1]:

        # UPON MATCHING, A NEW PAIR OF TOKENS IS GENERATED AND RESPOND
        new_auth = AuthServiceDb.update_pair_tokens(user_id=get_jwt_identity())
        return response(True, {'access_token': new_auth.access_token, 'refresh_token': new_auth.refresh_token}, 200)

    # IF DO NOT MATCH RETURN WITHOUT SUCCESS
    return response(False, {'msg': 'invalid refresh token'}, 401)
