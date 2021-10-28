from src.models.firm import Firm
from sqlalchemy import not_


def create(title, description, client_id):
    # CREATE NEW FIRM AND RETURN
    new_firm = Firm(title=title, description=description, client_id=client_id)
    new_firm.save_db()
    return new_firm


def update(firm_id, client_id, title, description):
    # GET FIRM BY ID AND UPDATE & RETURN
    firm = Firm.query.filter_by(id=firm_id, client_id=client_id).first()
    firm.title = title
    firm.description = description
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
