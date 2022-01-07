from src.models.firm_model import Firm
from sqlalchemy import not_


def create(req_body, client_id):
    # CREATE NEW FIRM AND RETURN
    new_firm = Firm(req_body['title'], req_body['activity_address'], req_body['legal_address'],
                    req_body['phone_number'], req_body['email_address'], req_body['tax_payer_number'],
                    req_body['state_register_number'], req_body['leader_position'], req_body['leader_full_name'],
                    req_body['accountant_position'], req_body['accountant_full_name'], req_body['cashier_full_name'],
                    client_id)
    new_firm.save_db()
    return new_firm


def update(firm_id, req_body, client_id):
    # GET FIRM BY ID AND UPDATE & RETURN
    firm = Firm.query.filter_by(id=firm_id, client_id=client_id).first()

    firm.title = req_body['title']
    firm.activity_address = req_body['activity_address']
    firm.legal_address = req_body['legal_address']
    firm.phone_number = req_body['phone_number']
    firm.email_address = req_body['email_address']
    firm.tax_payer_number = req_body['tax_payer_number']
    firm.state_register_number = req_body['state_register_number']
    firm.leader_position = req_body['leader_position']
    firm.leader_full_name = req_body['leader_full_name']
    firm.accountant_position = req_body['accountant_position']
    firm.accountant_full_name = req_body['accountant_full_name']
    firm.cashier_full_name = req_body['cashier_full_name']
    firm.update_db()
    return firm


def delete(firm_id, client_id):
    # GET FIRM BY ID AND CLIENT ID. DELETE AND RETURN
    firm = Firm.query.filter_by(id=firm_id, client_id=client_id).first()
    firm.delete_db()
    return firm


def get_by_title_client_id(title, client_id):
    # GET FIRM BY TITLE AND CLIENT ID & RETURN
    firm = Firm.query.filter_by(title=title, client_id=client_id).first()
    return firm


def get_by_id_client_id(firm_id, client_id):
    # GET FIRM BY ID AND CLIENT ID & RETURN
    firm = Firm.query.filter_by(id=firm_id, client_id=client_id).first()
    return firm


def get_all_ids_by_client_id(client_id):
    firms_arr = []
    # GET ALL FIRM BY THIS USER CLIENT ID
    # ITERATE OVER ONE AT A TIME AND INSERT THE FIRM OBJECT INTO THE ARRAY
    for firm in Firm.query.filter_by(client_id=client_id).all():
        firms_arr.append(firm.id)
    return firms_arr


def get_by_client_id_title_exclude_id(firm_id, client_id, title):
    # GET FIRM BY CLIENT ID TITLE, AND EXCLUDE FIRM ID
    firm = Firm.query.filter(Firm.id != firm_id, Firm.client_id == client_id, Firm.title == title).first()
    return firm
