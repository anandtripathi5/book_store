from flask import Flask
from flask_jwt_extended import JWTManager

from models import get_session
from constants.common_constants import FLASK_CONFIG
from config import FLASK_APP_NAME
from helper import config_logger


def create_app():
    # flask bookapp configuration
    app = Flask(FLASK_APP_NAME)
    app.config.from_object(FLASK_CONFIG)

    # database session
    database_url = app.config.get("DATABASE_URL")
    if not database_url:
        raise Exception("DATABASE-URL-NOT-SET")
    session = get_session(database_url=database_url)

    # logger configuration
    config_logger(app)
    from resources.restful import restful_api
    restful_api(app)
    jwt_extended_mobile = JWTManager(app)

    # teardown database session
    def close_session(response_or_exc):
        session.remove()
        return response_or_exc
    app.teardown_appcontext(close_session)
    return app


main_app = create_app()

if __name__ == "__main__":
    main_app.run(host="0.0.0.0", port=5007)