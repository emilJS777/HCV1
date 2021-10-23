from src.models import User, UserRole
from src._response import response


# CREATE NEW USER
def user_create(user_name, password):
    # IF FIND THIS USER NAME RETURN RESPONSE CONFLICT
    if User.query.filter_by(name=user_name).first():
        return response(False, {'msg': 'user name is taken'}, 409)

    # ELSE USER BY THIS NAME SAVE
    new_user = User(name=user_name, password=password)
    new_user.save_db()
    return response(True, {'msg': 'new user by id {} successfully created'.format(new_user.id)}, 200)


# ROLE GET BY ID
def user_get_by_id(user_id):
    # GET USER BY ID END VERIFY USER DOES IT EXIST
    # IF NO RETURN NOT FOUND
    user = User.query.filter_by(id=user_id).first()
    if not user:
        return response(False, {'msg': 'user by this id not found'}, 404)

    # ELSE RETURN THIS USER AND STATUS OK
    return response(True, {'name': user.name}, 200)


# GET ALL USER
def user_get_all():
    arr = []
    # GET ALL USER
    users = User.query.all()

    # ITERATE OVER ONE AT A TIME AND INSERT THE USER OBJECT INTO THE ARRAY
    for user in users:
        arr.append({'id': user.id, 'name': user.name})
    return response(True, arr, 200)


# UPDATE USER
def user_update(user_id, user_name):
    # GET USER BY ID AND VERIFY DOES IT EXIST
    # IF NO RETURN NOT FOUND
    user = User.query.filter_by(id=user_id).first()
    if not user:
        return response(False, {'msg': 'user by this id not found'}, 404)

    # ELSE CHANGE AND UPDATE DB
    # AND RETURN RESPONSE OK
    user.name = user_name
    user.update_db()
    return response(True, {'msg': 'user successfully update'}, 200)


# DELETE ROLE BY ID
def user_delete(user_id):
    # GET USER BY ID AND VERIFY DIES EXIST
    # IF NO RETURN NOT FOUND
    user = User.query.filter_by(id=user_id).first()
    if not user:
        return response(False, {"msg": "user by this id not found"}, 404)

    # GETS ALL CONNECTIONS WITH ROLE AND REMOVE
    user_roles = UserRole.query.filter_by(user_id=user_id).all()
    for user_role in user_roles:
        user_role.delete_db()

    # REMOVE THIS USER FROM DB
    user.delete_db()
    return response(True, {'msg': "this user successfully deleted"}, 200)

