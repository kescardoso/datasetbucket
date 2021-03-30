# datasetbucket

This is a python-flask application build upon a CRUD system (Create, Read, Update and Delete) 
with the purpose of store and display information about dataset structures based on Machine Learning models.

You will be able to find and read reports from a wiki styled list of information 
about data containing population and demographic subjects.

### Check the deployed version on Heroku: https://datasetbucket.herokuapp.com/

## Installation and Local Deployment via VSCode

### Installation

1. Install python3 and pip3 in your machine

    https://www.python.org

2. Open a new VSCode workspace and install the Python extension

    https://marketplace.visualstudio.com/items?itemName=ms-python.python

4. Create a virtual environment

    On the vscode terminal:

    `Python3 -m venv venv`

    After running the command, the folders will be automatically set up on your workspace

    And then run:

    `source venv/bin/activate`

    And only now accept or install pylint


5. Install Flask

    On the vscode terminal:

    ` pip3 install flask `
    
    Write a "Hello Flask" to see if Flask is working

    Click on Run and Debug and choose to run as Flask

    watch the command line for the local web server address to appear

    Click on it, and a new window will open with your Hello Flask

### Local Deployment

Before you commit your changes to Github for the first time, download datasetbucket project folders to your environment and follow the instructions bellow.

1. If you can't locate these folders in your workspace, make sure you create an env.py and .gitignore files to keep your sensitive data secret

    On the vscode terminal:

    `touch env.py`

    `touch .gitignore`

    Open the .gitignore and insert:

    `env.py`

    `__pycache__`

    Save and close .gitignore

2. Open env.py and enter the following:

    `import os`

    `os.environ.setdefault("IP", "0.0.0.0")`

    `os.environ.setdefault("PORT", "5000")`

    `os.environ.setdefault("SECRET_KEY", "secret_key_here")`

    `os.environ.setdefault("MONGO_URI", "value_from mongoDB_here")`

    `os.environ.setdefault("MONGO_DBNAME", "value_from mongoDB_here")`

## Technologies used

- Python - an interpreted, high-level and general-purpose programming language, great for data base structured projects
- Pip - a package manager for Python, that allows developers to install and manage additional libraries and dependencies that are not distributed as part of the standard library.
- Flask - a Python framework that depends on the Jinja template engine and the Werkzeug WSGI toolkit
- MongoDB - a document database (stores data in JSON-like documents) with a horizontal, scale-out architecture that can support huge volumes of both data and traffic.
- [Materialize](https://materializecss.com/) - a modern front-end framework (responsive and mobile-first, similar to Bootstrap) that helps developers build a stylish and responsive application.
- Git - a version control system for for source code management; it allows tracking file changes and coordinating work on those files among multiple people and machines.
- GitHub - a code hosting platform for version control and collaboration. It lets developers work remotely and together on projects from anywhere.