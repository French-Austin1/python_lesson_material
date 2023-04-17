<style> .markdown-body { font-size: 1em; } .markdown-body h1 { color: #409f42; } .markdown-body h2 { color: #409f42; } .markdown-body h3 { text-decoration: underline; } .markdown-body p { color: #909090 } </style>

# Python Day 3

Todays lesson will be covering the following topics:

- Flask Basics
- SQLAlchemy Basics
- ORM
- Flask-SQLAlchemy
- Jinja Templating
- html basics


## Venv

Venv is a tool to create isolated Python environments. The basic problem being addressed is one of dependencies and versions, and indirectly permissions.

you can create a virtual environment by running the following command:

```bash
python3 -m venv venv
```

## Flask Basics

Flask is a micro web framework written in Python. It is classified as a microframework because it does not require particular tools or libraries. It has no database abstraction layer, form validation, or any other components where pre-existing third-party libraries provide common functions.

There are lots of plugins for flask that add functionality to the framework. Some of the most popular plugins are:

- Flask-SQLAlchemy
- Flask-Login
- Flask-WTF
- Flask-Bootstrap

### Installation

To install flask, run the following command in your terminal:

```bash
pip install flask
```

### Hello World

To create a flask application, create a new file called `app.py` and add the following code:

```python
from flask import Flask

app = Flask(__name__) # create a new flask app, __name__ is the name of the current python module

@app.route('/') # this is a decorator, it tells flask what URL should trigger the function below
def hello_world(): 
    return 'Hello, World!' 
```

To run the application, run the following command in your terminal:

```bash
python app.py
```

You should see the following output:

```bash
 * Serving Flask app "app" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://
```

Copy the url that is displayed in your terminal and paste it into your browser. You should see the following output:

```bash
Hello, World!
```

### Templates

Flask uses templates to render html. To create a template, create a new folder called `templates` and add a new file called `index.html`. Add the following code to the file:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>Hello, World!</h1>
</body>
</html>
```

To render the template, add the following code to your `app.py` file:

```python
from flask import Flask, render_template

app = Flask(__name__) # create a new flask app, __name__ is the name of the current python module

@app.route('/')
def index():
    return render_template('index.html')
```

Run the application the same way as before.

### Static Files

Flask uses the `static` folder to serve static files. Static files are files that do not change. To create a static folder, create a new folder called `static` and add a new file called `style.css`. Add the following code to the file:

```css
body {
    background-color: #409f42;
}
```

To link the css file to your html file, add the following code to your `index.html` file:

```html
<link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
```

Run the application the same way as before.

### Forms

Flask uses the `request` object to access form data. To create a form, add the following code to your `index.html` file:

```html
<form action="/" method="POST">
    <input type="text" name="name">
    <input type="submit" value="Submit">
</form>

<h1>Hello, {{ name }}!</h1>
```

To access the form data, add the following code to your `app.py` file:

```python
from flask import Flask, render_template, request

app = Flask(__name__) # create a new flask app, __name__ is the name of the current python module

@app.route('/', methods=['GET', 'POST']) # add the methods parameter to the route decorator
def index():
    if request.method == 'POST':
        name = request.form['name']
        return render_template('index.html', name=name)
    return render_template('index.html')
```

Run the application the same way as before.

### Cookies and Sessions

Cookies are small files that are stored on the client side. They are used to store information about the user. Sessions are used to store information about the user on the server side. Flask uses the `session` object to access session data.

To create a cookie, add the following code to your `app.py` file:

```python
from flask import Flask, render_template, request, make_response

app = Flask(__name__) # create a new flask app


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        response = make_response(render_template('index.html', name=name))
        response.set_cookie('name', name)
        return response
    return render_template('index.html')
```

To access the cookie, add the following code to your `index.html` file:

```html
<h1>Hello, {{ name }}!</h1>
```



## SQLAlchemy Basics

SQLAlchemy is the Python SQL toolkit and Object Relational Mapper. It is used to create and manage relational databases. When using SQLAlchemy with Flask, it is recommended to use Flask-SQLAlchemy.

SQLAlchemy supports many different databases. The most popular databases are:

- SQLite
- MySQL
- PostgreSQL
- Oracle
- Microsoft SQL Server



### Installation

To install Flask-SQLAlchemy, run the following command in your terminal:

```bash
pip install flask-sqlalchemy
```

### Basic Usage

To create a database, create a new file called `database.py` and add the following code:

```python
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = 'sqlite:///./sql_app.db' # create a database file called sql_app.db

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False} # connect_args is used to prevent an error when using sqlite
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine) # create a session object

Base = declarative_base() # create a base class for the models
```

To create a model, create a new file called `models.py` and add the following code:

```python
from sqlalchemy import Column, Integer, String

from .database import Base

class User(Base):
    __tablename__ = 'users' # set the table name

    id = Column(Integer, primary_key=True, index=True) # set the id column, primary_key=True means that the id column is the primary key, index=True means that the id column is indexed
    name = Column(String, unique=True, index=True) # set the name column, unique=True means that the name column is unique so there can't be two users with the same name.
    email = Column(String, unique=True, index=True) # set the email column
    password = Column(String) # set the password column
