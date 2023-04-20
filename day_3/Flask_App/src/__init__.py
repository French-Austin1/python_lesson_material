import os
from flask import Flask, render_template, request, make_response, session, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.declarative import declarative_base

def main():

    # set the app
    app = Flask(__name__)

    # set the database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db' # relative path
    db = SQLAlchemy(app) # create the database object

    from .data_classes import User, base
    base.metadata.create_all(db.engine) # create the tables

    
    # set the secret key
    SECRET_KEY = '1234567890'
    app.config['SECRET_KEY'] = SECRET_KEY # set the secret key for the session

    people = ["tony", "john", "frank"]

    @app.route('/', methods=['GET']) # set the route for the home page
    @app.route('/home', methods=['GET']) # you can set multiple routes for the same function
    def home():
        if 'name' in request.cookies: # check if the cookie exists
            name = request.cookies['name'] 
            return render_template('home.html', name=name)
        return render_template('home.html', people=people)
    
    
    @app.route('/set-cookie', methods=['GET', 'POST'])
    def set_cookie():
        if request.method == 'POST': # check if the request is a POST request (form submission)
            name = request.form['name']
            response = make_response(render_template('home.html', name=name)) 
            response.set_cookie('name', name)   
            return response
        return render_template('login.html')
    
    @app.route('/session', methods=['GET'])
    def session_page():
        if 'name' in session: # check if the session exists
            name = session['name']
            return render_template('home.html', name=name)
        else:
            # create a session
            session['name'] = 'Tony'
            return redirect(url_for('session_page'))
    
    return app # return the app so that it can be run in the main.py file
