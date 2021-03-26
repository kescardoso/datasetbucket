import os

from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for
    )
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

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


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)  # update to False prior to submission
