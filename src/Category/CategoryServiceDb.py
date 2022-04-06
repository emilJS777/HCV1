from .CategoryModel import Category
from flask import g
from typing import List


def create(title: str, description: str) -> Category:
    # CREATE NEW CATEGORY
    category: Category = Category(title=title, description=description, client_id=g.client_id)
    category.save_db()
    return category


def delete(category_id: int) -> Category:
    # DELETE CATEGORY BY ID
    category: Category = Category.query.filter_by(id=category_id, client_id=g.client_id).first()
    category.delete_db()
    return category


def update(category_id: int, title: str, description: str) -> Category:
    # UPDATE CATEGORY BY ID
    category: Category = Category.query.filter_by(id=category_id, client_id=g.client_id).first()
    category.title = title
    category.description = description
    category.update_db()
    return category


def get_by_title(title: str) -> Category:
    # GET CATEGORY BY TITLE
    category: Category = Category.query.filter_by(title=title, client_id=g.client_id).first()
    return category


def get_all() -> List:
    # GET ALL CATEGORIES
    categories: List[Category] = Category.query.filter_by(client_id=g.client_id).all()
    arr: List = []

    for category in categories:
        arr.append({'id': category.id, 'title': category.title, 'description': category.description})
    return arr


def get_by_id(category_id: int) -> Category:
    # GET CATEGORY BY ID
    category: Category = Category.query.filter_by(id=category_id, client_id=g.client_id).first()
    return category
