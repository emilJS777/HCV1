from src.models.user import User


def delete_bind(firm_id, user_id):
    # GET USER AND DELETE BIND FIRM
    user = User.query.filter_by(id=user_id, firm_id=firm_id).first()
    user.firm_id = None
    user.update_db()


def get_by_user_id_firm_id(user_id, firm_id):
    # GET AND RETURN USER BY USER ID AND FIRM ID
    user = User.query.filter_by(id=user_id, firm_id=firm_id).first()
    return user


def create_bind(firm_id, user_id):
    # CREATE BIND BY FIRM ID AND USER ID WHERE CREATOR ID = CREATOR ID
    user = User.query.filter_by(id=user_id).first()
    user.firm_id = firm_id
    user.update_db()


def get_user_ids_by_firm_id(firm_id):
    arr_user_ids = []
    # GET ALL USERS WHICH CREATE USER IN A CYCLE TO LOVE ID AND RETURN THE OPENER
    for user in User.query.filter_by(firm_id=firm_id).all():
        arr_user_ids.append(user.id)
    return arr_user_ids
