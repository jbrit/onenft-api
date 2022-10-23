import sentry_sdk
from sentry_sdk.integrations.flask import FlaskIntegration
from flask import Flask
from flask_cors import CORS
from flask_restful import abort
from flask_migrate import Migrate
from webargs.flaskparser import parser
from config import app_config
from views import api_blueprint, docs
from models import db

# This error handler is necessary for usage with Flask-RESTful
# pylint: disable=unused-argument
@parser.error_handler
def handle_request_parsing_error(err, req, schema, **kwargs):
    """webargs error handler that uses Flask-RESTful's abort function to return
    a JSON error response to the client.
    """
    abort(422, errors=err.messages)




migrate = Migrate()

def create_app():
    sentry_sdk.init(
        dsn="https://00075a88100047cb8f4107d63658e980@o971311.ingest.sentry.io/4504034076131328",
        integrations=[
            FlaskIntegration(),
        ],
        traces_sample_rate=1.0
    )
    app = Flask(__name__)
    cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
    app.config.update(app_config)
    app.register_blueprint(api_blueprint)
    db.init_app(app)
    migrate.init_app(app, db)
    docs.init_app(app)
    return app