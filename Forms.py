from wtforms import Form, StringField, TextAreaField, validators

class CreatePostForm(Form):
    Title = StringField('Title', [validators.Length(min=1, max=150), validators.DataRequired()])
    Content = TextAreaField('Content', [validators.Optional()])


