# datasetbucket

This is a python-flask application build upon a data-base CRUD system (Create, Read, Update and Delete) 
with the purpose of store and display information about dataset structures based on Machine Learning models.

You will be able to find and read reports from a wiki styled list of information 
about data containing population and demographic subjects.

[Click here to view the deployed app on Heroku](https://datasetbucket.herokuapp.com/)

## Project Installation and Local Deployment

### Installation

1. Install [python3 and pip3](https://www.python.org) in your machine
    
2. Download or clone [the datasetbucket project folders](https://github.com/kescardoso/datasetbucket) into your local workspace

3. Create a virtual environment: `Python3 -m venv venv`

    After running this command, the folders will be automatically set up on your workspace.

4. Run: `source venv/bin/activate`

5. Install Flask: `pip3 install flask`

### Local Deployment

1. Create an `env.py` file to keep your sensitive data secret

2. Open `env.py` and enter the following:

    `import os`

    `os.environ.setdefault("SECRET_KEY", "secret_key_here")`

    `os.environ.setdefault("MONGO_URI", "value_from mongoDB_here")`

    `os.environ.setdefault("MONGO_DBNAME", "value_from mongoDB_here")`

3. Wire up MongoDB and its functionalities with Flask, by installing `flask-pymongo` and `dnspython`

    `pip3 install flask-pymongo`

    `pip3 install dnspython`

4. Run the `app.py` in debug mode as a flask application to see the project in your local deployed http address.

## Technologies used

- [Python](https://www.python.org/) - an interpreted, high-level and general-purpose programming language, great for data base structured projects
- [Pip](https://pypi.org/project/pip/) - a package manager for Python, that allows developers to install and manage additional libraries and dependencies that are not distributed as part of the standard library.
- [Flask](https://flask.palletsprojects.com/) - a Python framework that depends on the Jinja template engine and the Werkzeug WSGI toolkit
- [MongoDB](https://www.mongodb.com/) - a document database (stores data in JSON-like documents) with a horizontal, scale-out architecture that can support huge volumes of both data and traffic.
- [Materialize](https://materializecss.com/) - a modern front-end framework (responsive and mobile-first, similar to Bootstrap) that helps developers build a stylish and responsive application.
- [Git](https://git-scm.com/) - a version control system for for source code management; it allows tracking file changes and coordinating work on those files among multiple people and machines.
- [GitHub](https://github.com/) - a open-source code hosting platform for version control and collaboration. It lets developers work remotely and together on projects from anywhere.