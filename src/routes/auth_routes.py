from src import app
from src.controllers import auth_controller

# LOGIN ROUTE
app.add_url_rule("/api/login", view_func=auth_controller.login, methods=["POST"])

# REFRESH TOKEN ROUTE
app.add_url_rule("/api/refresh", view_func=auth_controller.refresh_token, methods=["PUT"])
