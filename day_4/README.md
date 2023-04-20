<style> .markdown-body { font-size: 1em; } .markdown-body h1 { color: #409f42; } .markdown-body h2 { color: #409f42; } .markdown-body h3 { text-decoration: underline; } .markdown-body p { color: #909090 } </style>

# Python Day 4

- Flask-login and Flask-WTForms
- Flask-SQLAlchemy and ORM
- Testing Flask Applications
- Bootstrap


## Flask-Login and Flask-WTForms

Flask-Login provides user session management for Flask. It handles the common tasks of logging in, logging out, and remembering your users’ sessions over extended periods of time.

Flask-WTForms is a simple integration of Flask and WTForms, including CSRF, file upload, and reCAPTCHA support.

You can use it in conjunction with SQLAlchemy to store your user data in a database and Flask-WTForms to handle your login and registration forms.

### Using Flask-WTForms

To create a new form in Flask-WTForms, add the following code to your `app.py` file:

```python
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8)])
    submit = SubmitField('Login')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        user = User.query.filter_by(email=email).first()
        if user and user.password == password:
            login_user(user)
            return redirect(url_for('index'))
        return '<h1>Invalid email or password</h1>'
    return render_template('login.html', form=form)
```

To show the form in your template, you would use the following code:

```html
<form method="POST">
    {{ form.hidden_tag() }}
    {{ form.email.label }} {{ form.email() }}
    {{ form.password.label }} {{ form.password() }}
    {{ form.submit() }}
</form>
```

## Flask-SQLAlchemy

 Flask-Sqlalchemy is a wrapper for SQLAlchemy. It is used to simplify the usage of SQLAlchemy with Flask.

 Some of the most useful features of Flask-SQLAlchemy are:

  -   It is configured using the `SQLALCHEMY_DATABASE_URI` configuration key. The value of this key should be a string that represents the database URI. For example, `sqlite:///./sql_app.db` is the URI for a SQLite database called `sql_app.db` that is stored in the current directory.

  -   It automatically creates a database session that is available inside view functions. The session is available using the `current_session` object.

  -   It provides a `Model` class that is a declarative base which can be used to declare models.

  -   It provides a `Query` class that is a subclass of `sqlalchemy.orm.Query` and adds some convenience methods to it.

  -   It provides a `SQLAlchemy` class that is a subclass of `sqlalchemy.orm.Session` and adds some convenience methods to it.


### Flask-SQLAlchemy Basics

To use Flask-SQLAlchemy, add the following code to your `app.py` file:

```python

from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__) # create a new flask app
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./sql_app.db' # set the database URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # set track modifications to false to prevent a warning
db = SQLAlchemy(app) # create a new SQLAlchemy object

class User(db.Model): # create a new model
    __tablename__ = 'users' # set the table name

    id = db.Column(db.Integer, primary_key=True, index=True) # set the id column
    name = db.Column(db.String, unique=True, index=True) # set the name column
    email = db.Column(db.String, unique=True, index=True) # set the email column
    password = db.Column(db.String) # set the password column

    def __repr__(self):
        return f'User {self.name}' # return the user name when printing the user

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST': # check if the request method is POST
        name = request.form.get('name') # get the name from the form
        email = request.form.get('email') # get the email from the form
        password = request.form.get('password') # get the password from the form

        user = User(name=name, email=email, password=password) # create a new user
        db.session.add(user) # add the user to the database session
        db.session.commit() # commit the changes to the database
        return render_template('index.html', msg='User created successfully!') # render the index template

    return render_template('index.html', msg='') # render the index template

@app.route('/users')
def users():
    users = User.query.all() # get all the users
    return render_template('users.html', users=users) # render the users template

if __name__ == '__main__':
    app.run(debug=True)
```

## ORM

ORM stands for Object Relational Mapping. It is a technique that lets you query and manipulate data from a database using an object-oriented paradigm.


## Flask-SQLAlchemy Relationships

There are two types of relationships in SQLAlchemy:

  -   One-to-one relationship: A one-to-one relationship is a relationship between two tables in which each row in one table is related to one and only one row in the other table.

  -   One-to-many relationship: A one-to-many relationship is a relationship between two tables in which each row in one table is related to one or more rows in the other table.


### One-to-One Relationship

To create a one-to-one relationship, add the following code to your `app.py` file:

```python
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

class Profile(db.Model): # create a new model
    __tablename__ = 'profiles' # set the table name

    id = db.Column(db.Integer, primary_key=True, index=True) # set the id column
    bio = db.Column(db.String) # set the bio column
    user_id = db.Column(db.Integer, ForeignKey('users.id')) # set the user id column

    user = relationship('User', back_populates='profile') # create a relationship with the user model

    def __repr__(self):
        return f'Profile {self.bio}' # return the profile bio when printing the profile

class User(db.Model): # create a new model
    __tablename__ = 'users' # set the table name

    id = db.Column(db.Integer, primary_key=True, index=True) # set the id column
    name = db.Column(db.String, unique=True, index=True) # set the name column
    email = db.Column(db.String, unique=True, index=True) # set the email column
    password = db.Column(db.String) # set the password column

    profile = relationship('Profile', uselist=False, back_populates='user') # create a relationship with the profile model

    def __repr__(self):
        return f'User {self.name}' # return the user name when printing the user
```

### One-to-Many Relationship

One to many relationships are used to represent a one-to-many relationship between two tables. For example, a user can have many posts, but a post can only have one user.

To create a one-to-many relationship, add the following code to your `app.py` file:

```python
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

class Post(db.Model): # create a new model
    __tablename__ = 'posts' # set the table name

    id = db.Column(db.Integer, primary_key=True, index=True) # set the id column
    title = db.Column(db.String) # set the title column
    content = db.Column(db.String) # set the content column
    user_id = db.Column(db.Integer, ForeignKey('users.id')) # set the user id column

    user = relationship('User', back_populates='posts') # create a relationship with the user model

    def __repr__(self):
        return f'Post {self.title}' # return the post title when printing the post

class User(db.Model): # create a new model
    __tablename__ = 'users' # set the table name

    id = db.Column(db.Integer, primary_key=True, index=True) # set the id column
    name = db.Column(db.String, unique=True, index=True) # set the name column
    email = db.Column(db.String, unique=True, index=True) # set the email column
    password = db.Column(db.String) # set the password column

    posts = relationship('Post', back_populates='user') # create a relationship with the post model

    def __repr__(self):
        return f'User {self.name}' # return the user name when printing the user
```

## bootstrap

Bootstrap is a free and open-source CSS framework directed at responsive, mobile-first front-end web development. It contains CSS- and JavaScript-based design templates for typography, forms, buttons, navigation and other interface components.

Documentation: https://getbootstrap.com/docs/4.5/getting-started/introduction/

### Adding bootstrap to your project

To add bootstrap to your project, add the following code to your `base.html` file:

```html
{% block head %}
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" integrity="sha384-JcKb8q3iqJ61gNV9KGb8thSsNjpSL0n8PARn9HuZOnIxN0hoP+VmmDGMN5t9UJ0Z" crossorigin="anonymous">
{% endblock %}
```

## Testing flask applications

You can test all components of your application, including the database, views, models, and forms.

### Testing the database

To test the database, you can use the `pytest` library. Here is an example of a test that checks if the database has and admin user:

```python
from app import app, db
from app.models import User

def test_database():
    assert User.query.filter_by(name='admin').first() # check if the database has an admin user

def test_admin_password():
    admin = User.query.filter_by(name='admin').first() # get the admin user
    assert admin.check_password('admin') # check if the admin password is correct
```

### Testing the views

When testing the views, there are two approaches:

  -   Testing the view function: This approach tests the view function directly without the need to run the application server.

  -   Testing the view with the test client: This approach tests the view by simulating a client making requests to the application without the need to run the application server.

here is a side-by-side implementation of the two approaches:

```python
from app import app
from app.models import User

def test_index():
    client = app.test_client() # create a test client
    response = client.get('/') # send a get request to the index route
    assert response.status_code == 200 # check that the status code is 200
    assert 'Hello World!' in response.data # check that the response contains the string 'Hello World!'
```
  
  ```python
from app import app
from app.models import User

def test_index():
    with app.test_request_context(): # create a test request context
        response = index() # call the index view function
        assert response.status_code == 200 # check that the status code is 200
        assert 'Hello World!' in response.data # check that the response contains the string 'Hello World!'
```

### Testing the forms

Forms are very important to test because they are the main way to interact with the application. Try to have as much coverage as possible when testing the forms. Here is an example of a test that checks if the login form is valid:

```python
from app import app
from app.forms import LoginForm

def test_login_form():
    client = app.test_client() # create a test client
    response = client.post('/login', data=dict(username='admin', password='admin'), follow_redirects=True) # send a post request to the login route
    assert response.status_code == 200 # check that the status code is 200
    assert 'You are logged in!' in response.data # check that the response contains the string 'You are logged in!'
```
## Writing a package to test your entire application

With pytest, you can create a directory called `tests` and add files that start with `test_` to it. Each file will be a test module. You can also add a `conftest.py` file to the `tests` directory to add fixtures and other test configuration.

Here is an example of a `conftest.py` file:

```python
import pytest
from app import create_app, db
from app.models import User

@pytest.fixture
def app():
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://'
    with app.app_context():
        db.create_all()
        yield app

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def runner(app):
    return app.test_cli_runner()
```

## Deploying flask applications

Flask applications can be deployed in many ways. Here are some of the most common ways:

    -   Deploying with a web server gateway interface (WSGI) server: This is the most common way to deploy flask applications. You can use a WSGI server like gunicorn or uWSGI to deploy your application.
    
    -   Deploying with a container: You can use a container like Docker to deploy your application.
    
    -   Deploying with a cloud provider: You can use a cloud provider like Heroku to deploy your application.

### Deploying with a WSGI server

To deploy your application with a WSGI server, you need to create a `wsgi.py` file in the root directory of your project. Here is an example of a `wsgi.py` file:

```python
from app import create_app

app = create_app()
```

You can then use a WSGI server like gunicorn to run your application:

```bash
gunicorn wsgi:app
```

### Deploying with a container

To deploy your application with a container, you need to create a `Dockerfile` in the root directory of your project. Here is an example of a `Dockerfile`:

```dockerfile
FROM python:3.8

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "wsgi.py"]
```

You can then use the `docker` command to build and run your application:

```bash
docker build -t flask-app .
docker run -d -p 5000:5000 flask-app
```

### using ngrok to test your application

You can use ngrok to test your application locally. ngrok is a tool that creates a secure tunnel from a public endpoint to your local machine. You can then use the public endpoint to test your application.

You can also use ngrok to test your application on a mobile device or send it to a friend to test it.

To use ngrok, you need to download it from the [ngrok website](https://ngrok.com/download). Once you have downloaded it and made a free account, you can run the following command to start ngrok:

```bash
ngrok http 5000
```

## Useful sites and documentation

    -  [Flask documentation](https://flask.palletsprojects.com/en/1.1.x/)
    -  [Bootstrap documentation](https://getbootstrap.com/docs/4.5/getting-started/introduction/)
    -  [Flask_login documentation](https://flask-login.readthedocs.io/en/latest/)
    -  [Flask_sqlalchemy documentation](https://flask-sqlalchemy.palletsprojects.com/en/2.x/)
    -  [Flask_wtf documentation](https://flask-wtf.readthedocs.io/en/stable/)
    -  [Flask_bootstrap documentation](https://pythonhosted.org/Flask-Bootstrap/)
    -  [Pypi](https://pypi.org/)
