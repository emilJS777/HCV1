from . import CategoryFirmServiceDb
from src.Category import CategoryServiceDb
from src.Firm import FirmServiceDb
from src._response import response
from typing import List


# BIND CATEGORY FIRM
def bind_category_firm(category_id: int, firm_id: int):
    # GET CATEGORY BY ID AND FIRM BY ID AND VERIFY. IF NOT FOUND RETURN NOT FOUND
    if not CategoryServiceDb.get_by_id(category_id=category_id) or not FirmServiceDb.get_by_id(firm_id=firm_id):
        return response(False, {'msg': 'Category and/or Firm not found'}, 404)

    # GET CATEGORY_FIRM BY CATEGORY ID AND FIRM ID AND VERIFY. IF RECORD EXIST RETURN CONFLICT
    elif CategoryFirmServiceDb.get_by_category_id_firm_id(category_id=category_id, firm_id=firm_id):
        return response(False, {'msg': 'record exists'}, 409)

    # ELSE CREATE AN ENTRY WITH CATEGORY ID AND FIRM ID AND RETURN OK
    else:
        CategoryFirmServiceDb.create_bind(category_id=category_id, firm_id=firm_id)
        return response(True, {'msg': 'Category and Firm successfully tied'}, 200)


# DELETE BIND CATEGORY FIRM
def unbind_category_firm(category_id: int, firm_id: int):
    # GET BY CATEGORY ID AND FIRM ID AND VERIFY. IF NOT FOUND RETURN NOT FOUND
    if not CategoryFirmServiceDb.get_by_category_id_firm_id(category_id=category_id, firm_id=firm_id):
        return response(False, {'msg': 'entry does not exist'}, 404)

    # ELSE REMOVE THIS RECORD AND RETURN OK
    else:
        CategoryFirmServiceDb.delete_bind(category_id=category_id, firm_id=firm_id)
        return response(True, {'msg': 'record successfully deleted'}, 200)


# GEt FIRm IDS BY CATEGORY ID
def get_firm_ids_by_category_id(category_id: int):
    # GET CATEGORY BY ID AND VERIFY IF NOT FOUND RETURN NOT FOUND
    if not CategoryServiceDb.get_by_id(category_id=category_id):
        return response(False, {'msg': 'Category not found'}, 404)

    # ELSE RETURN FIRM IDS BY CATEGORY ID
    else:
        firm_ids: List[int] = CategoryFirmServiceDb.get_firm_ids_by_category_id(category_id=category_id)
        return response(True, firm_ids, 200)
    