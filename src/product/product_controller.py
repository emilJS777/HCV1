from . import product_service, product_validator
from flask import request
from src.auth import auth_middleware
from src.client import client_middleware
from flask_expects_json import expects_json


# CREATE
@auth_middleware.check_authorize
@client_middleware.check_client(required=True)
@expects_json(product_validator.product_schema)
def create_product() -> dict:
    req: dict = request.get_json()
    res: dict = product_service.create(body=req)
    return res


# UPDATE
@auth_middleware.check_authorize
@client_middleware.check_client(required=True)
@expects_json(product_validator.product_schema)
def update_product(product_id: int) -> dict:
    req: dict = request.get_json()
    res: dict = product_service.update(
        product_id=product_id,
        body=req
    )
    return res


# DELETE
@auth_middleware.check_authorize
@client_middleware.check_client(required=True)
def delete_product(product_id: int) -> dict:
    res: dict = product_service.delete(product_id)
    return res


# GET BY ID
@auth_middleware.check_authorize
@client_middleware.check_client(required=True)
def get_by_id_product(product_id: int) -> dict:
    res: dict = product_service.get_by_id(product_id)
    return res


# GET ALL IDS
@auth_middleware.check_authorize
@client_middleware.check_client(required=True)
def get_all_ids_product() -> dict:
    res: dict = product_service.get_all_ids()
    return res


# GET ALL IDS BY STORAGE ID
@auth_middleware.check_authorize
@client_middleware.check_client(required=True)
def get_all_ids_product_by_storage_id(storage_id: int) -> dict:
    res: dict = product_service.get_all_ids_by_storage_id(storage_id)
    return res
