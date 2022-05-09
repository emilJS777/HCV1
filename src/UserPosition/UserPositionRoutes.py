from src import app
from . import UserPositionController

# GET USER IDS BY POSITION ID
app.add_url_rule("/api/user-position",
                 view_func=UserPositionController.get_users_by_position_id, methods=["GET"])

# BIND USER POSITION
app.add_url_rule("/api/user-position",
                 view_func=UserPositionController.bind_user_position, methods=["POST"])

# UNBIND USER POSITION
app.add_url_rule("/api/user-position",
                 view_func=UserPositionController.unbind_user_position, methods=["DELETE"])
