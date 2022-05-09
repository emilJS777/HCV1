from src import app
from . import ProductController

# CREATE
app.add_url_rule("/api/product", view_func=ProductController.create_product, methods=["POST"])

# UPDATE
app.add_url_rule("/api/product/<int:product_id>", view_func=ProductController.update_product, methods=["PUT"])

# DELETE
app.add_url_rule("/api/product/<int:product_id>", view_func=ProductController.delete_product, methods=["DELETE"])

# GET BY ID
app.add_url_rule("/api/product/<int:product_id>", view_func=ProductController.get_by_id_product, methods=["GET"])

# GET ALL IDS
app.add_url_rule("/api/product", view_func=ProductController.get_all_product, methods=["GET"])

# GET ALL BY STORAGE ID
app.add_url_rule("/api/product_by_storage_id", view_func=ProductController.get_all_product_by_storage_id, methods=["GET"])
