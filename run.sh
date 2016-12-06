#!/bin/bash
# python -m unittest discover
# coverage run -m unittest discover -s tests/
pypy manage.py db:init
pypy manage.py db:migrate
uwsgi --socket 0.0.0.0:8000 --protocol=http -w wsgi