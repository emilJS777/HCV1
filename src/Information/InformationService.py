from . import InformationServiceDb
from .InformationServiceDb import Information
from src._response import response
from typing import List
from src.InformationFirm import InformationFirmServiceDb


# CREATE information
def create_information(title: str, description: str):
    # GET information BY TITLE AND VERIFY IF EXIST RETURN CONFLICT
    if InformationServiceDb.get_by_title(title=title):
        return response(False, {'msg': f'Information by title {title} exist'}, 409)

    # ELSE SAVE NEW information AND RETURN
    InformationServiceDb.create(title=title, description=description)
    return response(True, {'msg': 'new Information successfully created'}, 200)


# DELETE information
def delete_information(information_id: int):
    # GET information BY IF AND VERIFY IF NOT FOUND RETURN NOT FOUND
    if not InformationServiceDb.get_by_id(information_id=information_id):
        return response(False, {'msg': f'Information by id {information_id} not found'}, 404)

    # FET ALL FIRM IDS WHERE IS BINDED THIS INFORMATION ID IND DELETE ALL BIND
    for firm_id in InformationFirmServiceDb.get_firm_ids_by_information_id(information_id):
        InformationFirmServiceDb.delete_bind(
            information_id=information_id,
            firm_id=firm_id
        )

    # ELSE DELETE THIS information BY ID AND RETURN OK
    InformationServiceDb.delete(information_id=information_id)
    return response(True, {'msg': 'Information successfully deleted!'}, 200)


# UPDATE information
def update_information(information_id: int, title: str, description: str):
    # GET information BY ID AND VERIFY IF NOT FOUND RETURN NOT FOUND
    if not InformationServiceDb.get_by_id(information_id=information_id):
        return response(False, {'msg': f'Information by id {information_id} not found'}, 404)

    # ELSE UPDATE information BY ID AND RETURN OK
    InformationServiceDb.update(information_id=information_id, title=title, description=description)
    return response(True, {'msg': 'Information successfully updated!'}, 200)


# GET ALL information
def get_all_information():
    informations: List = InformationServiceDb.get_all()
    return response(True, informations, 200)


# GET information BY ID
def get_information_by_id(information_id: int):
    information: Information = InformationServiceDb.get_by_id(information_id=information_id)
    # GET information BY ID AND VERIFY. IF NOT FOUND RETURN NOT FOUND
    if not information:
        return response(False, {'msg': f'Information by id {information_id} not found'}, 404)

    # ELSE RETURN information & OK
    return response(True, {'id': information.id, 'title': information.title, 'description': information.description}, 200)
