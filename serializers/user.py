from marshmallow import Schema, fields

class UserSchema(Schema):
    address = fields.Str(dump_only=True)
    active = fields.Boolean(dump_only=True)
    name = fields.Str()
    profile_picture = fields.Str()
    collections = fields.Nested('CollectionSchema', many=True, dump_only=True)

class SiweLoginSchema(Schema):
    signature = fields.Str(required=True)
    # dict field for message
    message = fields.Dict(required=True)

class LoginResponse(Schema):
    access_token = fields.Str(required=True)