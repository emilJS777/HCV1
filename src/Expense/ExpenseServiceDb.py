from .ExpenseModel import Expense
from flask import g
from typing import List


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
def get_all_ids_by_firm_id(firm_id: int) -> List[int]:
    expenses: List[Expense] = Expense.query.filter_by(firm_id=firm_id,
                                                      client_id=g.client_id).all()
    expense_ids: List[int] = []
    for expense in expenses:
        expense_ids.append(expense.id)

    return expense_ids


# GET BY ID
def get_by_id(expense_id: int) -> Expense:
    expense: Expense = Expense.query.filter_by(id=expense_id,
                                               client_id=g.client_id).first()
    return expense
