from .CategoryFirmModel import CategoryFirm
from flask import g
from typing import List


# CREATE CATEGORY FIRM BIND
def create_bind(category_id: int, firm_id: int) -> CategoryFirm:
    category_firm: CategoryFirm = CategoryFirm(category_id=category_id, firm_id=firm_id,
                                               client_id=g.client_id)
    category_firm.save_db()
    return category_firm


# DELETE CATEGORY FIRM BIND
def delete_bind(category_id: int, firm_id: int) -> CategoryFirm:
    category_firm: CategoryFirm = CategoryFirm.query.filter_by(category_id=category_id, firm_id=firm_id,
                                                               client_id=g.client_id).first()
    category_firm.delete_db()
    return category_firm


# GET FIRM IDS BY CATEGORY ID
def get_firm_ids_by_category_id(category_id: int) -> List[int]:
    category_firms: List[CategoryFirm] = CategoryFirm.query.filter_by(category_id=category_id,
                                                                      client_id=g.client_id).all()
    firm_ids: List[int] = []
    for category_firm in category_firms:
        firm_ids.append(category_firm.firm_id)
    return firm_ids


# GET BY CATEGORY ID FIRM ID
def get_by_category_id_firm_id(category_id: int, firm_id: int) -> CategoryFirm:
    category_firm: CategoryFirm = CategoryFirm.query.filter_by(category_id=category_id, firm_id=firm_id,
                                                               client_id=g.client_id).first()
    return category_firm


# GET CATEGORY IDS BY FIRM ID
def get_category_ids_by_firm_id(firm_id: int) -> List[int]:
    categories_firm: List[CategoryFirm] = CategoryFirm.query.filter_by(firm_id=firm_id, client_id=g.client_id).all()
    category_ids: List[int] = []
    for category_firm in categories_firm:
        category_ids.append(category_firm.category_id)
    return category_ids

