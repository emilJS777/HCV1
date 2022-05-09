from src.ClientUser import ClientUserServiceDb
# from src.user_permission import user_permission_service_db
from . import UserServiceDb
from src._response import response


# CREATE NEW USER
def create_user(ticket, user_name, password):
    # IF TICKET NOT FOUND RETURN NOT FOUND
    if not UserServiceDb.get_by_ticket(ticket=ticket):
        return response(False, {'msg': 'ticket not found'}, 404)

    # IF FIND THIS USERNAME RETURN RESPONSE CONFLICT
    if UserServiceDb.get_by_name(name=user_name):
        return response(False, {'msg': 'User name is taken'}, 409)

    # ELSE USER BY THIS NAME SAVE
    new_user = UserServiceDb.create(ticket=ticket, name=user_name, password=password)
    return response(True, {'msg': 'new User by id {} successfully created'.format(new_user.id)}, 200)


# CREATE USER TICKET
def create_user_ticket(creator_id: int, full_name: str, client_id: int):
    # CREATE USER AND VERIFY IF CREATOR TIED TO CLIENT means to bind the new User too
    user = UserServiceDb.create_ticket(
        creator_id=creator_id,
        full_name=full_name,
        client_id=client_id)

    # IF CLIENT ID EXIST BIND NEW USER AND CLIENT ID
    ClientUserServiceDb.create_bind(
        client_id=client_id,
        user_id=user.id
    )

    return response(True, {'id': user.id, 'ticket': user.ticket}, 200)


# USER GET BY ID
def user_get_by_id(user_id):
    # ELSE IF CLIENT ID EXIST RETURN ALL USERS BY CLIENT ID
    user = UserServiceDb.get_by_id(user_id=user_id)

    # IF USER NOT FOUND RETURN NOT FOUND
    if not user:
        return response(False, {'msg': 'User by this id not found'}, 404)

    # ELSE RETURN THIS USER AND STATUS OK
    return response(True, {'id': user.id, 'name': user.name, 'full_name': user.full_name,
                           'position_id': user.position_id}, 200)


# GET ALL USER
def user_get_all(page: int, per_page: int):
    users: dict = UserServiceDb.get_all(page=page, per_page=per_page)
    return response(True, users, 200)


# UPDATE USER
def user_update(user_id: int, full_name: str):
    # GET USER BY ID AND VERIFY DOES IT EXIST. IF NO RETURN NOT FOUND
    user = UserServiceDb.get_by_id(user_id=user_id)
    if not user:
        return response(False, {'msg': 'User not found'}, 404)

    # ELSE CHANGE AND UPDATE DB AND RETURN RESPONSE OK
    UserServiceDb.update(user_id=user_id, full_name=full_name)
    return response(True, {'msg': 'User successfully update'}, 200)


# DELETE USER BY ID CLIENT ID
def user_delete(user_id):
    # IF CLIENT EXIST FIND USER BY ID AND THIS CLIENT ID
    # GET AND VERIFY IF CLiENT AND USER BY ID NOT FOUND RETURN NOT FOUND
    if not UserServiceDb.get_by_id(user_id=user_id):
        return response(False, {'msg': 'User not found'}, 404)

    # REMOVE THIS USER FROM DB AND THIS USER AND PERMISSION BIND
    UserServiceDb.delete(user_id=user_id)
    # user_permission_service_db.delete_all_by_user_id(user_id=user_id)
    return response(True, {'msg': "this User successfully deleted"}, 200)
