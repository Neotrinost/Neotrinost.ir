#for developement server on: $env:FLASK_ENV = "development"
from flask import render_template, Flask, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/account/login")
def login():
    return render_template("login.html")

@app.route("/login/", methods = ['POST'])
def check():
    amir = {'Username' : 'amir', 'Password' : '1234'}
    anna_mirhosseiny = {'Username' : 'mirhosseiny', 'Password' : '1234'}
    shahriar = {'Username' : 'shahriaarrr', 'Password' : '1234'}

    Username = request.form['Username']
    Password = request.form['Password']

    if Username.lower() == shahriar['Username'] and Password == shahriar['Password']:
        return render_template("test.html", Username = Username)

    elif Username.lower() == amir['Username'] and Password == amir['Password']:
        return render_template("test.html", Username = Username)
        
    elif Username.lower() == anna_mirhosseiny['Username'] and Password == anna_mirhosseiny['Password']:
        return render_template("test.html", Username = Username)

    return "wrong username or password"

# @app.route("/account/logout")

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html')

if __name__ == "__main__":
    app.run("0.0.0.0", 5000)
