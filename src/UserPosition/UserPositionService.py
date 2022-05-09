from . import UserPositionServiceDb
from src.User import UserServiceDb
from src.Position import PositionServiceDb
from src._response import response
from typing import List


# BIND USER POSITION
def bind_user_position(user_id: int, position_id: int) -> dict:
    if not UserServiceDb.get_by_id(user_id) or not PositionServiceDb.get_by_id(position_id):
        return response(False, {'msg': 'User and/or Position not found'}, 404)

    UserPositionServiceDb.bind_user_position(user_id=user_id, position_id=position_id)
    return response(True, {'msg': 'User Position successfully binding'}, 200)


# UNBIND USER POSITION
def unbind_user_position(user_id: int, position_id: int) -> dict:
    if not UserServiceDb.get_by_id(user_id) or not PositionServiceDb.get_by_id(position_id):
        return response(False, {'msg': 'User and/or Position not found'}, 404)

    UserPositionServiceDb.unbind_user_position(user_id, position_id)
    return response(True, {'msg': 'binding successfully deleted'}, 200)


# GET USER IDS BY POSITION ID
def get_users_by_position_id(position_id: int, page: int, per_page: int) -> dict:
    if not PositionServiceDb.get_by_id(position_id):
        return response(False, {'msg': 'Position not found'}, 404)

    users: dict = UserPositionServiceDb.get_users_by_position_id(
        position_id=position_id,
        page=page,
        per_page=per_page
    )
    return response(True, users, 200)
