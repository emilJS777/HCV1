from . import user_position_service_db
from src.user import user_service_db
from src.position import position_service_db
from src._response import response
from typing import List


# BIND USER POSITION
def bind_user_position(user_id: int, position_id: int) -> dict:
    if not user_service_db.get_by_id(user_id) or not position_service_db.get_by_id(position_id):
        return response(False, {'msg': 'user and/or position not found'}, 404)

    user_position_service_db.bind_user_position(user_id=user_id, position_id=position_id)
    return response(True, {'msg': 'user position successfully binding'}, 200)


# UNBIND USER POSITION
def unbind_user_position(user_id: int, position_id: int) -> dict:
    if not user_service_db.get_by_id(user_id) or not position_service_db.get_by_id(position_id):
        return response(False, {'msg': 'user and/or position not found'}, 404)

    user_position_service_db.unbind_user_position(user_id, position_id)
    return response(True, {'msg': 'binding successfully deleted'}, 200)


# GET USER IDS BY POSITION ID
def get_user_ids_by_position_id(position_id: int) -> dict:
    if not position_service_db.get_by_id(position_id):
        return response(False, {'msg': 'position not found'}, 404)

    user_ids: List[int] = user_position_service_db.get_user_ids_by_position_id(position_id)
    return response(True, user_ids, 200)
