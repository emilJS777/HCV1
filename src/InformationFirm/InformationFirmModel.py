from src import db


class InformationFirm(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    information_id = db.Column(db.Integer, nullable=False)
    firm_id = db.Column(db.Integer, nullable=False)
    client_id = db.Column(db.Integer, nullable=False)

    # CONSTRUCTOR
    def __init__(self, information_id: int, firm_id: int, client_id: int):
        self.information_id = information_id
        self.firm_id = firm_id
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
