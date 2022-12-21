import os
from flask import Flask
from flask_smorest import Api
from views.user import blp as UserBlueprint
from views.http_method import blp as HttpMethodBlueprint
import models # Needed to create tables in the database
from db import db


def create_app(db_url=None):
    """
    Configures and return a new flask app
    """
    
    app = Flask(__name__)
    app.config["PROPAGATE_EXCEPTION"] = True
    app.config["API_TITLE"] = "On Call API"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
    app.config["SQLALCHEMY_DATABASE_URI"] = db_url or os.getenv("DATABASE_URL", "mysql+pymysql://root:superdad77@localhost/alx")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
    db.init_app(app)

    with app.app_context():
        db.create_all()

    api = Api(app)
    api.register_blueprint(UserBlueprint)
    api.register_blueprint(HttpMethodBlueprint)

    return app
