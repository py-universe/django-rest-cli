# Basic Template
The Basic template comes bundled with:

- git initialized
- Readme file with project setup instructions
- python-decouple: for managing environment varibales 
[See Package Docs Here](https://pypi.org/project/python-decouple/). 
- drf-spactacular: for auto-generating APi docs 
[See Package Docs Here](https://drf-spectacular.readthedocs.io/en/latest/readme.html). 


# Medior Template
The Medior template comes bundled with:

- **Everything in the Basic Template +**
- A custom user model defined in a `users` app
- dj-database-url: for connecting to various databases 
[See Package Docs Here](https://github.com/jazzband/dj-database-url). 
- pre-commit, black, isort, flake8: for code linting with pre-commit hooks 
[See this tutorial for more on working with pre-commit hooks in Python](https://ljvmiranda921.github.io/notebook/2018/06/21/precommits-using-black-and-flake8/)


# Advanced Template
The Advanced template comes bundled with:

- **Everything in the Medior Template +**
- pytest-django: for writing unit tests with pytest 
[See Package Docs Here](https://pytest-django.readthedocs.io/en/latest/). 
- Docker for containerization. We are using docker to setup the postgres db for this project as well.
[check out this tutorial for guide on how to work with docker, and postgres in Django](
	https://learndjango.com/tutorials/django-docker-and-postgresql-tutorial
)
- Authentication endpoints defined in an `authentication` app with the `dj-rest-auth and all-auth` packages.
[See Package Docs Here](https://dj-rest-auth.readthedocs.io/en/latest/introduction.html). 