#!/usr/bin/python3
"""
This module create the checks table in the database
and maps it to the CheckModel.
"""

from db import db

class CheckModel(db.Model):
    """
    Defines a user object that maps to the user table in the database.
    This table has a relationship with the users and http_methods table.
    """
    __tablename__ = "checks"

    id = db.Column(db.Integer, nullable=False, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    url = db.Column(db.String(1024), nullable=False)
    method_id = db.Column(db.Integer, db.ForeignKey("http_methods.id"), nullable=False)
    status_code = db.Column(db.Integer, nullable=False)
    check_count = db.Column(db.Integer, default=0, nullable=True)
    status = db.Column(db.Boolean, nullable=True, default=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    # on_call_user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=True)

    method = db.relationship("HttpMethodModel", back_populates="checks")
    user = db.relationship("UserModel", back_populates="checks")
    # on_call_user = db.relationship("UserModel", back_populates="on_call_users")