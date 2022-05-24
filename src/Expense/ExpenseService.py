from . import ExpenseServiceDb
from src.Firm import FirmServiceDb
from src._response import response
from typing import List


# CREATE
def create(expense_type: str, price: float, description: str, firm_id: int) -> dict:
    # GET FIRM BY ID IF NOT FOUND RETURN NOT FOUND
    if not FirmServiceDb.get_by_id(firm_id):
        return response(False, {'msg': 'firm not found'}, 404)

    ExpenseServiceDb.create(
        expense_type=expense_type,
        description=description,
        price=price,
        firm_id=firm_id
    )
    return response(True, {'msg': 'expense successfully created'}, 200)


# GET ALL IDS BY FIRM ID
def get_all_by_firm_id(page: int, per_page: int, firm_id: int) -> dict:
    # GET FIRM BY ID IF NOT FOUND RETURN NOT FOUND
    if not FirmServiceDb.get_by_id(firm_id):
        return response(False, {'msg': 'firm not found'}, 404)

    expenses: dict = ExpenseServiceDb.get_all_by_firm_id(
        page=page,
        per_page=per_page,
        firm_id=firm_id
    )
    return response(True, expenses, 200)


# GET BY ID
def get_by_id(expense_id: int) -> dict:
    # GET BY ID AND VERIFY IF NOT FOUND RETURN NOT FOUND
    expense: ExpenseServiceDb.Expense = ExpenseServiceDb.get_by_id(expense_id)
    if not expense:
        return response(False, {'msg': 'expense not found'}, 404)

    return response(True, {'id': expense.id,
                           'expense_type': expense.expense_type,
                           'description': expense.description,
                           'price': expense.price,
                           'firm_id': expense.firm_id}, 200)
