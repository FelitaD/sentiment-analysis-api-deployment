from flask import Flask
from flask_jwt_extended import JWTManager

from api.db import db


def create_app():
    app = Flask(__name__)
    app.config['PROPAGATE_EXCEPTIONS'] = True
    app.config['SECRET_KEY'] = b'_5#y@!L"F4gweg28z\n\xec]/'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
    with app.app_context():
        db.init_app(app)
        db.Model.metadata.reflect(db.engine)
    jwt = JWTManager(app)

    return app
