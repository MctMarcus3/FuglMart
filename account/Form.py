from wtforms import Form, validators, PasswordField, StringField, TextAreaField
from wtforms.fields.html5 import EmailField
import email_validator


class CreateUserForm(Form):
    email = EmailField('Email', [validators.Email(), validators.DataRequired()], render_kw={"placeholder": "cookie@fugl.store"})
    password = PasswordField('Password',
                             [validators.Length(min=1, max=150),
                              validators.DataRequired()])


class UserProfile(Form):
    email = EmailField('Email', render_kw={"placeholder": "cookie@fugl.store", 'disabled':'disabled'})
    street_address = TextAreaField('Street Address', [validators.DataRequired()])
    postal_code = StringField('Postal Code', [validators.Length(min=6, max=6), validators.DataRequired()])
    number = StringField('Phone Number', [validators.Length(min=8, max=8), validators.DataRequired()])
    username = StringField('Username', [validators.Length(min=3, max=20), validators.DataRequired()])
