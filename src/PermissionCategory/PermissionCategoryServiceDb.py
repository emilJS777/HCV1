from .PermissionCategoryModel import PermissionCategory
from typing import List


def create(title: str, description: str) -> PermissionCategory:
    permission_category: PermissionCategory = PermissionCategory(title=title, description=description)
    permission_category.save_db()
    return permission_category


def update(permission_category_id: int, title: str, description: str) -> PermissionCategory:
    permission_category: PermissionCategory = PermissionCategory.query.filter_by(id=permission_category_id).first()
    permission_category.title = title
    permission_category.description = description
    permission_category.update_db()
    return permission_category


def delete(permission_category_id: int) -> PermissionCategory:
    permission_category: PermissionCategory = PermissionCategory.query.filter_by(id=permission_category_id).first()
    permission_category.delete_db()
    return permission_category


def get_by_id(permission_category_id: int) -> PermissionCategory:
    permission_category: PermissionCategory = PermissionCategory.query.filter_by(id=permission_category_id).first()
    return permission_category


def get_by_title(title: str) -> dict:
    permission_category: PermissionCategory = PermissionCategory.query.filter_by(title=title).first()
    return permission_category


def get_all() -> List[dict]:
    permission_categories: List[dict] = []
    for permission_category in PermissionCategory.query.all():
        permission_categories.append({'id': permission_category.id,
                                      'title': permission_category.title,
                                      'description': permission_category.description})
    return permission_categories
