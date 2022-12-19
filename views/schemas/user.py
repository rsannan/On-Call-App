from marshmallow import Schema, fields


class PlainUserSchema(Schema):
    id = fields.Int(required=True, dump_only=True)
    firstname = fields.Str(required=True)
    lastname = fields.Str(required=True)
    email = fields.Str(required=True)
    phone = fields.Str(required=True)
    password = fields.Str(required=True, load_only=True)
