from . import category_service_db
from .category_service_db import Category
from src._response import response
from typing import List
from src.category_firm import category_firm_service_db


# CREATE CATEGORY
def create_category(title: str, description: str):
    # GET CATEGORY BY TITLE AND VERIFY IF EXIST RETURN CONFLICT
    if category_service_db.get_by_title(title=title):
        return response(False, {'msg': f'category by title {title} exist'}, 409)

    # ELSE SAVE NEW CATEGORY AND RETURN
    category_service_db.create(title=title, description=description)
    return response(True, {'msg': 'new category successfully created'}, 200)


# DELETE CATEGORY
def delete_category(category_id: int):
    # GET CATEGORY BY IF AND VERIFY IF NOT FOUND RETURN NOT FOUND
    if not category_service_db.get_by_id(category_id=category_id):
        return response(False, {'msg': f'category by id {category_id} not found'}, 404)

    # GET FIRM IDS BY THIS CATEGORY. IF FIRM LENGTH MORE 0 RETURN FORBIDDEN
    if len(category_firm_service_db.get_firm_ids_by_category_id(category_id=category_id)) > 0:
        return response(False, {'msg': 'firms are stored in this category'}, 403)

    # ELSE DELETE THIS CATEGORY BY ID AND RETURN OK
    category_service_db.delete(category_id=category_id)
    return response(True, {'msg': 'category successfully deleted!'}, 200)


# UPDATE CATEGORY
def update_category(category_id: int, title: str, description: str):
    # GET CATEGORY BY ID AND VERIFY IF NOT FOUND RETURN NOT FOUND
    if not category_service_db.get_by_id(category_id=category_id):
        return response(False, {'msg': f'category by id {category_id} not found'}, 404)

    # ELSE UPDATE CATEGORY BY ID AND RETURN OK
    category_service_db.update(category_id=category_id, title=title, description=description)
    return response(True, {'msg': 'category successfully updated!'}, 200)


# GET ALL CATEGORIES
def get_all_category():
    categories: List = category_service_db.get_all()
    return response(True, categories, 200)


# GET CATEGORY BY ID
def get_category_by_id(category_id: int):
    category: Category = category_service_db.get_by_id(category_id=category_id)
    # GET CATEGORY BY ID AND VERIFY. IF NOT FOUND RETURN NOT FOUND
    if not category:
        return response(False, {'msg': f'category by id {category_id} not found'}, 404)

    # ELSE RETURN CATEGORY & OK
    return response(True, {'id': category.id, 'title': category.title, 'description': category.description}, 200)
