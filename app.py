import os
import re
import time
from flask import Flask, flash, render_template, redirect, request, session, url_for, send_file
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash

from runTerminalCommands import startCommands # only importing this function prevents the whole .py file from executing on startup

if os.path.exists("env.py"):
    import env


# Create an instance of Flask (the Flask app)
app = Flask(__name__)

# Connect Mongo to Flask (via PyMongo) and config vars from env.py
app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

# Connect MongoDB to the Flask app (instance created above)
mongo = PyMongo(app)


# Home : Show All Datasets
@app.route("/")
@app.route("/all_datasets")
def all_datasets():
    datasets = list(mongo.db.datasets.find())
    categories = list(mongo.db.categories.find())
    locations = list(mongo.db.locations.find())
    return render_template("datasets.html", 
                            datasets=datasets, 
                            categories=categories,
                            locations=locations)


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


# Analyse dataset from Kaggle
@app.route("/analyse_data", methods=["GET", "POST"])
def analyse_data():
    if request.method == "POST":
        fileString = request.form.get("file_name")
        # StartCommands is the function in runTerminalCommands.py 
        # that starts the download/running/analysis of the dataset
        if fileString is not None:
            split_filename = fileString.split('.com/')
            fileString = split_filename[1]
            reportMade = startCommands(fileString) # startCommands is the function in runTerminalCommands.py that starts the download/running/analysis of the dataset
            if reportMade:
                time.sleep(3)
                try:
                    return send_file("./reportdir/report.pdf", as_attachment=True) # downloads to user's downloads computer 
                except:
                    return render_template("analyse.html", dataToRender="Unable able to send report")
            else:
                return render_template("analyse.html", dataToRender="Demographic data not found, unable to generate report")

    return render_template("analyse.html")



# Add New Dataset
@app.route("/add_dataset", methods=["GET", "POST"])
def add_dataset():
    """ Insert new informatiom from the form into the db """
    if request.method == "POST":
        is_todo = "On" if request.form.get("is_todo") else "Off"
        dataset = {
            "category_name": str(request.form.getlist("category_name")),
            "location_name": request.form.getlist("location_name"),
            "dataset_name": request.form.get("dataset_name"),
            "dataset_description": request.form.get("dataset_description"),
            "is_todo": is_todo,
            "last_update": request.form.get("last_update"),
            "created_by": session["user"]
        }
        mongo.db.datasets.insert_one(dataset)
        flash("New Dataset Successfully Added")
        return redirect(url_for("all_datasets"))

    """ Wire up the db to dynamically generate the category and location collection """
    categories = mongo.db.categories.find().sort("category_name")
    locations = mongo.db.locations.find().sort("location_name")
    return render_template("add_dataset.html", 
                            categories=categories, 
                            locations=locations)


# Edit Dataset
@app.route("/edit_dataset<dataset_id>", methods=["GET", "POST"])
def edit_dataset(dataset_id):
    if request.method == "POST":
        is_todo = "On" if request.form.get("is_todo") else "Off"
        category_select = "category_name" if category_name is string else "category"
        save_edit = {
            "category_select": request.form.getlist("category_select"),
            "location_name": request.form.get("location_name"),
            "dataset_name": request.form.get("dataset_name"),
            "dataset_description": request.form.get("dataset_description"),
            "dataset_report": request.form.get("dataset_report"),
            "is_todo": is_todo,
            "last_update": request.form.get("last_update"),
            "created_by": session["user"]
        }
        mongo.db.datasets.update({"_id": ObjectId(dataset_id)}, save_edit)
        flash("Dataset Successfully Updated")

    """ Retrieve a dataset by its id, and convert it to a bson data type """
    dataset = mongo.db.datasets.find_one({"_id": ObjectId(dataset_id)})
    categories = mongo.db.categories.find().sort("category_select")
    locations = mongo.db.locations.find().sort("location_name")

    return render_template("edit_dataset.html", 
                            dataset=dataset, 
                            categories=categories,
                            locations=locations)


# Delete Dataset
@app.route("/delete_dataset/<dataset_id>")
def delete_dataset(dataset_id):
    mongo.db.datasets.remove({"_id": ObjectId(dataset_id)})
    flash("Dataset Successfully Deleted")
    return redirect(url_for("all_datasets"))


# Show All Categories
@app.route("/all_categories")
def all_categories():
    categories = list(mongo.db.categories.find().sort("category_name"))
    return render_template("categories.html", categories=categories)


# Add Category
@app.route("/add_category", methods=["GET", "POST"])
def add_category():
    if request.method == "POST":
        category ={
            "category_name": request.form.get("category_name"),
            "created_by": session["user"]
        }
        mongo.db.categories.insert_one(category)
        flash("New Category Added")
        return redirect(url_for("all_categories"))

    return render_template("add_category.html")


# Edit Category
@app.route("/edit_category/<category_id>", methods=["GET", "POST"])
def edit_category(category_id):
    if request.method == "POST":
        save_edit = {
            "category_name": request.form.get("category_name")
        }
        mongo.db.categories.update({"_id": ObjectId(category_id)}, save_edit)
        flash("Category Successfully Updated")
        return redirect(url_for("all_categories"))

    category = mongo.db.categories.find_one({"_id": ObjectId(category_id)})
    return render_template("edit_category.html", category=category)


# Delete Category
@app.route("/delete_category/<category_id>")
def delete_category(category_id):
    mongo.db.categories.remove({"_id": ObjectId(category_id)})
    flash("Category Successfully Deleted")
    return redirect(url_for("all_categories"))


# Show Datasets by Categories
@app.route('/datasets_in/<category>')
def datasets_in(category):
    """ Query datasets by each category """
    return render_template('by_category.html', category=category,
                           datasets=mongo.db.datasets.find({'category_name': category}).sort('dataset_name'))


# Show All Locations
@app.route("/all_locations")
def all_locations():
    locations = list(mongo.db.locations.find().sort("location_name"))
    return render_template("locations.html", locations=locations)


# Add Location
@app.route("/add_location", methods=["GET", "POST"])
def add_location():
    if request.method == "POST":
        location ={
            "location_name": request.form.get("location_name"),
            "created_by": session["user"]
        }
        mongo.db.locations.insert_one(location)
        flash("New Location Added")
        return redirect(url_for("all_locations"))

    return render_template("add_location.html")


# Edit Location
@app.route("/edit_location/<location_id>", methods=["GET", "POST"])
def edit_location(location_id):
    if request.method == "POST":
        save_edit = {
            "location_name": request.form.get("location_name")
        }
        mongo.db.locations.update({"_id": ObjectId(location_id)}, save_edit)
        flash("Location Successfully Updated")
        return redirect(url_for("all_locations"))

    location = mongo.db.locations.find_one({"_id": ObjectId(location_id)})
    return render_template("edit_location.html", location=location)


# Delete Location
@app.route("/delete_location/<location_id>")
def delete_location(location_id):
    mongo.db.locations.remove({"_id": ObjectId(location_id)})
    flash("LOcation Successfully Deleted")
    return redirect(url_for("all_locations"))


# Show Datasets by Locations
@app.route('/datasets_at/<location>')
def datasets_at(location):
    """ Query datasets by each location """
    return render_template('by_location.html', location=location,
                           datasets=mongo.db.datasets.find({'location_name': location}).sort('dataset_name'))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)  # set to False prior to submission
