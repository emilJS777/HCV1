from .user_model import User
from flask_bcrypt import generate_password_hash
from .user_helper import generate_ticket_code


def create(ticket, name, password, first_name, last_name):
    # CREATE AND RETURN NEW USER
    new_user = User.query.filter_by(ticket=ticket).first()
    new_user.name = name
    new_user.password_hash = generate_password_hash(password)
    new_user.first_name = first_name
    new_user.last_name = last_name
    new_user.ticket = None
    new_user.update_db()
    return new_user


def create_ticket(creator_id):
    # CREATE NEW USER AND TICKET
    user = User(ticket=generate_ticket_code(), creator_id=creator_id)
    user.save_db()
    return user


def update(user_id, creator_id, user_name, first_name, last_name):
    # GET USER BY ID AND CREAtOR ID & UPDATE NAME
    user = User.query.filter_by(id=user_id, creator_id=creator_id).first()
    user.name = user_name
    user.first_name = first_name
    user.last_name = last_name
    user.update_db()
    return user


def delete(user_id, creator_id):
    # GET USER BY USER ID AND CREATOR ID & DELETE
    user = User.query.filter_by(id=user_id, creator_id=creator_id).first()
    user.delete_db()
    return user


def get_by_name(name):
    # GET USER BY NAME AND RETURN
    user = User.query.filter_by(name=name).first()
    return user


def get_by_id(user_id):
    # GET USER BY ID
    user = User.query.filter_by(id=user_id).first()
    return user


def get_by_ticket(ticket):
    # GET USER MODEL BY TICKET
    user = User.query.filter_by(ticket=ticket).first()
    return user


def get_by_id_creator_id(user_id, creator_id):
    # GET AND RETURN USER BY ID AND CREATOR ID
    user = User.query.filter_by(id=user_id, creator_id=creator_id).first()
    return user


def get_all_by_creator_id(creator_id):
    arr = []
    # GET ALL USER BY CREATOR ID
    # ITERATE OVER ONE AT A TIME AND INSERT THE USER OBJECT INTO THE ARRAY
    users = User.query.filter_by(creator_id=creator_id).all()
    for user in users:
        arr.append({'id': user.id, 'name': user.name})

    return arr
