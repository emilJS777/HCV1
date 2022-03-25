from src import app
from . import product_controller

# CREATE
app.add_url_rule("/api/product", view_func=product_controller.create_product, methods=["POST"])

# UPDATE
app.add_url_rule("/api/product/<int:product_id>", view_func=product_controller.update_product, methods=["PUT"])

# DELETE
app.add_url_rule("/api/product/<int:product_id>", view_func=product_controller.delete_product, methods=["DELETE"])

# GET BY ID
app.add_url_rule("/api/product/<int:product_id>", view_func=product_controller.get_by_id_product, methods=["GET"])

# GET ALL IDS
app.add_url_rule("/api/product", view_func=product_controller.get_all_ids_product, methods=["GET"])
