# datasetbucket

This is a python-flask application build upon a data-base CRUD system (Create, Read, Update and Delete) 
with the purpose of store and display information about dataset structures based on Machine Learning models.

You will be able to find and read reports from a wiki styled list of information 
about data containing population and demographic subjects.

[Click here to view the deployed app on Heroku](https://datasetbucket.herokuapp.com/)

## Technologies used

- [MongoDB](https://www.mongodb.com/) - a document database (stores data in JSON-like documents) with a horizontal, scale-out architecture that can support huge volumes of both data and traffic.
- [Materialize](https://materializecss.com/) - a modern front-end framework (responsive and mobile-first, similar to Bootstrap) that helps developers build a stylish and responsive application.
- [Python](https://www.python.org/) - an interpreted, high-level and general-purpose programming language, great for data base structured projects.
- [Pip](https://pypi.org/project/pip/) - a package manager for Python, that allows developers to install and manage additional libraries and dependencies that are not distributed as part of the standard library.
- [Flask](https://flask.palletsprojects.com/) - a Python framework that depends on the Jinja template engine and the Werkzeug WSGI toolkit.
- [Heroku](https://www.heroku.com/) - used for the app deployment, Heroku is a platform as a service (PaaS) that enables developers to build, run, and operate applications entirely in the cloud.
- [Git](https://git-scm.com/) - a version control system for for source code management; it allows tracking file changes and coordinating work on those files among multiple people and machines.
- [GitHub](https://github.com/) - a open-source code hosting platform for version control and collaboration. It lets developers work remotely and together on projects from anywhere.

## Project Installation and Local Deployment

### Installation

1. Install [python3 and pip3](https://www.python.org) in your machine
    
2. Download or clone [the datasetbucket project folders](https://github.com/kescardoso/datasetbucket) into your local workspace

3. Create a virtual environment: `Python3 -m venv venv`

    After running this command, the folders will be automatically set up on your workspace.

4. Run: `source venv/bin/activate`

5. Install Flask: `pip3 install flask`

### Local Deployment

1. Create an `env.py` file to keep your sensitive data secret.

2. Open `env.py` and enter the following:

    `import os`

    `os.environ.setdefault("SECRET_KEY", "secret_key_here")`

    `os.environ.setdefault("MONGO_URI", "value_from mongoDB_here")`

    `os.environ.setdefault("MONGO_DBNAME", "value_from mongoDB_here")`

3. Wire up MongoDB and its functionalities with Flask, by installing `flask-pymongo` and `dnspython`

    `pip3 install flask-pymongo`

    `pip3 install dnspython`

4. Wire up Kaggle

    Kaggle API allows the developer to download datasets directly from the terminal.

    1. Create a [kaggle account](https://kaggle.com)

    2. Run: `pip3 install kaggle`

    3. Go to the 'Account' tab in your Kaggle profile and scroll to the 'API' section. Click 'Create new API Token' and add the `kaggle.json` file, which will download to your project structure.

    4. You may need to install the following packages to enable all the commands and functionalities:

    `pip3 install reportlab`

    `pip3 install statistics`

    `pip3 install sklearn`

    For more complete and detailed instructions on how to use the Kaggle API, visit [Kaggle's documentation](https://www.kaggle.com/docs/api#getting-started-installation-&-authentication).

5. Run the `app.py` in debug mode as a flask application to see the project in your locally deployed http address.

## Heroku Deployment

1. Fulfil all Heroku requirements by freezing your dependencies and creating a Procfile:

    Run these two commands:

    `pip3 freeze > requirements.txt`

    `echo web: python app.py > Procfile`

    Commit and push your changes.

2. Create a new app from your Heroku dashboard.

3. Add your environmental variables to Heroku, by going to 'Settings', and then to 'Config Vars', and enter the sensitive information from your MongoDB and your `env.py` file:

    `import os`

    `os.environ.setdefault("SECRET_KEY", "your_secret_key_here")`

    `os.environ.setdefault("MONGO_URI", "value_from mongoDB_here")`

    `os.environ.setdefault("MONGO_DBNAME", "value_from mongoDB_here")`

5. From your Heroku dashboard, wire up your heroku app to your git repository, by going to:
    - "Deploy" > "Deployment Method" > and click: "Connect to GitHub"
    - Search your repo from the dropdown, and connect
    - Choose a branch to deploy your changes
    - Deploy your branch and view app

## Connect to Kaggle

Kaggle API allows the developer to download datasets directly from the terminal/command-line

1. Create a kaggle account at https://kaggle.com

2. `pip install kaggle`

3. Go to 'Account' tab in your kaggle profile a scroll to 'API' section. Click 'Create new API Token' and add the kaggle.json file that will download to your project structure.

For more complete instructions on how to use the Kaggle API, go to https://www.kaggle.com/docs/api#getting-started-installation-&-authentication

## Libraires you might need to install

`pip install os`
`pip install time`
`pip install sys`
`pip install json`
`pip install csv`
`pip install reportlab`
`pip install numpy`
`pip install statistics`
`pip install sklearn.linear_model`


## Technologies used

- Python - an interpreted, high-level and general-purpose programming language, great for data base structured projects
- Pip - a package manager for Python, that allows developers to install and manage additional libraries and dependencies that are not distributed as part of the standard library.
- Flask - a Python framework that depends on the Jinja template engine and the Werkzeug WSGI toolkit
- MongoDB - a document database (stores data in JSON-like documents) with a horizontal, scale-out architecture that can support huge volumes of both data and traffic.
- [Materialize](https://materializecss.com/) - a modern front-end framework (responsive and mobile-first, similar to Bootstrap) that helps developers build a stylish and responsive application.
- Git - a version control system for for source code management; it allows tracking file changes and coordinating work on those files among multiple people and machines.
- GitHub - a code hosting platform for version control and collaboration. It lets developers work remotely and together on projects from anywhere.

