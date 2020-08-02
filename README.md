# themillennialspress-backend

Backend in Django Rest Framework

## Setup

### Install

```bash
1. Install Python3, PostgreSQL, Redis and ELasticsearch.
2. pip install virtualenv
3. virtualenv newsenv   #creating virtual environment
4. source newsenv/bin/activate  #acivate the virtual environment
5. pip install -r requirements.txt  #install the dependencies
```

### Setup Database

```bash
1. sudo -u postgres psql
2. create database test;
3. create user testuser with password 'Admin@123';
4. grant all privileges on database test to testuser;
5. \q
```

### Setup django with db

```bash
1. python manage.py makemigrations
2. python manage.py migrate
```

### Run Django Server

```bash
1. python manage.py runserver
```
