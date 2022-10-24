from flask import Blueprint
from flask_apispec import FlaskApiSpec
from flask_restful import Api
from resources.collection import Collection, CollectionMetadata, Collections, TokenMetadata

from resources.user import Login, Me, User, Users

api_blueprint = Blueprint("api", __name__)
api = Api(api_blueprint)

# API routes -- start
api.add_resource(Login, "/api/login")
api.add_resource(Me, "/api/me")
api.add_resource(User, "/api/user")
api.add_resource(Users, "/api/users")
api.add_resource(Collection, "/api/collection")
api.add_resource(Collections, "/api/collections")
api.add_resource(CollectionMetadata, "/api/collection/metadata")
api.add_resource(TokenMetadata, "/api/token/metadata")
# API routes -- end


docs = FlaskApiSpec()

# API docs -- start
docs.register(Login, blueprint="api")
docs.register(Me, blueprint="api")
docs.register(User, blueprint="api")
docs.register(Users, blueprint="api")
docs.register(Collection, blueprint="api")
docs.register(Collections, blueprint="api")
docs.register(CollectionMetadata, blueprint="api")
docs.register(TokenMetadata, blueprint="api")
# API docs -- end