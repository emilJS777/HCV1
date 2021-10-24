from src.models import Client, UserRole, Role, RolePermission
from src._response import response
from flask import g


# CREATE NEW CLIENT
def client_create(client_name):
    # IF FIND THIS CLIENT NAME RETURN RESPONSE CONFLICT
    if Client.query.filter_by(name=client_name, creator_id=g.user_id).first():
        return response(False, {'msg': 'client name is taken'}, 409)

    # ELSE CLIENT BY THIS NAME SAVE
    new_client = Client(name=client_name, creator_id=g.user_id)
    new_client.save_db()
    return response(True, {'msg': 'new client by id {} successfully created'.format(new_client.id)}, 200)


# CLIENT GET BY ID
def client_get_by_id(client_id):
    # GET CLIENT BY ID END VERIFY USER DOES IT EXIST
    # IF NO RETURN NOT FOUND
    client = Client.query.filter_by(id=client_id, creator_id=g.user_id).first()
    if not client:
        return response(False, {'msg': 'client by this id not found'}, 404)

    # ELSE RETURN THIS CLIENT AND STATUS OK
    return response(True, {'name': client.name}, 200)


# GET ALL CLIENT
def client_get_all():
    arr = []
    # GET ALL CLIENT
    clients = Client.query.filter_by(creator_id=g.user_id).all()

    # ITERATE OVER ONE AT A TIME AND INSERT THE CLIENT OBJECT INTO THE ARRAY
    for client in clients:
        arr.append({'id': client.id, 'name': client.name})
    return response(True, arr, 200)


# UPDATE CLIENT
def client_update(client_id, client_name):
    # GET CLIENT BY ID AND VERIFY DOES IT EXIST
    # IF NO RETURN NOT FOUND
    client = Client.query.filter_by(id=client_id, creator_id=g.user_id).first()
    if not client:
        return response(False, {'msg': 'client by this id not found'}, 404)

    # ELSE CHANGE AND UPDATE DB
    # AND RETURN RESPONSE OK
    client.name = client_name
    client.update_db()
    return response(True, {'msg': 'client successfully update'}, 200)


# DELETE CLIENT BY ID
def client_delete(client_id):
    # GET CLIENT BY ID AND VERIFY DIES EXIST
    # IF NO RETURN NOT FOUND
    client = Client.query.filter_by(id=client_id, creator_id=g.user_id).first()
    if not client:
        return response(False, {"msg": "client by this id not found"}, 404)

    # REMOVE THIS CLIENT FROM DB
    client.delete_db()
    return response(True, {'msg': "this client successfully deleted"}, 200)



