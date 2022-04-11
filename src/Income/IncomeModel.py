from src import db
from datetime import datetime


class Income(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Numeric(8, 2))
    firm_id = db.Column(db.Integer, nullable=False)
    information_id = db.Column(db.Integer, nullable=False)
    income_type_id = db.Column(db.Integer, nullable=False)

    creation_date = db.Column(db.DateTime, default=datetime.utcnow())
    client_id = db.Column(db.Integer, nullable=False)

    # CONSTRUCTOR
    def __init__(self, price: float, firm_id: int, information_id: int, income_type_id: int, client_id: int):
        self.price = price
        self.firm_id = firm_id
        self.information_id = information_id
        self.income_type_id = income_type_id
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
