import os
import re

from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for
    )
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash

if os.path.exists("env.py"):
    import env


# Create an instance of Flask (Flask app)
app = Flask(__name__)

# Connect MongoDb to Flask (via PyMongo), and the secret key from env vars (env.py)
app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

# Connect Mongo to the Flask app (instance created above)
mongo = PyMongo(app)


# Home Page : displays the wiki list of datasets
@app.route("/")
@app.route("/get_datasets")
def get_datasets():
    datasets = mongo.db.datasets.find()
    return render_template("datasets.html", datasets=datasets)


# Registration Page : displays user registration form
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        """ Check if username already exists in db """
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()}
        )

        if existing_user:
            """ If username was found in db, register and insert user to db """
            flash("Username already exists")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        """ Put the new registered user into a session cookie """
        session["user"] = request.form.get("username").lower()
        flash("Registration Seccessful")
    return render_template("register.html")


# Login Page : displays user login form 
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        """ Check if username already exists in db """
        existing_user = mongo.db.users.find_one({"username": request.form.get("username").lower()})
    
        if existing_user:
            """ If username was found in db: ensure hashed password matches user input """
            if check_password_hash(existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome, {}".format(request.form.get("username")))
            else:
                """ invalid password match """
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            """ If username does not exist, warn user """
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))
    return render_template("login.html")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)  # update to False prior to submission
