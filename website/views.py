from flask import Blueprint, render_template

views = Blueprint('views', __name__) #just name same as file

@views.route('/')
def home():
    return render_template("home.html")
    
