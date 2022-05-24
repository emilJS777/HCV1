from src import db
from datetime import datetime


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    title = db.Column(db.String(50), nullable=False)
    code = db.Column(db.String(50), nullable=False)
    unit_id = db.Column(db.Integer, nullable=False)

    wholesale_price = db.Column(db.Numeric(8, 2), nullable=False)
    retail_price = db.Column(db.Numeric(8, 2), nullable=False)
    count = db.Column(db.Numeric(8, 2), nullable=False)

    storage_id = db.Column(db.Integer, nullable=False)
    client_id = db.Column(db.Integer, nullable=False)
    creation_date = db.Column(db.DateTime, default=datetime.utcnow())

    # CONSTRUCTOR
    def __init__(self,
                 title: str,
                 code: str,
                 wholesale_price: str,
                 retail_price: str,
                 storage_id: int,
                 count: float,
                 unit_id: int,
                 client_id: int):
        self.title = title
        self.code = code
        self.unit_id = unit_id
        self.count = count

        self.wholesale_price = wholesale_price
        self.retail_price = retail_price

        self.storage_id = storage_id
        self.client_id = client_id

    # SAVE DB SELF
    def save_db(self):
        db.session.add(self)
        db.session.commit()

    # DELETE DB
    def delete_db(self):
        db.session.delete(self)
        db.session.commit()

    # UPDATE DATABASE
    @staticmethod
    def update_db():
        db.session.commit()

