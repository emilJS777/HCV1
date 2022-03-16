from . import user_position_service
from flask import request

from ..auth import auth_middleware
from ..client import client_middleware
from ..permission import permission_middleware


@auth_middleware.check_authorize
@client_middleware.check_client(required=False)
@permission_middleware.check_permission("user_edit")
def bind_user_position() -> dict:
    req: dict = request.get_json()
    res: dict = user_position_service.bind_user_position(user_id=req['user_id'], position_id=req['position_id'])
    return res


@auth_middleware.check_authorize
@client_middleware.check_client(required=False)
@permission_middleware.check_permission("user_edit")
def unbind_user_position() -> dict:
    req: dict = request.get_json()
    res: dict = user_position_service.unbind_user_position(user_id=req['user_id'], position_id=req['position_id'])
    return res


@auth_middleware.check_authorize
@client_middleware.check_client(required=False)
@permission_middleware.check_permission("user_get")
def get_user_ids_by_position_id(position_id: int) -> dict:
    res: dict = user_position_service.get_user_ids_by_position_id(position_id=position_id)
    return res
