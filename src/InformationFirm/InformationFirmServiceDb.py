from .InformationFirmModel import InformationFirm
from flask import g
from typing import List


# CREATE INFORMATION FIRM BIND
def create_bind(information_id: int, firm_id: int) -> InformationFirm:
    information_firm: InformationFirm = InformationFirm(information_id=information_id, firm_id=firm_id,
                                                        client_id=g.client_id)
    information_firm.save_db()
    return information_firm


# DELETE INFORMATION FIRM BIND
def delete_bind(information_id: int, firm_id: int) -> InformationFirm:
    information_firm: InformationFirm = InformationFirm.query.filter_by(information_id=information_id, firm_id=firm_id,
                                                                        client_id=g.client_id).first()
    information_firm.delete_db()
    return information_firm


# GET FIRM IDS BY INFORMATION ID
def get_firm_ids_by_information_id(information_id: int) -> List[int]:
    information_firms: List[InformationFirm] = InformationFirm.query.filter_by(information_id=information_id,
                                                                               client_id=g.client_id).all()
    firm_ids: List[int] = []
    for information_firm in information_firms:
        firm_ids.append(information_firm.firm_id)
    return firm_ids


# GET BY Information ID FIRM ID
def get_by_information_id_firm_id(information_id: int, firm_id: int) -> InformationFirm:
    information_firm: InformationFirm = InformationFirm.query.filter_by(information_id=information_id,
                                                                        firm_id=firm_id,
                                                                        client_id=g.client_id).first()
    return information_firm


# GET information IDS BY FIRM ID
def get_information_ids_by_firm_id(firm_id: int) -> List[int]:
    informations_firm: List[InformationFirm] = InformationFirm.query.filter_by(firm_id=firm_id, client_id=g.client_id).all()
    information_ids: List[int] = []

    for information_firm in informations_firm:
        information_firm.append(information_firm.information_id)
    return information_ids

