# variables
PROD_PORT = 5000
DEV_PORT = 5001


# environment
install:
	poetry install


# launch
run:
	gunicorn --bind 0.0.0.0:${PROD_PORT} --workers 1 --timeout 300 app.wsgi:app

debug:
	flask --app app/base --debug run --port=${DEV_PORT}