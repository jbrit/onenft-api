from functools import wraps
from auth_middleware import token_required
from serializers.collection import CollectionSchema
from flask_apispec import marshal_with, use_kwargs
from utils import Resource, update_object_from_dict
from flask import abort
from marshmallow import fields
import models

def collection_owner(f):
    @wraps(f)
    @token_required
    def decorated(*args, **kwargs):
        current_user = kwargs.get('current_user')
        collection = models.db.get_or_404(models.Collection, kwargs.get('collection_address'))
        if collection.owner != current_user.address:
            abort(403, "You are not the owner of this collection")
        return f(*args, **kwargs)
    return decorated


class Collections(Resource):
    @marshal_with(CollectionSchema(many=True))
    def get(self):
        return models.Collection.query.all()
    
    @use_kwargs({'collection_address': fields.Str()}, location="query") # it passes collection_address to the function
    @use_kwargs(CollectionSchema())
    @marshal_with(CollectionSchema())
    @token_required
    def post(self, current_user, collection_address, **kwargs):
        # check if collection exists
        collection = models.Collection.query.filter_by(address=collection_address).first()
        if collection is not None:
            abort(400, "Collection already exists")
        collection = models.Collection(owner=current_user.address, address=collection_address)
        update_object_from_dict(collection, kwargs)
        models.db.session.add(collection)
        models.db.session.commit()
        return collection


class Collection(Resource):
    @use_kwargs({'address': fields.Str()}, location="query")
    @marshal_with(CollectionSchema())
    def get(self, address):
        return models.db.get_or_404(models.Collection, address)

    @use_kwargs({'collection_address': fields.Str()}, location="query") # it passes collection_address to the function
    @use_kwargs(CollectionSchema(partial=True)) # it passes the collection schema to the function as kwargs
    @marshal_with(CollectionSchema())
    @collection_owner # it passes current_user to the function
    def patch(self, collection_address, current_user, **kwargs):
        collection = models.db.get_or_404(models.Collection, collection_address)
        update_object_from_dict(collection, kwargs)
        models.db.session.commit()
        return collection

