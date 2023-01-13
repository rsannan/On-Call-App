#!/usr/bin/python3
"""
Defines a schemal for http header
"""
from marshmallow import fields, Schema


class HTTPHeaderSchema(Schema):
    """
    Defines a schema for http header
    """
    id = fields.Int(dump_only=True, required=True)
    check_id = fields.Int(required=False)
    value = fields.Str(required=False)
    key = fields.Str(required=True)

    
