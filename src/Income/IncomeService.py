from . import IncomeServiceDb
from src.Firm import FirmServiceDb
from src.Information import InformationServiceDb
from src._response import response
from typing import List


# CREATE
def create(price: float, firm_id: int, information_id: int, income_type_id: int) -> dict:
    # GET FIRM BY ID & INFORMATION BY ID. IF NOT FOUND RETURN NOT FOUND
    if not FirmServiceDb.get_by_id(firm_id) or not InformationServiceDb.get_by_id(information_id):
        return response(False, {'msg': 'firm and/or information not found'}, 200)

    # GET INCOME TYPE BY ID AND VEriFY IF EXIST CREATE INCOME AND RETURN OK
    for income_type in IncomeServiceDb.income_types:
        if income_type['id'] == income_type_id:

            IncomeServiceDb.create(
                price=price,
                firm_id=firm_id,
                information_id=information_id,
                income_type_id=income_type_id
            )
            return response(True, {'msg': 'income successfully created'}, 200)

    # ELSE RETURN INCOME type NOT FOUND
    return response(False, {'msg': 'income type not found'}, 200)


# GET ALL IDS BY FIRM ID
def get_all_by_filter(firm_id: int, income_type_id: int, page: int, per_page: int) -> dict:
    # GET FIRM BY ID IF NOT FOUND RETURN NOT FOUND
    if not FirmServiceDb.get_by_id(firm_id):
        return response(False, {'msg': 'firm not found'}, 200)

    incomes: dict = IncomeServiceDb.get_all_by_filter(
        firm_id=firm_id,
        income_type_id=income_type_id,
        page=page,
        per_page=per_page
    )
    return response(True, incomes, 200)


# GET BY ID
def get_by_id(income_id: int) -> dict:
    # GET BY ID AND VERIFY IF NOT FOUND RETURN NOT FOUND
    income: IncomeServiceDb.Income = IncomeServiceDb.get_by_id(income_id)
    if not income:
        return response(False, {'msg': 'income not found'}, 200)
    else:
        return response(True, {'id': income.id,
                               'price': income.price,
                               'firm_id': income.firm_id,
                               'information_id': income.information_id,
                               'income_type_id': income.income_type_id}, 200)


# GET ALL INCOME TYPES
def get_all_income_types() -> dict:
    income_types: List[dict] = IncomeServiceDb.income_types
    return response(True, income_types, 200)


# GET INCOME TYPE BY ID
def get_by_id_income_type(income_type_id: int) -> dict:
    # GET ALL INCOME TYPES FROM SERVICE DB CATCH BY ID AND RETURN HIM
    for income_type in IncomeServiceDb.income_types:
        if income_type['id'] == income_type_id:
            return response(True, {'id': income_type['id'], 'title': income_type['title']}, 200)

    # IF NOT FOUND RETURN NOT FOUND
    return response(False, {'msg': 'income type not found'}, 200)
