# Installation

## Installation pre-requesites:

- Install pip globally:
```bash
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python3 get-pip.py
source ~/.bashrc
```

- Install `pipenv`: pip install --user pipenv

- Note: if you have `python 3.9` then you should install `djangorestframework-simplejwt==4.6.0` by issuing `pipenv install djangorestframework-simplejwt==4.6.0`

## Installation
- Clone project: `git clone git@github.com:devkurultay/django-react-starter-kg.git`

- Go to project `cd django-react-starter-kg`

- Install project dependecies: `pipenv install`

- Activate the project's virtual environment: `pipenv shell`

- Go to `backend` and run migrations: `cd backend/ && ./manage.py migrate`

## Run the project
- Create superuser: `./manage.py createsuperuser`

- Run the server: `./manage.py runserver`

- Open the project in your browser (this leads to Swagger UI): `http://localhost:8000/sw/`