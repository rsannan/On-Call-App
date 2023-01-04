#!/usr/bin/python3
"""
This module contains the schemas for validating
incoming and outgoing requests to the checks endpoint
"""

from marshmallow import Schema, fields
from views.schemas.user import ReadUserSchema


class CheckCreateSchema(Schema):
    id = fields.Int(dump_only=True)
    title = fields.Str()
    url = fields.Str()
    method_id = fields.Int()
    status_code = fields.Integer()
    check_count = fields.Int()
    status = fields.Bool(dump_only=True)
    user_id = fields.Int(required=True, dump_only=True)


class CheckReadSchema(Schema):
    id = fields.Int(dump_only=True)
    title = fields.Str()
    url = fields.Str()
    method_id = fields.Int()
    status_code = fields.Integer()
    check_count = fields.Int()
    status = fields.Bool(dump_only=True)
    user_id = fields.Int(required=True)    
    user = fields.Nested(ReadUserSchema())


class CheckUpdateSchema(Schema):
    id = fields.Int(dump_only=True)
    title = fields.Str()
    url = fields.Str()
    method_id = fields.Int()
    status_code = fields.Integer()
    check_count = fields.Int()
    status = fields.Bool()
    user_id = fields.Int(dump_only=True)    
    user = fields.Nested(ReadUserSchema)



