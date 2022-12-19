from marshmallow import Schema, fields


class CreateUserSchema(Schema):
    id = fields.Int(required=True, dump_only=True)
    firstname = fields.Str(required=True)
    lastname = fields.Str(required=True)
    email = fields.Str(required=True)
    phone = fields.Str(required=True)
    password = fields.Str(required=True, load_only=True)

class ReadUserSchema(Schema):
    id = fields.Int(dump_only=True)
    firstname = fields.Str(dump_only=True)
    lastname = fields.Str(dump_only=True)
    email = fields.Str(dump_only=True)
    phone = fields.Str(dump_only=True)

class UserUpdateSchema(Schema):
    id = fields.Int()
    firstname = fields.Str()
    lastname = fields.Str()
    email = fields.Str()
    phone = fields.Str()






