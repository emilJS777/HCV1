from src import app
from . import UserController

# GET ALL USER
app.add_url_rule("/api/user", view_func=UserController.user_get, methods=["GET"])

# GET USER BY ID
app.add_url_rule("/api/user/<int:user_id>", view_func=UserController.user_get_by_id, methods=["GET"])

# POST USER
app.add_url_rule("/api/user", view_func=UserController.create_user, methods=["POST"])

# CREATE USER TICKET
app.add_url_rule("/api/user/ticket", view_func=UserController.create_user_ticket, methods=["POST"])

# PUT USER
app.add_url_rule("/api/user/<int:user_id>", view_func=UserController.user_update, methods=["PUT"])

# DELETE USER
app.add_url_rule("/api/user/<int:user_id>", view_func=UserController.user_delete, methods=["DELETE"])
