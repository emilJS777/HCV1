from src import db


class Client(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    description = db.Column(db.String(120), nullable=False)
    max_count_firms = db.Column(db.Integer, nullable=False)
    creator_id = db.Column(db.Integer, nullable=False)

    # CONSTRUCTOR
    def __init__(self, name, description, max_count_firms, creator_id):
        self.name = name
        self.description = description
        self.max_count_firms = max_count_firms
        self.creator_id = creator_id

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
