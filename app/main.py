#for developement server on: $env:FLASK_ENV = "development"
#for save all databace edit's please write db.commit() after edit databace

from flask import Flask, render_template, request, g

from lib.forms import LoginForm
from lib.database import username, password

app = Flask(__name__)
app.config['SECRET_KEY'] = '1234'

@app.route("/")
def index():
    return render_template("home.html")

@app.route("/blog")
def blog():
    return render_template("blog.html")

@app.route("/about")
def about():
    return render_template("about.html")


#admin routes
@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/login")
def login():
    login_form = LoginForm()
    return render_template('login.html', login_form = login_form)

@app.route("/submit/", methods = ['POST'])
def submit():
    login_form = LoginForm(request.form)
    if login_form.validate_on_submit():
        form_username = login_form.username.data
        form_password = login_form.password.data

        if form_username == username and form_password == password:
            return render_template("panel.html", username = username)
        else:
            return render_template("Error/user.html", error = "Username or Password is incorrect")
        
    # return "OK"


#Errors
@app.errorhandler(404)
def page_not_found(error):
    return render_template('Error/404.html')

@app.errorhandler(400)
def forbiden(error):
    return render_template('Error/400.html')

@app.errorhandler(500)
def server(error):
    return render_template('Error/500.html')

@app.errorhandler(502)
def other_server(error):
    return render_template("Error/502.html")

@app.errorhandler(503)
def crash_server(error):
    return render_template("Error/503.html")



if __name__ == "__main__":
    app.run()
