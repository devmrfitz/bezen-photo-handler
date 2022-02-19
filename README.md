This is a REST based backend for a webapp that provides a simple way to upload images , along-with some data like name, 
weight, etc).

## Tech Stack
- Django & Django Rest Framework: Project structure and the entirety of the REST API.
- Celery: Asynchronous (background) tasks.
- Redis: Serves as broker for celery.
- Docker-compose: Running and deploying the app.
- ImageMagick and wand: Image processing (resizing).
- Nginx: Serving the static and media files.
- Gunicorn: Serving the django app in production.

## How to run the app
You need to have [Docker Compose](https://docs.docker.com/compose/) installed on your machine.
Once that is done, clone this repository, cd into it and run the following command:
`cd docker && sudo docker-compose up -p bezen -d`. Now you can access the app at `http://localhost/`

## Available endpoints
- Record management
  - GET request on `/records`: List all the records.
  - GET request on `/records/<record_id>`: Get a single record.
  - POST request on `/records`: Create a new record.
  - PUT request on `/records/<record_id>`: Update a record.
  - DELETE request on `/records/<record_id>`: Delete a record.
- GET request on `/image/<record_id>/`: Get the image (resized to 140x140px) of a record.

## How to run the tests
1) Run the app as described [above](#how-to-run-the-app).
2) Run the tests with the following command:
`sudo docker exec bezen_uwsgi python manage.py test`

## Flow of the app
1) User POSTs a new record, along with an image.
2) The record is saved in the database, along with the image uploaded by the user.
3) Before returning the response, the server creates a background celery job to resize the image.
4) Celery worker processes the job and resizes the image in-place using Wand(ImageMagick).
