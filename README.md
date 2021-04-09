# DATASET BUCKET & BIAS AUDITOR

![label](https://user-images.githubusercontent.com/54631569/114139488-bfc68000-992c-11eb-9b11-28084dd9b8bc.png)

[Check out our project on Heroku!](https://datasetbucket.herokuapp.com/)

## About

A dataset bucket and a machine learning bias auditor 📈, fully responsive web-app built on Python, with [Flask](https://flask.palletsprojects.com/en/1.1.x/), [the MaterializeCSS UI grid system](https://materializecss.com/) and the [Kaggle API](https://www.kaggle.com/docs/api).

Based on a CRUD (Create, Read, Update and Delete) data-base system to generate, store and display dataset structures.

You will be able to find and read reports from a **wiki styled list** of information about data containing _population_ and _demographic_ subjects. 

👩 👳🏾‍♂️ 👱🏻‍♀️ 🧔🏾 👩🏼‍🦰 👨🏿‍🦳

## Motivation

The whole world is data-driven.

However, data can often be misleading, inaccurate, or unrepresentative. When this biased data used in analytics or ML models, it not only produces inaccurate results, but also results in disastrous implications for minority groups and classes.

To confront this dangerous problem, we built a web app that analyzes a dataset for bias, and also suggests possible changes you can make to improve the quality of your dataset. 📊


## Technologies used

- [MongoDB](https://www.mongodb.com/) - a document database (stores data in JSON-like documents) with a horizontal, scale-out architecture that can support huge volumes of both data and traffic.
- [Materialize](https://materializecss.com/) - a modern front-end framework (responsive and mobile-first, similar to Bootstrap) that helps developers build a stylish and responsive application.
- [Python](https://www.python.org/) - an interpreted, high-level and general-purpose programming language, great for data base structured projects.
- [Pip](https://pypi.org/project/pip/) - a package manager for Python, that allows developers to install and manage additional libraries and dependencies that are not distributed as part of the standard library.
- [Flask](https://flask.palletsprojects.com/) - a Python framework that depends on the Jinja template engine and the Werkzeug WSGI toolkit.
- [Heroku](https://www.heroku.com/) - used for the app deployment, Heroku is a platform as a service (PaaS) that enables developers to build, run, and operate applications entirely in the cloud.
- [Git](https://git-scm.com/) - a version control system for for source code management; it allows tracking file changes and coordinating work on those files among multiple people and machines.
- [GitHub](https://github.com/) - a open-source code hosting platform for version control and collaboration. It lets developers work remotely and together on projects from anywhere.

##### We used a lot of python libraries for building this project. Know more about them from [LIBRARIES.md](https://github.com/kescardoso/datasetbucket/blob/main/LIBRARIES.md).

## App Walkthrough

<img width="1111" alt="responsive" src="https://user-images.githubusercontent.com/54631569/114216890-237c9780-9985-11eb-9f9a-f8269d034396.png">

#### 1. OPEN THE APP
[Head on to our app deployed on Heroku.](https://datasetbucket.herokuapp.com/)

![image](https://user-images.githubusercontent.com/54631569/114146731-9100d780-9935-11eb-9700-52d6ed2ccbdb.png)

You will see a **WELCOME** screen, it has the same basic instructions to get started and what you can expect from the app.

#### 2. DATATAGS

In the **data tags** tab, you can find various tags associated with the reports uploaded on the app. 

![image](https://user-images.githubusercontent.com/54631569/114147605-79761e80-9936-11eb-8d32-b42ac288e8de.png)

By clicking the **view** button on any of the available tags, you can see the dataset, analytical reports, and other information about the TAG.

![image](https://user-images.githubusercontent.com/54631569/114148794-cad2dd80-9937-11eb-855f-996f2d4e2f06.png)

#### 3. DATASETS

The **datasets** tab has the list of all the datasets, to which an analytical report was generated. It is presented in the form of an accordion collapsable styled list, so you can click on any dataset you wish to explore and all the information related to that particular dataset will be displayed. 

![image](https://user-images.githubusercontent.com/54631569/114149794-eb4f6780-9938-11eb-8709-2e313cad1f99.png)

You can view the author, the development status, tags associated, and an option to download the analytical report. 

#### 4. REGISTER / LOG IN

Using the **register** tab you will land on the registration page, where you can create an account on this app.

![image](https://user-images.githubusercontent.com/54631569/114149979-20f45080-9939-11eb-83a1-171fca78f160.png)

If you are already a user of our app, head on the **log in** page.

💟 _By being a registered user of our app, you will have access to upload new datasets to the app and generate reports for those._

###### 5. ANALYSE

_After logging into the app_ go to the * analyze* tab. You will see a menu to `enter the kaggle URL`. After adding a valid Kaggle dataset URL. Click on `GET ANALYSIS REPORT`.

![image](https://user-images.githubusercontent.com/54631569/114151798-218de680-993b-11eb-8054-a7a52811994f.png)

You will see a progress bar till the report gets generated. Once it stops, the report gets downloaded automatically by the name of `report.pdf`.

![image](https://user-images.githubusercontent.com/54631569/114153383-e12f6800-993c-11eb-8c2c-4ecf9d1c1de9.png)

It would have all the details related to your dataset and what all improvements are possible.

## 📩 Project Installation and Local Deployment

### Prerequisites

 Install [python3 and pip3](https://www.python.org) in your machine

 Create an account on [Kaggle](https://www.kaggle.com/)

### Installation
    
1. Download or clone [this project](https://github.com/kescardoso/datasetbucket) into your local workspace

2. Create a virtual environment using the command: `Python3 -m venv venv`

    _After running this command, the folders will be automatically set up on your workspace._

3. Activate your python interpretor using the command: 
    
    `source venv/bin/activate` : mac
    
    `.\venv\Scripts\activate` : windows

4. Install [Flask](https://flask.palletsprojects.com/en/1.1.x/) using the command:
    
    `pip3 install Flask`

    and all the required dependencies with: 

    `pip3 install -r requirements.txt`

### Local Deployment

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
        
        _If you are on macOS/linux, and you need help getting to your ~/.kaggle/ folder, follow these instructions: [Kaggle installation on macOS/Linux](https://adityashrm21.github.io/Setting-Up-Kaggle/)_

    3. Wire up MongoDB and its functionalities with Flask, by installing `flask-pymongo` and `dnspython`. Use:

        `pip3 install flask-pymongo`

        `pip3 install dnspython`
    
    
    4. Run the `app.py` in debug mode as a flask application or use the following command: 

        `python3 -m flask run`
    
        to see the project in your locally deployed `http` address.

    5. You may need to install the following packages to enable all the commands and functionalities:

        `pip3 install reportlab`

        `pip3 install statistics`

        `pip3 install sklearn`

    

### Heroku Deployment

1. Fulfil all Heroku requirements by chequing and freezing your dependencies and by creating a Procfile:

    You can run these two commands to fulfill the purpose:

    `pip3 freeze > requirements.txt`

    `echo web: python app.py > Procfile`

_You may need to install gunicorn. For a good tutorial, check [this youtube tutorial]( "https://www.youtube.com/watch?v=9GCLwYlM8cc")_

   **Commit and push your changes.**

2. Create a new app from your [Heroku dashboard](https://www.heroku.com/).

3. Add your environmental variables to Heroku, by going to **Settings**, and then to **Config Vars**, and enter the sensitive information from your MongoDB and your `env.py` file:

    ```
    import os

    os.environ.setdefault("SECRET_KEY", "your_secret_key_here")
    os.environ.setdefault("MONGO_URI", "value_from mongoDB_here")
    os.environ.setdefault("MONGO_DBNAME", "value_from mongoDB_here")
    ```

4. From your Heroku dashboard, wire up your Heroku app to your git repository, by going to:

    - **Deploy** > **Deployment Method** > click: **Connect to GitHub**

    - Search your repo from the dropdown, and connect

    - Choose a branch to deploy your changes

    - Deploy your branch and view the app

### References

🔸 If you want to test run the project on your local computer, follow the guidelines in [installation guide](https://github.com/kescardoso/datasetbucket#-project-installation-and-local-deployment).

🔸 If you wish to contribute to the existing project, follow the guidelines in [CONTRIBUTION.md](https://github.com/kescardoso/datasetbucket/blob/main/CONTRIBUTION.md).

## Challenges

- Encountering bugs when deploying on Heroku
- Accounting for different formatting of different datasets and types of files (JSON and CSV)
- Ensuring that the app works for both macOS and Windows
- Learning about lots of new technologies and languages for our team, including Python, Flask, HTML, CSS, Javascript, Matplot, file parsing, and data analysis
- Working in different time zones

## Lessons / Takeaways

- Plan more in advance instead of diving into code headfirst
- Deploy on Heroku earlier
- Spend less time getting program to run on different files, but do more analysis for one specific file

## Accomplishments / Contributions

- Overall, we are proud to have completed a tough project and develop a functional web app that effectively parses files, handles multiple types of datasets, and generates PDFs!
- What are we proud to accomplish / what did we work on?
    - "Gaining a better understanding of Python, and having a first real dive in data analytics — it changed how I see machine learning forver!" -Kes
    - "Learning to use python better and parsing with pandas database, integrating back + front end, and deploying on heroku!" -Elizabeth
    - "Working with images and extracting useful info out of it to generate reports!" -Sakshi
    - "Parsing files, generating histograms, and connecting the analysis to the PDFs was super exciting for me!" -Will

## Next Steps

- Implement more advanced metrics and recommendations for dataset analysis
- Allow users to upload their own datasets in addition to datasets on kaggle

## Contributors

⭐[Elizabeth Crouther](https://github.com/eliboss)

⭐[Kes Cardoso](https://github.com/kescardoso)

⭐[Sakshi Gupta](https://github.com/sakshigupta265)

⭐[William Yang](https://github.com/wyang0216)

## Navigate

➡ [CONTRIBUTION.md](https://github.com/kescardoso/datasetbucket/blob/main/CONTRIBUTION.md)

➡ [LIBRARIES.md](https://github.com/kescardoso/datasetbucket/blob/main/LIBRARIES.md)


### Thank You! ✨
