from wtforms import Form, StringField, DecimalField, IntegerField, validators
from .Validators import UPCValidator


class CreateInventoryForm(Form):
    productName = StringField('ProductName', [validators.Length(
                            min=1,
                            max=80,
                            message="Product Name must be a minimum of 1 to 80 characters"),
                            validators.InputRequired()])
    stock = IntegerField('Stock',  [validators.NumberRange(
                        min=0,
                        message="Stock must not be a negative number"),
                         validators.InputRequired()])

    upc = StringField('UPC', [validators.InputRequired(), UPCValidator()])
    price = DecimalField('Price', [validators.NumberRange(min=0), validators.InputRequired()],
                         places=2, rounding=None)


class UpdateInventoryForm(Form):
    productName = StringField('ProductName', [validators.Length(min=1, max=80),
                              validators.InputRequired()])
    stock = IntegerField('Stock',  [validators.NumberRange(min=0),
                         validators.InputRequired()])
    price = DecimalField('Price', [validators.NumberRange(min=0),
                         validators.InputRequired()], places=2, rounding=None)
