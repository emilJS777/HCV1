from flask import request
from src.services import firm
from src.middleware import permission, auth, client


# CREATE NEW FIRM
@auth.check_authorize
@permission.check_permission("create_firm")
@client.check_client
def firm_post():
    req = request.get_json()
    res = firm.firm_create(firm_title=req['title'], firm_description=req['description'])
    return res


# GET FIRM BY ID
@auth.check_authorize
@permission.check_permission("get_firm_by_id")
@client.check_client
def firm_get_by_id(firm_id):
    res = firm.firm_get_by_id(firm_id=firm_id)
    return res


# GET ALL FIRM
@auth.check_authorize
@permission.check_permission("get_firms")
@client.check_client
def firm_get():
    res = firm.firm_get_all()
    return res


# UPDATE FIRM BY ID
@auth.check_authorize
@permission.check_permission("update_firm")
@client.check_client
def firm_update():
    req = request.get_json()
    res = firm.firm_update(firm_id=req['id'], firm_title=req['title'], firm_description=req['description'])
    return res


# DELETE FIRM BY ID
@auth.check_authorize
@permission.check_permission("delete_firm")
@client.check_client
def firm_delete():
    req = request.get_json()
    res = firm.firm_delete(firm_id=req['id'])
    return res
