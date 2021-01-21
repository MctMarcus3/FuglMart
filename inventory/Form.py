from wtforms import Form, StringField, DecimalField, IntegerField, validators


class CreateInventoryForm(Form):
    productName = StringField('ProductName', [validators.Length(min=1, max=80),
                              validators.DataRequired()])
    stock = IntegerField('Stock',  [validators.NumberRange(min=0),
                         validators.DataRequired()])
    upc = StringField('UPC', [validators.Length(min=13, max=13),
                      validators.DataRequired()])  # TODO: Implement Bar Code Reader
    price = DecimalField('Price', [validators.NumberRange(min=0),
                         validators.DataRequired()], places=2, rounding=None)


class UpdateInventoryForm(Form):
    productName = StringField('ProductName', [validators.Length(min=1, max=80),
                              validators.DataRequired()])
    stock = IntegerField('Stock',  [validators.NumberRange(min=0),
                         validators.DataRequired()])
    price = DecimalField('Price', [validators.NumberRange(min=0),
                         validators.DataRequired()], places=2, rounding=None)
