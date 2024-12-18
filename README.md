
## Setup
```
$ mkdir flask-pto-api
$ cd flask-pto-api
```

We will then initialize our virtual environment and install the necessary packages. We will use a package manager called “pip” to download these packages. Pip is a package within Python that can download packages from an external repository.
```
$ pip install pipenv
$ python -m venv venv 
$ source venv\bin\activate
$ pipenv shell
$ pip install Flask Flask-SQLAlchemy Flask-JWT-Extended Flask-Migrate
```

Here we install “Flask”, “Flask-SQLAlchemy”, “Flask-JWT-Extended", and “Flask-Migrate”. These packages will be used to create the backbone of our API. The latest versions provided by pip at the time of this being built are Flask 3.0, Flask-JWT-Extended 4.5.3, Flask-Migrate 4.0.5, and FlaskSQLAlchemy 3.1.1.

* Flask is a web framework for Python that provides a lightweight and modular structure for rapid REST API development.
* Flask-SQLAlchemy is an extension for Flask that simplifies database integration by providing SQLAlchemy support from within Python.
* Flask-JWT-Extended is an extension for Flask that adds support for JSON Web Tokens (JWT), allowing user authentication and authorization. Flask-Migrate is an extension for Flask that integrates Alembic, a database migration framework. This will automate the process of managing database schema changes as the application grows. 

## Database Initialization and Models

A data model typically refers to the representation of the application's data structure using Flask-SQLAlchemy. Models are defined as Python classes, each representing a table in the database, and they include attributes that map to the table's columns. 

Now that we are here, it is time to initialize our Flask database. In your terminal, run the following commands:
```
$ flask db init
$ flask db migrate
$ flask db upgrade
```

The **‘flask db init’** command initializes a new migration environment. It creates a "migrations" directory in your Flask project if it doesn't exist already. This directory will be used to store migration scripts that track changes to the database schema over time. 

The **‘flask db migrate’** command generates an automatic migration script based on the changes detected in the models (data models or database tables) of your Flask application. It analyzes the differences between the current state of the database and the state defined by the models and creates a migration script to apply those changes. 

The **‘flask db upgrade’** command applies the changes specified in the migration scripts to the actual database. It brings the database schema up to date with the latest version defined by the models. This command is typically run after ‘flask db migrate’ to execute the generated migration script. You generally want to run ‘flask db migrate’ and ‘flask db upgrade’ any time you make changes to your data models.
