from . import firm_user_service_db
from src.user import user_service_db
from src.firm import firm_service_db
from src._response import response
from flask import g


# GET USER IDS BY FIRM ID
def get_user_ids_by_firm_id(firm_id):
    # VERIFY IF FIRM BY ID AND CLIENT_ID NOT FOUND RETURN CODE 404
    if not firm_service_db.get_by_id_client_id(firm_id=firm_id, client_id=g.client_id):
        return response(False, {'msg': 'firm not found'}, 404)

    # GET USER IDS BY FIRM ID AND RETURN ARR USER IDS
    user_ids = firm_user_service_db.get_user_ids_by_firm_id(firm_id=firm_id)
    return response(True, user_ids, 200)


# BIND FIRM USER
def bind_firm_user(firm_id, user_id):
    #  IF ONE OF THEM DOES NOT EXIST RETURN NOT FOUND
    if not user_service_db.get_by_id_creator_id(user_id=user_id, creator_id=g.user_id) \
            or not firm_service_db.get_by_id_client_id(firm_id=firm_id, client_id=g.client_id):
        return response(False, {'msg': 'firm or/and user not found'}, 404)

    # IF THE USER HAS SUCH FIRM ID RETURN ANSWER ABOUT THE EXISTENCE OF THIS RECORD
    if firm_user_service_db.get_by_user_id_firm_id(user_id=user_id, firm_id=firm_id):
        return response(False, {'msg': 'this firm has such user'}, 409)

    #  ELSE ASSIGN USER FIRM ID
    firm_user_service_db.create_bind(firm_id=firm_id, user_id=user_id)
    return response(True, {'msg': 'firm user successfully linked'}, 200)


# UNBIND FIRM USER
def unbind_firm_user(firm_id, user_id):
    #  IF ONE OF THEM DOES NOT EXIST RETURN NOT FOUND
    if not user_service_db.get_by_id_creator_id(user_id=user_id, creator_id=g.user_id) \
            or not firm_service_db.get_by_id_client_id(firm_id=firm_id, client_id=g.client_id):
        return response(False, {'msg': 'firm or/and user not found'}, 404)

    # IF THE USER DOESN'T HAVE SUCH FIRM ID, RETURN AN ANSWER ABOUT THE ABSENCE OF THIS RECORD
    if not firm_user_service_db.get_by_user_id_firm_id(user_id=user_id, firm_id=firm_id):
        return response(False, {'msg': 'the client does not have such a user'}, 409)

    # ELSE ASSIGN USER FIRM ID NONE
    firm_user_service_db.delete_bind(firm_id=firm_id, user_id=user_id)
    return response(True, {'msg': 'firm user link successfully deleted'}, 200)
