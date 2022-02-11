from . import email_service_db
from src._response import response
from flask import g


# CREATE NEW EMAIL
def email_create(address):
    # GET EMAIL BY USER ID AND VERIFY. IF EMAIL EXIST RETURN CONFLICT
    if email_service_db.get_by_user_id(user_id=g.user_id):
        return response(False, {'msg': 'you already have an email'}, 409)

    # GET EMAIL BY ADDRESS AND VERIFY. IF ADDRESS EXIST RETURN CONFLICT
    if email_service_db.get_by_address(address=address):
        return response(False, {'msg': 'the address already exists in the system'}, 409)

    # ELSE CREATE NEW EMAIL ADDRESS FOR USER AND RETURN OK
    else:
        email = email_service_db.create(address=address, user_id=g.user_id)
        return response(True, {'msg': f'email by address {email.address} successfully created, '
                                      f'an activation code has been sent to your address'}, 200)


# UPDATE EMAIL
def email_update(address):
    # GET EMAIL BY USER ID AND VERIFY. IF EMAIL NOT EXIST RETURN NOT FOUND
    if not email_service_db.get_by_user_id(user_id=g.user_id):
        return response(False, {'msg': 'email address not found'}, 404)

    # GET EMAIL BY ADDRESS AND VERIFY. IF ADDRESS EXIST RETURN CONFLICT
    if email_service_db.get_by_address(address=address):
        return response(False, {'msg': 'the address already exists in the system'}, 409)

    # ELSE UPDATE EMAIL ADDRESS BY USER ID AND RETURN OK
    else:
        email = email_service_db.update(address=address, user_id=g.user_id)
        return response(True, {'msg': f'your email address successfully updated on {email.address}, '
                                      f'an activation code has been sent to your address'}, 200)


# DELETE EMAIL
def email_delete():
    # GET EMAIL BY USER ID AND VERIFY. IF EMAIL NOT EXIST RETURN NOT FOUND
    if not email_service_db.get_by_user_id(user_id=g.user_id):
        return response(False, {'msg': 'email address not found'}, 404)

    # ELSE DELETE EMAIL BY USER ID AND RETURN OK
    else:
        email = email_service_db.delete(user_id=g.user_id)
        return response(True, {'msg': f'your email {email.address} successfully deleted'}, 200)


# GET EMAIL BY USER ID
def email_get_by_user_id(user_id):
    # GET EMAIL BY USER ID AND VERIFY. IF NOT FOUND RETURN NOT FOUND
    email = email_service_db.get_by_user_id(user_id=user_id)
    if not email:
        return response(False, {'msg': 'email not found'}, 404)

    # ELSE RETURN EMAIL
    return response(True, {'address': email.address, 'active': email.active}, 200)
