from src import app
from src.controllers import client_user

# GET USER IDS BY CLIENT ID
app.add_url_rule("/api/client-user/<int:client_id>",
                 view_func=client_user.get_user_ids_by_client_id, methods=["GET"])

# BIND CLIENT USER
app.add_url_rule("/api/client-user", view_func=client_user.bind_client_user, methods=["POST"])

# UNBIND CLIENT USER
app.add_url_rule("/api/client-user", view_func=client_user.unbind_client_user, methods=["DELETE"])
