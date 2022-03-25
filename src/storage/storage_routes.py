from src import app
from . import storage_controller


# CREATE
app.add_url_rule("/api/storage", view_func=storage_controller.create_storage, methods=["POST"])

# UPDATE
app.add_url_rule("/api/storage/<int:storage_id>", view_func=storage_controller.update_storage, methods=["PUT"])

# DELETE
app.add_url_rule("/api/storage/<int:storage_id>", view_func=storage_controller.delete_storage, methods=["DELETE"])

# GET BY ID
app.add_url_rule("/api/storage/<int:storage_id>", view_func=storage_controller.get_by_id_storage, methods=["GET"])

# GET ALL IDS
app.add_url_rule("/api/storage", view_func=storage_controller.get_all_ids_storage, methods=["GET"])
