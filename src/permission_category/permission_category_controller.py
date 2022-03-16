from . import permission_category_service
from flask import request


# CREATE
def create() -> dict:
    req: dict = request.get_json()
    res: dict = permission_category_service.create(
        title=req['title'],
        description=req['description']
    )
    return res


# UPDATE
def update(permission_category_id: int) -> dict:
    req: dict = request.get_json()
    res: dict = permission_category_service.update(
        permission_category_id=permission_category_id,
        title=req['title'],
        description=req['description']
    )
    return res


# DELETE
def delete(permission_category_id: int) -> dict:
    res: dict = permission_category_service.delete(
        permission_category_id=permission_category_id
    )
    return res


# GET BY ID
def get_by_id(permission_category_id: int) -> dict:
    res: dict = permission_category_service.get_by_id(
        permission_category_id=permission_category_id
    )
    return res


# GET ALL
def get_all() -> dict:
    res: dict = permission_category_service.get_all()
    return res
