from src import app
from . import StorageController


# CREATE
app.add_url_rule("/api/storage", view_func=StorageController.create_storage, methods=["POST"])

# UPDATE
app.add_url_rule("/api/storage/<int:storage_id>", view_func=StorageController.update_storage, methods=["PUT"])

# DELETE
app.add_url_rule("/api/storage/<int:storage_id>", view_func=StorageController.delete_storage, methods=["DELETE"])

# GET BY ID
app.add_url_rule("/api/storage/<int:storage_id>", view_func=StorageController.get_by_id_storage, methods=["GET"])

# GET ALL IDS
app.add_url_rule("/api/storage", view_func=StorageController.get_all_storage, methods=["GET"])
