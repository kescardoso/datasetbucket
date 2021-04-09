# DATASET BUCKET & BIAS AUDITOR

![label](https://user-images.githubusercontent.com/54631569/114139488-bfc68000-992c-11eb-9b11-28084dd9b8bc.png)

## About

Dataset Bucket 📈 is a python-flask web application build upon a CRUD (Create, Read, Update and Delete) database system to generate, store and display dataset structures.

It's a machine learning bias auditor. Built with [Python-Flask](https://flask.palletsprojects.com/en/1.1.x/), [MaterializeCSS](https://materializecss.com/) and the [Kaggle API](https://www.kaggle.com/docs/api).

You will be able to find and read reports from a **wiki styled list** of information about data containing _population_ and _demographic_ subjects. 

👩 👳🏾‍♂️ 👱🏻‍♀️ 🧔🏾 👩🏼‍🦰 👨🏿‍🦳

## Motivation

The whole world is data-driven, but we are still not sure if the data used in testing the machine learning models are biased to one thing, person, or group. If this is the case the chances are extremely high that the model doesn't yield accurate results. 

To overcome this issue, we came up with an idea to create a web app that tells you if the dataset you are using is biased or not, and also suggests possible changes you can make to improve the quality of your analysis. 📊


## Technologies and Frameworks Used

- [Flask](https://flask.palletsprojects.com/)

- [Git](https://git-scm.com/)

- [GitHub](https://github.com/)

- [Heroku](https://www.heroku.com/)

- [Materialize](https://materializecss.com/)

- [MongoDB](https://www.mongodb.com/)

- [Pip](https://pypi.org/project/pip/)

- [Python](https://www.python.org/)

##### We used a lot of python libraries for building this project. Know more about them from [LIBRARIES.md]().

## App Walkthrough

###### 1. OPEN THE APP
[Head on to our app deployed on Heroku.](https://datasetbucket.herokuapp.com/)

![image](https://user-images.githubusercontent.com/54631569/114146731-9100d780-9935-11eb-9700-52d6ed2ccbdb.png)

You will see a **WELCOME** screen, it has the same basic instructions to get started and what you can expect from the app.

###### 2. DATATAGS

In the **data tags** tab, you can find various tags associated with the reports uploaded on the app. 

![image](https://user-images.githubusercontent.com/54631569/114147605-79761e80-9936-11eb-8d32-b42ac288e8de.png)

By clicking the **view** button on any of the available tags, you can see the dataset, analytical reports, and other information about the TAG.

![image](https://user-images.githubusercontent.com/54631569/114148794-cad2dd80-9937-11eb-855f-996f2d4e2f06.png)

###### 3. DATASETS

The **datasets** tab has the list of all the datasets, to which an analytical report was generated. It is presented in the form of an accordion collapsable styled list, so you can click on any dataset you wish to explore and all the information related to that particular dataset will be displayed. 

![image](https://user-images.githubusercontent.com/54631569/114149794-eb4f6780-9938-11eb-8709-2e313cad1f99.png)

You can view the author, the development status, tags associated, and an option to download the analytical report. 

###### 4. REGISTER / LOG IN

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

## References

🔸 If you want to test run the project on your local computer, follow the guidelines in [TEST.md](https://github.com/kescardoso/datasetbucket/TEST.md).

🔸 If you wish to contribute to the existing project, follow the guidelines in [CONTRIBUTION.md]().

## Contributors

⭐[Elizabeth Crouther]()

⭐[Kes Cardoso]()

⭐[Sakshi Gupta]()

⭐[William Yang]()

## Navigate

➡ [CONTRIBUTION.md]()

➡ [LIBRARIES.md]()

➡ [TEST.md]()

## Thank You! ✨
