from src.models import Firm, Client, User
from src._response import response
from flask import g


# CREATE NEW FIRM
def firm_create(firm_title, firm_description):
    # FIND USER AND VERIFY DOES THE USER HAVE A CLIENT ID
    user = User.query.filter_by(id=g.user_id).first()
    client = Client.query.filter_by(id=user.client_id).first()

    if not client:
        return response(False, {'msg': 'you do not have a client, create a client'}, 404)

    # IF FIND THIS FIRM NAME RETURN RESPONSE CONFLICT
    if Firm.query.filter_by(title=firm_title, client_id=client.id).first():
        return response(False, {'msg': 'firm title is taken'}, 409)

    # ELSE FIRM BY THIS NAME SAVE
    new_firm = Firm(title=firm_title, description=firm_description, client_id=client.id)
    new_firm.save_db()
    return response(True, {'msg': 'new firm by id {} successfully created'.format(new_firm.id)}, 200)


# FIRM GET BY ID
def firm_get_by_id(firm_id):
    # GET FIRM BY ID END VERIFY USER DOES IT EXIST
    # IF NO RETURN NOT FOUND
    user = User.query.filter_by(id=g.user_id).first()
    firm = Firm.query.filter_by(id=firm_id, client_id=user.client_id).first()
    if not firm:
        return response(False, {'msg': 'firm by this id not found'}, 404)

    # ELSE RETURN THIS FIRM AND STATUS OK
    return response(True, {'title': firm.title, 'description': firm.description}, 200)


# GET ALL FIRM
def firm_get_all():
    arr = []
    # GET ALL FIRM BY THIS USER CLIENT ID
    user = User.query.filter_by(id=g.user_id).first()
    firms = Firm.query.filter_by(client_id=user.client_id).all()

    # ITERATE OVER ONE AT A TIME AND INSERT THE FIRM OBJECT INTO THE ARRAY
    for firm in firms:
        arr.append({'id': firm.id, 'title': firm.title})
    return response(True, arr, 200)


# UPDATE FIRM
def firm_update(firm_id, firm_title, firm_description):
    # GET FIRM BY ID AND VERIFY DOES IT EXIST
    # IF NO RETURN NOT FOUND
    user = User.query.filter_by(id=g.user_id).first()
    firm = Firm.query.filter_by(id=firm_id, client_id=user.client_id).first()
    if not firm:
        return response(False, {'msg': 'firm by this id not found'}, 404)

    # ELSE CHANGE AND UPDATE DB
    # AND RETURN RESPONSE OK
    firm.title = firm_title
    firm.description = firm_description
    firm.update_db()
    return response(True, {'msg': 'firm successfully update'}, 200)


# DELETE FIRM BY ID
def firm_delete(firm_id):
    # GET FIRM BY ID AND VERIFY DIES EXIST
    # IF NO RETURN NOT FOUND
    user = User.query.filter_by(id=g.user_id).first()
    firm = Firm.query.filter_by(id=firm_id, client_id=user.client_id).first()
    if not firm:
        return response(False, {"msg": "firm by this id not found"}, 404)

    # REMOVE THIS FIRM FROM DB
    firm.delete_db()
    return response(True, {'msg': "this firm successfully deleted"}, 200)

