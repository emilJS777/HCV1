from src.firm_user import firm_user_service_db
from . import firm_service_db
from src.client import client_service_db
from src._response import response


# CREATE NEW FIRM
def firm_create(req_body, client_id):
    # IF FIND THIS FIRM TITLE RETURN RESPONSE CONFLICT
    if firm_service_db.get_by_title_client_id(title=req_body['title'], client_id=client_id):
        return response(False, {'msg': 'firm title is taken'}, 409)

    # IF THE NUMBER OF FIRMS IS ATTACHED RETURN LIMIT LOST
    client = client_service_db.get_by_id(client_id=client_id)
    if not len(firm_service_db.get_all_ids_by_client_id(client_id=client_id)) < client.max_count_firms:
        return response(False, {'msg': 'limit lost'}, 202)

    # ELSE FIRM BY THIS TITLE SAVE
    else:
        new_firm = firm_service_db.create(req_body=req_body, client_id=client_id)
        return response(True, {'msg': 'new firm by id {} successfully created'.format(new_firm.id)}, 200)


# FIRM GET BY ID
def firm_get_by_id(firm_id, client_id):
    # GET FIRM BY ID END VERIFY USER DOES IT EXIST. IF NO RETURN NOT FOUND
    firm = firm_service_db.get_by_id_client_id(firm_id=firm_id, client_id=client_id)
    if not firm:
        return response(False, {'msg': 'firm by this id not found'}, 404)

    # ELSE RETURN THIS FIRM AND STATUS OK
    return response(True, {'title': firm.title,
                           'activity_address': firm.activity_address,
                           'legal_address': firm.legal_address,
                           'phone_number': firm.phone_number,
                           'email_address': firm.email_address,
                           'tax_payer_number': firm.tax_payer_number,
                           'state_register_number': firm.state_register_number,
                           'leader_position': firm.leader_position,
                           'leader_full_name': firm.leader_full_name,
                           'accountant_position': firm.accountant_position,
                           'accountant_full_name': firm.accountant_full_name,
                           'cashier_full_name': firm.cashier_full_name}, 200)


# GET ALL FIRM
def firm_get_all(client_id):
    # GET ALL CLIENTS BY CLIENT ID
    firms_ids = firm_service_db.get_all_ids_by_client_id(client_id=client_id)
    return response(True, firms_ids, 200)


# UPDATE FIRM
def firm_update(firm_id, req_body, client_id):
    # GET FIRM BY ID AND VERIFY DOES IT EXIST. IF NO RETURN NOT FOUND
    if not firm_service_db.get_by_id_client_id(firm_id=firm_id, client_id=client_id):
        return response(False, {'msg': 'firm by this id not found'}, 404)

    # VERIFY IF THERE IS A FIRM WITH THE SAME TITLE RETURN CONFLICT
    if firm_service_db.get_by_client_id_title_exclude_id(firm_id=firm_id, client_id=client_id, title=req_body['title']):
        return response(False, {'msg': 'firm by this title exist'}, 409)

    # ELSE CHANGE AND UPDATE DB AND RETURN RESPONSE OK
    firm_service_db.update(firm_id=firm_id, client_id=client_id, req_body=req_body)
    return response(True, {'msg': 'firm successfully update'}, 200)


# DELETE FIRM BY ID
def firm_delete(firm_id, client_id):
    # GET FIRM BY ID AND VERIFY DIES EXIST. IF NO RETURN NOT FOUND
    if not firm_service_db.get_by_id_client_id(firm_id=firm_id, client_id=client_id):
        return response(False, {"msg": "firm by this id not found"}, 404)

    # GET USERS BY FIRM ID AND REMOVE BIND
    for user_id in firm_user_service_db.get_user_ids_by_firm_id(firm_id=firm_id):
        firm_user_service_db.delete_bind(firm_id=firm_id, user_id=user_id)

    # REMOVE THIS FIRM FROM DB
    firm_service_db.delete(firm_id=firm_id, client_id=client_id)
    return response(True, {'msg': "this firm successfully deleted"}, 200)

