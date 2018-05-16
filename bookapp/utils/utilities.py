from flask_basicauth import BasicAuth

basic_auth = None


def flask_admin_auth(app):
    global basic_auth
    if basic_auth:
        return basic_auth
    basic_auth = BasicAuth(app)
    return basic_auth