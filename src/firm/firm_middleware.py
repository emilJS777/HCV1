from flask import g
from src._response import response
from functools import wraps
from src.user import user_service_db


# CHECk FIRM
# MIDDLEWARE FOR ASSIGNMENT g.firm_id
def check_firm(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        # GET USER BY g.user_id AND VERIFY whether this user is tied to any firm
        # IF NO RETURN FIRM NOT FOUND
        firm_id = user_service_db.get_by_id(user_id=g.user_id).firm_id
        if not firm_id:
            return response(False, {'msg': 'you are not tied to a firm'}, 404)

        # ELSE ASSIGN g.firm_id ID FIRM BY USER FIRM ID
        g.firm_id = firm_id
        return f(*args, **kwargs)

    return decorated_function
