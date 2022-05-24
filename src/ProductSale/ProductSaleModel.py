from sqlalchemy import func
from src.__general.Parents import Model
from src import db


class ProductSale(Model, db.Model):
    product_id = db.Column(db.Integer, nullable=False)
    count = db.Column(db.Numeric(8, 2), nullable=False)
    wholesale = db.Column(db.Boolean, default=False)
    total_price = db.Column(db.Numeric(8, 2), nullable=False)

    unit_id = db.Column(db.Integer, nullable=False)
    storage_id = db.Column(db.Integer, nullable=False)
    income_type_id = db.Column(db.Integer, nullable=False)

    client_id = db.Column(db.Integer, nullable=False)
    creation_date = db.Column(db.Date(), default=func.now())

    def __init__(self, product_id: int, count: float, wholesale: bool, total_price: float,
                 storage_id: int, income_type_id: int, client_id: int):
        self.product_id = product_id
        self.count = count
        self.wholesale = wholesale
        self.total_price = total_price
        self.storage_id = storage_id
        self.income_type_id = income_type_id
        self.client_id = client_id
