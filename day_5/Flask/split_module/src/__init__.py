from flask import Flask
from .models import db, User
from .veiws import views
from flask_login import LoginManager

def main():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = 'asdf1234'
    
    db.init_app(app)
    
    login_manager = LoginManager()
    login_manager.init_app(app)
    
    app.register_blueprint(views)
    
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)
    
    return app