from src import app
from . import email_controller

# CREATE EMAIL
app.add_url_rule("/api/email", view_func=email_controller.email_create, methods=["POST"])

# UPDATE EMAIL
app.add_url_rule("/api/email", view_func=email_controller.email_update, methods=["PUT"])

# DELETE EMAIL
app.add_url_rule("/api/email", view_func=email_controller.email_delete, methods=["DELETE"])

# GET BY USER ID EMAIL
app.add_url_rule("/api/email", view_func=email_controller.email_get_by_user_id, methods=["GET"])
