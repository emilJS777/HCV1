from src.services_db import client_service_db, firm_service_db, firm_user_service_db
from src._response import response
from flask import g


# CREATE NEW CLIENT
def client_create(client_name):
    # IF FIND THIS CLIENT NAME RETURN RESPONSE CONFLICT
    if client_service_db.get_by_name_creator_id(client_name=client_name, creator_id=g.user_id):
        return response(False, {'msg': 'client name is taken'}, 409)

    # ELSE CLIENT BY THIS NAME SAVE
    new_client = client_service_db.create(client_name=client_name, creator_id=g.user_id)
    return response(True, {'msg': 'new client by id {} successfully created'.format(new_client.id)}, 200)


# CLIENT GET BY ID
def client_get_by_id(client_id):
    # GET CLIENT BY ID END VERIFY USER DOES IT EXIST
    # IF NO RETURN NOT FOUND
    client = client_service_db.get_by_id_creator_id(client_id=client_id, creator_id=g.user_id)
    if not client:
        return response(False, {'msg': 'client by this id not found'}, 404)

    # ELSE RETURN THIS CLIENT AND STATUS OK
    return response(True, {'name': client.name}, 200)


# GET ALL CLIENT
def client_get_all():
    # GET ALL CLIENT IDS BY CREATOR ID
    client_ids = client_service_db.get_all_ids_by_creator_id(creator_id=g.user_id)
    return response(True, client_ids, 200)


# UPDATE CLIENT
def client_update(client_id, client_name):
    # GET CLIENT BY ID AND VERIFY DOES IT EXIST. IF NO RETURN NOT FOUND
    if not client_service_db.get_by_id_creator_id(client_id=client_id, creator_id=g.user_id):
        return response(False, {'msg': 'client by this id not found'}, 404)

    # IF CLIENT BY THIS NAME EXIST RETURN CONFLICT
    if client_service_db.get_by_creator_id_name_exclude_id(client_id=client_id, creator_id=g.user_id, name=client_name):
        return response(False, {'msg': 'client by this name exist'}, 409)

    # ELSE CHANGE AND UPDATE DB, AND RETURN RESPONSE OK
    client_service_db.update(client_id=client_id, name=client_name)
    return response(True, {'msg': 'client successfully update'}, 200)


# DELETE CLIENT BY ID
def client_delete(client_id):
    # GET CLIENT BY ID AND VERIFY DIES EXIST. IF NO RETURN NOT FOUND
    if not client_service_db.get_by_id_creator_id(client_id=client_id, creator_id=g.user_id):
        return response(False, {"msg": "client by this id not found"}, 404)

    # GET ALL FIRMS BY THIS CLIENT ID AND REMOVE ALL
    for firm_id in firm_service_db.get_all_ids_by_client_id(client_id=client_id):
        firm_service_db.delete(firm_id=firm_id, client_id=client_id)

        # GET ALL FIRM_USER LINKS AND REMOVE
        for user_id in firm_user_service_db.get_user_ids_by_firm_id(firm_id=firm_id):
            firm_user_service_db.delete_bind(firm_id=firm_id, user_id=user_id)

    # REMOVE THIS CLIENT FROM DB
    client_service_db.delete(client_id=client_id, creator_id=g.user_id)
    return response(True, {'msg': "this client successfully deleted"}, 200)



