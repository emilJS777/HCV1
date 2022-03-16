from . import permission_category_service_db
from src._response import response
from typing import List


# CREATE
def create(title: str, description: str) -> dict:
    if permission_category_service_db.get_by_title(title):
        return response(False, {'msg': 'category by this title exist'}, 409)

    permission_category_service_db.create(
        title,
        description
    )
    return response(True, {'msg': 'category successfully created'}, 200)


# UPDATE
def update(permission_category_id: int, title: str, description: str) -> dict:
    if not permission_category_service_db.get_by_id(permission_category_id):
        return response(False, {'msg': 'category not found'}, 404)

    permission_category_service_db.update(
        permission_category_id,
        title,
        description
    )
    return response(True, {'msg': 'category successfully updated'}, 200)


# DELETE
def delete(permission_category_id: int) -> dict:
    if not permission_category_service_db.get_by_id(permission_category_id):
        return response(False, {'msg': 'category not found'}, 404)

    permission_category_service_db.delete(
        permission_category_id
    )
    return response(True, {'msg': 'category successfully deleted'}, 200)


# GET BY ID
def get_by_id(permission_category_id: int) -> dict:
    permission_category: permission_category_service_db.PermissionCategory = \
        permission_category_service_db.get_by_id(permission_category_id)

    if not permission_category:
        return response(False, {'msg': 'category not found'}, 404)

    return response(True, {
        'id': permission_category.id,
        'title': permission_category.title,
        'description': permission_category.description
    }, 200)


# GET ALL
def get_all() -> dict:
    permission_categories: List[dict] = permission_category_service_db.get_all()
    return response(
        True,
        permission_categories,
        200
    )
