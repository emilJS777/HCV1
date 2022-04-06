from . import IncomeService
from flask import request
from src.Auth import AuthMiddleware
from src.Client import ClientMiddleware
from src.Permission import PermissionMiddleware


# CREATE
@AuthMiddleware.check_authorize
@ClientMiddleware.check_client(required=True)
@PermissionMiddleware.check_permission("income_edit")
def create_income() -> dict:
    req: dict = request.get_json()
    res: dict = IncomeService.create(
        for_what=req['expense_type'],
        price=req['price'],
        firm_id=req['firm_id']
    )
    return res


# GET ALL IDS BY FIRM ID
@AuthMiddleware.check_authorize
@ClientMiddleware.check_client(required=True)
@PermissionMiddleware.check_permission("income_get")
def get_all_income_ids_by_firm_id() -> dict:
    res: dict = IncomeService.get_all_ids_by_firm_id(firm_id=int(request.args.get('firm_id')))
    return res


# GET BY ID
@AuthMiddleware.check_authorize
@ClientMiddleware.check_client(required=True)
def get_by_id_income(income_id: int) -> dict:
    res: dict = IncomeService.get_by_id(income_id=income_id)
    return res
