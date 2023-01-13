#!/usr/bin/python3
"""
This module contains the schemas for validating
incoming and outgoing requests to the checks endpoint
"""

from marshmallow import Schema, fields
from views.schemas.user import ReadUserSchema
from views.schemas.http_header import HTTPHeaderSchema


class CheckCreateSchema(Schema):
    id = fields.Int(dump_only=True)
    title = fields.Str()
    url = fields.Str()
    method_id = fields.Int()
    data = fields.Str()
    status_code = fields.Int()
    response_status_code = fields.Int(dump_only=True)
    created_at = fields.DateTime(),
    last_checked = fields.DateTime(),
    response_time = fields.Int()
    status = fields.Bool(dump_only=True)
    user_id = fields.Int(required=True, dump_only=True)
    headers = fields.List(fields.Nested(HTTPHeaderSchema, required=False))


class CheckReadSchema(Schema):
    id = fields.Int(dump_only=True)
    title = fields.Str()
    url = fields.Str()
    method_id = fields.Int()
    data = fields.Str()
    status_code = fields.Integer()
    response_time = fields.Int()
    created_at = fields.DateTime(dump_only=True),
    last_checked = fields.DateTime(dump_only=True),
    status = fields.Bool(dump_only=True)
    user_id = fields.Int(required=True)    
    user = fields.Nested(ReadUserSchema())
    response_status_code = fields.Int(dump_only=True)
    headers = fields.List(fields.Nested(HTTPHeaderSchema, required=False))


class CheckUpdateSchema(Schema):
    id = fields.Int(dump_only=True)
    title = fields.Str()
    url = fields.Str()
    method_id = fields.Int()
    data = fields.Str()
    status_code = fields.Integer()
    response_time = fields.Int()
    status = fields.Bool()
    user_id = fields.Int(dump_only=True)    
    user = fields.Nested(ReadUserSchema, dump_only=True)
    created_at = fields.Date(dump_only=True),
    last_checked = fields.Date(dump_only=True),
    response_status_code = fields.Int(dump_only=True)
    headers = fields.List(fields.Nested(HTTPHeaderSchema))