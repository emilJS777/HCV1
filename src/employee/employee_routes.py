from src import app
from . import employee_controller

# GET ALL EMPLOYEE
app.add_url_rule("/api/employee", view_func=employee_controller.employee_get, methods=["GET"])

# GET EMPLOYEE BY ID
app.add_url_rule("/api/employee/<int:employee_id>", view_func=employee_controller.employee_get_by_id, methods=["GET"])

# POST EMPLOYEE
app.add_url_rule("/api/employee", view_func=employee_controller.employee_create, methods=["POST"])

# PUT EMPLOYEE
app.add_url_rule("/api/employee/<int:employee_id>", view_func=employee_controller.employee_update, methods=["PUT"])

# DELETE EMPLOYEE
app.add_url_rule("/api/employee/<int:employee_id>", view_func=employee_controller.employee_delete, methods=["DELETE"])
