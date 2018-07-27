## Python cookiecutter api using the `hug` REST framework

> Check out [hug](http://www.hug.rest/). It's basically Flask but much better.

## Requirements
- Python >= 3.6 with pip installed

## Quickstart
Install the latest [Cookiecutter](https://github.com/audreyr/cookiecutter) if you haven't installed it yet (this requires Cookiecutter 1.4.0 or higher):
```
pip install --user cookiecutter
```

Generate a Hug REST API project with the following command and specify your project settings
```
cookiecutter https://github.com/kabirkhan/cookiecutter-hug
```

To run locally without Docker
```
pip install --user pipenv
cd hug_cookiecutter
pipenv install

pipenv shell
hug -f app.py
```

To run behind uwsgi inside a Docker container run
```
docker build . -t {YOUR_PROJECT_NAME}
docker run -it -p 8080:8080 -e PORT=8080 {YOUR_PROJECT_NAME}
```

visit http://`localhost`:8080/health

(localhost could be replaced with `0.0.0.0` or `hostname`)
For documentation of all routes visit a 404 page route (e.g. http://localhost:8080)

## Helpful resources

- https://github.com/timothycrosley/hug