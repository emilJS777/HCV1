from src import app
from src.controllers import auth

# LOGIN ROUTE
app.add_url_rule("/api/login", view_func=auth.login, methods=["POST"])

# REFRESH TOKEN ROUTE
app.add_url_rule("/api/refresh", view_func=auth.refresh_token, methods=["PUT"])
