from src import app
from . import user_position_controller

# GET USER IDS BY POSITION ID
app.add_url_rule("/api/user-position/<int:position_id>",
                 view_func=user_position_controller.get_user_ids_by_position_id, methods=["GET"])

# BIND USER POSITION
app.add_url_rule("/api/user-position",
                 view_func=user_position_controller.bind_user_position, methods=["POST"])

# UNBIND USER POSITION
app.add_url_rule("/api/user-position",
                 view_func=user_position_controller.unbind_user_position, methods=["DELETE"])
