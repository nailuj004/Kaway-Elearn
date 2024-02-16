from flask import Blueprint

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return "<p>logout</>"

@auth.route('/sign-up')
def sign_up():
    return "<p>Sign Up</>"