import os

import sys
from datetime import timedelta

FLASK_APP_NAME = os.environ.get("FLASK_APP_NAME")
DEBUG = os.environ.get("FLASK_DEBUG")
DATABASE_URL = os.environ.get("DATABASE_URL")
SECRET_KEY = "my_secret_key"
JWT_EXPIRATION_DELTA = timedelta(days=120)
JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=2)
JWT_REFRESH_TOKEN_EXPIRES = timedelta(days=999999)

DEFAULT_LOGGER_NAME = os.environ.get("DEFAULT_LOGGER_NAME")
LOGGING_CONFIG = dict(
    version=1,
    formatters={
        'compact': {
            'format': '%(process)d - %(asctime)s - %(filename)s - '
                      '%(module)s - %(funcName)s - %(lineno)d - '
                      '[%(levelname)s] - %(message)s'
        },
        'err_report': {'format': '%(asctime)s\n%(message)s'}
    },
    handlers={
        DEFAULT_LOGGER_NAME: {
            'class': 'logging.StreamHandler',
            'stream': sys.stdout,
            'formatter': 'compact',
            'level': 'DEBUG'
        },
        'critical_err': {
            'class': 'logging.handlers.SMTPHandler',
            'formatter': 'err_report',
            'mailhost': ("localhost", 25),
            'fromaddr': 'no-reply@onehop.co',
            'toaddrs': [
                'anand.tripathi507@gmail.com'
            ],
            'subject': 'Book store exception occurred'
        }
    },
    loggers={
        DEFAULT_LOGGER_NAME: {
            'handlers': [DEFAULT_LOGGER_NAME],
            'level': 'DEBUG',
            'propagate': False
        },
        'crash': {
            'handlers': ['critical_err', DEFAULT_LOGGER_NAME],
            'level': 'ERROR',
            'propagate': False
        },
    }
)
