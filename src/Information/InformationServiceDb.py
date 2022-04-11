from .InformationModel import Information
from flask import g
from typing import List


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


def get_all() -> List:
    # GET ALL information
    informations: List[Information] = Information.query.filter_by(client_id=g.client_id).all()
    arr: List = []

    for information in informations:
        arr.append({'id': information.id,
                    'title': information.title,
                    'description': information.description,
                    'unit_id': information.unit_id})
    return arr


def get_by_id(information_id: int) -> Information:
    # GET information BY ID
    information: Information = Information.query.filter_by(id=information_id, client_id=g.client_id).first()
    return information
