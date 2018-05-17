from flask_restful import fields, marshal_with
from marshmallow import Schema, fields as field
from webargs.flaskparser import use_kwargs

from functionality.book import get_book_details, rent_book, delete_book
from functionality.login import validate_user
from models import session
from resources.base_resource import BaseResource
from utils.utilities import get_current_jwt_identity

book_store_get_details = dict(
    book_list=fields.List(
        fields.Nested(
            dict(
                id=fields.Integer,
                book_name=fields.String
            )
        )
    )
)


class BookStoreRequestFormat(Schema):
    book_id = field.Int(required=True)

    class Meta:
        strict = True


class BookStore(BaseResource):
    decorators = BaseResource.decorators + [get_current_jwt_identity]

    @marshal_with(book_store_get_details)
    def get(self, user_id):
        response = get_book_details()
        return response

    @use_kwargs(BookStoreRequestFormat)
    def post(self, user_id, **kwargs):
        response = rent_book(user_id=user_id, book_id=kwargs.get('book_id'))
        session.commit()
        return response

    @use_kwargs(BookStoreRequestFormat)
    def delete(self, user_id, **kwargs):
        delete_book(user_id=user_id, book_id=kwargs.get('book_id'))
        session.commit()
        return dict(response="success")
