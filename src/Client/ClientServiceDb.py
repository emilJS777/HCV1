from .ClientModel import Client
from flask import g
from src._general.helpers.paginate import get_page_items


def create(name: str, description: str, max_count_firms: int, creator_id: int or None, parent_id: int or None):
    # CREATE NEW CLIENT ASSIGN NAME AND CREATOR ID & RETURN
    new_client = Client(
        name=name,
        description=description,
        max_count_firms=max_count_firms,
        creator_id=creator_id,
        parent_id=parent_id
    )
    new_client.save_db()
    return new_client


def update(client_id: int, name: str, max_count_firms: int, description: str):
    # GET CLIENT BY ID AND UPDATE & RETURN
    client = Client.query.filter_by(id=client_id).first()
    client.name = name
    client.description = description
    client.max_count_firms = max_count_firms
    client.update_db()
    return client


def delete(client_id: int) -> Client:
    # GET CLIENT BY ID AND CREATOR ID. DELETE AND RETURN
    client = Client.query.filter_by(id=client_id, parent_id=g.client_id).first()
    client.delete_db()
    return client


def get_self_client() -> Client:
    # GET CLIENT REQUESTER USER
    client: Client = Client.query.filter_by(id=g.client_id).first()
    return client


def get_by_id(client_id: int):
    # GET CLIENT BY ID AND return
    client = Client.query.filter_by(id=client_id, parent_id=g.client_id).first()
    return client


def get_by_name(name: str):
    # GET CLIENT BY NAME AND CREATOR ID & RETURN
    client = Client.query.filter_by(name=name, parent_id=g.client_id).first()
    return client


# def get_by_id_creator_id(client_id, creator_id):
#     # GET CLIENT BY ID AND CREATOR ID & RETURN
#     Client = Client.query.filter_by(id=client_id, creator_id=creator_id).first()
#     return Client

def get_all_clients(page, per_page):
    # GET ALL CLIENT, ITERATE OVER ONE AT A TIME AND INSERT THE CLIENT OBJECT INTO THE ARRAY

    # client_ids = []
    # for client in Client.query.filter_by(parent_id=g.client_id).all():
    #     client_ids.append(client.id)
    # return client_ids
    return get_page_items(Client.query.filter_by(parent_id=g.client_id).order_by(-Client.id).paginate(page=page, per_page=per_page))


def get_by_creator_id_name_exclude_id(client_id, name):
    # GET CLIENT BY CREATOR ID, NAME, AND EXCLUDE CLIENT ID
    client = Client.query.filter(Client.id != client_id, Client.parent_id == g.client_id, Client.name == name).first()
    return client


def get_first_client() -> Client:
    # GET FIRST CLIENT
    client: Client = Client.query.first()
    return client
