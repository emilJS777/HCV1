from src import app
from src.controllers import role

# GET ALL ROLE
app.add_url_rule("/api/role", view_func=role.role_get, methods=["GET"])

# GET ROLE BY ID
app.add_url_rule("/api/role/<int:role_id>", view_func=role.role_get_by_id, methods=["GET"])

# POST ROLE
app.add_url_rule("/api/role", view_func=role.role_post, methods=["POST"])

# PUT ROLE
app.add_url_rule("/api/role", view_func=role.role_update, methods=["PUT"])

# DELETE ROLE
app.add_url_rule("/api/role", view_func=role.role_delete, methods=["DELETE"])
