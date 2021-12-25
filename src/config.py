from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from datetime import datetime
import logging

app = Flask(__name__)
api = Api(app)

# CONNECT TO DATABASE CONFIG
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:Current-Root-Password@localhost/accounting_db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)
db.init_app(app)
db.create_all()
migrate = Migrate(app, db)

# CONNECT JWT CONFIG
app.config["JWT_SECRET_KEY"] = "H^&67KCsn@77G"
app.config["JWT_ACCESS_EXP"] = 20
app.config["JWT_REFRESH_EXP"] = 3000
jwt = JWTManager(app)

# LOGGING
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(f"{datetime.utcnow()}")
