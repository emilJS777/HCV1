from src import app
from . import permission_category_controller

# CREATE
app.add_url_rule(
    "/api/permission_category",
    view_func=permission_category_controller.create,
    methods=["POST"]
)


# UPDATE
app.add_url_rule(
    "/api/permission_category/<int:permission_category_id>",
    view_func=permission_category_controller.update,
    methods=["PUT"]
)


# DELETE
app.add_url_rule(
    "/api/permission_category/<int:permission_category_id>",
    view_func=permission_category_controller.delete,
    methods=["DELETE"]
)


# GET BY ID
app.add_url_rule(
    "/api/permission_category/<int:permission_category_id>",
    view_func=permission_category_controller.get_by_id,
    methods=["GET"]
)


# GET ALL
app.add_url_rule(
    "/api/permission_category",
    view_func=permission_category_controller.get_all,
    methods=["GET"]
)


