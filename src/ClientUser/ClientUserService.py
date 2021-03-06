from . import ClientUserServiceDb
from src.User import UserServiceDb
from src.Client import ClientServiceDb
from src._response import response
from flask import g


# GET USER IDS BY CLIENT ID
def get_users_by_client_id(page: int, per_page: int, client_id: int):
    # GET ALL USERS WHICH CREATE USER
    users = ClientUserServiceDb.get_users_by_client_id(page=page, per_page=per_page, client_id=client_id)
    return response(True, users, 200)


# BIND CLIENT USER
def bind_client_user(client_id, user_id):
    #  IF ONE OF THEM DOES NOT EXIST RETURN NOT FOUND
    if not ClientServiceDb.get_by_id(client_id=client_id) \
            or not UserServiceDb.get_by_id_creator_id(user_id=user_id, creator_id=g.user_id):
        return response(False, {'msg': 'Client or/and User not found'}, 200)

    # IF THE USER HAS SUCH CLIENT ID RETURN ANSWER ABOUT THE EXISTENCE OF THIS RECORD
    if ClientUserServiceDb.get_by_user_id_client_id(user_id=user_id, client_id=client_id):
        return response(False, {'msg': 'this Client has such User'}, 200)

    #  ELSE BIND USER CLIENT ID
    ClientUserServiceDb.create_bind(client_id=client_id, user_id=user_id)
    return response(True, {'msg': 'Client User successfully linked'}, 200)


# UNBIND CLIENT USER
def unbind_client_user(client_id, user_id):
    #  IF ONE OF THEM DOES NOT EXIST RETURN NOT FOUND
    if not ClientServiceDb.get_by_id(client_id=client_id) \
            or not UserServiceDb.get_by_id_creator_id(user_id=user_id, creator_id=g.user_id):
        return response(False, {'msg': 'Client or/and User not found'}, 200)

    # IF THE USER DOESN'T HAVE SUCH CLIENT ID, RETURN AN ANSWER ABOUT THE ABSENCE OF THIS RECORD
    if not ClientUserServiceDb.get_by_user_id_client_id(user_id=user_id, client_id=client_id):
        return response(False, {'msg': 'the Client does not have such a User'}, 200)

    # GET USER BY ID AND REMOVE BIND ON CLIENT
    ClientUserServiceDb.delete_bind(client_id=client_id, user_id=user_id)
    return response(True, {'msg': 'Client User link successfully deleted'}, 200)
