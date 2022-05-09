from src import app
from . import PositionController

# CREATE
app.add_url_rule("/api/position", view_func=PositionController.create, methods=["POST"])

# UPDATE
app.add_url_rule("/api/position/<int:position_id>", view_func=PositionController.update, methods=["PUT"])

# DELETE
app.add_url_rule("/api/position/<int:position_id>", view_func=PositionController.delete, methods=["DELETE"])

# GET BY ID
app.add_url_rule("/api/position/<int:position_id>", view_func=PositionController.get_by_id, methods=["GET"])

# GET ALL IDS
app.add_url_rule("/api/position", view_func=PositionController.get_all, methods=["GET"])
