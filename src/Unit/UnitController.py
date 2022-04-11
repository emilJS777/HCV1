from src.Auth import AuthMiddleware
from src.Client import ClientMiddleware
from typing import List
from src._response import response


units: List[dict] = [{'id': 1, 'title': 'հատ'}, {'id': 2, 'title': 'կգ'}, {'id': 3, 'title': 'խորանարդ'}]


# GET ALL LIST
@AuthMiddleware.check_authorize
@ClientMiddleware.check_client(required=True)
def unit_get_all() -> dict:
    return response(True, units, 200)


# GET BY ID
@AuthMiddleware.check_authorize
@ClientMiddleware.check_client(required=True)
def unit_get_by_id(unit_id: int) -> dict:
    for unit in units:
        if unit['id'] == unit_id:
            return response(True, {'id': unit['id'], 'title': unit['title']}, 200)

    return response(False, {'msg': 'unit by this id not found'}, 404)

