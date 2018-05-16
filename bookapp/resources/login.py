from flask_jwt_extended import create_access_token, \
    jwt_refresh_token_required, get_jwt_identity
from flask_restful import fields, marshal_with
from marshmallow import Schema, fields as field
from webargs.flaskparser import use_kwargs
from functionality.login import validate_user
from resources.base_resource import BaseResource


class LoginRequestFormat(Schema):
    user_name = field.Str(required=True)
    password = field.Str(required=True)

    class Meta:
        strict = True


login_response_format = dict(
    access_token=fields.String,
    refresh_token=fields.String
)


class Login(BaseResource):

    @marshal_with(login_response_format)
    @use_kwargs(LoginRequestFormat)
    def get(self, **kwargs):
        response = validate_user(**kwargs)
        return response


class Refresh(BaseResource):
    decorators = BaseResource.decorators + [jwt_refresh_token_required]

    @marshal_with(login_response_format)
    def get(self):
        current_user_id = get_jwt_identity()
        return {
                'access_token': create_access_token(identity=current_user_id),
        }
