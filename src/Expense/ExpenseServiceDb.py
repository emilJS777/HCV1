from .ExpenseModel import Expense
from flask import g
from typing import List
from src._general.helpers.paginate import get_page_items


# CREATE
def create(expense_type: str, price: float, firm_id: int) -> Expense:
    expense = Expense(
        expense_type=expense_type,
        price=price,
        firm_id=firm_id
    )
    expense.client_id = g.client_id
    expense.save_db()
    return expense


# GET ALL BY FIRM ID
def get_all_by_firm_id(page: int, per_page: int, firm_id: int) -> dict:
    return get_page_items(
        Expense.query.filter_by(firm_id=firm_id, client_id=g.client_id)
        .order_by(-Expense.id)
        .paginate(page=page, per_page=per_page)
    )


# GET BY ID
def get_by_id(expense_id: int) -> Expense:
    expense: Expense = Expense.query.filter_by(id=expense_id,
                                               client_id=g.client_id).first()
    return expense
