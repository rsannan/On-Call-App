#!/usr/bin/python3
"""
Defines a schemal for http header
"""
from marshmallow import fields, Schema
from views.schemas.checks import CheckCreateSchema

class HTTPHeaderSchema(Schema):
    """
    Defines a schema for http header
    """
    id = fields.Int()
    key = fields.Str(required=true),
    value = fields.Str(require=true),
    check_id = fields.Int(True)
    
