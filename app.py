#!/usr/bin/python3
"""
This is the root module of this application
"""
import os
import redis
from rq import Queue
from flask import Flask, jsonify
from flask_smorest import Api
from flask_cors import CORS
from views.user import blp as UserBlueprint
from views.http_method import blp as HttpMethodBlueprint
from views.checks import blp as CheckBlueprint
import models # This is needed to create tables in the database
from db import db
from worker import worker
from flask_jwt_extended import JWTManager
from tasks import init_worker

def create_app(db_url=None):
    """
    Configures and return a new flask app
    """
    redis_connection = redis.from_url(os.getenv("REDIS_URL"))

    app = Flask(__name__)
    CORS(app)
    app.queue = Queue("checks", connection=redis_connection)
    app.config["PROPAGATE_EXCEPTION"] = True
    app.config["API_TITLE"] = "On Call API"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
    app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
    app.config["SQLALCHEMY_DATABASE_URI"] =\
        db_url or os.getenv("DATABASE_URL", "mysql+pymysql://oncall:$$Superdad77@localhost/oncall")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
    db.init_app(app)

    with app.app_context():
        db.create_all()

    @app.get("/")
    def app_root():
        return "** On Call App API **\n"

    app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SCRETE_KEY")
    app.config["JWT_ACCESS_TOKEN_EXPIRES"] = False
    jwt = JWTManager(app)

    @jwt.unauthorized_loader
    def unauthoized_request(token):
        return jsonify({"message": "Access denied. No token provided."}), 401

   
        

    api = Api(app)
    api.register_blueprint(UserBlueprint)
    api.register_blueprint(HttpMethodBlueprint)
    api.register_blueprint(CheckBlueprint)

    app.queue.enqueue(init_worker)

    return app


if __name__ == "__main__":
    app = create_app();
    app.run()






