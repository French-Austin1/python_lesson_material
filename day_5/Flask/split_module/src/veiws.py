from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user, login_user, logout_user
from .models import db, User

views = Blueprint('views', __name__)

@views.route('/')
@views.route('/home')
def home():
    if current_user.is_authenticated:
        return render_template('home.html', username=current_user.username)
    else:
        return render_template('home.html')
    
@views.route('/login', methods=['GET', 'POST'])
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
            return redirect(url_for('views.home'))
        else:
            # tell the user the login failed
            return render_template('login.html', error='Invalid username or password')
    else:
        return render_template('login.html')
    
@views.route('/register', methods=['GET', 'POST'])
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
            return redirect(url_for('views.home'))
    else:
        return render_template('register.html')
    
@views.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('views.home'))