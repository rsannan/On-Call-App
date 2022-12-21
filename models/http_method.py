from db import db

class HttpMethodModel(db.Model):
    __tablename__ = "http_methods"

    id = db.Column(db.Integer, nullable=False, primary_key=True)
    name = db.Column(db.String(20), nullable=False, unique=True)