from src import app
from . import ExpenseController


# CREATE EXPENSE
app.add_url_rule("/api/expense", view_func=ExpenseController.create_expense, methods=["POST"])

# GET ALL IDS
app.add_url_rule("/api/expense", view_func=ExpenseController.get_all_expenses_by_firm_id, methods=["GET"])

# GET BY ID
app.add_url_rule("/api/expense/<int:expense_id>", view_func=ExpenseController.get_by_id_expense, methods=["GET"])
