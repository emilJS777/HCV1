from . import StorageServiceDb
from src._response import response
from typing import List
from src.Firm import FirmServiceDb


# CREATE
def create(title: str, code: str, address: str, storekeeper: str, firm_id: int) -> dict:
    if not FirmServiceDb.get_by_id(firm_id):
        return response(False, {'msg': 'Firm not found'}, 404)

    StorageServiceDb.create(
        title=title,
        code=code,
        address=address,
        storekeeper=storekeeper,
        firm_id=firm_id
    )
    return response(True, {'msg': 'Storage successfully created'}, 200)


# UPDATE
def update(storage_id: int, title: str, code: str, address: str, storekeeper: str, firm_id: int) -> dict:
    if not FirmServiceDb.get_by_id(firm_id):
        return response(False, {'msg': 'Firm not found'}, 404)

    if not StorageServiceDb.get_by_id(storage_id):
        return response(False, {'msg': 'Storage not found'}, 404)

    StorageServiceDb.update(
        storage_id=storage_id,
        title=title,
        code=code,
        address=address,
        storekeeper=storekeeper,
        firm_id=firm_id
    )
    return response(True, {'msg': 'Storage successfully created'}, 200)


# DELETE
def delete(storage_id: int) -> dict:
    if not StorageServiceDb.get_by_id(storage_id):
        return response(False, {'msg': 'Storage not found'}, 404)

    StorageServiceDb.delete(storage_id)
    return response(True, {'msg': 'Storage successfully deleted'}, 200)


# GET BY ID
def get_by_id(storage_id: int) -> dict:
    storage: StorageServiceDb.Storage = StorageServiceDb.get_by_id(storage_id)
    if not storage:
        return response(False, {'msg': 'Storage not found'}, 404)

    return response(True, {'id': storage.id,
                           'code': storage.code,
                           'title': storage.title,
                           'address': storage.address,
                           'storekeeper': storage.storekeeper,
                           'firm_id': storage.firm_id}, 200)


# GET ALL IDS
def get_all_ids() -> dict:
    storage_ids: List[int] = StorageServiceDb.get_all_ids()
    return response(True, storage_ids, 200)
