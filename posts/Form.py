from wtforms import Form, StringField, TextAreaField, validators


class CreatePostForm(Form):
    title = StringField('Title', [validators.Length(min=1, max=150), validators.DataRequired()])
    content = TextAreaField('Content', [validators.Optional()])
