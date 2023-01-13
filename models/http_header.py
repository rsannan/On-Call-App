#!/usr/bin/python3
"""
Contains the code for creating a table
for http-headers in the database
"""

from db import db

class HTTPHeaderModel(db.Model):
    """
    Defines an Object Relational Mapper class for 
    HTTP headers.
    """
    __tablename__ = "http_headers"
    
    id = db.Column(db.Integer, nullable=False, primary_key=True)
    key = db.Column(db.String(200), nullable=False)
    value = db.Column(db.String(2048), nullable=False)
    check_id = db.Column(db.Integer, db.ForeignKey("checks.id"), nullable=False)

    check = db.relationship("CheckModel", back_populates="headers")
