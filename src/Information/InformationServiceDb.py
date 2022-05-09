from .InformationModel import Information
from flask import g
from typing import List
from src._general.helpers.paginate import get_page_items


units: List[dict] = [{'id': 1, 'title': 'հատ'}, {'id': 2, 'title': 'կգ'}, {'id': 3, 'title': 'խորանարդ'}]


def create(title: str, description: str, unit_id: int) -> Information:
    # CREATE NEW information
    information: Information = Information(
        title=title,
        description=description,
        unit_id=unit_id,
        client_id=g.client_id
    )
    information.save_db()
    return information


def delete(information_id: int) -> Information:
    # DELETE information BY ID
    information: Information = Information.query.filter_by(id=information_id, client_id=g.client_id).first()
    information.delete_db()
    return information


def update(information_id: int, title: str, description: str, unit_id: int) -> Information:
    # UPDATE information BY ID
    information: Information = Information.query.filter_by(id=information_id, client_id=g.client_id).first()
    information.title = title
    information.description = description
    information.unit_id = unit_id
    information.update_db()
    return information


def get_by_title(title: str) -> Information:
    # GET information BY TITLE
    information: Information = Information.query.filter_by(title=title, client_id=g.client_id).first()
    return information


def get_all(page: int, per_page: int) -> dict:
    # # GET ALL information
    # informations: List[Information] = Information.query.filter_by(client_id=g.client_id).all()
    # arr: List = []
    #
    # for information in informations:
    #     arr.append({'id': information.id,
    #                 'title': information.title,
    #                 'description': information.description,
    #                 'unit_id': information.unit_id})
    # return arr
    return get_page_items(
        Information.query.filter_by(client_id=g.client_id)
            .order_by(-Information.id)
            .paginate(page=page, per_page=per_page)
    )


def get_by_id(information_id: int) -> Information:
    # GET information BY ID
    information: Information = Information.query.filter_by(id=information_id, client_id=g.client_id).first()
    return information


# GET UNIT BY ID
def unit_get_by_id(unit_id: int) -> dict:
    for unit in units:
        if unit['id'] == unit_id:
            return unit


# GET ALL UNITS
def unit_get_all() -> List[dict]:
    return units

