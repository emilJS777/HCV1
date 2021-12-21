from src.services_db import firm_service_db, firm_user_service_db
from src._response import response
from flask import g


# CREATE NEW FIRM
def firm_create(firm_title, firm_description):
    # IF FIND THIS FIRM NAME RETURN RESPONSE CONFLICT
    if firm_service_db.get_by_title_client_id(title=firm_title, client_id=g.client_id):
        return response(False, {'msg': 'firm title is taken'}, 409)

    # ELSE FIRM BY THIS NAME SAVE
    new_firm = firm_service_db.create(title=firm_title, description=firm_description, client_id=g.client_id)
    return response(True, {'msg': 'new firm by id {} successfully created'.format(new_firm.id)}, 200)


# FIRM GET BY ID
def firm_get_by_id(firm_id):
    # GET FIRM BY ID END VERIFY USER DOES IT EXIST
    # IF NO RETURN NOT FOUND
    firm = firm_service_db.get_by_id_client_id(firm_id=firm_id, client_id=g.client_id)
    if not firm:
        return response(False, {'msg': 'firm by this id not found'}, 404)

    # ELSE RETURN THIS FIRM AND STATUS OK
    return response(True, {'title': firm.title, 'description': firm.description}, 200)


# GET ALL FIRM
def firm_get_all():
    # GET ALL CLIENTS BY CLIENT ID
    firms_ids = firm_service_db.get_all_ids_by_client_id(client_id=g.client_id)
    return response(True, firms_ids, 200)


# UPDATE FIRM
def firm_update(firm_id, firm_title, firm_description):
    # GET FIRM BY ID AND VERIFY DOES IT EXIST. IF NO RETURN NOT FOUND
    if not firm_service_db.get_by_id_client_id(firm_id=firm_id, client_id=g.client_id):
        return response(False, {'msg': 'firm by this id not found'}, 404)

    # VERIFY IF THERE IS A FIRM WITH THE SAME TITLE RETURN CONFLICT
    if firm_service_db.get_by_client_id_title_exclude_id(firm_id=firm_id, client_id=g.client_id, title=firm_title):
        return response(False, {'msg': 'firm by this title exist'}, 409)

    # ELSE CHANGE AND UPDATE DB AND RETURN RESPONSE OK
    firm_service_db.update(firm_id=firm_id, client_id=g.client_id, title=firm_title, description=firm_description)
    return response(True, {'msg': 'firm successfully update'}, 200)


# DELETE FIRM BY ID
def firm_delete(firm_id):
    # GET FIRM BY ID AND VERIFY DIES EXIST. IF NO RETURN NOT FOUND
    if not firm_service_db.get_by_id_client_id(firm_id=firm_id, client_id=g.client_id):
        return response(False, {"msg": "firm by this id not found"}, 404)

    # GET USERS BY FIRM ID AND REMOVE BIND
    for user_id in firm_user_service_db.get_user_ids_by_firm_id(firm_id=firm_id):
        firm_user_service_db.delete_bind(firm_id=firm_id, user_id=user_id)

    # REMOVE THIS FIRM FROM DB
    firm_service_db.delete(firm_id=firm_id, client_id=g.client_id)
    return response(True, {'msg': "this firm successfully deleted"}, 200)

