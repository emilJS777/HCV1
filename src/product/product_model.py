from src import db


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    title = db.Column(db.String(50), nullable=False)
    code = db.Column(db.String(50), nullable=False)
    unit_measurement = db.Column(db.String(30), nullable=False)
    group = db.Column(db.String(30), nullable=False)
    atgaa_classifier = db.Column(db.String(30), nullable=False)
    account = db.Column(db.String(30), nullable=False)

    wholesale_price = db.Column(db.String(30), nullable=False)
    retail_price = db.Column(db.String(30), nullable=False)
    other_currency = db.Column(db.String(30), nullable=False)
    wholesale_price_other_currency = db.Column(db.Numeric, nullable=False)

    hcb_coefficient = db.Column(db.String(30), nullable=False)
    accounting_method = db.Column(db.String(30), nullable=False)

    # CONSTRUCTOR
    def __init__(self, title):
        self.title = title

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

