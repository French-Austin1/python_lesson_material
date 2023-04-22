from flask import Flask, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "asdf1234"

db = SQLAlchemy(app)

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    password_hash = db.Column(db.String(120), unique=True)

    def __repr__(self):
        return '<User %r>' % self.username
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

@app.route('/')
@app.route('/home')
def home():
    if current_user.is_authenticated:
        return render_template('home.html', username=current_user.username)
    else:
        return render_template('home.html')
    
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # get the username and password from the form
        username = request.form['username']
        password = request.form['password']
        
        # get the user from the database
        user = User.query.filter_by(username=username).first()
        
        # check if the user exists and the password is correct
        if user and user.check_password(password):
            # log the user in
            login_user(user)
            return redirect(url_for('home'))
        else:
            # tell the user the login failed
            return render_template('login.html', error='Invalid username or password')
    else:
        return render_template('login.html')
    
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # get the username and password from the form
        username = request.form['username']
        password = request.form['password']
        
        # check if the username is already taken
        if User.query.filter_by(username=username).first():
            return render_template('register.html', error='Username already taken')
        else:
            # create a new user
            user = User(username=username)
            user.set_password(password)
            
            # add the user to the database
            db.session.add(user)
            db.session.commit()
            
            # log the user in
            login_user(user)
            return redirect(url_for('home'))
    else:
        return render_template('register.html')
    
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
