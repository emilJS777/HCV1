from src.user_role import user_role_service_db
from src.client_user import client_user_service_db
from src.firm_user import firm_user_service_db
from . import user_service_db
from src._response import response
from flask import g


# CREATE NEW USER
def create_user(ticket, user_name, password, first_name, last_name):
    # IF TICKET NOT FOUND RETURN NOT FOUND
    if not user_service_db.get_by_ticket(ticket=ticket):
        return response(False, {'msg': 'ticket not found'}, 404)

    # IF FIND THIS USERNAME RETURN RESPONSE CONFLICT
    if user_service_db.get_by_name(name=user_name):
        return response(False, {'msg': 'user name is taken'}, 409)

    # ELSE USER BY THIS NAME SAVE
    new_user = user_service_db.create(ticket=ticket, name=user_name, password=password,
                                      first_name=first_name, last_name=last_name)
    return response(True, {'msg': 'new user by id {} successfully created'.format(new_user.id)}, 200)


# CREATE USER TICKET
def create_user_ticket(creator_id):
    creator = user_service_db.get_by_id(user_id=creator_id)
    user = user_service_db.create_ticket(creator_id=creator_id)

    # IF CREATOR USER HAS CLIENT ID BIND NEW USER AND THIS CLIENT ID
    if creator.client_id:
        client_user_service_db.create_bind(client_id=creator.client_id, user_id=user.id)

    # IF CREATOR USER HAS FIRM ID BIND NEW USER AND THIS FIRM ID
    if creator.firm_id:
        firm_user_service_db.create_bind(firm_id=creator.firm_id, user_id=user.id)

    return response(True, {'id': user.id, 'ticket': user.ticket}, 200)


# USER GET BY ID
def user_get_by_id(user_id):
    # GET USER BY ID END VERIFY USER DOES IT EXIST. IF NO RETURN NOT FOUND
    user = user_service_db.get_by_id_creator_id(user_id=user_id, creator_id=g.user_id)
    if not user:
        return response(False, {'msg': 'user by this id not found'}, 404)

    # ELSE RETURN THIS USER AND STATUS OK
    return response(True, {'name': user.name, 'first_name': user.first_name, 'last_name': user.last_name}, 200)


# GET ALL USER
def user_get_all():
    # GET AND RETURN USERS BY CREATOR ID
    users = user_service_db.get_all_by_creator_id(creator_id=g.user_id)
    return response(True, users, 200)


# UPDATE USER
def user_update(user_id, user_name, first_name, last_name):
    # GET USER BY ID AND VERIFY DOES IT EXIST. IF NO RETURN NOT FOUND
    user = user_service_db.get_by_id_creator_id(user_id=user_id, creator_id=g.user_id)
    if not user:
        return response(False, {'msg': 'user by this id not found'}, 404)

    # IF USER BY ThiS NAME FOUND RETURN CONFLICT
    if user_service_db.get_by_name(name=user_name):
        return response(False, {'msg': 'user name is taken'}, 409)

    # ELSE CHANGE AND UPDATE DB AND RETURN RESPONSE OK
    user_service_db.update(user_id=user_id, creator_id=g.user_id, user_name=user_name,
                           first_name=first_name, last_name=last_name)
    return response(True, {'msg': 'user successfully update'}, 200)


# DELETE USER BY ID
def user_delete(user_id):
    # GET USER BY ID AND VERIFY DIES EXIST IF NO RETURN NOT FOUND
    if not user_service_db.get_by_id_creator_id(user_id=user_id, creator_id=g.user_id):
        return response(False, {"msg": "user by this id not found"}, 404)

    # GETS ALL CONNECTIONS WITH ROLE AND REMOVE
    user_role_service_db.delete_all_by_user_id(user_id=user_id)

    # REMOVE THIS USER FROM DB
    user_service_db.delete(user_id=user_id, creator_id=g.user_id)
    return response(True, {'msg': "this user successfully deleted"}, 200)
