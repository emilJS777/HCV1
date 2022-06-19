from . import PermissionCategoryServiceDb
from src._response import response
from typing import List


# CREATE
def create(title: str, description: str) -> dict:
    if PermissionCategoryServiceDb.get_by_title(title):
        return response(False, {'msg': 'Information by this title exist'}, 200)

    PermissionCategoryServiceDb.create(
        title,
        description
    )
    return response(True, {'msg': 'Information successfully created'}, 200)


# UPDATE
def update(permission_category_id: int, title: str, description: str) -> dict:
    if not PermissionCategoryServiceDb.get_by_id(permission_category_id):
        return response(False, {'msg': 'Information not found'}, 200)

    PermissionCategoryServiceDb.update(
        permission_category_id,
        title,
        description
    )
    return response(True, {'msg': 'Information successfully updated'}, 200)


# DELETE
def delete(permission_category_id: int) -> dict:
    if not PermissionCategoryServiceDb.get_by_id(permission_category_id):
        return response(False, {'msg': 'Information not found'}, 200)

    PermissionCategoryServiceDb.delete(
        permission_category_id
    )
    return response(True, {'msg': 'Information successfully deleted'}, 200)


# GET BY ID
def get_by_id(permission_category_id: int) -> dict:
    permission_category: PermissionCategoryServiceDb.PermissionCategory = \
        PermissionCategoryServiceDb.get_by_id(permission_category_id)

    if not permission_category:
        return response(False, {'msg': 'Information not found'}, 200)

    return response(True, {
        'id': permission_category.id,
        'title': permission_category.title,
        'description': permission_category.description
    }, 200)


# GET ALL
def get_all() -> dict:
    permission_categories: List[dict] = PermissionCategoryServiceDb.get_all()
    return response(
        True,
        permission_categories,
        200
    )
