from flask_restful import fields, marshal_with
from marshmallow import Schema, fields as field
from webargs.flaskparser import use_kwargs

from functionality.book import get_book_details, rent_book, delete_book
from functionality.user_statment import get_user_statement
from models import session
from resources.base_resource import BaseResource
from utils.utilities import get_current_jwt_identity

user_statement_response = dict(
    book_charges=fields.Float,
    number_of_books=fields.Integer
)


class UserStatement(BaseResource):
    decorators = BaseResource.decorators + [get_current_jwt_identity]

    @marshal_with(user_statement_response)
    def get(self, user_id):
        response = get_user_statement(user_id=user_id)
        return response
