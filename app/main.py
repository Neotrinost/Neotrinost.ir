#for developement server on: $env:FLASK_ENV = "development"
from flask import render_template, Flask

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/account/login")
def login():
    return render_template("login.html")

# @app.route("/account/logout")

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html')

if __name__ == "__main__":
    app.run("0.0.0.0", 5000)
