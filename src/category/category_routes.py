from src import app
from . import category_controller

# GET ALL CATEGORIES
app.add_url_rule("/api/category", view_func=category_controller.category_get_all, methods=["GET"])

# GET CATEGORY BY ID
app.add_url_rule("/api/category/<int:category_id>", view_func=category_controller.category_get_by_id, methods=["GET"])

# POST CATEGORY
app.add_url_rule("/api/category", view_func=category_controller.category_create, methods=["POST"])

# PUT CATEGORY
app.add_url_rule("/api/category/<int:category_id>", view_func=category_controller.category_update, methods=["PUT"])

# DELETE CATEGORY
app.add_url_rule("/api/category/<int:category_id>", view_func=category_controller.category_delete, methods=["DELETE"])
