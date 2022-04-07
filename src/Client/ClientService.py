from . import ClientServiceDb
from src._response import response
from flask import g


# CREATE NEW CLIENT
def client_create(name, description, max_count_firms):
    # IF FIND THIS CLIENT NAME RETURN RESPONSE CONFLICT
    if ClientServiceDb.get_by_name(name=name):
        return response(False, {'msg': 'Client name is taken'}, 409)

    # ELSE CLIENT BY THIS NAME SAVE
    new_client = ClientServiceDb.create(name=name,
                                        description=description,
                                        max_count_firms=max_count_firms,
                                        creator_id=g.user_id,
                                        parent_id=g.client_id
                                        )
    return response(True, {'msg': 'new Client by id {} successfully created'.format(new_client.id)}, 200)


# CLIENT GET BY ID
def client_get_by_id(client_id):
    # GET CLIENT BY ID END VERIFY USER DOES IT EXIST. IF NO RETURN NOT FOUND
    client = ClientServiceDb.get_by_id(client_id=client_id)
    if not client:
        return response(False, {'msg': 'Client by this id not found'}, 404)

    # ELSE RETURN THIS CLIENT AND STATUS OK
    return response(True, {'name': client.name, 'description': client.description,
                           'max_count_firms': client.max_count_firms}, 200)


# GET ALL CLIENT
def client_get_all():
    # GET ALL CLIENT IDS BY CREATOR ID
    client_ids = ClientServiceDb.get_all_ids()
    return response(True, client_ids, 200)


# UPDATE CLIENT
def client_update(client_id, name, description, max_count_firms):
    # GET CLIENT BY ID AND VERIFY DOES IT EXIST. IF NO RETURN NOT FOUND
    if not ClientServiceDb.get_by_id(client_id=client_id):
        return response(False, {'msg': 'Client by this id not found'}, 404)

    # IF CLIENT BY THIS NAME EXIST RETURN CONFLICT
    if ClientServiceDb.get_by_creator_id_name_exclude_id(client_id=client_id, name=name):
        return response(False, {'msg': 'Client by this name exist'}, 409)

    # ELSE CHANGE AND UPDATE DB, AND RETURN RESPONSE OK
    ClientServiceDb.update(client_id=client_id,
                           name=name,
                           description=description,
                           max_count_firms=max_count_firms)
    return response(True, {'msg': 'Client successfully update'}, 200)


# DELETE CLIENT BY ID
def client_delete(client_id):
    # GET CLIENT BY ID AND VERIFY DIES EXIST. IF NO RETURN NOT FOUND
    if not ClientServiceDb.get_by_id(client_id=client_id):
        return response(False, {"msg": "Client by this id not found"}, 404)

    # REMOVE THIS CLIENT FROM DB
    ClientServiceDb.delete(client_id=client_id)
    return response(True, {'msg': "this Client successfully deleted"}, 200)


