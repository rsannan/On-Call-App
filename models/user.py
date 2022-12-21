#!/usr/bin/python3
"""
This module contains the code for creating a Table
in the database.
"""

from db import db


class UserModel(db.Model):
    """
    Defines a user model that maps to the users table
    in the database.
    """
    __tablename__ = "users"

    id = db.Column(db.Integer, nullable=False, primary_key=True)
    firstname = db.Column(db.String(50), nullable=False)
    lastname = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False, unique=True)
    phone = db.Column(db.String(15), nullable=False)
    password = db.Column(db.String(1024), nullable=False)

    checks = db.relationship("CheckModel", lazy="dynamic", back_populates="user")