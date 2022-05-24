from .IncomeModel import Income
from flask import g
from typing import List
from src.__general.helpers.paginate import get_page_items


income_types: List[dict] = [{'id': 1, 'title': 'անկանխիկ,'},
                            {'id': 2, 'title': 'կանխիկ'},
                            {'id': 3, 'title': 'կանխիկ ֆիրմաներով'}]


# CREATE
def create(price: float, firm_id: int, information_id: int, income_type_id: int) -> Income:
    income = Income(
        price=price,
        firm_id=firm_id,
        information_id=information_id,
        income_type_id=income_type_id,
        client_id=g.client_id
    )
    income.save_db()
    return income


# GET ALL BY FIRM ID
def get_all_by_filter(firm_id: int, income_type_id: int, page: int, per_page: int) -> dict:
    # incomes: List[Income] = Income.query.filter_by(firm_id=firm_id,
    #                                                income_type_id=income_type_id,
    #                                                client_id=g.client_id).all()
    # income_ids: List[int] = []
    # for income in incomes:
    #     income_ids.append(income.id)
    # return income_ids
    return get_page_items(
        Income.query.filter_by(firm_id=firm_id, income_type_id=income_type_id, client_id=g.client_id)
        .order_by(-Income.id)
        .paginate(page=page, per_page=per_page)
    )


# GET BY ID
def get_by_id(income_id: int) -> Income:
    income: Income = Income.query.filter_by(id=income_id,
                                            client_id=g.client_id).first()
    return income
