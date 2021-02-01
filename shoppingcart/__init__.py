from flask import Blueprint, render_template, request, url_for, redirect, session, app
from .shoppingcart import Item
import shelve
from wtforms import Form, StringField, RadioField, SelectField, TextAreaField, validators
from .addshoppingcart import AddshoppingcartForm
shoppingcart = Blueprint("shoppingcart",
                         __name__,
                         static_folder="static",
                         template_folder="templates")

@shoppingcart.route('/addshoppingcart', methods=['GET', 'POST'])
def add_cart():
    add_shopping_cart = AddshoppingcartForm(request.form)
    if request.method == 'POST' and add_shopping_cart.validate():
        cart_dict = {}
        db = shelve.open('shoppingcart.db', 'c')

        try:
            cart_dict = db['Item']
        except:
            print("Error in retrieving Cart from shoppingcart.db.")

        cart = Item(add_shopping_cart.item_code.data, add_shopping_cart.item_name.data, add_shopping_cart.item_amount.data, add_shopping_cart.receit_number.data, add_shopping_cart.item_price.data)
        cart_dict[cart.get_item_code()] = cart
        db['Item'] = cart_dict

        # Test codes
        cart_dict = db['Item']
        cart = cart_dict[cart.get_item_code()]
        print(cart.get_item_code(), cart.get_item_name(), "was stored in storage.db successfully with item_code ==", cart.get_item_amount())

        db.close()


        return redirect(url_for('home'))
    return render_template('addCart.html', form=add_shopping_cart)


@shoppingcart.route("/")
def index():
    return render_template('product.html')

@shoppingcart.route('/retrieveCart')
def retrieve_cart():

    return render_template('retrieveCart.html')
