from wtforms import Form, TextAreaField, validators, StringField, RadioField, SelectField


class AddshoppingcartForm(Form):
    item_code = StringField('Item code', [validators.Optional()])
    item_name = StringField('Item name', [validators.Optional()])
    item_amount = StringField('Item amount', [validators.Optional()])
    receit_number = StringField('Receipt number', [validators.Optional()])
    item_price = TextAreaField('Item price', [validators.Optional()])
