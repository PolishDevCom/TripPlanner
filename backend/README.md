# Trip Planner

Live version: 

Website presenting trips created for the user. Using map and places APIs. User choose country/city and budget for adventure and website creates trip offer with highlighted interesting places. Routes can be edited, rated and shared. Created with Django + React frameworks.

Status: In progress 


## Table of contents
* [Technologies](#technologies)
* [Setup](#setup)
* [Contact](#contact)

## Technologies
* Python version: 3.7
* Django version: 3.1.1
* DRF version: 3.11.1

## Setup

### How to setup database?

Pre-requirements
```
$ sudo apt-get update
$ sudo apt-get install python3-pip python3-dev libpq-dev postgresql postgresql-contrib
```

Create a database and database user

```
$ sudo -u postgres psql
```
```
postgres=# CREATE DATABASE tripplanner;
postgres=# CREATE USER tripadmin WITH PASSWORD 'trippass';
postgres=# ALTER ROLE tripadmin SET client_encoding TO 'utf8';
postgres=# ALTER ROLE tripadmin SET default_transaction_isolation TO 'read committed';
postgres=# ALTER ROLE tripadmin SET timezone TO 'UTC';
postgres=# GRANT ALL PRIVILEGES ON DATABASE tripplanner TO tripadmin;
postgres=# \q

```

Update `settings.py` file.
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'tripplanner',
        'USER': 'tripadmin',
        'PASSWORD': 'trippass',
        'HOST': 'localhost',
        'PORT': '',
    }
}
```

Migrate and create superuser
```
(project-venv) $ cd backend
(project-venv) $ python manage.py makemigrations
(project-venv) $ python manage.py migrate
(project-venv) $ python manage.py createsuperuser
```

## Contact
