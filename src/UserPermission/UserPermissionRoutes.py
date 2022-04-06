from src import app
from . import UserPermissionController


# CREATE BIND
app.add_url_rule("/api/user-permission", view_func=UserPermissionController.create_bind, methods=["POST"])

# DELETE BIND
app.add_url_rule("/api/user-permission", view_func=UserPermissionController.delete_bind, methods=["DELETE"])

# GET PERMISSION IDS BY USER ID FIRM ID
app.add_url_rule("/api/user-permission", view_func=UserPermissionController.get_permission_ids_by_user_firm, methods=["GET"])
