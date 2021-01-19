from flask import Blueprint, render_template, request, url_for, redirect, session
from .shoppingcart import Item
import shelve

shoppingcart = Blueprint("shoppingcart",
                         __name__,
                         static_folder="static",
                         template_folder="templates")


@shoppingcart.route("/")
def index():
    return render_template('product.html')
