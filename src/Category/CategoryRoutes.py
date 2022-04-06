from src import app
from . import CategoryController

# GET ALL CATEGORIES
app.add_url_rule("/api/category", view_func=CategoryController.category_get_all, methods=["GET"])

# GET CATEGORY BY ID
app.add_url_rule("/api/category/<int:category_id>", view_func=CategoryController.category_get_by_id, methods=["GET"])

# POST CATEGORY
app.add_url_rule("/api/category", view_func=CategoryController.category_create, methods=["POST"])

# PUT CATEGORY
app.add_url_rule("/api/category/<int:category_id>", view_func=CategoryController.category_update, methods=["PUT"])

# DELETE CATEGORY
app.add_url_rule("/api/category/<int:category_id>", view_func=CategoryController.category_delete, methods=["DELETE"])
