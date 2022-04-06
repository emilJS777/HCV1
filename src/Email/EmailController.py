from . import EmailService, EmailValidator
from flask import request
from src.Auth import AuthMiddleware
from flask_expects_json import expects_json


# CREATE EMAIL
@AuthMiddleware.check_authorize
@expects_json(EmailValidator.email_schema)
def email_create():
    req = request.get_json()
    res = EmailService.email_create(address=req['address'])
    return res


# UPDATE EMAIL
@AuthMiddleware.check_authorize
@expects_json(EmailValidator.email_schema)
def email_update():
    req = request.get_json()
    res = EmailService.email_update(address=req['address'])
    return res


# DELETE EMAIL
@AuthMiddleware.check_authorize
def email_delete():
    res = EmailService.email_delete()
    return res


# GET BY USER ID EMAIL
@AuthMiddleware.check_authorize
def email_get_by_user_id():
    user_id = request.args['user_id']
    res = EmailService.email_get_by_user_id(user_id=user_id)
    return res
