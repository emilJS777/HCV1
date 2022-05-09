from src.User.UserModel import User
from typing import List
from flask import g
from src._general.helpers.paginate import get_page_items


def bind_user_position(user_id: int, position_id: int) -> User:
    user: User = User.query.filter_by(id=user_id).first()
    user.position_id = position_id
    user.update_db()
    return user


def unbind_user_position(user_id: int, position_id: int) -> User:
    user: User = User.query.filter_by(id=user_id, position_id=position_id).first()
    user.position_id = None
    user.update_db()
    return user


def get_users_by_position_id(position_id: int, page: int, per_page: int) -> dict:
    # users: List[User] = User.query.filter_by(position_id=position_id, firm_id=g.firm_id).all() \
    #     if g.firm_id else \
    #     User.query.filter_by(position_id=position_id, client_id=g.client_id).all()
    # user_ids: List[int] = []
    # for user in users:
    #     user_ids.append(user.id)
    # return user_ids
    return get_page_items(
        User.query.filter_by(position_id=position_id, client_id=g.client_id)
            .order_by(-User.id)
            .paginate(page=page, per_page=per_page)
    )

