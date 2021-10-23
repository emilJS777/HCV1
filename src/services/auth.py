from src.models import User, Auth
from flask_bcrypt import check_password_hash
from flask import request
from src._response import response
from flask_jwt_extended import get_jwt_identity


def login(user_name, password):
    # FIND THE USER BY NAME AND CHECK IF THE PASSWORD
    # IS INCORRECT OR THE USER IS NOT FOUND
    # RETURN RESPONSE UNAUTHORIZED
    user = User.query.filter_by(name=user_name).first()
    if not user or not check_password_hash(user.password_hash, password):
        return response(False, {'msg': 'invalid user name and/or password'}, 401)

    # IF EVERYTHING MATCHES, GET AUTHORIZATION BY USER ID
    # OR CREATE A NEW TOKEN PAIR AND ISSUED IN ANSWER
    new_auth = Auth.query.filter_by(user_id=user.id).first() or Auth(user_id=user.id)
    new_auth.generate_access_token()
    new_auth.generate_refresh_token()
    new_auth.update_db() or new_auth.save_db()

    return response(True, {'access_token': new_auth.access_token,
                           "refresh_token": new_auth.refresh_token}, 200)


# REFRESH TOKEN
def refresh_token():
    # GET AUTH BY USER ID AND CHECK
    # FOR COMPLIANCE WITH THE REFRESH TOKEN
    auth = Auth.query.filter_by(user_id=get_jwt_identity()).first()
    if auth.refresh_token == request.headers['authorization'].split(' ')[1]:

        # UPON MATCHING, A NEW PAIR OF TOKENS IS GENERATED AND RESPOND
        auth.generate_access_token()
        auth.generate_refresh_token()
        auth.update_db()
        return response(True, {'access_token': auth.access_token, 'refresh_token': auth.refresh_token}, 200)

    # IF DO NOT MATCH RETURN WITHOUT SUCCESS
    return response(False, {'msg': 'invalid refresh token'}, 401)
