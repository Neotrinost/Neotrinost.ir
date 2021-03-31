#for developement server on: $env:FLASK_ENV = "development"

from flask import Flask, render_template, request

from lib.forms import LoginForm, ContactUs, NewPost
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

@app.route("/panel")
def panel():
    newpost_form = NewPost()
    return render_template("panel.html", new_form = newpost_form)

@app.route("/newpost/", methods = ['POST'])
def newpost():
    new_form = NewPost(request.form)
    if new_form.validate_on_submit():
        form_title = new_form.title.data
        form_text = new_form.text.data

        return form_title

@app.route("/login")
def login():
    login_form = LoginForm()
    return render_template('login.html', login_form = login_form)

@app.route("/contact")
def contact():
    contact_form = ContactUs()
    return render_template("contact.html", con = contact_form)

@app.route("/subscribe/", methods = ['POST'])
def subscribe():
    contact_form = ContactUs(request.form)
    if contact_form.validate_on_submit():
        form_username = contact_form.email.data

        return form_username


#Errors
@app.errorhandler(404)
def page_not_found(error):
    return render_template("Error/error.html", context = ['404', '404 Page not found', 'Sorry, This page is not found'])

@app.errorhandler(405)
def method_not_allowed(error):
    return render_template("Error/error.html", context = ['405', '405 Method Not Allowed', 'The method is not allowed for the requested URL'])

@app.errorhandler(400)
def forbiden(error):
    return render_template("Error/error.html", context = ['400', '400 Bad Request', 'Sorry, an error has occured, There is a bad requeste'])

@app.errorhandler(500)
def server(error):
    return render_template("Error/error.html", context = ['500', '500 Internal Server Error', 'The server encountered an internal error and was unable to complete your request . Either the server is overloaded or there is an error in the application'])

@app.errorhandler(502)
def other_server(error):
    return render_template("Error/error.html", context = ['502', '502 Gateway Error', 'Sorry, Bad gateway'])

@app.errorhandler(503)
def crash_server(error):
    return render_template("Error/error.html", context = ['503', '503 Service Error', 'Sorry, service is Unavailable'])



if __name__ == "__main__":
    app.run()
