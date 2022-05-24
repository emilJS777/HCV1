from .StorageModel import Storage
from typing import List
from flask import g
from src.__general.helpers.paginate import get_page_items


# CREATE
def create(title: str, code: str, address: str, storekeeper: str, firm_id: int) -> Storage:
    storage: Storage = Storage(
        title=title,
        code=code,
        address=address,
        storekeeper=storekeeper,
        firm_id=firm_id,
        client_id=g.client_id
    )
    storage.save_db()
    return storage


# DELETE
def delete(storage_id: int) -> Storage:
    storage: Storage = Storage.query.filter_by(id=storage_id).first()
    storage.delete_db()
    return storage


# UPDATE
def update(storage_id: int, title: str, code: str, address: str, storekeeper: str, firm_id: int) -> Storage:
    storage: Storage = Storage.query.filter_by(id=storage_id).first()
    storage.title = title
    storage.code = code
    storage.address = address
    storage.storekeeper = storekeeper
    storage.firm_id = firm_id
    storage.update_db()
    return storage


# GET BY ID
def get_by_id(storage_id: int) -> Storage:
    storage: Storage = Storage.query.filter_by(id=storage_id, client_id=g.client_id).first()
    return storage


# GET ALL IDS
def get_all(page: int, per_page: int) -> dict:
    # storages: List[Storage] = Storage.query.filter_by(client_id=g.client_id).all()
    # storage_ids: List[int] = []
    # for storage in storages:
    #     storage_ids.append(storage.id)
    # return storage_ids
    return get_page_items(
        Storage.query.filter_by(client_id=g.client_id)
            .order_by(-Storage.id)
            .paginate(page=page, per_page=per_page)
    )
