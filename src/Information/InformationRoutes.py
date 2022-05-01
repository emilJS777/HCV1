from src import app
from . import InformationController

# GET ALL informations
app.add_url_rule("/api/information",
                 view_func=InformationController.information_get_all,
                 methods=["GET"])

# GET information BY ID
app.add_url_rule("/api/information/<int:information_id>",
                 view_func=InformationController.information_get_by_id,
                 methods=["GET"])

# POST information
app.add_url_rule("/api/information",
                 view_func=InformationController.information_create,
                 methods=["POST"])

# PUT information
app.add_url_rule("/api/information/<int:information_id>",
                 view_func=InformationController.information_update,
                 methods=["PUT"])

# DELETE information
app.add_url_rule("/api/information/<int:information_id>",
                 view_func=InformationController.information_delete,
                 methods=["DELETE"])


# GET ALL UNIT LIST
app.add_url_rule("/api/information/unit", view_func=InformationController.get_unit_all, methods=["GET"])

# GET UNIT BY ID
app.add_url_rule("/api/information/unit/<int:unit_id>",
                 view_func=InformationController.get_unit_by_id,
                 methods=["GET"])
