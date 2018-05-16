from flask_jwt_extended import create_access_token, create_refresh_token
from flask_restful import fields, marshal_with
from marshmallow import Schema, fields as field
from webargs.flaskparser import use_kwargs

from functionality.users import create_user
from models import session
from resources.base_resource import BaseResource


class SignUpRequestFormat(Schema):
    user_name = field.Str(required=True)
    email = field.Str(required=True)
    password = field.Str(required=True)

    class Meta:
        strict = True


sign_up_response_format = dict(
    access_token=fields.String,
    refresh_token=fields.String
)


class SignUp(BaseResource):

    @marshal_with(sign_up_response_format)
    @use_kwargs(SignUpRequestFormat)
    def post(self, *args, **kwargs):
        user_id = create_user(**kwargs)
        session.commit()
        return {
            'access_token': create_access_token(
                identity=user_id),
            'refresh_token': create_refresh_token(
                identity=user_id)
        }
