#!/bin/bash
exec gunicorn -w 2 -b 0.0.0.0:5007 --log-level=debug flask_app:main_app --access-logfile /dev/stdout
