from datetime import datetime
from src import db
from flask_bcrypt import generate_password_hash


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    password_hash = db.Column(db.String, nullable=False)
    creation_date = db.Column(db.DateTime, default=datetime.utcnow())
    # NOT REQUIRE FIELDS
    creator_id = db.Column(db.Integer)
    client_id = db.Column(db.Integer)
    firm_id = db.Column(db.Integer)

    # CONSTRUCTOR
    def __init__(self, name, password):
        self.name = name
        self.password_hash = generate_password_hash(password)

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
