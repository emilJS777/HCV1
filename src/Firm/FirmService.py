from . import FirmServiceDb
from src.InformationFirm import InformationFirmServiceDb
from src.Client import ClientServiceDb
from src._response import response
from flask import g
from typing import List
from src.Permission import PermissionServiceDb
from src.UserPermission import UserPermissionServiceDb


# CREATE NEW FIRM
def firm_create(req_body):
    # IF FIND THIS FIRM TITLE RETURN RESPONSE CONFLICT
    if FirmServiceDb.get_by_title(title=req_body['title']):
        return response(False, {'msg': 'Firm title is taken'}, 200)

    # IF THE NUMBER OF FIRMS IS ATTACHED RETURN LIMIT LOST
    if not len(FirmServiceDb.get_all_ids()) < ClientServiceDb.get_self_client().max_count_firms:
        return response(False, {'msg': 'limit lost'}, 200)

    # ELSE FIRM BY THIS TITLE SAVE
    else:
        new_firm = FirmServiceDb.create(req_body=req_body)
        if new_firm:

            permissions = PermissionServiceDb.get_all_by_self_client(firm=True)

            for permission in permissions:

                UserPermissionServiceDb.create(
                    user_id=g.user_id,
                    permission_id=permission.id,
                    firm_id=new_firm.id,
                    client_id=g.client_id
                )

        return response(True, {'msg': 'new Firm by id {} successfully created'.format(new_firm.id)}, 200)


# FIRM GET BY ID
def firm_get_by_id(firm_id):
    # GET FIRM BY ID END VERIFY USER DOES IT EXIST. IF NO RETURN NOT FOUND
    firm = FirmServiceDb.get_by_id(firm_id=firm_id)
    if not firm:
        return response(False, {'msg': 'Firm by this id not found'}, 200)

    # ELSE RETURN THIS FIRM AND STATUS OK
    return response(True, {'id': firm.id,
                           'title': firm.title,
                           'description': firm.description,
                           'activity_address': firm.activity_address,
                           'legal_address': firm.legal_address,
                           'phone_number': firm.phone_number,
                           'email_address': firm.email_address,
                           'tax_payer_number': firm.tax_payer_number,
                           'state_register_number': firm.state_register_number,
                           'insurer_account_number': firm.insurer_account_number,
                           'hvhh': firm.hvhh,
                           'leader_position': firm.leader_position,
                           'leader_full_name': firm.leader_full_name,
                           'accountant_position': firm.accountant_position,
                           'accountant_full_name': firm.accountant_full_name,
                           'cashier_full_name': firm.cashier_full_name}, 200)


# GET ALL FIRM
def firm_get_all(page: int, per_page: int) -> dict:
    # GET ALL CLIENTS BY CLIENT ID
    firms_ids: dict = FirmServiceDb.get_all(page=page, per_page=per_page)
    return response(True, firms_ids, 200)


# UPDATE FIRM
def firm_update(firm_id: int, req_body):
    # GET FIRM BY ID AND VERIFY DOES IT EXIST. IF NO RETURN NOT FOUND
    if not FirmServiceDb.get_by_id(firm_id=firm_id):
        return response(False, {'msg': 'Firm by this id not found'}, 200)

    # VERIFY IF THERE IS A FIRM WITH THE SAME TITLE RETURN CONFLICT
    if FirmServiceDb.get_by_title_exclude_id(firm_id=firm_id, title=req_body['title']):
        return response(False, {'msg': 'Firm by this title exist'}, 200)

    # ELSE CHANGE AND UPDATE DB AND RETURN RESPONSE OK
    FirmServiceDb.update(firm_id=firm_id, req_body=req_body)
    return response(True, {'msg': 'Firm successfully update'}, 200)


# DELETE FIRM BY ID
def firm_delete(firm_id: int):
    # GET FIRM BY ID AND VERIFY DIES EXIST. IF NO RETURN NOT FOUND
    if not FirmServiceDb.get_by_id(firm_id=firm_id):
        return response(False, {"msg": "Firm by this id not found"}, 200)

    # IF THIS FIRM TIED TO INFORMATION REMOVE THIS BINDING
    for information_id in InformationFirmServiceDb.get_information_ids_by_firm_id(firm_id=firm_id):
        InformationFirmServiceDb.delete_bind(information_id=information_id, firm_id=firm_id)

    # REMOVE THIS FIRM FROM DB
    FirmServiceDb.delete(firm_id=firm_id)
    return response(True, {'msg': "this Firm successfully deleted"}, 200)

