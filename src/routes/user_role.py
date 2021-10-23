from src import app
from src.controllers import user_role

# GET ROLE IDS BY USER ID
app.add_url_rule("/api/user-role/<int:user_id>",
                 view_func=user_role.get_role_ids_by_user_id, methods=["GET"])

# BIND USER ROLE
app.add_url_rule("/api/user-role", view_func=user_role.bind_user_role, methods=["POST"])

# UNBIND USER ROLE
app.add_url_rule("/api/user-role", view_func=user_role.unbind_user_role, methods=["DELETE"])
