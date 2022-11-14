#!/usr/bin/env bash
poetry run gunicorn --bind 0.0.0.0:5000 --workers 1 --timeout 300 app.wsgi:app