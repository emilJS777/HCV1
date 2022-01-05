from src import db


class Email(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    address = db.Column(db.String(60), nullable=False)
    activation_code = db.Column(db.Integer)
    active = db.Column(db.Boolean, default=False)
    user_id = db.Column(db.Integer, nullable=False)

    # CONSTRUCTOR
    def __init__(self, address, user_id):
        self.address = address
        self.user_id = user_id

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
