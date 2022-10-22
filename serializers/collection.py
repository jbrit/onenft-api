from marshmallow import Schema, fields, validate

from constants import COLLECTION_CATEGORIES

class CollectionSchema(Schema):
    address = fields.Str(dump_only=True)
    owner = fields.Str(dump_only=True)
    name = fields.Str()
    description = fields.Str()
    image = fields.Str()
    royalty = fields.Int()
    twitter = fields.Str()
    instagram = fields.Str()
    discord = fields.Str()
    telegram = fields.Str()
    website = fields.Str()
    email = fields.Str()
    platform_created = fields.Boolean()
    category = fields.Str(validate=validate.OneOf(COLLECTION_CATEGORIES))