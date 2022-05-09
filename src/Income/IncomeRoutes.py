from src import app
from . import IncomeController


# CREATE INCOME
app.add_url_rule("/api/income", view_func=IncomeController.create_income, methods=["POST"])

# GET ALL
app.add_url_rule("/api/income", view_func=IncomeController.get_all_income_by_filter, methods=["GET"])

# GET BY ID
app.add_url_rule("/api/income/<int:income_id>", view_func=IncomeController.get_by_id_income, methods=["GET"])

# GET ALL INCOME TYPES
app.add_url_rule("/api/income/type",
                 view_func=IncomeController.get_all_income_types,
                 methods=["GET"])

# GET INCOME TYPE BY ID
app.add_url_rule("/api/income/type/<int:income_type_id>",
                 view_func=IncomeController.get_by_id_income_type,
                 methods=["GET"])
