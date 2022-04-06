from . import AuthService
from flask import request
from flask_jwt_extended import jwt_required


def login():
    req = request.get_json()
    res = AuthService.login(user_name=req['user_name'], password=req['password'])
    return res


@jwt_required(refresh=True)
def refresh_token():
    res = AuthService.refresh_token()
    return res
