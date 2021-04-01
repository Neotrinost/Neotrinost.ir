from flask_wtf import FlaskForm
from flask_wtf.recaptcha import validators
from wtforms import TextField, PasswordField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    id = TextField(validators = [DataRequired()])
    username = TextField(validators = [DataRequired()])
    password = PasswordField(validators = [DataRequired()])

class ContactUs(FlaskForm):
    email = TextField(validators = [DataRequired()])

class NewPost(FlaskForm):
    title = TextField(validators = [DataRequired()])
    text = TextField(validators = [DataRequired()])