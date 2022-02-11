from src import app
from . import user_role_controller

# GET ROLE IDS BY USER ID
app.add_url_rule("/api/user-role/<int:user_id>",
                 view_func=user_role_controller.get_role_ids_by_user_id, methods=["GET"])

# BIND USER ROLE
app.add_url_rule("/api/user-role", view_func=user_role_controller.bind_user_role, methods=["POST"])

# UNBIND USER ROLE
app.add_url_rule("/api/user-role", view_func=user_role_controller.unbind_user_role, methods=["DELETE"])
