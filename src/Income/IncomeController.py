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
        price=req['price'],
        firm_id=req['firm_id'],
        information_id=req['information_id'],
        income_type_id=req['income_type_id']
    )
    return res


# GET ALL IDS BY FIRM ID
@AuthMiddleware.check_authorize
@ClientMiddleware.check_client(required=True)
@PermissionMiddleware.check_permission("income_get")
def get_all_income_by_filter() -> dict:
    res: dict = IncomeService.get_all_by_filter(firm_id=int(request.args.get('firm_id')),
                                                income_type_id=int(request.args.get('income_type_id')),
                                                page=int(request.args.get('page')),
                                                per_page=int(request.args.get('per_page'))
                                                )
    return res


# GET BY ID
@AuthMiddleware.check_authorize
@ClientMiddleware.check_client(required=True)
def get_by_id_income(income_id: int) -> dict:
    res: dict = IncomeService.get_by_id(income_id)
    return res


# GET ALL INCOME TYPES
@AuthMiddleware.check_authorize
@ClientMiddleware.check_client(required=True)
def get_all_income_types() -> dict:
    res: dict = IncomeService.get_all_income_types()
    return res


# GET INCOME TYPE BY ID
@AuthMiddleware.check_authorize
@ClientMiddleware.check_client(required=True)
def get_by_id_income_type(income_type_id: int) -> dict:
    res: dict = IncomeService.get_by_id_income_type(income_type_id)
    return res
