from src import db


class Storage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    code = db.Column(db.String(50), nullable=False)
    address = db.Column(db.String(80), nullable=False)
    storekeeper = db.Column(db.String(80), nullable=False)

    firm_id = db.Column(db.Integer, nullable=False)
    client_id = db.Column(db.Integer, nullable=False)

    # CONSTRUCTOR
    def __init__(self, title: str, code: str, address: str, storekeeper: str, firm_id: int, client_id: int):
        self.title = title
        self.code = code
        self.address = address
        self.storekeeper = storekeeper
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
