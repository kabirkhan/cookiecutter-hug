#!/bin/bash

pipenv run uwsgi --http 0.0.0.0:${PORT} --wsgi-file server.py --callable __hug_wsgi__