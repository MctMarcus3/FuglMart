from wtforms import Form, validators, PasswordField
from wtforms.fields.html5 import EmailField
from wtforms import IntegerField, StringField
import email_validator


class CreateUserForm(Form):
    email = EmailField('Email', [validators.Email(), validators.DataRequired()], render_kw={"placeholder": "cookie@fugl.store"})
    password = PasswordField('Password', [validators.Length(min=1, max=150), validators.DataRequired()])
    username = StringField(label=('Username'))
    number = IntegerField('Mobile Number', [validators.NumberRange(min=80000000, max=99999999), validators.DataRequired()])
    postal_code = IntegerField('Postal Code', [validators.NumberRange(min=100000, max=999999), validators.DataRequired()])

class LoginUserForm(Form):
    email = EmailField('Email', [validators.Email(), validators.DataRequired()], render_kw={"placeholder": "cookie@fugl.store"})
    password = PasswordField('Password', [validators.Length(min=1, max=150), validators.DataRequired()])

class UserProfile(Form):
    email = EmailField('Email', [validators.Email(), validators.DataRequired()], render_kw={"placeholder": "cookie@fugl.store"})
    username = StringField('Username')
    number = IntegerField('Mobile Number', [validators.NumberRange(min=80000000, max=99999999), validators.DataRequired()])
    postal_code = IntegerField('Postal Code', [validators.NumberRange(min=100000, max=999999), validators.DataRequired()])
