from src import app
from . import position_controller

# CREATE
app.add_url_rule("/api/position", view_func=position_controller.create, methods=["POST"])

# UPDATE
app.add_url_rule("/api/position/<int:position_id>", view_func=position_controller.update, methods=["PUT"])

# DELETE
app.add_url_rule("/api/position/<int:position_id>", view_func=position_controller.delete, methods=["DELETE"])

# GET BY ID
app.add_url_rule("/api/position/<int:position_id>", view_func=position_controller.get_by_id, methods=["GET"])

# GET ALL IDS
app.add_url_rule("/api/position", view_func=position_controller.get_all_ids, methods=["GET"])
