from wtforms import Form, validators, PasswordField
from wtforms.fields.html5 import EmailField
import email_validator


class CreateUserForm(Form):
    email = EmailField('Email', [validators.Email(), validators.DataRequired()])
    password = PasswordField('Password',
                             [validators.Length(min=1, max=150),
                              validators.DataRequired()])