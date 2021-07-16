# Dojo CKL Django

This is a simple project to learn the basics of [Django](https://www.djangoproject.com/) and [Django Rest Framework](https://www.django-rest-framework.org/) following the TDD (Test Driven Development) philosophy.

## How to run the project

- Make sure that you have [python](https://www.python.org/) 3.8.0 installed.

After this you can run (Linux based system):

```shell
$ git clone https://github.com/CaioTeixeira95/dojo_django.git
$ cd dojo_django
$ python3 -m venv venv
$ source venv/bin/activate
```

Installing the project dependencies:

```shell
$ pip install -r requirements.txt
```

Running the tests:

```shell
$ pytest -v
```

Initiating the Django development server:

```shell
$ python manage.py runserver
```

## Our initial goals with this project:

- [x] Create a Restaurant model
- [x] Run migrations
- [ ] Create a Restaurant serializer
- [ ] Create a Restaurant viewset
- [ ] Create a Restaurant routes
- [ ] Create a Restaurant model admin
