from src import app
from . import user_permission_controller

# GET PERMISSION IDS BY USER ID
app.add_url_rule("/api/user-permission/<int:user_id>",
                 view_func=user_permission_controller.get_permission_ids_by_user_id, methods=["GET"])

# BIND USEr PERMISSION
app.add_url_rule("/api/user-permission", view_func=user_permission_controller.bind_user_permission, methods=["POST"])

# UNBIND USER PERMISSION
app.add_url_rule("/api/user-permission", view_func=user_permission_controller.unbind_user_permission, methods=["DELETE"])

