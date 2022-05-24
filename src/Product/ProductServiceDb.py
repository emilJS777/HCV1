from .ProductModel import Product
from flask import g
from typing import List
from src.__general.helpers.paginate import get_page_items


# CREATE
def create(body: dict) -> Product:
    product: Product = Product(
        title=body['title'],
        code=body['code'],
        unit_id=body['unit_id'],
        wholesale_price=body['wholesale_price'],
        retail_price=body['retail_price'],
        storage_id=body['storage_id'],
        client_id=g.client_id,
        count=body['count']
    )
    product.save_db()
    return product


# UPDATE
def update(product_id: int, body: dict) -> Product:
    product: Product = Product.query.filter_by(id=product_id).first()
    product.title = body['title']
    product.code = body['code']
    product.unit_id = body['unit_id']
    product.wholesale_price = body['wholesale_price']
    product.retail_price = body['retail_price']
    product.storage_id = body['storage_id']
    product.count = body['count']
    product.update_db()
    return product


# CHANGE PRODUCT COUNT
def update_count(product_id: int, count: float) -> Product:
    product: Product = Product.query.filter_by(id=product_id).first()
    product.count = count
    product.update_db()
    return product


# DELETE
def delete(product_id: int) -> Product:
    product: Product = Product.query.filter_by(id=product_id).first()
    product.delete_db()
    return product


# GET BY ID
def get_by_id(product_id: int) -> Product:
    product: Product = Product.query.filter_by(id=product_id, client_id=g.client_id).first()
    return product


# GET ALL IDS
def get_all(page: int, per_page: int) -> dict:
    # products: List[Product] = Product.query.filter_by(client_id=g.client_id).all()
    # product_ids: List[int] = []
    # for product in products:
    #     product_ids.append(product.id)
    # return product_ids
    return get_page_items(
        Product.query.filter_by(client_id=g.client_id)
            .order_by(-Product.id)
            .paginate(page=page, per_page=per_page)
    )


# GET ALL IDS BY STORAGE ID
def get_all_by_storage_id(storage_id: int, page: int, per_page: int) -> dict:
    # products: List[Product] = Product.query.filter_by(client_id=g.client_id, storage_id=storage_id).all()
    # product_ids: List[int] = []
    # for product in products:
    #     product_ids.append(product.id)
    # return product_ids
    return get_page_items(
        Product.query.filter_by(client_id=g.client_id, storage_id=storage_id)
            .order_by(-Product.id)
            .paginate(page=page, per_page=per_page)
    )

