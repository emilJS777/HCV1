from src import db
from datetime import datetime


class Income(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    for_what = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Numeric(8, 2))
    firm_id = db.Column(db.Integer, nullable=False)
    creation_date = db.Column(db.DateTime, default=datetime.utcnow())
    client_id = db.Column(db.Integer, nullable=False)

    # CONSTRUCTOR
    def __init__(self, for_what: str, price: float, firm_id: int):
        self.for_what = for_what
        self.price = price
        self.firm_id = firm_id

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
