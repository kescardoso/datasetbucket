import os
import re

from flask import Flask, flash, render_template, redirect, request, session, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash

if os.path.exists("env.py"):
    import env


# Create an instance of Flask (Flask app)
app = Flask(__name__)

# Connect Mongo to Flask (via PyMongo), and the secret key from env.py
app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

# Connect Mongo to the Flask app (instance created above)
mongo = PyMongo(app)


# Home : main list of datasets
@app.route("/")
@app.route("/all_datasets")
def all_datasets():
    datasets = list(mongo.db.datasets.find())
    return render_template("datasets.html", datasets=datasets)


# New User Registration
@app.route("/register", methods=["GET", "POST"])
def register():
    """ Check if username already exists in db """
    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()}
        )

        """ If username was found in db, register and insert user to db """
        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        """ Put the new registered user into a session cookie
        and redirect user to profile page """
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful")
        return redirect(url_for("profile", username=session["user"]))

    return render_template("register.html")


# User Login 
@app.route("/login", methods=["GET", "POST"])
def login():
    """ Check if username already exists in db """
    if request.method == "POST":
        existing_user = mongo.db.users.find_one({"username": request.form.get("username").lower()})

        """ If username was found in db: 
        ensure hashed password matches user input """
        if existing_user:
            if check_password_hash(existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome, {}".format(request.form.get("username")))
                return redirect(url_for("profile", username=session["user"]))
            else:
                """ Invalid password match """
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))
        else:
            """ If username does not exist, warn user """
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


# User Profile
@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    """ Grab the session user's username from db (ignore the password) """
    username = mongo.db.users.find_one({"username": session["user"]})["username"]

    """ Confirm true user session cookie """
    if session["user"]:
        return render_template("profile.html", username=username)

    return redirect(url_for("login"))


# User Logout
@app.route("/logout")
def logout():
    """ Remove user from session cookies """
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


# Add new dataset
@app.route("/add_dataset", methods=["GET", "POST"])
def add_dataset():
    """ Insert new informatiom from the form into the db """
    if request.method == "POST":
        is_todo = "On" if request.form.get("is_todo") else "Off"
        dataset = {
            "category_name": request.form.get("category_name"),
            "dataset_name": request.form.get("dataset_name"),
            "dataset_description": request.form.get("dataset_description"),
            "is_todo": is_todo,
            "last_update": request.form.get("last_update"),
            "created_by": session["user"]
        }
        mongo.db.datasets.insert_one(dataset)
        flash("New Dataset Successfully Added")
        return redirect(url_for("all_datasets"))

    """ Wire up the db to dynamically generate the category collection """
    categories = mongo.db.categories.find().sort("category_name")
    return render_template("add.html", categories=categories)


# Edit Dataset (edit and/or delete information from the db)
@app.route("/edit_dataset<dataset_id>", methods=["GET", "POST"])
def edit_dataset(dataset_id):
    if request.method == "POST":
        is_todo = "On" if request.form.get("is_todo") else "Off"
        save_edit = {
            "category_name": request.form.get("category_name"),
            "dataset_name": request.form.get("dataset_name"),
            "dataset_description": request.form.get("dataset_description"),
            "is_todo": is_todo,
            "last_update": request.form.get("last_update"),
            "created_by": session["user"]
        }
        mongo.db.datasets.update({"_id": ObjectId(dataset_id)}, save_edit)
        flash("Dataset Successfully Updated")

    """ Retrieve a dataset by its id, and convert it to a bson data type """
    dataset = mongo.db.datasets.find_one({"_id": ObjectId(dataset_id)})
    categories = mongo.db.categories.find().sort("category_name")
    return render_template("edit.html", dataset=dataset, categories=categories)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)  # update to False prior to submission
