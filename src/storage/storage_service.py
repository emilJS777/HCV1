from . import storage_service_db
from src._response import response
from typing import List
from src.firm import firm_service_db


# CREATE
def create(title: str, code: str, address: str, storekeeper: str, firm_id: int) -> dict:
    if not firm_service_db.get_by_id(firm_id):
        return response(False, {'msg': 'firm not found'}, 404)

    storage_service_db.create(
        title=title,
        code=code,
        address=address,
        storekeeper=storekeeper,
        firm_id=firm_id
    )
    return response(True, {'msg': 'storage successfully created'}, 200)


# UPDATE
def update(storage_id: int, title: str, code: str, address: str, storekeeper: str, firm_id: int) -> dict:
    if not firm_service_db.get_by_id(firm_id):
        return response(False, {'msg': 'firm not found'}, 404)

    if not storage_service_db.get_by_id(storage_id):
        return response(False, {'msg': 'storage not found'}, 404)

    storage_service_db.update(
        storage_id=storage_id,
        title=title,
        code=code,
        address=address,
        storekeeper=storekeeper,
        firm_id=firm_id
    )
    return response(True, {'msg': 'storage successfully created'}, 200)


# DELETE
def delete(storage_id: int) -> dict:
    if not storage_service_db.get_by_id(storage_id):
        return response(False, {'msg': 'storage not found'}, 404)

    storage_service_db.delete(storage_id)
    return response(True, {'msg': 'storage successfully deleted'}, 200)


# GET BY ID
def get_by_id(storage_id: int) -> dict:
    storage: storage_service_db.Storage = storage_service_db.get_by_id(storage_id)
    if not storage:
        return response(False, {'msg': 'storage not found'}, 404)

    return response(True, {'id': storage.id,
                           'code': storage.code,
                           'title': storage.title,
                           'address': storage.address,
                           'storekeeper': storage.storekeeper,
                           'firm_id': storage.firm_id}, 200)


# GET ALL IDS
def get_all_ids() -> dict:
    storage_ids: List[int] = storage_service_db.get_all_ids()
    return response(True, storage_ids, 200)
