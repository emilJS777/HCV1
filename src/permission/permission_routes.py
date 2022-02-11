from src import app
from . import permission_controller

# GET ALL PERMISSIONS
app.add_url_rule("/api/permission", view_func=permission_controller.permission_get, methods=["GET"])

# GET PERMISSION BY ID
app.add_url_rule("/api/permission/<int:permission_id>",
                 view_func=permission_controller.permission_get_by_id, methods=["GET"])

# THIS ROUTES FOR DEVELOPER
# # POST PERMISSION
app.add_url_rule("/api/permission", view_func=permission_controller.permission_post, methods=["POST"])

# PUT PERMISSION
app.add_url_rule("/api/permission", view_func=permission_controller.permission_update, methods=["PUT"])

# DELETE PERMISSION
app.add_url_rule("/api/permission", view_func=permission_controller.permission_delete, methods=["DELETE"])
