from .role_model import Role
from flask import g


def get_by_id(role_id):
    # GET BY ID AND RETURN
    role = Role.query.filter_by(id=role_id).first()
    return role


def get_by_name(name):
    # GET AND RETURN ROLE BY NAME AND CREATOR ID
    role = Role.query.filter_by(name=name).first()
    return role


def create(name, creator_id):
    # CREATE NEW ROLE ASSIGN NAME AND CREATOR ID
    role = Role(name=name, creator_id=creator_id)
    role.save_db()
    return role


def update(role_id, name):
    # GET ROLE BY ID AND ASSIGN NEW NAME & UPDATE
    role = Role.query.filter_by(id=role_id, creator_id=g.user_id).first()
    role.name = name
    role.update_db()
    return role


def delete(role_id):
    # GET ROLE BY ID DELETE AND RETURN
    role = Role.query.filter_by(id=role_id, creator_id=g.user_id).first()
    role.delete_db()
    return role


def get_all_ids():
    arr = []
    # GET ALL ROLE
    # ITERATE OVER ONE AT A TIME AND INSERT THE ROLE OBJECT INTO THE ARRAY
    for role in Role.query.filter(Role.creator_id != None).all():
        arr.append({'id': role.id, 'name': role.name})

    return arr
