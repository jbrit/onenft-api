from functools import wraps
from auth_middleware import token_required
from siwe import SiweMessage
from serializers.user import LoginResponse, SiweLoginSchema, UserSchema
from flask_apispec import marshal_with, use_kwargs
from utils import Resource
from flask import abort, current_app
import models
import jwt

class Login(Resource):
    @use_kwargs(SiweLoginSchema())
    @marshal_with(LoginResponse())
    def post(self, **kwargs):
        message = kwargs.get('message')

        # replace camel with snake case to be parsed correctly
        if message.get('issuedAt'):
            message['issued_at'] = message['issuedAt']
            del message['issuedAt']
        if message.get('chainId'):
            message["chain_id"] = message["chainId"]
            del message["chainId"]

        signature = kwargs.get('signature')
        message = SiweMessage(message=message)
        try:
            message.verify(signature=signature)
        except Exception as e:
            abort(400, str(e))
        address = message.address

        # check if user exists and create if not
        user = models.User.query.filter_by(address=address).first()
        if user is None:
            user = models.User(address=address)
            models.db.session.add(user)
            models.db.session.commit()

        if not user.active:
            abort(403)

        token = {"access_token" : jwt.encode({'address': address}, current_app.config['SECRET_KEY'], algorithm='HS256')}
        return token


class Me(Resource):
    @token_required
    @marshal_with(UserSchema())
    def get(self, **kwargs):
        return kwargs.get('current_user')

