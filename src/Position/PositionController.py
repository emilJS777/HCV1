from . import PositionService
from flask import request
from src.Auth import AuthMiddleware
from src.Permission import PermissionMiddleware
from src.Client import ClientMiddleware


@AuthMiddleware.check_authorize
@ClientMiddleware.check_client(required=True)
@PermissionMiddleware.check_permission("user_edit")
def create() -> dict:
    req: dict = request.get_json()
    res: dict = PositionService.create(title=req['title'])
    return res


@AuthMiddleware.check_authorize
@ClientMiddleware.check_client(required=True)
@PermissionMiddleware.check_permission("user_edit")
def update(position_id: int) -> dict:
    req: dict = request.get_json()
    res: dict = PositionService.update(position_id=position_id, title=req['title'])
    return res


@AuthMiddleware.check_authorize
@ClientMiddleware.check_client(required=True)
@PermissionMiddleware.check_permission("user_edit")
def delete(position_id: int) -> dict:
    res: dict = PositionService.delete(position_id)
    return res


@AuthMiddleware.check_authorize
@ClientMiddleware.check_client(required=True)
def get_by_id(position_id: int) -> dict:
    res: dict = PositionService.get_by_id(position_id)
    return res


@AuthMiddleware.check_authorize
@ClientMiddleware.check_client(required=True)
def get_all() -> dict:
    res: dict = PositionService.get_all(
        page=int(request.args.get('page')),
        per_page=int(request.args.get('per_page'))
    )
    return res
