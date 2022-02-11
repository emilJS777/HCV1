from datetime import datetime
from src import db
from flask_bcrypt import generate_password_hash


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(18), nullable=False)
    password_hash = db.Column(db.String(200), nullable=False)
    first_name = db.Column(db.String(15), nullable=False)
    last_name = db.Column(db.String(15), nullable=False)
    creation_date = db.Column(db.DateTime, default=datetime.utcnow())
    # NOT REQUIRE FIELDS
    creator_id = db.Column(db.Integer)
    client_id = db.Column(db.Integer)
    firm_id = db.Column(db.Integer)

    # CONSTRUCTOR
    def __init__(self, name, password, first_name, last_name, creator_id):
        self.name = name
        self.password_hash = generate_password_hash(password)
        self.first_name = first_name
        self.last_name = last_name
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
