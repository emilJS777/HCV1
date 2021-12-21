from src import app
from src.controllers import role_permission_controller

# GET PERMISSION IDS BY ROLE ID
app.add_url_rule("/api/role-permission/<int:role_id>",
                 view_func=role_permission_controller.get_permission_ids_by_role_id, methods=["GET"])

# BIND ROLE PERMISSION
app.add_url_rule("/api/role-permission", view_func=role_permission_controller.bind_role_permission, methods=["POST"])

# UNBIND ROLE PERMISSION
app.add_url_rule("/api/role-permission", view_func=role_permission_controller.unbind_role_permission, methods=["DELETE"])
