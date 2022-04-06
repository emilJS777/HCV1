from .IncomeModel import Income
from flask import g
from typing import List


# CREATE
def create(for_what: str, price: float, firm_id: int) -> Income:
    income = Income(
        for_what=for_what,
        price=price,
        firm_id=firm_id
    )
    income.client_id = g.client_id
    income.save_db()
    return income


# GET ALL BY FIRM ID
def get_all_ids_by_firm_id(firm_id: int) -> List[int]:
    incomes: List[Income] = Income.query.filter_by(firm_id=firm_id,
                                                   client_id=g.client_id).all()
    income_ids: List[int] = []
    for income in incomes:
        income_ids.append(income.id)

    return income_ids


# GET BY ID
def get_by_id(expense_id: int) -> Income:
    income: Income = Income.query.filter_by(id=expense_id,
                                            client_id=g.client_id).first()
    return income
