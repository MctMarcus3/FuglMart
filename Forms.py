from wtforms import Form, StringField, TextAreaField, validators

class CreatePostForm(Form):
    Title = StringField('Title', [validators.Length(min=1, max=150), validators.DataRequired()])
    Content = TextAreaField('Content', [validators.Optional()])

class createProduct_form(Form):
    Name = StringField('Name', [validators.Length(min=1, max=150), validators.DataRequired()])
    Productno = StringField('Productno', [validators.Length(min=1, max=150), validators.DataRequired()])
    remarks = TextAreaField('Remarks', [validators.Optional()])


