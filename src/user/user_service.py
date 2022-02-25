from src.client_user import client_user_service_db
from src.user_permission import user_permission_service_db
from . import user_service_db
from src._response import response
from src.firm_user import firm_user_service_db
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
def create_user_ticket(creator_id, client_id, firm_id):
    # CREATE USER AND VERIFY IF CREATOR TIED TO CLIENT means to bind the new user too
    user = user_service_db.create_ticket(creator_id=creator_id)

    # IF CLIENT ID EXIST BIND NEW USER AND CLIENT ID
    if client_id:
        client_user_service_db.create_bind(client_id=client_id, user_id=user.id)

    # IF FIRM ID EXIST BIND NEW USER AND FIRM ID
    if firm_id:
        firm_user_service_db.bind_firm_user(firm_id=firm_id, user_id=user.id)

    return response(True, {'id': user.id, 'ticket': user.ticket}, 200)


# USER GET BY ID
def user_get_by_id(user_id):
    # ELSE IF CLIENT ID EXIST RETURN ALL USERS BY CLIENT ID
    user = user_service_db.get_by_id(user_id=user_id)

    # # ELSE RETURN ALL USERS BY CREATOR ID
    # else:
    #     user = user_service_db.get_by_id_creator_id(user_id=user_id, creator_id=g.user_id)

    # IF USER NOT FOUND RETURN NOT FOUND
    if not user:
        return response(False, {'msg': 'user by this id not found'}, 404)

    # ELSE RETURN THIS USER AND STATUS OK
    return response(True, {'name': user.name, 'first_name': user.first_name, 'last_name': user.last_name}, 200)


# GET ALL USER
def user_get_all():
    users = user_service_db.get_all()
    return response(True, users, 200)


# UPDATE USER
def user_update(user_id, user_name, first_name, last_name):
    # GET USER BY ID AND VERIFY DOES IT EXIST. IF NO RETURN NOT FOUND
    user = user_service_db.get_by_id(user_id=user_id)
    if not user:
        return response(False, {'msg': 'user by this id not found'}, 404)

    # IF USER BY ThiS NAME FOUND RETURN CONFLICT
    if user_service_db.get_by_name(name=user_name):
        return response(False, {'msg': 'user name is taken'}, 409)

    # ELSE CHANGE AND UPDATE DB AND RETURN RESPONSE OK
    user_service_db.update(user_id=user_id, user_name=user_name,
                           first_name=first_name, last_name=last_name)
    return response(True, {'msg': 'user successfully update'}, 200)


# DELETE USER BY ID CLIENT ID
def user_delete(user_id):
    # IF CLIENT EXIST FIND USER BY ID AND THIS CLIENT ID
    # GET AND VERIFY IF CLiENT AND USER BY ID NOT FOUND RETURN NOT FOUND
    if not user_service_db.get_by_id(user_id=user_id):
        return response(False, {'msg': 'user not found'}, 404)

    # REMOVE THIS USER FROM DB AND THIS USER AND PERMISSION BIND
    user_service_db.delete(user_id=user_id)
    user_permission_service_db.delete_all_by_user_id(user_id=user_id)
    return response(True, {'msg': "this user successfully deleted"}, 200)
