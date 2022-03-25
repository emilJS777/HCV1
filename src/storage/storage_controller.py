from flask_expects_json import expects_json
from . import storage_service, storage_validator
from flask import request
from src.auth import auth_middleware
from src.client import client_middleware


# CREATE
@auth_middleware.check_authorize
@client_middleware.check_client(required=True)
@expects_json(storage_validator.storage_schema)
def create_storage() -> dict:
    req: dict = request.get_json()
    res: dict = storage_service.create(
        title=req['title'],
        code=req['code'],
        address=req['address'],
        storekeeper=req['storekeeper'],
        firm_id=req['firm_id']
    )
    return res


# UPDATE
@auth_middleware.check_authorize
@client_middleware.check_client(required=True)
@expects_json(storage_validator.storage_schema)
def update_storage(storage_id: int) -> dict:
    req: dict = request.get_json()
    res: dict = storage_service.update(
        storage_id=storage_id,
        title=req['title'],
        code=req['code'],
        address=req['address'],
        storekeeper=req['storekeeper'],
        firm_id=req['firm_id']
    )
    return res


# DELETE
@auth_middleware.check_authorize
@client_middleware.check_client(required=True)
def delete_storage(storage_id: int) -> dict:
    res: dict = storage_service.delete(storage_id)
    return res


# GET BY ID
@auth_middleware.check_authorize
@client_middleware.check_client(required=True)
def get_by_id_storage(storage_id: int) -> dict:
    res: dict = storage_service.get_by_id(storage_id)
    return res


# GET ALL IDS
@auth_middleware.check_authorize
@client_middleware.check_client(required=True)
def get_all_ids_storage() -> dict:
    res: dict = storage_service.get_all_ids()
    return res

