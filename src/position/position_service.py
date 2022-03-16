from . import position_service_db
from src._response import response
from typing import List


def create(title: str) -> dict:
    # GET BY TITLE IF EXIST REtURN CONFLICT
    if position_service_db.get_by_title(title):
        return response(False, {'msg' 'position by this title exist'}, 409)

    # ELSE CREATE NE POSITION
    position_service_db.create(title)
    return response(True, {'msg': 'position successfully created'}, 200)


def update(position_id: int, title: str) -> dict:
    # GET BY ID AND VERIFY IF NOT FOUND RETURN NOT FOUND
    if not position_service_db.get_by_id(position_id):
        return response(False, {'msg': 'position not found'}, 404)

    # GET BY TITLE IF EXIST REtURN CONFLICT
    if position_service_db.get_by_title(title):
        return response(False, {'msg': 'position by this title exist'}, 409)

    position_service_db.update(position_id, title)
    return response(True, {'msg': 'position successfully updated'}, 200)


def delete(position_id: int) -> dict:
    # GET BY ID AND VERIFY IF NOT FOUND RETURN NOT FOUND
    if not position_service_db.get_by_id(position_id):
        return response(False, {'msg': 'position not found'}, 404)

    # ELSE REMOVE POSITION AND RETURN OK
    position_service_db.delete(position_id)
    return response(True, {'msg': 'position successfully deleted'}, 200)


def get_by_id(position_id: int) -> dict:
    # GET BY ID AND VERIFY IF NOT FOUND RETURN NOT FOUND
    position: position_service_db.Position = position_service_db.get_by_id(position_id)
    if not position:
        return response(False, {'msg': 'position not found'}, 404)

    # ELSE RETURN POSITION FIELD
    return response(True, {'id': position.id, 'title': position.title}, 200)


def get_all_ids() -> dict:
    position_ids: List[int] = position_service_db.get_all_ids()
    return response(True, position_ids, 200)
