from src import db


class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(20), nullable=False)
    last_name = db.Column(db.String(20), nullable=False)
    date_birth = db.Column(db.DateTime, nullable=False)
    passport_id = db.Column(db.String(35), nullable=False)
    firm_id = db.Column(db.Integer, nullable=False)

    # CONSTRUCTOR
    def __init__(self, first_name, last_name, date_birth, passport_id, firm_id):
        self.first_name = first_name
        self.last_name = last_name
        self.date_birth = date_birth
        self.passport_id = passport_id
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
