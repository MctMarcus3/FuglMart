from wtforms import Form, StringField, TextAreaField, validators, PasswordField
from wtforms.fields.html5 import EmailField
import email_validator


class CreatePostForm(Form):
    title = StringField('Title', [validators.Length(min=1, max=150), validators.DataRequired()])
    content = TextAreaField('Content', [validators.Optional()])

class createProduct_form(Form):
    Name = StringField('Name', [validators.Length(min=1, max=150), validators.DataRequired()])
    Productno = StringField('Productno', [validators.Length(min=1, max=150), validators.DataRequired()])
    remarks = TextAreaField('Remarks', [validators.Optional()])

class CreateUserForm(Form):
    email = EmailField('Email', [validators.Email(), validators.DataRequired()])
    password = PasswordField('Password', [validators.Length(min=1, max=150), validators.DataRequired()])
