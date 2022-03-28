from .user_firm_model import UserFirm
from typing import List


# CREATE BIND
def create_bind(user_id: int, firm_id: int) -> UserFirm:
    user_firm: UserFirm = UserFirm(user_id=user_id, firm_id=firm_id)
    user_firm.save_db()
    return user_firm


# DELETE BIND
def delete_bind(user_id: int, firm_id: int) -> UserFirm:
    user_firm: UserFirm = UserFirm.query.filter_by(user_id=user_id, firm_id=firm_id).first()
    user_firm.delete_db()
    return user_firm


# GET BY USER ID FIRM ID
def get_by_user_id_firm_id(user_id: int, firm_id: int) -> UserFirm:
    user_firm: UserFirm = UserFirm.query.filter_by(user_id=user_id, firm_id=firm_id).first()
    return user_firm


# GET FIRM IDS BY USER ID
def get_firm_ids_by_user_id(user_id: int) -> List[int]:
    user_firms: List[UserFirm] = UserFirm.query.filter_by(user_id=user_id).all()

    firm_ids: List[int] = []

    for user_firm in user_firms:
        firm_ids.append(user_firm.firm_id)

    return firm_ids
