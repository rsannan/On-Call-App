#!/usr/bin/python3
"""
This module create the HttpMethodModel and
maps it to the http_methods table in the database.
"""

from db import db

class HttpMethodModel(db.Model):
    __tablename__ = "http_methods"

    id = db.Column(db.Integer, nullable=False, primary_key=True)
    name = db.Column(db.String(20), nullable=False, unique=True)

    checks = db.relationship("CheckModel", back_populates="method", lazy="dynamic")