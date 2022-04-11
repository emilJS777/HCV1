from src import app
from . import UnitController


# GET ALL UNIT LIST
app.add_url_rule("/api/unit", view_func=UnitController.unit_get_all, methods=["GET"])

# GET UNIT BY ID
app.add_url_rule("/api/unit/<int:unit_id>", view_func=UnitController.unit_get_by_id, methods=["GET"])
