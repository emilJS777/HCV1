from src import app
from . import role_controller

# GET ALL ROLE
app.add_url_rule("/api/role", view_func=role_controller.role_get, methods=["GET"])

# # GET ROLE BY ID
# app.add_url_rule("/api/role/<int:role_id>", view_func=role_controller.role_get_by_id, methods=["GET"])
#
# # POST ROLE
# app.add_url_rule("/api/role", view_func=role_controller.role_post, methods=["POST"])
#
# # PUT ROLE
# app.add_url_rule("/api/role", view_func=role_controller.role_update, methods=["PUT"])
#
# # DELETE ROLE
# app.add_url_rule("/api/role", view_func=role_controller.role_delete, methods=["DELETE"])
