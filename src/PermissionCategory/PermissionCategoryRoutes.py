from src import app
from . import PermissionCategoryController

# CREATE
app.add_url_rule(
    "/api/permission_category",
    view_func=PermissionCategoryController.create_permission_category,
    methods=["POST"]
)


# UPDATE
app.add_url_rule(
    "/api/permission_category/<int:permission_category_id>",
    view_func=PermissionCategoryController.update_permission_category,
    methods=["PUT"]
)


# DELETE
app.add_url_rule(
    "/api/permission_category/<int:permission_category_id>",
    view_func=PermissionCategoryController.delete_permission_category,
    methods=["DELETE"]
)


# GET BY ID
app.add_url_rule(
    "/api/permission_category/<int:permission_category_id>",
    view_func=PermissionCategoryController.get_by_id_permission_category,
    methods=["GET"]
)


# GET ALL
app.add_url_rule(
    "/api/permission_category",
    view_func=PermissionCategoryController.get_by_id_permission_category,
    methods=["GET"]
)


