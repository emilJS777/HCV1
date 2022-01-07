from src import db


class Firm(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    title = db.Column(db.String(30), nullable=False)
    activity_address = db.Column(db.String(100), nullable=False)
    legal_address = db.Column(db.String(100), nullable=False)
    phone_number = db.Column(db.String(50), nullable=False)
    email_address = db.Column(db.String(50), nullable=False)
    tax_payer_number = db.Column(db.Integer, nullable=False)
    state_register_number = db.Column(db.Integer, nullable=False)

    leader_position = db.Column(db.String(50), nullable=False)
    leader_full_name = db.Column(db.String(120), nullable=False)
    accountant_position = db.Column(db.String(50), nullable=False)
    accountant_full_name = db.Column(db.String(120), nullable=False)
    cashier_full_name = db.Column(db.String(120), nullable=False)

    client_id = db.Column(db.Integer, nullable=False)

    # CONSTRUCTOR
    def __init__(self, title, activity_address, legal_address, phone_number, email_address,
                 tax_payer_number, state_register_number, leader_position, leader_full_name,
                 accountant_position, accountant_full_name, cashier_full_name, client_id):
        self.title = title
        self.activity_address = activity_address
        self.legal_address = legal_address
        self.phone_number = phone_number
        self.email_address = email_address
        self.tax_payer_number = tax_payer_number
        self.state_register_number = state_register_number
        self.leader_position = leader_position
        self.leader_full_name = leader_full_name
        self.accountant_position = accountant_position
        self.accountant_full_name = accountant_full_name
        self.cashier_full_name = cashier_full_name

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
