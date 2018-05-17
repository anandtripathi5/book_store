from functools import wraps

from flask_basicauth import BasicAuth
from flask_jwt_extended import get_jwt_identity, jwt_required

basic_auth = None


def flask_admin_auth(app):
    global basic_auth
    if basic_auth:
        return basic_auth
    basic_auth = BasicAuth(app)
    return basic_auth


def get_current_jwt_identity(fn):

    @wraps(fn)
    @jwt_required
    def wrapper(*args, **kwargs):
        current_user_id = get_jwt_identity()
        return fn(current_user_id, *args, **kwargs)
    return wrapper
