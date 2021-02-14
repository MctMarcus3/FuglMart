from wtforms import StringField, DecimalField, IntegerField, validators, SelectField
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from .Validators import UPCValidator
import csv

# Import Categories
with open('inventory/catagories.csv', 'r', encoding='utf-8') as csv_file:
    categories = csv.reader(csv_file, delimiter=',')
    next(categories)
    categories = list(categories)
    categories.sort()


class InventoryForm(FlaskForm):
    productName = StringField('Product Name', validators=[
        validators.Length(
            min=1,
            max=80,
            message="Product Name must be a minimum of 1 to 80 characters"),
        validators.InputRequired()])
    stock = IntegerField('Stock', validators=[
        validators.NumberRange(
                min=0,
                message="Stock must be a postive number"),
        validators.InputRequired()])

    price = DecimalField('Price', validators=[
        validators.NumberRange(
            min=0,
            message="Stock must be a postive number"),
        validators.InputRequired()],
        places=2,
        rounding=None)

    company = StringField('Product Company', validators=[
        validators.Length(
            min=1,
            message="Company Name must be a minimum of 1 character"
        ),
        validators.InputRequired()])

    category = SelectField('Category', choices=categories)

    upc = StringField('UPC', validators=[validators.optional()], render_kw={'disabled': ''})

    image = FileField('Image', validators=[
        FileRequired(),
        FileAllowed(['jpg', 'png'], 'Images only!')
        ],
        render_kw={"onchange": "loadFile(event)"})


class CreateInventoryForm(InventoryForm):
    upc = StringField('UPC', validators=[
        UPCValidator(),
        validators.InputRequired()
        ])
