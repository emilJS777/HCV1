from src._response import response
from src.models import Client, User
from flask import g


# GET USER IDS BY CLIENT ID
def get_user_ids_by_client_id(client_id):
    # GET ALL USERS WHICH CREATE USER
    users = User.query.filter_by(client_id=client_id, creator_id=g.user_id).all()

    # IN A CYCLE TO LOVE ID AND RETURN THE OPENER
    arr_user_ids=[]
    for user in users:
        arr_user_ids.append(user.id)

    return response(True, arr_user_ids, 200)


# BIND CLIENT USER
def bind_client_user(client_id, user_id):
    # GET USER AND CUSTOMER AND CHECK
    client = Client.query.filter_by(id=client_id, creator_id=g.user_id).first()
    user = User.query.filter_by(id=user_id, creator_id=g.user_id).first()

    #  IF ONE OF THEM DOES NOT EXIST RETURN NOT FOUND
    if not client or not user:
        return response(False, {'msg': 'client or/and user not found'}, 404)

    # IF THE USER HAS SUCH CLIENT ID RETURN ANSWER ABOUT THE EXISTENCE OF THIS RECORD
    if user.client_id == client_id:
        return response(False, {'msg': 'this client has such user'}, 409)

    #  ELSE DELETE USER'S CLIENT ID
    user.client_id = client_id
    user.update_db()
    return response(True, {'msg': 'client user successfully linked'}, 200)


# UNBIND CLIENT USER
def unbind_client_user(client_id, user_id):
    # GET USER AND CUSTOMER AND CHECK
    client = Client.query.filter_by(id=client_id, creator_id=g.user_id).first()
    user = User.query.filter_by(id=user_id, creator_id=g.user_id).first()

    # IF ONE OF THEM DOES NOT EXIST RETURN NOT FOUND
    if not client or not user:
        return response(False, {'msg': 'client or/and user not found'}, 404)

    # IF THE USER DOESN'T HAVE SUCH CLIENT ID, RETURN AN ANSWER ABOUT THE ABSENCE OF THIS RECORD
    if not user.client_id == client_id:
        return response(False, {'msg': 'the client does not have such a user'}, 409)

    user.client_id = None
    user.update_db()
    return response(True, {'msg': 'client user link successfully deleted'}, 200)
