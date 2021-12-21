from src.models.user_model import User


def create(name, password, creator_id):
    # CREATE AND RETURN NEW USER
    new_user = User(name=name, password=password, creator_id=creator_id)
    new_user.save_db()
    return new_user


def update(user_id, creator_id, user_name):
    # GET USER BY ID AND CREAtOR ID & UPDATE NAME
    user = User.query.filter_by(id=user_id, creator_id=creator_id).first()
    user.name = user_name
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
