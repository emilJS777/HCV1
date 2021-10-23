from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager


app = Flask(__name__)
api = Api(app)

# CONNECT TO DATABASE CONFIG
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///../hc.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)
db.init_app(app)
db.create_all()
migrate = Migrate(app, db)

# CONNECT JWT CONFIG
app.config["JWT_SECRET_KEY"] = "H^&67KCsn@77G"
app.config["JWT_ACCESS_EXP"] = 30
app.config["JWT_REFRESH_EXP"] = 3000
jwt = JWTManager(app)
