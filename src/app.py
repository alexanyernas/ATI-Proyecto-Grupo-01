#!/usr/bin/env python
import flask 

app = flask.Flask(__name__)

@app.route('/')
def home_controller():
    return flask.render_template('home/homePage.html')

@app.route('/auth/login')
def login_controller():
    return flask.render_template('auth/loginPage.html')

@app.route('/auth/register')
def register_controller():
    return flask.render_template('auth/registerPage.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0')     # open for everyone