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

# Connect MongoDb to Flask (via PyMongo), and the env vars from os
app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

# Connect mongo to communicate with the flask app (instance created above)
mongo = PyMongo(app)


@app.route("/")
@app.route("/get_datasets")
def get_datasets():
    datasets = mongo.db.datasets.find()
    return render_template("datasets.html", datasets=datasets)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        """Check if username already exists in db"""
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()}
        )

        if existing_user:
            """If username exists and was found in db"""
            flash("Username already exists")
            return redirect(url_for("register"))

        register = {
            """If username was not found in db, invite to register"""
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        """Insert new user in db"""
        mongo.db.users.insert_one(register)

        """Put the new user into a session cookie"""
        session["user"] = request.form.get("username").lower()
        flash("Registration Seccessful")
    return render_template("register.html")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)  # update to False prior to submission
