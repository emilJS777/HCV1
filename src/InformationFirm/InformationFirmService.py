from . import InformationFirmServiceDb
from src.Information import InformationServiceDb
from src.Firm import FirmServiceDb
from src._response import response
from typing import List


# BIND CATEGORY FIRM
def bind_information_firm(information_id: int, firm_id: int):
    # GET INFORMATION BY ID AND FIRM BY ID AND VERIFY. IF NOT FOUND RETURN NOT FOUND
    if not InformationServiceDb.get_by_id(information_id=information_id) or not FirmServiceDb.get_by_id(firm_id=firm_id):
        return response(False, {'msg': 'Information and/or Firm not found'}, 404)

    # GET INFORMATION_FIRM BY INFORMATION ID AND FIRM ID AND VERIFY. IF RECORD EXIST RETURN CONFLICT
    elif InformationFirmServiceDb.get_by_information_id_firm_id(information_id=information_id, firm_id=firm_id):
        return response(False, {'msg': 'record exists'}, 409)

    # ELSE CREATE AN ENTRY WITH INFORMATION ID AND FIRM ID AND RETURN OK
    else:
        InformationFirmServiceDb.create_bind(information_id=information_id, firm_id=firm_id)
        return response(True, {'msg': 'Information and Firm successfully tied'}, 200)


# DELETE BIND INFORMATION FIRM
def unbind_information_firm(information_id: int, firm_id: int):
    # GET BY INFORMATION ID AND FIRM ID AND VERIFY. IF NOT FOUND RETURN NOT FOUND
    if not InformationFirmServiceDb.get_by_information_id_firm_id(information_id=information_id, firm_id=firm_id):
        return response(False, {'msg': 'entry does not exist'}, 404)

    # ELSE REMOVE THIS RECORD AND RETURN OK
    else:
        InformationFirmServiceDb.delete_bind(information_id=information_id, firm_id=firm_id)
        return response(True, {'msg': 'record successfully deleted'}, 200)


# GEt FIRm IDS BY INFORMATION ID
def get_firms_by_information_id(information_id: int, page: int, per_page: int):
    # GET INFORMATION BY ID AND VERIFY IF NOT FOUND RETURN NOT FOUND
    if not InformationServiceDb.get_by_id(information_id=information_id):
        return response(False, {'msg': 'Information not found'}, 404)

    # ELSE RETURN FIRM IDS BY INFORMATION ID
    else:
        firms: dict = InformationFirmServiceDb.get_firms_by_information_id(
            information_id=information_id,
            page=page,
            per_page=per_page
        )
        return response(True, firms, 200)
    