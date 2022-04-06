from .EmailModel import Email


def create(address, user_id):
    # CREATE NEW EMAIL AND RETURN
    email = Email(address=address, user_id=user_id)
    email.save_db()
    return email


def update(address, user_id):
    # UPDATE EMAIL ADDRESS AND RETURN
    email = Email.query.filter_by(user_id=user_id).first()
    email.address = address
    email.update_db()
    return email


def delete(user_id):
    # DELETE EMAIL BY USER ID AND RETURN
    email = Email.query.filter_by(user_id=user_id).first()
    email.delete_db()
    return email


def get_by_user_id(user_id):
    # GET EMAIL BY USER ID AND RETURN
    email = Email.query.filter_by(user_id=user_id).first()
    return email


def get_by_address(address):
    # GET EMAIL BY ADDRESS AND RETURN
    email = Email.query.filter_by(address=address).first()
    return email
