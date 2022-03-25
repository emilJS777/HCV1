from src import db
from datetime import datetime


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    title = db.Column(db.String(50), nullable=False)
    code = db.Column(db.String(50), nullable=False)
    unit_measurement = db.Column(db.String(30), nullable=False)
    group = db.Column(db.String(30), nullable=False)
    atgaa_classifier = db.Column(db.String(30), nullable=False)
    account = db.Column(db.String(30), nullable=False)

    wholesale_price = db.Column(db.Numeric(8, 2), nullable=False)
    retail_price = db.Column(db.Numeric(8, 2), nullable=False)
    other_currency = db.Column(db.String(30), nullable=False)
    wholesale_price_other_currency = db.Column(db.String(30), nullable=False)

    hcb_coefficient = db.Column(db.String(30), nullable=False)
    accounting_method = db.Column(db.String(30), nullable=False)

    client_id = db.Column(db.Integer, nullable=False)
    firm_id = db.Column(db.Integer)

    creation_date = db.Column(db.DateTime, default=datetime.utcnow())

    # CONSTRUCTOR
    def __init__(self,
                 title: str,
                 code: str,
                 unit_measurement: str,
                 group: str,
                 atgaa_classifier: str,
                 account: str,
                 wholesale_price: str,
                 retail_price: str,
                 other_currency: str,
                 wholesale_price_other_currency: str,
                 hcb_coefficient: str,
                 accounting_method: str,
                 client_id: int,
                 firm_id: int):
        self.title = title
        self.code = code
        self.unit_measurement = unit_measurement
        self.group = group

        self.atgaa_classifier = atgaa_classifier
        self.account = account
        self.wholesale_price = wholesale_price
        self.retail_price = retail_price

        self.other_currency = other_currency
        self.wholesale_price_other_currency = wholesale_price_other_currency
        self.hcb_coefficient = hcb_coefficient
        self.accounting_method = accounting_method

        self.client_id = client_id
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

