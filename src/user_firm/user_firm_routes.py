from src import app
from . import user_firm_controller


# CREATE BIND
app.add_url_rule("/api/user_firm",
                 view_func=user_firm_controller.create_bind,
                 methods=["POST"])

# DELETE BIND
app.add_url_rule("/api/user_firm",
                 view_func=user_firm_controller.delete_bind,
                 methods=["DELETE"])

# GET FIRM IDS BY USER ID
app.add_url_rule("/api/firm_ids_by_user_id/<int:user_id>",
                 view_func=user_firm_controller.get_firm_ids_by_user_id,
                 methods=["GET"])
