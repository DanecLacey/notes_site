from flask import Blueprint, render_template

#How you set up roots and URLs is the most basic part of Flask

auth = Blueprint('auth', __name__) #just name same as file

@auth.route('/login')
def login():
    return render_template("login.html", text = "Testing", user = "fart")

@auth.route('/logout')
def logout():
    return "<p>Logout</p>"

@auth.route('/sign-up')
def sign_up():
    return render_template("sign_up.html")
