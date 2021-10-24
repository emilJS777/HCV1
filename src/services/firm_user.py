from src._response import response
from src.models import Firm, User
from flask import g


# GET USER IDS BY FIRM ID
def get_user_ids_by_firm_id(firm_id):
    # GET ALL USERS WHICH CREATE USER
    users = User.query.filter_by(firm_id=firm_id, creator_id=g.user_id).all()

    # IN A CYCLE TO LOVE ID AND RETURN THE OPENER
    arr_user_ids=[]
    for user in users:
        arr_user_ids.append(user.id)

    return response(True, arr_user_ids, 200)


# BIND FIRM USER
def bind_firm_user(firm_id, user_id):
    # GET USER AND FIRM AND CHECK
    user = User.query.filter_by(id=g.user_id).first()
    employee = User.query.filter_by(id=user_id, creator_id=g.user_id).first()
    firm = Firm.query.filter_by(id=firm_id, client_id=user.client_id).first()

    #  IF ONE OF THEM DOES NOT EXIST RETURN NOT FOUND
    if not employee or not firm:
        return response(False, {'msg': 'firm or/and user not found'}, 404)

    # IF THE USER HAS SUCH FIRM ID RETURN ANSWER ABOUT THE EXISTENCE OF THIS RECORD
    if employee.firm_id == firm_id:
        return response(False, {'msg': 'this firm has such user'}, 409)

    #  ELSE DELETE USER'S CLIENT ID
    employee.firm_id = firm_id
    employee.update_db()
    return response(True, {'msg': 'firm user successfully linked'}, 200)


# UNBIND FIRM USER
def unbind_firm_user(firm_id, user_id):
    # GET USER AND FIRM AND CHECK
    user = User.query.filter_by(id=g.user_id).first()
    firm = Firm.query.filter_by(id=firm_id, client_id=user.client_id).first()
    employee = User.query.filter_by(id=user_id, firm_id=firm_id).first()

    # IF ONE OF THEM DOES NOT EXIST RETURN NOT FOUND
    if not firm or not employee:
        return response(False, {'msg': 'firm or/and user not found'}, 404)

    # IF THE USER DOESN'T HAVE SUCH FIRM ID, RETURN AN ANSWER ABOUT THE ABSENCE OF THIS RECORD
    if not employee.firm_id == firm_id:
        return response(False, {'msg': 'the client does not have such a user'}, 409)

    employee.firm_id = None
    employee.update_db()
    return response(True, {'msg': 'firm user link successfully deleted'}, 200)
