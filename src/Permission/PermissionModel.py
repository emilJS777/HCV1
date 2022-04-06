from src import db


class Permission(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=True, nullable=False)
    title = db.Column(db.String(50), unique=True, nullable=False)
    category_id = db.Column(db.Integer)
    client_id = db.Column(db.Integer, nullable=False)
    firm = db.Column(db.Boolean, default=False)

    # CONSTRUCTOR
    def __init__(self, name: str, title: str):
        self.name = name
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
