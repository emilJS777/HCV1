from src import app
from src.controllers import firm_user

# GET USER IDS BY FIRM ID
app.add_url_rule("/api/firm-user/<int:firm_id>",
                 view_func=firm_user.get_user_ids_by_firm_id, methods=["GET"])

# BIND CLIENT FIRM
app.add_url_rule("/api/firm-user", view_func=firm_user.bind_firm_user, methods=["POST"])

# UNBIND CLIENT FIRM
app.add_url_rule("/api/firm-user", view_func=firm_user.unbind_firm_user, methods=["DELETE"])
