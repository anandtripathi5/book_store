from flask_cors import CORS
from flask_restful import Api

from resources.book_store_demo import BookStoreDemo


def restful_api(app):
    CORS(app, resources={r"/*": {"origins": "*"}})

    api = Api(app, prefix="/api/v1")
    api.add_resource(BookStoreDemo, '/book_store_demo', strict_slashes=False)