```

To create a database, add the following code to your `database.py` file:

```python
Base.metadata.create_all(bind=engine) # create the database
```

To create a user, add the following code to your `database.py` file:

```python
from .models import User

def get_db():
    db = SessionLocal() # create a new session
    try:
        yield db # yield the session
    finally:
        db.close() # close the session

def create_user(db: Session, name: str, email: str, password: str):
    db_user = User(name=name, email=email, password=password) # create a new user
    db.add(db_user) # add the user to the session
    db.commit() # commit the changes to the database
    db.refresh(db_user) # refresh the user
    return db_user # return the user
```

To get a user, add the following code to your `database.py` file:

```python

def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first() # get the user with the specified id
```

To run the code, create a new file called `main.py` and add the following code:

```python
from sqlalchemy.orm import Session

from .database import engine, get_db
from .models import User

def main():
    Base.metadata.create_all(bind=engine) # create the database

    db = next(get_db()) # create a new session

    user = create_user(db, name='John Doe', email='John.Doe@mysite.com', password='password') # create a new user
    print(user.id) # print the user id
    print(user.name) # print the user name
    print(user.email) # print the user email
    print(user.password) # print the user password

    user = get_user(db, user_id=1) # get the user with the id 1
    print(user.id) # print the user id
    print(user.name) # print the user name
    print(user.email) # print the user email
    print(user.password) # print the user password

if __name__ == '__main__':
    main()
```

 Flask-Sqlalchemy is a wrapper for SQLAlchemy. It is used to simplify the usage of SQLAlchemy with Flask.

 Some of the most useful features of Flask-SQLAlchemy are:

  -   It is configured using the `SQLALCHEMY_DATABASE_URI` configuration key. The value of this key should be a string that represents the database URI. For example, `sqlite:///./sql_app.db` is the URI for a SQLite database called `sql_app.db` that is stored in the current directory.

  -   It automatically creates a database session that is available inside view functions. The session is available using the `current_session` object.

  -   It provides a `Model` class that is a declarative base which can be used to declare models.

  -   It provides a `Query` class that is a subclass of `sqlalchemy.orm.Query` and adds some convenience methods to it.

  -   It provides a `SQLAlchemy` class that is a subclass of `sqlalchemy.orm.Session` and adds some convenience methods to it.


## jinja2

Jinja2 is a modern and designer-friendly templating language for Python. It is fast, widely used, and secure with the optional sandboxed template execution environment.

### Jinja2 Basics

To use Jinja2 templates in your html files, you will want to create a base template that will be extended by other templates. To create a base template, create a new file called `base.html` in the `templates` folder and add the following code:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}{% endblock %}</title>
</head>
<body>
    {% block content %}{% endblock %}
</body>
</html>
```

jinja2 uses the `{% %}` syntax to execute python code. The `block` tag is used to define a block that can be extended by other templates. The `title` block is used to set the title of the page and the `content` block is used to set the content of the page.

To extend the base template, create a new file called `index.html` in the `templates` folder and add the following code:

```html
{% extends 'base.html' %}

{% block title %}Home{% endblock %}

{% block content %}
    <h1>Home</h1>
{% endblock %}
```

The `extends` tag is used to extend the base template. The `title` block is used to set the title of the page and the `content` block is used to set the content of the page.

### Jinja2 Variables

To use variables in your templates, you will need to pass the variables to the template when rendering it. To pass variables to the template, add the following code to your `app.py` file:

```python
@app.route('/')
def index():
    name = 'John Doe'
    return render_template('index.html', name=name) # pass the name variable to the template
```

To use the variable in the template, add the following code to your `index.html` file:

```html
{% extends 'base.html' %}

{% block title %}Home{% endblock %}

{% block content %}
    <h1>Home</h1>
    <p>Hello {{ name }}!</p>
{% endblock %}
```

### Jinja2 Loops

To use loops in your templates, you will need to pass the variables to the template when rendering it. To pass variables to the template, add the following code to your `app.py` file:

```python
@app.route('/')
def index():
    names = ['John Doe', 'Jane Doe', 'Joe Doe']
    return render_template('index.html', names=names) # pass the names variable to the template
```

To use the variable in the template, add the following code to your `index.html` file:

```html
{% extends 'base.html' %}

{% block title %}Home{% endblock %}

{% block content %}
    <h1>Home</h1>
    {% for name in names %}
        <p>Hello {{ name }}!</p>
    {% endfor %}
{% endblock %}
```

### Jinja2 Conditionals

To use conditionals in your templates, you will need to pass the variables to the template when rendering it. To pass variables to the template, add the following code to your `app.py` file:

```python
@app.route('/')
def index():
    name = 'John Doe'
    return render_template('index.html', name=name) # pass the name variable to the template
```

To use the variable in the template, add the following code to your `index.html` file:

```html
{% extends 'base.html' %}

{% block title %}Home{% endblock %}

{% block content %}
    <h1>Home</h1>
    {% if name %}
        <p>Hello {{ name }}!</p>
    {% else %}
        <p>Hello World!</p>
    {% endif %}
{% endblock %}
```