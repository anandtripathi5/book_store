from flask import current_app as app
from flask_restful import Resource

from utils.resource_exceptions import handle_exceptions


class BaseResource(Resource):
    decorators = [handle_exceptions]

    def __init__(self):
        app.logger.debug(
            'In the constructor of {}'.format(self.__class__.__name__))

