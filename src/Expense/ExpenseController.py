from . import ExpenseService
from flask import request
from src.Auth import AuthMiddleware
from src.Client import ClientMiddleware
from src.Permission import PermissionMiddleware


# CREATE
@AuthMiddleware.check_authorize
@ClientMiddleware.check_client(required=True)
@PermissionMiddleware.check_permission("expense_edit")
def create_expense() -> dict:
    req: dict = request.get_json()
    res: dict = ExpenseService.create(
        expense_type=req['expense_type'],
        price=req['price'],
        firm_id=req['firm_id']
    )
    return res


# GET ALL IDS BY FIRM ID
@AuthMiddleware.check_authorize
@ClientMiddleware.check_client(required=True)
@PermissionMiddleware.check_permission("expense_get")
def get_all_expenses_by_firm_id() -> dict:
    res: dict = ExpenseService.get_all_by_firm_id(
        page=int(request.args.get('page')),
        per_page=int(request.args.get('per_page')),
        firm_id=int(request.args.get('firm_id'))
    )
    return res


# GET BY ID
@AuthMiddleware.check_authorize
@ClientMiddleware.check_client(required=True)
def get_by_id_expense(expense_id: int) -> dict:
    res: dict = ExpenseService.get_by_id(expense_id=expense_id)
    return res
