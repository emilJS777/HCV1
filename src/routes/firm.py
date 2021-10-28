from src import app
from src.controllers import firm

# GET ALL FIRM
app.add_url_rule("/api/firm", view_func=firm.firm_get, methods=["GET"])

# GET FIRM BY ID
app.add_url_rule("/api/firm/<int:firm_id>", view_func=firm.firm_get_by_id, methods=["GET"])

# POST FIRM
app.add_url_rule("/api/firm", view_func=firm.firm_post, methods=["POST"])

# PUT FIRM
app.add_url_rule("/api/firm", view_func=firm.firm_update, methods=["PUT"])

# DELETE FIRM
app.add_url_rule("/api/firm", view_func=firm.firm_delete, methods=["DELETE"])