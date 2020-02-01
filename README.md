# layerfive-demo
Angular with django database used postgres and django rest framework


## Prerequisites
* Users must have python installed on thier system
* Linux users can have git installed using `sudo apt-get install git`
* Must have virtual environment installted using `sudo apt-get install python3-virtualenv`
* Must have below libs installed to work with postgresql.
* Install these libs `sudo apt-get install python3-pip python3-dev libpq-dev postgresql postgresql-contrib`
* Now you are ready to go.

## Steps to run the project
* Clone the repository.
* Go the project directory
* Create and activate the virtual envrionment
* Using `python3 -m venv <virtual_env_name>` and `source <virtual_env_name>/bin/activate`
* install django using `pip install django==3.0.2`
* install drf using `pip install djangorestframework`
* install psycopg2 using `pip install psycopg2`
* Now create the database and the database user
* refer to this post - `https://www.digitalocean.com/community/tutorials/how-to-use-postgresql-with-your-django-application-on-ubuntu-14-04`
* install django-environ using `pip install django-environ`
* Now create a file named as `.env` and place it along with the `settings.py` file.
* Inside the `.env` file set `DEBUG` To `True` and `DATABASE_URL` To `psql://user:pass@127.0.0.1/dbname`
* Now run `python manage.py makemigrations layerfive`
* run `python manage.py migrate`
* run `python manage.py createsuperuser`
* Finally Run `python manage.py runserver`
* Congo vist `127.0.0.1:8000`
