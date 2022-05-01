from flask import Blueprint, render_template, request, flash
from flask_login import current_user

hello = Blueprint('hello', __name__)
hello.secret_key = "dkanrjsk dlqfurgka"

@hello.route("/hello")
def index():
    flash("What is you name?")
    return render_template("hello.html", user=current_user)

@hello.route("/greet", methods=["POST","GET"])
def greet():
    flash("Hi " + str(request.form['name_input']) + ", great to see you!")
    return render_template("hello.html", user=current_user)

