from src import app
from . import AuthController

# LOGIN ROUTE
app.add_url_rule("/api/login", view_func=AuthController.login, methods=["POST"])

# REFRESH TOKEN ROUTE
app.add_url_rule("/api/refresh", view_func=AuthController.refresh_token, methods=["PUT"])
