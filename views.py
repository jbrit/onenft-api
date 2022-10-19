from flask import Blueprint
from flask_apispec import FlaskApiSpec
from flask_restful import Api

from resources.user import Login, Me

api_blueprint = Blueprint("api", __name__)
api = Api(api_blueprint)

# API routes -- start
api.add_resource(Login, "/api/login")
api.add_resource(Me, "/api/me")
# API routes -- end


docs = FlaskApiSpec()

# API docs -- start
docs.register(Login, blueprint="api")
docs.register(Me, blueprint="api")
# API docs -- end