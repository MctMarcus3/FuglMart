from wtforms import Form, TextAreaField, validators, StringField


class createProduct_form(Form):
    Name = StringField('Name', [validators.Length(min=1, max=150), validators.DataRequired()])
    Productno = StringField('Productno',
                            [validators.Length(min=1, max=150),
                             validators.DataRequired()])
    remarks = TextAreaField('Remarks', [validators.Optional()])
