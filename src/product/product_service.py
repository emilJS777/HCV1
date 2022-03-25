from . import product_service_db
from src._response import response
from typing import List
from src.storage import storage_service_db


# CREATE
def create(body: dict) -> dict:
    if not storage_service_db.get_by_id(storage_id=body['storage_id']):
        return response(False, {'msg': 'storage not found'}, 404)

    product_service_db.create(body)
    return response(True, {'msg': 'product successfully created'}, 200)


# UPDATE
def update(product_id: int, body: dict) -> dict:
    if not storage_service_db.get_by_id(storage_id=body['storage_id']):
        return response(False, {'msg': 'storage not found'}, 404)

    if not product_service_db.get_by_id(product_id):
        return response(False, {'msg': 'product not found'}, 404)

    product_service_db.update(
        product_id=product_id,
        body=body
    )
    return response(True, {'msg': 'product successfully updated'}, 200)


# DELETE
def delete(product_id: int) -> dict:
    if not product_service_db.get_by_id(product_id):
        return response(False, {'msg': 'product not found'}, 404)

    product_service_db.delete(product_id)
    return response(True, {'msg': 'product successfully deleted'}, 200)


# GET BY ID
def get_by_id(product_id: int) -> dict:
    product: product_service_db.Product = product_service_db.get_by_id(product_id)
    if not product:
        return response(False, {'msg': 'product not found'}, 404)

    return response(True, {'id': product.id,
                           'title': product.title,
                           'code': product.code,
                           'unit_measurement': product.unit_measurement,
                           'group': product.group,
                           'atgaa_classifier': product.atgaa_classifier,
                           'account': product.account,
                           'wholesale_price': product.wholesale_price,
                           'retail_price': product.retail_price,
                           'other_currency': product.other_currency,
                           'wholesale_price_other_currency': product.wholesale_price_other_currency,
                           'hcb_coefficient': product.hcb_coefficient,
                           'accounting_method': product.accounting_method,
                           'storage_id': product.storage_id}, 200)


# GET ALL IDS
def get_all_ids() -> dict:
    product_ids: List[int] = product_service_db.get_all_ids()
    return response(True, product_ids, 200)


# GET ALL IDS BY STORAGE ID
def get_all_ids_by_storage_id(storage_id: int) -> dict:
    product_ids: List[int] = product_service_db.get_all_ids_by_storage_id(storage_id)
    return response(True, product_ids, 200)
