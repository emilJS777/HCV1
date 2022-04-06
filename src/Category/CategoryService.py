from . import CategoryServiceDb
from .CategoryServiceDb import Category
from src._response import response
from typing import List
from src.CategoryFirm import CategoryFirmServiceDb


# CREATE CATEGORY
def create_category(title: str, description: str):
    # GET CATEGORY BY TITLE AND VERIFY IF EXIST RETURN CONFLICT
    if CategoryServiceDb.get_by_title(title=title):
        return response(False, {'msg': f'Category by title {title} exist'}, 409)

    # ELSE SAVE NEW CATEGORY AND RETURN
    CategoryServiceDb.create(title=title, description=description)
    return response(True, {'msg': 'new Category successfully created'}, 200)


# DELETE CATEGORY
def delete_category(category_id: int):
    # GET CATEGORY BY IF AND VERIFY IF NOT FOUND RETURN NOT FOUND
    if not CategoryServiceDb.get_by_id(category_id=category_id):
        return response(False, {'msg': f'Category by id {category_id} not found'}, 404)

    # GET FIRM IDS BY THIS CATEGORY. IF FIRM LENGTH MORE 0 RETURN FORBIDDEN
    if len(CategoryFirmServiceDb.get_firm_ids_by_category_id(category_id=category_id)) > 0:
        return response(False, {'msg': 'firms are stored in this Category'}, 403)

    # ELSE DELETE THIS CATEGORY BY ID AND RETURN OK
    CategoryServiceDb.delete(category_id=category_id)
    return response(True, {'msg': 'Category successfully deleted!'}, 200)


# UPDATE CATEGORY
def update_category(category_id: int, title: str, description: str):
    # GET CATEGORY BY ID AND VERIFY IF NOT FOUND RETURN NOT FOUND
    if not CategoryServiceDb.get_by_id(category_id=category_id):
        return response(False, {'msg': f'Category by id {category_id} not found'}, 404)

    # ELSE UPDATE CATEGORY BY ID AND RETURN OK
    CategoryServiceDb.update(category_id=category_id, title=title, description=description)
    return response(True, {'msg': 'Category successfully updated!'}, 200)


# GET ALL CATEGORIES
def get_all_category():
    categories: List = CategoryServiceDb.get_all()
    return response(True, categories, 200)


# GET CATEGORY BY ID
def get_category_by_id(category_id: int):
    category: Category = CategoryServiceDb.get_by_id(category_id=category_id)
    # GET CATEGORY BY ID AND VERIFY. IF NOT FOUND RETURN NOT FOUND
    if not category:
        return response(False, {'msg': f'Category by id {category_id} not found'}, 404)

    # ELSE RETURN CATEGORY & OK
    return response(True, {'id': category.id, 'title': category.title, 'description': category.description}, 200)
