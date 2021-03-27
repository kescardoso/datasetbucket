# datasetbucket

This is a python-flask application build upon a CRUD system (Create, Read, Update and Delete) 
with the purpose of store and display information about dataset structures based on Machine Learning models.

You will be able to find and read reports from a wiki styled list of information 
about data containing population and demographic subjects.

### Check the deployed version on Heroku: https://datasetbucket.herokuapp.com/

## Python and Flask installation via VSCode

### Prior to install this project in your local environment, follow these steps to make sure all the requirements are in place and working

1. Install python in your machine

    https://www.python.org

    If on a Mac, you can use home-brew with 

    `brew install python3`

    This command will install python3 and pip3

2. Open a new VSCode workspace (as you usually do) and install the Python extension

    https://marketplace.visualstudio.com/items?itemName=ms-python.python

3. Test a “Hello Python” print statement to see if python is working

    create file: hello.py

    and enter this:

    `msg = “Hello World!`

    `print(msg)`

    Check the terminal for the print.

4. Create a virtual environment

    On the terminal:

    `Python3 -m venv venv`

    The folders will be automatically set up on your workspace

5. Accept vscode tip to use this folder as your workspace

6. Before installing Linter pylint

    On the terminal:

    ` source venv/bin/activate `

    And the accept or install pylint

7. Install Flask

    On the terminal:

    ` pip3 install flask `

8. Test a "Hello Flask" to see if Flask is working

    https://flask.palletsprojects.com/en/1.1.x/quickstart/

    create file: app.py

    enter this:

    `from flask import Flask`

    `app = Flask(__name__)`


    `@app.route(‘/‘)`

    `def hello_world():`

    `    return 'Hello, World!’`

    Check the Hello Flask by going to Play Debug menu on VSCode

    Click on Run and Debug

    and choose to run as Flask

    watch the command line for the local web server address to appear

    Click on it, and a new window will open with your Hello Flask

## Local Deployment via VSCode
### Download the project folders to your local environment and before you commit your changes to Github for the first time, follow these steps:

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

    This information will help create the integration between mongoBD and python-flask and redirect debug to your main terminal via the command `python3 app.py` (this will give you a port at 5000 to open a new window and run the app on your browser). 
    
    You can still use vscode debug functionality to run the port, by opening the app.py file, going to the debug menu, click on degug and run, and then chose Flask to run your aplication from the dropdown.
    
    If you use `python3 app.py` and open the 5000 port from the command line, and further you need to stop the port to commit changes or use your terminal, in the vscode terminal window type `ctrl+c` to stop running the server and commit your changes.

## Heroku Deployment

1. Fulfil all Heroku requirements by freezing your dependencies and creating a Procfile:

    On the terminal (vscode):

    `pip3 freeze > requirements.txt`

    `echo web: python app.py > Procfile`

    Commit and push your changes.

2. Open your Heroku Dashboard and create a new app. Name your app and choose your region.

3. Connect your heroku app to your git repository, by going to:

    - "Deploy" Menu > "Deployment method" > Click: "Connect to GitHub"

    - "Connect to GitHub" > search your repo from the dropdown, and connect

    - Choose a branch to deploy your changes

4. Add your Config Vars to Heroku.

    Navigate to the settings menu, and then to Config Vars session, and enter here the sensitive information from your env.py file.

5. Connect your GitHub Repo

## Connect MongoDB with Flask via flask-pymongo

Flask-PyMongo is a 3rd-party library that helps connect the MongoDB database and the datasetbucket application by using a database url. On the vscode terminal, install:

1. `pip3 install flask-pymongo`

2. `pip3 install dnspython`

3. `pip3 freeze > requirements.txt`


## Technologies used

- Python - an interpreted, high-level and general-purpose programming language, great for data base structured projects
- Pip - a package manager for Python, that allows developers to install and manage additional libraries and dependencies that are not distributed as part of the standard library.
- Flask - a Python framework that depends on the Jinja template engine and the Werkzeug WSGI toolkit
- MongoDB - a document database (stores data in JSON-like documents) with a horizontal, scale-out architecture that can support huge volumes of both data and traffic.
- [Materialize](https://materializecss.com/) - a modern front-end framework (responsive and mobile-first, similar to Bootstrap) that helps developers build a stylish and responsive application.
- Git - a version control system for for source code management; it allows tracking file changes and coordinating work on those files among multiple people and machines.
- GitHub - a code hosting platform for version control and collaboration. It lets developers work remotely and together on projects from anywhere.