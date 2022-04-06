from .ProductModel import Product
from flask import g
from typing import List


# CREATE
def create(body: dict) -> Product:
    product: Product = Product(
        title=body['title'],
        code=body['code'],
        unit_measurement=body['unit_measurement'],
        group=body['group'],

        atgaa_classifier=body['atgaa_classifier'],
        account=body['account'],
        wholesale_price=body['wholesale_price'],
        retail_price=body['retail_price'],

        other_currency=body['other_currency'],
        wholesale_price_other_currency=body['wholesale_price_other_currency'],
        hcb_coefficient=body['hcb_coefficient'],
        accounting_method=body['accounting_method'],
        storage_id=body['storage_id'],
        client_id=g.client_id
    )
    product.save_db()
    return product


# UPDATE
def update(product_id: int, body: dict) -> Product:
    product: Product = Product.query.filter_by(id=product_id).first()
    product.title = body['title']
    product.code = body['code']
    product.unit_measurement = body['unit_measurement']
    product.group = body['group']

    product.atgaa_classifier = body['atgaa_classifier']
    product.account = body['account']
    product.wholesale_price = body['wholesale_price']
    product.retail_price = body['retail_price']

    product.other_currency = body['other_currency']
    product.wholesale_price_other_currency = body['wholesale_price_other_currency']
    product.hcb_coefficient = body['hcb_coefficient']
    product.accounting_method = body['accounting_method']
    product.storage_id = body['storage_id']
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
def get_all_ids() -> List[int]:
    products: List[Product] = Product.query.filter_by(client_id=g.client_id).all()
    product_ids: List[int] = []

    for product in products:
        product_ids.append(product.id)

    return product_ids


# GET ALL IDS BY STORAGE ID
def get_all_ids_by_storage_id(storage_id: int) -> List[int]:
    products: List[Product] = Product.query.filter_by(client_id=g.client_id, storage_id=storage_id).all()
    product_ids: List[int] = []

    for product in products:
        product_ids.append(product.id)

    return product_ids
