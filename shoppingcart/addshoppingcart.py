from flask import Blueprint, render_template, request, url_for, redirect, session
from .shoppingcart import Item
import shelve
from wtforms import Form, StringField, RadioField, SelectField, TextAreaField, validators

class AddshoppingcartForm(Form):
    item_code = StringField('Item code', [validators.Optional()])
    item_name = StringField('Item name', [validators.Optional()])
    item_amount = StringField('Item amount', [validators.Optional()])

    item_price = TextAreaField('Item price', [validators.Optional()])
