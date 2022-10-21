from flask import Blueprint
from flask_apispec import FlaskApiSpec
from flask_restful import Api

from resources.user import Login, Me, User, Users

api_blueprint = Blueprint("api", __name__)
api = Api(api_blueprint)

# API routes -- start
api.add_resource(Login, "/api/login")
api.add_resource(Me, "/api/me")
api.add_resource(User, "/api/user")
api.add_resource(Users, "/api/users")
# API routes -- end


docs = FlaskApiSpec()

# API docs -- start
docs.register(Login, blueprint="api")
docs.register(Me, blueprint="api")
docs.register(User, blueprint="api")
docs.register(Users, blueprint="api")
# API docs -- end