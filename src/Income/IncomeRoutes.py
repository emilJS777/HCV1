from src import app
from . import IncomeController


# CREATE INCOME
app.add_url_rule("/api/income", view_func=IncomeController.create_income, methods=["POST"])

# GET ALL IDS
app.add_url_rule("/api/income", view_func=IncomeController.get_all_income_ids_by_firm_id, methods=["GET"])

# GET BY ID
app.add_url_rule("/api/income/<int:income_id>", view_func=IncomeController.get_by_id_income, methods=["GET"])
