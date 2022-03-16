from . import position_service
from flask import request
from src.auth import auth_middleware
from src.permission import permission_middleware


@auth_middleware.check_authorize
@permission_middleware.check_permission("position_edit")
def create() -> dict:
    req: dict = request.get_json()
    res: dict = position_service.create(title=req['title'])
    return res


@auth_middleware.check_authorize
@permission_middleware.check_permission("position_edit")
def update(position_id: int) -> dict:
    req: dict = request.get_json()
    res: dict = position_service.update(position_id=position_id, title=req['title'])
    return res


@auth_middleware.check_authorize
@permission_middleware.check_permission("position_edit")
def delete(position_id: int) -> dict:
    res: dict = position_service.delete(position_id)
    return res


def get_by_id(position_id: int) -> dict:
    res: dict = position_service.get_by_id(position_id)
    return res


def get_all_ids() -> dict:
    res: dict = position_service.get_all_ids()
    return res
