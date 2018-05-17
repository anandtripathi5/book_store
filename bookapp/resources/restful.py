from flask_admin import Admin
from flask_restful import Api
from models import session
from models.admin_model import ModelView
from models.book import Book, UserBookMapping
from models.users import User
from resources.book import BookStore
from resources.login import Login, Refresh
from resources.user_statement import UserStatement
from sign_up import SignUp


def restful_api(app):
    api = Api(app, prefix="/api/v1")
    api.add_resource(SignUp, '/signup', strict_slashes=False)
    api.add_resource(Login, '/login', strict_slashes=False)
    api.add_resource(Refresh, '/refresh', strict_slashes=False)
    api.add_resource(BookStore, '/book_store', endpoint="get_book_details",
                     strict_slashes=False)
    api.add_resource(BookStore, '/book_store', endpoint="rent_book",
                     strict_slashes=False)
    api.add_resource(BookStore, '/book_store', endpoint="delete_book",
                     strict_slashes=False)
    api.add_resource(UserStatement, '/user_statement',
                     endpoint="get_user_statement", strict_slashes=False)


    # admin
    admin = Admin(app, template_mode='bootstrap3')
    admin.add_view(ModelView(User, session))
    admin.add_view(ModelView(Book, session))
    admin.add_view(ModelView(UserBookMapping, session))

