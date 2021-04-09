# 📩 Project Installation and Local Deployment


## Prerequisites

 Install [python3 and pip3](https://www.python.org) in your machine

 Create an account on [Kaggle](https://www.kaggle.com/)


## Installation
    
1. Download or clone [this project](https://github.com/kescardoso/datasetbucket) into your local workspace

2. Create a virtual environment using the command: `Python3 -m venv venv`

    _After running this command, the folders will be automatically set up on your workspace._

3. Activate your python interpretor using the command: 
    
    `source venv/bin/activate` : mac
    
    `.\venv\Scripts\activate` : windows

4. Install [Flask](https://flask.palletsprojects.com/en/1.1.x/) using the command:
    
    `pip install Flask`

    and all the required dependencies with: 

    `pip3 install -r requirements.txt`

## Local Deployment

1. Create an `env.py` file to keep your sensitive data secret.

2. Open `env.py` and enter the following:

    ```python
    import os

    os.environ.setdefault("SECRET_KEY", "secret_key_here")
    os.environ.setdefault("MONGO_URI", "value_from mongoDB_here")
    os.environ.setdefault("MONGO_DBNAME", "value_from mongoDB_here")
    ```

3. Wire up [Kaggle](https://www.kaggle.com/)

    [Kaggle API](https://www.kaggle.com/docs/api) allows the developer to download datasets directly from the terminal.

    1. Make sure you have a [kaggle account](https://kaggle.com)

    2. Follow these steps to download `kaggle.json` files, which helps to run the API:
        
        - Go to the **Account** tab in your Kaggle profile and scroll to the **API** section. 
        
        - Click **Create new API Token**. This will download the `kaggle.json` file, add it to the `/.kaggle` path.

        _For more complete and detailed instructions on how to use the Kaggle API, visit [Kaggle's documentation](https://www.kaggle.com/docs/api#getting-started-installation-&-authentication)._

    3. Wire up MongoDB and its functionalities with Flask, by installing `flask-pymongo` and `dnspython`. Use:

        `pip3 install flask-pymongo`

        `pip3 install dnspython`
    
    
    4. Run the `app.py` in debug mode as a flask application or use the following command: 

        `pyhon3 -m flask run`
    
        to see the project in your locally deployed `http` address.

    5. You may need to install the following packages to enable all the commands and functionalities:

        `pip3 install reportlab`

        `pip3 install statistics`

        `pip3 install sklearn`

    

## Heroku Deployment

1. Fulfil all Heroku requirements by chequing and freezing your dependencies and by creating a Procfile:

    You can run these two commands to fulfill the purpose:

    `pip3 freeze > requirements.txt`

    `echo web: python app.py > Procfile`

    **Commit and push your changes.**

2. Create a new app from your [Heroku dashboard](https://www.heroku.com/).

3. Add your environmental variables to Heroku, by going to **Settings**, and then to **Config Vars**, and enter the sensitive information from your MongoDB and your `env.py` file:

    `import os`

    `os.environ.setdefault("SECRET_KEY", "your_secret_key_here")`

    `os.environ.setdefault("MONGO_URI", "value_from mongoDB_here")`

    `os.environ.setdefault("MONGO_DBNAME", "value_from mongoDB_here")`

4. From your Heroku dashboard, wire up your Heroku app to your git repository, by going to:

    - **Deploy** > **Deployment Method** > click: **Connect to GitHub**

    - Search your repo from the dropdown, and connect

    - Choose a branch to deploy your changes

    - Deploy your branch and view the app


## Navigate

➡ [README.md]()

➡ [CONTRIBUTION.md]()

➡ [LIBRARIES.md]()
