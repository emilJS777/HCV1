from src.services_db import role_db, role_permission_db, user_role_db
from src._response import response
from flask import g


# GET PERMISSION IDS BY ROLE ID
def get_permission_ids_by_role_id(role_id):
    # CHECK WHETHER THE USER HAS SUCH ROLE IF NO ISSUE
    if not role_db.get_by_id_creator_id(role_id=role_id, creator_id=g.user_id):
        return response(False, {'msg': 'role not found'}, 404)

    # GET PERMISSION IDS BY ROLE ID
    permission_ids = role_permission_db.get_permission_ids_by_role_id(role_id=role_id)
    return response(True, permission_ids, 200)


# BIND ROLE PERMISSION
def bind_role_permission(role_id, permission_id):
    # IF ROLE ID NOT FIND RETURN 404 NOT FOUND
    if not role_db.get_by_id_creator_id(role_id=role_id, creator_id=g.user_id):
        return response(False, {'msg': 'role by this id not found'}, 404)

    # GET ROLE ID FROM USER AND OVERRIDE RESOLUTION
    for roleId in user_role_db.get_role_ids_by_user_id(user_id=g.user_id):
        for permissionId in role_permission_db.get_permission_ids_by_role_id(role_id=roleId):

            # IF THE USER HAS FIND RELEVANT PERMISSION
            if permissionId == permission_id:

                # CHECK WHETHER THIS COMMUNICATION EXISTS IN THE DATABASE
                if role_permission_db.get_by_role_id_permission_id(role_id, permission_id):
                    return response(False, {'msg': 'such a connection already exists'}, 409)

                # IF THERE IS NO CONNECTION, WE WILL CONNECT AND
                # RESPOND THE RESPONSE ABOUT A SUCCESSFUL CONNECTION
                role_permission_db.create_bind(role_id=role_id, permission_id=permission_id)
                return response(True, {'msg': 'new link role permission successfully created'}, 200)

    # IF THE USER DOESN'T HAVE SUCH PERMISSION RETURN ANSWER
    return response(False, {'msg': 'you do not have such permission'}, 403)


# UNBIND ROLE PERMISSION
def unbind_role_permission(role_id, permission_id):
    # CHECK WHETHER THE USER HAS SUCH ROLE IF NO ISSUE
    if not role_db.get_by_id_creator_id(role_id=role_id, creator_id=g.user_id):
        return response(False, {'msg': 'role not found'}, 404)

    # GET AND CHECK WHETHER THIS COMMUNICATION EXISTS. IF NO RETURN NOT FOUND
    if not role_permission_db.get_by_role_id_permission_id(role_id, permission_id):
        return response(False, {'msg': 'this link not found'}, 404)

    # IF EXIST DELETE FROM DB AND RESPONSE
    role_permission_db.delete_bind(role_id=role_id, permission_id=permission_id)
    return response(True, {'msg': 'role permission link successfully deleted'}, 200)
