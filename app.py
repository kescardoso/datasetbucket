import os

from flask import Flask
if os.path.exists("env.py"):
    import env


# Create an instance of Flask (Flask app)
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World... Again!'


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)  # update to False prior to submission
