from . import AuthService, AuthMiddleware
from flask import request, g
from flask_jwt_extended import jwt_required


def login():
    req = request.get_json()
    res = AuthService.login(user_name=req['user_name'], password=req['password'])
    return res


@AuthMiddleware.check_authorize
def get_profile() -> dict:
    res = AuthService.get_profile(g.user_id)
    return res


@jwt_required(refresh=True)
def refresh_token():
    res = AuthService.refresh_token()
    return res
