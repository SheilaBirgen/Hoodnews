# NeighbourhoodNews

## Description

**NeighbouhoodNews** is a web application that allows a user to stay in the loop with what is happening around their neighbourhood.

## BDD


## installations

These instructions will get you copy of this project up and running for local development and testing purposes.

### Prerequisites

- [Git](https://git-scm.com/)
- [Python](https://www.python.org/)
- [Pipenv](https://pypi.org/project/pipenv/)
- [PostgreSQL](https://www.postgresql.org/)

### Installation and Setup

Clone this repo and navigate to root folder:

```
$ git clone https://github.com/AhmadSAshraf/Hood-News.git
$ cd HoodNews
```

Create a virtualenv and install project dependencies:

```
$ pipenv install

```
Activate the virtualenv:

```
$ pipenv shell
```

### Database Configuration

Ensure you have PostgreSQL installed and running. Then,

Create a new database:

```
$ createdb db-name
```

Create a password for the db role:

```
$ psql db-name
db-name=# ALTER USER role-name PASSWORD 'new-password'
```
Note: `db-name` is the name of the database, `role-name` is the name of the PostgreSQL role or username to connect as and `new-password` is the user password.

### Launching the application

Create a `.env` file and set the following env variables:

```
SECRET_KEY=<YOUR_SECRET_KEY>
DEBUG='True'

DB_NAME='<YOUR_DATABASE_NAME>'
DB_USER='<YOUR_DATABASE_USER>'
DB_PASSWORD='<YOUR_DATABASE_PASSWORD>'
```

Run the following commands to create the database tables:

```
python manage.py makemigrations
python manage.py migrate
```

Finally, fire up server and navigate to http://127.0.0.1:8000/

```
python manage.py runserver
```

## Built using

- [Django](https://www.djangoproject.com/) - The web framework for perfectionists with deadlines.
- [django-rest-framework](https://www.django-rest-framework.org/) - A powerful and flexible toolkit for building Web APIs.
- [Bootstrap](https://getbootstrap.com/) - The world’s most popular framework for building responsive, mobile-first sites.

## CODEBEAT


## Contributors
[ AhmadSAshraf](https://github.com/AhmadSAshraf/Hood-News.git),
[ Jecinta ](https://github.com/Jecinta),
[ SheilaBirgen ](https://github.com/SheilaBirgen)

## License

Distributed under the MIT License. See [LICENSE](LICENSE) for more information.