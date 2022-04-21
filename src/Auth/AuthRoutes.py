from src import app
from . import AuthController

# LOGIN ROUTE
app.add_url_rule("/api/login", view_func=AuthController.login, methods=["POST"])

# GET PROFILE
app.add_url_rule("/api/login", view_func=AuthController.get_profile, methods=["GET"])

# REFRESH TOKEN ROUTE
app.add_url_rule("/api/refresh", view_func=AuthController.refresh_token, methods=["PUT"])


