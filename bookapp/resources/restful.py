from flask_restful import Api

from book_store_demo import BookStoreDemo
from resources.login import Login, Refresh
from sign_up import SignUp


def restful_api(app):
    api = Api(app, prefix="/api/v1")
    api.add_resource(BookStoreDemo, '/book_store_demo', strict_slashes=False)
    api.add_resource(SignUp, '/signup', strict_slashes=False)
    api.add_resource(Login, '/login', strict_slashes=False)
    api.add_resource(Refresh, '/refresh', strict_slashes=False)
