from . import IncomeServiceDb
from src.Firm import FirmServiceDb
from src._response import response
from typing import List


# CREATE
def create(for_what: str, price: float, firm_id: int) -> dict:
    # GET FIRM BY ID IF NOT FOUND RETURN NOT FOUND
    if not FirmServiceDb.get_by_id(firm_id):
        return response(False, {'msg': 'firm not found'}, 404)

    IncomeServiceDb.create(
        for_what=for_what,
        price=price,
        firm_id=firm_id
    )
    return response(True, {'msg': 'income successfully created'}, 200)


# GET ALL IDS BY FIRM ID
def get_all_ids_by_firm_id(firm_id: int) -> dict:
    # GET FIRM BY ID IF NOT FOUND RETURN NOT FOUND
    if not FirmServiceDb.get_by_id(firm_id):
        return response(False, {'msg': 'firm not found'}, 404)

    incomes_ids: List[int] = IncomeServiceDb.get_all_ids_by_firm_id(
        firm_id=firm_id
    )
    return response(True, incomes_ids, 200)


# GET BY ID
def get_by_id(income_id: int) -> dict:
    # GET BY ID AND VERIFY IF NOT FOUND RETURN NOT FOUND
    income: IncomeServiceDb.Income = IncomeServiceDb.get_by_id(income_id)
    if not income:
        return response(False, {'msg': 'income not found'}, 404)

    return response(True, {'id': income.id,
                           'for_what': income.for_what,
                           'price': income.price,
                           'firm_id': income.firm_id}, 200)
