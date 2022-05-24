from src.Firm.FirmModel import Firm
from sqlalchemy import not_
from flask import g
from src.__general.helpers.paginate import get_page_items
from typing import List


def create(req_body):
    # CREATE NEW FIRM AND RETURN
    new_firm = Firm(
        title=req_body['title'],
        description=req_body['description'],
        activity_address=req_body['activity_address'],
        legal_address=req_body['legal_address'],
        phone_number=req_body['phone_number'],
        email_address=req_body['email_address'],
        tax_payer_number=req_body['tax_payer_number'],
        state_register_number=req_body['state_register_number'],
        insurer_account_number=req_body['insurer_account_number'],
        hvhh=req_body['hvhh'],
        leader_position=req_body['leader_position'],
        leader_full_name=req_body['leader_full_name'],
        accountant_position=req_body['accountant_position'],
        accountant_full_name=req_body['accountant_full_name'],
        cashier_full_name=req_body['cashier_full_name'],
        client_id=g.client_id)
    new_firm.save_db()
    return new_firm


def update(firm_id, req_body):
    # GET FIRM BY ID AND UPDATE & RETURN
    firm = Firm.query.filter_by(id=firm_id, client_id=g.client_id).first()

    firm.title = req_body['title']
    firm.description = req_body['description']
    firm.activity_address = req_body['activity_address']
    firm.legal_address = req_body['legal_address']
    firm.phone_number = req_body['phone_number']
    firm.email_address = req_body['email_address']
    firm.tax_payer_number = req_body['tax_payer_number']
    firm.state_register_number = req_body['state_register_number']
    firm.insurer_account_number = req_body['insurer_account_number']
    firm.hvhh = req_body['hvhh']
    firm.leader_position = req_body['leader_position']
    firm.leader_full_name = req_body['leader_full_name']
    firm.accountant_position = req_body['accountant_position']
    firm.accountant_full_name = req_body['accountant_full_name']
    firm.cashier_full_name = req_body['cashier_full_name']
    firm.update_db()
    return firm


def delete(firm_id):
    # GET FIRM BY ID AND CLIENT ID. DELETE AND RETURN
    firm = Firm.query.filter_by(id=firm_id, client_id=g.client_id).first()
    firm.delete_db()
    return firm


def get_by_title(title):
    # GET FIRM BY TITLE AND CLIENT ID & RETURN
    firm = Firm.query.filter_by(title=title, client_id=g.client_id).first()
    return firm


def get_by_id(firm_id):
    # GET FIRM BY ID AND CLIENT ID & RETURN
    firm = Firm.query.filter_by(id=firm_id, client_id=g.client_id).first()
    return firm


def get_all_ids() -> List[int]:
    firms_arr = []
    # GET ALL FIRM BY THIS USER CLIENT ID
    # ITERATE OVER ONE AT A TIME AND INSERT THE FIRM OBJECT INTO THE ARRAY
    for firm in Firm.query.filter_by(client_id=g.client_id).all():
        firms_arr.append(firm.id)
    return firms_arr


def get_all(page: int, per_page: int) -> dict:
    return get_page_items(
        Firm.query.filter_by(client_id=g.client_id)
            .order_by(-Firm.id)
            .paginate(page=page, per_page=per_page)
    )


def get_by_title_exclude_id(firm_id, title):
    # GET FIRM BY CLIENT ID TITLE, AND EXCLUDE FIRM ID
    firm = Firm.query.filter(Firm.id != firm_id, Firm.client_id == g.client_id, Firm.title == title).first()
    return firm
