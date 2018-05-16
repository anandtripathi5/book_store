from functools import wraps
from flask_restful import abort
from werkzeug.exceptions import UnprocessableEntity

from flask import current_app as app
from sqlalchemy.exc import SQLAlchemyError, IntegrityError


def handle_exceptions(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        from models import session
        try:
            return fn(*args, **kwargs)
        except ValueError as val_err:
            app.logger.error(val_err)
            session.rollback()
            abort(400, message=val_err.message)
        except KeyError as key_err:
            app.logger.error(key_err)
            session.rollback()
            abort(400, message=key_err.message)
        except IOError as io_err:
            app.logger.error()
            session.rollback()
            abort(500, message=io_err.message)
        except IntegrityError as err:
            app.logger.error(err)
            session.rollback()
            abort(500, message=err.message)
        except SQLAlchemyError as sa_err:
            app.logger.error(sa_err)
            session.rollback()
            abort(500, message=sa_err.message)
        except UnprocessableEntity as sa_err:
            app.logger.error(sa_err)
            try:
                message = sa_err.data.get("messages", None)
            except Exception as sa_err:
                message = sa_err.message
            session.rollback()
            abort(422, message=message)
        except Exception as exc:
            app.logger.error(exc)
            session.rollback()
            abort(500, message=exc.message)

    return wrapper
