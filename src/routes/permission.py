from src import app
from src.controllers import permission

# GET ALL PERMISSIONS
app.add_url_rule("/api/permission", view_func=permission.permission_get, methods=["GET"])

# GET PERMISSION BY ID
app.add_url_rule("/api/permission/<int:permission_id>",
                 view_func=permission.permission_get_by_id, methods=["GET"])

# POST PERMISSION
app.add_url_rule("/api/permission", view_func=permission.permission_post, methods=["POST"])

# PUT PERMISSION
app.add_url_rule("/api/permission", view_func=permission.permission_update, methods=["PUT"])

# DELETE PERMISSION
app.add_url_rule("/api/permission", view_func=permission.permission_delete, methods=["DELETE"])
