from wtforms import Form, StringField, TextAreaField, validators


class CreatePostForm(Form):
    title = StringField('Title', [validators.Length(min=1, max=200), validators.DataRequired()])
    content = TextAreaField('Content', [validators.Optional()])


class CreateCommentForm(Form):
    comment = TextAreaField('Add Comment', [validators.Optional()])
    content = TextAreaField()
