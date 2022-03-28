from . import user_firm_service_db
from src.user import user_service_db
from src.firm import firm_service_db
from src._response import response
from typing import List


# CREATE BIND
def create_bind(user_id: int, firm_id: int) -> dict:
    # GET USER AND FIRM BY ID AND VERIFY IF NOT FOUND RETURN NOT FOUND
    if not user_service_db.get_by_id(user_id) or not firm_service_db.get_by_id(firm_id):
        return response(False, {'msg': 'user and/or firm not found'}, 404)

    # ELSE CREATE BIND
    user_firm_service_db.create_bind(
        user_id=user_id,
        firm_id=firm_id
    )
    return response(True, {'msg': 'bind successfully created'}, 200)


# DELETE BIND
def delete_bind(user_id: int, firm_id) -> dict:
    # GET USER FIRM BIND AND VERIFY IF NOT FOUND RETURN NOT FOUND
    if not user_firm_service_db.get_by_user_id_firm_id(user_id, firm_id):
        return response(False, {'msg': 'user firm bind not found'}, 404)

    # ELSE DELETE BIND
    user_firm_service_db.delete_bind(
        user_id=user_id,
        firm_id=firm_id
    )
    return response(True, {'msg': 'bind successfully deleted'}, 200)


# GET FIRM IDS BY USER ID
def get_firm_ids_by_user_id(user_id) -> dict:
    # GET FIRM IDS BY USER ID
    firm_ids: List[int] = user_firm_service_db.get_firm_ids_by_user_id(user_id)
    return response(True, firm_ids, 200)
