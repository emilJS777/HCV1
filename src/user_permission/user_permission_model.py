from src import db


class UserPermission(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    permission_id = db.Column(db.Integer, nullable=False)

    # CONSTRUCTOR
    def __init__(self, user_id, permission_id):
        self.user_id = user_id
        self.permission_id = permission_id

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
