from . import PositionServiceDb
from src._response import response
from typing import List


def create(title: str) -> dict:
    # GET BY TITLE IF EXIST REtURN CONFLICT
    if PositionServiceDb.get_by_title(title):
        return response(False, {'msg' 'Position by this title exist'}, 409)

    # ELSE CREATE NE POSITION
    PositionServiceDb.create(title)
    return response(True, {'msg': 'Position successfully created'}, 200)


def update(position_id: int, title: str) -> dict:
    # GET BY ID AND VERIFY IF NOT FOUND RETURN NOT FOUND
    if not PositionServiceDb.get_by_id(position_id):
        return response(False, {'msg': 'Position not found'}, 404)

    # GET BY TITLE IF EXIST REtURN CONFLICT
    if PositionServiceDb.get_by_title(title):
        return response(False, {'msg': 'Position by this title exist'}, 409)

    PositionServiceDb.update(position_id, title)
    return response(True, {'msg': 'Position successfully updated'}, 200)


def delete(position_id: int) -> dict:
    # GET BY ID AND VERIFY IF NOT FOUND RETURN NOT FOUND
    if not PositionServiceDb.get_by_id(position_id):
        return response(False, {'msg': 'Position not found'}, 404)

    # ELSE REMOVE POSITION AND RETURN OK
    PositionServiceDb.delete(position_id)
    return response(True, {'msg': 'Position successfully deleted'}, 200)


def get_by_id(position_id: int) -> dict:
    # GET BY ID AND VERIFY IF NOT FOUND RETURN NOT FOUND
    position: PositionServiceDb.Position = PositionServiceDb.get_by_id(position_id)
    if not position:
        return response(False, {'msg': 'Position not found'}, 404)

    # ELSE RETURN POSITION FIELD
    return response(True, {'id': position.id, 'title': position.title}, 200)


def get_all(page: int, per_page: int) -> dict:
    positions: dict = PositionServiceDb.get_all(page=page, per_page=per_page)
    return response(True, positions, 200)
