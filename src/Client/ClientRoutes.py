from src import app
from . import ClientController

# GET ALL CLIENT
app.add_url_rule("/api/client", view_func=ClientController.client_get, methods=["GET"])

# GET CLIENT BY ID
app.add_url_rule("/api/client/<int:client_id>", view_func=ClientController.client_get_by_id, methods=["GET"])

# POST CLIENT
app.add_url_rule("/api/client", view_func=ClientController.client_post, methods=["POST"])

# PUT CLIENT
app.add_url_rule("/api/client/<int:client_id>", view_func=ClientController.client_update, methods=["PUT"])

# DELETE CLIENT
app.add_url_rule("/api/client/<int:client_id>", view_func=ClientController.client_delete, methods=["DELETE"])
