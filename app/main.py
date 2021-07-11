# Importing Flask Things
from flask import Flask, render_template, request, session, redirect

from lib.forms import LoginForm, ContactUs, NewPost

# Starting The App #
app = Flask(__name__)

app.config['SECRET_KEY'] = '1234'

# Rendering Templates #

# Index
@app.route("/")
def index():
    return render_template("home.html")

# Login
@app.route("/login")
def login():
    if 'status' in session:
        return redirect("/")
    else:
        login_form = LoginForm()
        return render_template('login.html', login_form = login_form)

# Panel
@app.route("/panel")
def panel():
    if 'status' in session:
        newpost_form = NewPost()
        return render_template("panel.html", new_form = newpost_form)
    else:
        return redirect("/")

# New Post Back-End
@app.route("/newpost/", methods = ['POST'])
def newpost():
    new_form = NewPost(request.form)
    if new_form.validate_on_submit():
        form_title = new_form.title.data
        form_text = new_form.text.data

# Login Back-End
@app.route("/submit/", methods = ['POST'])
def submit():
    login_form = LoginForm(request.form)
    if login_form.validate_on_submit():
        form_username = login_form.username.data
        form_password = login_form.password.data
        if form_username == "amir" and form_password == "1234":
            session['status'] = True
            session['username'] = form_username
            return redirect("/panel")
        else:
            return render_template("Error/error.html", context = ['User Error', 'Sorry, Username or Password is incorrect'])

# Logout Back-End
@app.route("/logout")
def logout():
   session.pop('status', None)
   return redirect("/")

# Errors #

# 404 Page Not Found
@app.errorhandler(404)
def page_not_found(error):
    return render_template("Error/error.html", context = ['404', '404 Page not found', 'Sorry, This page is not found'])

# 405 Method Not Allowed
@app.errorhandler(405)
def method_not_allowed(error):
    return render_template("Error/error.html", context = ['405', '405 Method Not Allowed', 'The method is not allowed for the requested URL'])

# 400 Bad Request
@app.errorhandler(400)
def forbiden(error):
    return render_template("Error/error.html", context = ['400', '400 Bad Request', 'Sorry, an error has occured, There is a bad requeste'])

# 500 Internal Server Error
@app.errorhandler(500)
def server(error):
    return render_template("Error/error.html", context = ['500', '500 Internal Server Error', 'The server encountered an internal error and was unable to complete your request . Either the server is overloaded or there is an error in the application'])

# 502 Gateway Error
@app.errorhandler(502)
def other_server(error):
    return render_template("Error/error.html", context = ['502', '502 Gateway Error', 'Sorry, Bad gateway'])

# Srcive Error
@app.errorhandler(503)
def crash_server(error):
    return render_template("Error/error.html", context = ['503', '503 Service Error', 'Sorry, service is Unavailable'])

# App Running
if __name__ == "__main__":
    app.run()
