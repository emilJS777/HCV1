from flask import request
from src.services import client
from src.middleware import permission, auth


# CREATE NEW CLIENT
@auth.check_authorize
@permission.check_permission("create_client")
def client_post():
    req = request.get_json()
    res = client.client_create(client_name=req['name'])
    return res


# GET CREATE BY ID
@auth.check_authorize
@permission.check_permission("get_client_by_id")
def client_get_by_id(client_id):
    res = client.client_get_by_id(client_id=client_id)
    return res


# GET ALL CLIENT
@auth.check_authorize
@permission.check_permission("get_clients")
def client_get():
    res = client.client_get_all()
    return res


# UPDATE CLIENT BY ID
@auth.check_authorize
@permission.check_permission("update_client")
def client_update():
    req = request.get_json()
    res = client.client_update(client_id=req['id'], client_name=req['name'])
    return res


# DELETE CLIENT BY ID
@auth.check_authorize
@permission.check_permission("delete_client")
def client_delete():
    req = request.get_json()
    res = client.client_delete(client_id=req['id'])
    return res
