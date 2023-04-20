from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from .models import User, db # I had to import the db object from here rather than creating it in this module.
import os

# this is the database object that we will use to interact with the database
DB_NAME = "PreProd_DB.db"
SECRET_KEY = 'abcd1234'

def make_app():
    # Initialize the app
    app = Flask(__name__)

    # Configure the app
    app.config['SECRET_KEY'] = SECRET_KEY
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    


    '''  This is what I had to change to get this to work. '''

    db.init_app(app)
    db.create_all(app=app)
    db.app = app

    '''I had to create the db object in the models module and then pass the app context to the db object in this module.'''

    # import the views and models
    from .views import views
    
    # register the blueprints
    app.register_blueprint(views, url_prefix='/')
    


    # add the admin user to the database
    admin = User.query.filter_by( admin = True ).first()
    if admin is None:
        admin = User(name = 'Admin', email = 'admin@mysite.com', password = 'admin1234', admin = True)
        db.session.add(admin)
        db.session.commit()


    # Initialize the login manager
    login_manager = LoginManager() # this is used to manage the user sessions
    login_manager.init_app(app) # what this does is that it creates a session for the user when they login.
    login_manager.login_view = 'views.login' # this is the name of the function that handles the login page

    @login_manager.user_loader # this is a decorator that is used to load the user
    def load_user(id): 
        return User.query.get(int(id)) # This query gets the user from the database
    

    return app

