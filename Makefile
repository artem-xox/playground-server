# variables
PROD_PORT = 5000
DEV_PORT = 5001
IMAGE = playground-server
CONTAINER = ${IMAGE}-container

# environment
install:
	poetry install

# launch
run:
	gunicorn --bind 0.0.0.0:${PROD_PORT} --workers 1 --timeout 300 app.wsgi:app

debug:
	flask --app app/base --debug run --port=${DEV_PORT}

# docker
docker-build:
	docker build -t ${IMAGE} .

docker-up: docker-build
	docker run --name ${CONTAINER} --rm -p ${PROD_PORT}:${PROD_PORT} ${IMAGE}

docker-down:
	docker kill ${CONTAINER}

docker-reup: docker-down docker-up
