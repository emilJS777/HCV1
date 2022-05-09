from flask_expects_json import expects_json
from . import StorageService, StorageValidator
from flask import request
from src.Auth import AuthMiddleware
from src.Client import ClientMiddleware


# CREATE
@AuthMiddleware.check_authorize
@ClientMiddleware.check_client(required=True)
@expects_json(StorageValidator.storage_schema)
def create_storage() -> dict:
    req: dict = request.get_json()
    res: dict = StorageService.create(
        title=req['title'],
        code=req['code'],
        address=req['address'],
        storekeeper=req['storekeeper'],
        firm_id=req['firm_id']
    )
    return res


# UPDATE
@AuthMiddleware.check_authorize
@ClientMiddleware.check_client(required=True)
@expects_json(StorageValidator.storage_schema)
def update_storage(storage_id: int) -> dict:
    req: dict = request.get_json()
    res: dict = StorageService.update(
        storage_id=storage_id,
        title=req['title'],
        code=req['code'],
        address=req['address'],
        storekeeper=req['storekeeper'],
        firm_id=req['firm_id']
    )
    return res


# DELETE
@AuthMiddleware.check_authorize
@ClientMiddleware.check_client(required=True)
def delete_storage(storage_id: int) -> dict:
    res: dict = StorageService.delete(storage_id)
    return res


# GET BY ID
@AuthMiddleware.check_authorize
@ClientMiddleware.check_client(required=True)
def get_by_id_storage(storage_id: int) -> dict:
    res: dict = StorageService.get_by_id(storage_id)
    return res


# GET ALL IDS
@AuthMiddleware.check_authorize
@ClientMiddleware.check_client(required=True)
def get_all_storage() -> dict:
    res: dict = StorageService.get_all(
        page=int(request.args.get('page')),
        per_page=int(request.args.get('per_page'))
    )
    return res

