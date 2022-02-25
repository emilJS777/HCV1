from src import app
from . import category_firm_controller


# BIND CATEGORY FIRM
app.add_url_rule("/api/category-firm", view_func=category_firm_controller.bind_category_firm, methods=["POST"])

# UNBIND CATEGORY FIRM
app.add_url_rule("/api/category-firm", view_func=category_firm_controller.unbind_category_firm, methods=["DELETE"])

# GET FIRM IDS BY CATEGORY ID
app.add_url_rule("/api/category-firm/<int:category_id>", view_func=category_firm_controller.get_firm_ids_by_category_id, methods=["GET"])
