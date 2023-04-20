from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy

# The main thing I had to change to get this to work. I had to create the db object in this module and then import it into the views module.
# I had to do this because if the db object is created in __init__.py, then the db object is created before the app object is created.
# This caused the app object to be None when the db object was created so creating the db object in __init__.py caused an error.
db = SQLAlchemy()


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True, unique=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)
    admin = db.Column(db.Boolean, nullable=False, default=False)

    def __repr__(self):
        return f"{self.name}"
    
    def check_password(self, password):
        return self.password == password
    
    def get_id(self):
        return self.id
    
    def is_admin(self):
        return self.admin




