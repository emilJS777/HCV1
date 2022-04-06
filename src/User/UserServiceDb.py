from .UserModel import User
from flask_bcrypt import generate_password_hash
from .UserHelper import generate_ticket_code
from flask import g
from sqlalchemy import or_, and_
from typing import List


def create(ticket, name, password):
    # CREATE AND RETURN NEW USER
    new_user = User.query.filter_by(ticket=ticket).first()
    new_user.name = name
    new_user.password_hash = generate_password_hash(password)
    new_user.ticket = None
    new_user.update_db()
    return new_user


def create_ticket(creator_id, full_name: str, client_id: int):
    # CREATE NEW USER AND TICKET
    user = User(ticket=generate_ticket_code(), creator_id=creator_id)
    user.client_id = client_id
    user.full_name = full_name
    user.save_db()
    return user


def update(user_id: int, full_name: str) -> User:
    # GET USER BY ID AND CREAtOR ID & UPDATE NAME
    user: User = User.query.filter_by(id=user_id).first()
    user.full_name = full_name
    user.update_db()
    return user


def delete(user_id):
    # GET USER BY USER ID AND CREATOR ID & DELETE
    user = User.query.filter_by(id=user_id).first()
    user.delete_db()
    return user


def get_by_name(name):
    # GET USER BY NAME AND RETURN
    user = User.query.filter_by(name=name).first()
    return user


def get_by_id(user_id):
    # GET USER BY ID \ for firm_id or client_id or super admin
    user = User.query.filter_by(id=user_id, client_id=g.client_id).first()
    return user


def get_by_ticket(ticket):
    # GET USER MODEL BY TICKET
    user = User.query.filter_by(ticket=ticket).first()
    return user


def get_by_id_creator_id(user_id, creator_id):
    # GET AND RETURN USER BY ID AND CREATOR ID
    user = User.query.filter_by(id=user_id, creator_id=creator_id).first()
    return user
#
#
# def get_by_id_client_id(user_id, client_id):
#     # GET AND RETURN USER BY FIRM ID
#     User = User.query.filter_by(id=user_id, client_id=client_id).first()
#     return User


def get_first_by_creator_id(creator_id):
    # GET FIRST USER BY CREATOR ID
    user = User.query.filter_by(creator_id=creator_id).first()
    return user


# def get_all_by_creator_id(creator_id):
#     arr = []
#     # GET ALL USER BY CREATOR ID
#     # ITERATE OVER ONE AT A TIME AND INSERT THE USER OBJECT INTO THE ARRAY
#     users = User.query.filter_by(creator_id=creator_id).all()
#     for User in users:
#         arr.append({'id': User.id, 'name': User.name})
#
#     return arr


def get_all() -> List:
    arr: List[dict] = []
    # GET ALL USER BY CLIENT ID
    # ITERATE OVER ONE AT A TIME AND INSERT THE USER OBJECT INTO THE ARRAY
    users: List[User] = User.query.filter_by(client_id=g.client_id).all()

    for user in users:
        arr.append({'id': user.id, 'name': user.name, 'full_name': user.full_name})

    return arr
