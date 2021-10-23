from src import app
from src.controllers import user

# GET ALL USER
app.add_url_rule("/api/user", view_func=user.user_get, methods=["GET"])

# GET USER BY ID
app.add_url_rule("/api/user/<int:user_id>", view_func=user.user_get_by_id, methods=["GET"])

# POST USER
app.add_url_rule("/api/user", view_func=user.user_post, methods=["POST"])

# PUT USER
app.add_url_rule("/api/user", view_func=user.user_update, methods=["PUT"])

# DELETE USER
app.add_url_rule("/api/user", view_func=user.user_delete, methods=["DELETE"])
