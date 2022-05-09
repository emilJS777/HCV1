from src.User.UserModel import User
from src._general.helpers.paginate import get_page_items


def delete_bind(client_id, user_id):
    # GET USER AND DELETE BIND CLIENT
    user = User.query.filter_by(id=user_id, client_id=client_id).first()
    user.client_id = None
    user.update_db()


def get_users_by_client_id(page: int, per_page: int, client_id: int):
    # GET ALL USERS WHICH CREATE USER IN A CYCLE TO ID AND RETURN
    # arr_user_ids = []
    # for user in User.query.filter_by(client_id=client_id).all():
    #     arr_user_ids.append(user.id)
    # return arr_user_ids
    return get_page_items(User.query.filter_by(client_id=client_id).order_by(-User.id).paginate(page=page, per_page=per_page))




def get_by_user_id_client_id(user_id, client_id):
    # GET AND RETURN USER BY USER ID AND CLIENT ID
    user = User.query.filter_by(id=user_id, client_id=client_id).first()
    return user


def create_bind(client_id, user_id):
    # CREATE BIND BY CLIENT ID AND USER ID WHERE
    user = User.query.filter_by(id=user_id).first()
    user.client_id = client_id
    user.update_db()
