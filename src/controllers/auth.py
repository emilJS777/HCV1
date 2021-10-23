from src.services import auth
from flask import request
from flask_jwt_extended import jwt_required


def login():
    req = request.get_json()
    res = auth.login(user_name=req['user_name'], password=req['password'])
    return res


@jwt_required(refresh=True)
def refresh_token():
    res = auth.refresh_token()
    return res
