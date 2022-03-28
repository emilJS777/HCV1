from . import user_firm_service
from flask import request
from ..auth import auth_middleware
from ..client import client_middleware
from ..permission import permission_middleware


# CREATE BIND
@auth_middleware.check_authorize
@permission_middleware.check_permission("user_edit")
@permission_middleware.check_permission("firm_edit")
@client_middleware.check_client(required=False)
def create_bind() -> dict:
    req: dict = request.get_json()
    res: dict = user_firm_service.create_bind(
        user_id=req['user_id'],
        firm_id=req['firm_id']
    )
    return res


# DELETE BIND
@auth_middleware.check_authorize
@permission_middleware.check_permission("user_edit")
@permission_middleware.check_permission("firm_edit")
@client_middleware.check_client(required=False)
def delete_bind() -> dict:
    req: dict = request.get_json()
    res: dict = user_firm_service.delete_bind(
        user_id=req['user_id'],
        firm_id=req['firm_id']
    )
    return res


# GET FIRM IDS BY USER ID
@auth_middleware.check_authorize
@permission_middleware.check_permission("user_get")
@permission_middleware.check_permission("firm_get")
@client_middleware.check_client(required=False)
def get_firm_ids_by_user_id(user_id: int) -> dict:
    res: dict = user_firm_service.get_firm_ids_by_user_id(user_id)
    return res
