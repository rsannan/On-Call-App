from marshmallow import Schema, fields

class HttpMethodReadSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.String(dump_only=True)