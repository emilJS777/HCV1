from . import ProductServiceDb
from src._response import response
from typing import List
from src.Storage import StorageServiceDb


# CREATE
def create(body: dict) -> dict:
    if not StorageServiceDb.get_by_id(storage_id=body['storage_id']):
        return response(False, {'msg': 'Storage not found'}, 404)

    ProductServiceDb.create(body)
    return response(True, {'msg': 'Product successfully created'}, 200)


# UPDATE
def update(product_id: int, body: dict) -> dict:
    if not StorageServiceDb.get_by_id(storage_id=body['storage_id']):
        return response(False, {'msg': 'Storage not found'}, 404)

    if not ProductServiceDb.get_by_id(product_id):
        return response(False, {'msg': 'Product not found'}, 404)

    ProductServiceDb.update(
        product_id=product_id,
        body=body
    )
    return response(True, {'msg': 'Product successfully updated'}, 200)


# DELETE
def delete(product_id: int) -> dict:
    if not ProductServiceDb.get_by_id(product_id):
        return response(False, {'msg': 'Product not found'}, 404)

    ProductServiceDb.delete(product_id)
    return response(True, {'msg': 'Product successfully deleted'}, 200)


# GET BY ID
def get_by_id(product_id: int) -> dict:
    product: ProductServiceDb.Product = ProductServiceDb.get_by_id(product_id)
    if not product:
        return response(False, {'msg': 'Product not found'}, 404)

    return response(True, {'id': product.id,
                           'title': product.title,
                           'code': product.code,
                           'unit_id': product.unit_id,
                           'wholesale_price': product.wholesale_price,
                           'retail_price': product.retail_price,
                           'storage_id': product.storage_id}, 200)


# GET ALL IDS
def get_all(page: int, per_page: int) -> dict:
    products: dict = ProductServiceDb.get_all(
        page=page,
        per_page=per_page
    )
    return response(True, products, 200)


# GET ALL BY STORAGE ID
def get_all_by_storage_id(storage_id: int, page: int, per_page: int) -> dict:
    products: dict = ProductServiceDb.get_all_by_storage_id(
        storage_id=storage_id,
        page=page,
        per_page=per_page
    )
    return response(True, products, 200)
