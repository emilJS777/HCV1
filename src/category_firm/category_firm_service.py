from . import category_firm_service_db
from src.category import category_service_db
from src.firm import firm_service_db
from src._response import response
from typing import List


# BIND CATEGORY FIRM
def bind_category_firm(category_id: int, firm_id: int):
    # GET CATEGORY BY ID AND FIRM BY ID AND VERIFY. IF NOT FOUND RETURN NOT FOUND
    if not category_service_db.get_by_id(category_id=category_id) or not firm_service_db.get_by_id(firm_id=firm_id):
        return response(False, {'msg': 'category and/or firm not found'}, 404)

    # GET CATEGORY_FIRM BY CATEGORY ID AND FIRM ID AND VERIFY. IF RECORD EXIST RETURN CONFLICT
    elif category_firm_service_db.get_by_category_id_firm_id(category_id=category_id, firm_id=firm_id):
        return response(False, {'msg': 'record exists'}, 409)

    # ELSE CREATE AN ENTRY WITH CATEGORY ID AND FIRM ID AND RETURN OK
    else:
        category_firm_service_db.create_bind(category_id=category_id, firm_id=firm_id)
        return response(True, {'msg': 'category and firm successfully tied'}, 200)


# DELETE BIND CATEGORY FIRM
def unbind_category_firm(category_id: int, firm_id: int):
    # GET BY CATEGORY ID AND FIRM ID AND VERIFY. IF NOT FOUND RETURN NOT FOUND
    if not category_firm_service_db.get_by_category_id_firm_id(category_id=category_id, firm_id=firm_id):
        return response(False, {'msg': 'entry does not exist'}, 404)

    # ELSE REMOVE THIS RECORD AND RETURN OK
    else:
        category_firm_service_db.delete_bind(category_id=category_id, firm_id=firm_id)
        return response(True, {'msg': 'record successfully deleted'}, 200)


# GEt FIRm IDS BY CATEGORY ID
def get_firm_ids_by_category_id(category_id: int):
    # GET CATEGORY BY ID AND VERIFY IF NOT FOUND RETURN NOT FOUND
    if not category_service_db.get_by_id(category_id=category_id):
        return response(False, {'msg': 'category not found'}, 404)

    # ELSE RETURN FIRM IDS BY CATEGORY ID
    else:
        firm_ids: List[int] = category_firm_service_db.get_firm_ids_by_category_id(category_id=category_id)
        return response(True, firm_ids, 200)
    