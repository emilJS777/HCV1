from . import UserPositionService
from flask import request

from ..Auth import AuthMiddleware
from ..Client import ClientMiddleware
from ..Permission import PermissionMiddleware


@AuthMiddleware.check_authorize
@ClientMiddleware.check_client(required=True)
@PermissionMiddleware.check_permission("user_edit")
def bind_user_position() -> dict:
    req: dict = request.get_json()
    res: dict = UserPositionService.bind_user_position(user_id=req['user_id'], position_id=req['position_id'])
    return res


@AuthMiddleware.check_authorize
@ClientMiddleware.check_client(required=True)
@PermissionMiddleware.check_permission("user_edit")
def unbind_user_position() -> dict:
    req: dict = request.get_json()
    res: dict = UserPositionService.unbind_user_position(user_id=req['user_id'], position_id=req['position_id'])
    return res


@AuthMiddleware.check_authorize
@ClientMiddleware.check_client(required=True)
@PermissionMiddleware.check_permission("user_get")
def get_user_ids_by_position_id(position_id: int) -> dict:
    res: dict = UserPositionService.get_user_ids_by_position_id(position_id=position_id)
    return res
