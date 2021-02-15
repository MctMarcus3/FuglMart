from flask import Blueprint, render_template, request, url_for, redirect, session, app
from functools import wraps

from .shoppingcart import Item
import shelve
from wtforms import Form, StringField, RadioField, SelectField, TextAreaField, validators
from .addshoppingcart import AddshoppingcartForm

shoppingcart = Blueprint("shoppingcart",
                         __name__,
                         static_folder="static",
                         template_folder="templates")
def login_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        db = shelve.open('storage.db', 'c')
        if session.get("user_id") is None or db.get('Users') is None:
            return redirect(url_for('account.index'))

        db.close()
        val = func(*args, **kwargs)
        return val
    return wrapper

@shoppingcart.route('/addshoppingcart', methods=['GET', 'POST'])
def add_cart():
    add_shopping_cart = AddshoppingcartForm(request.form)
    if request.method == 'POST' and add_shopping_cart.validate():
        cart_dict = {}
        db = shelve.open('storage.db', 'c')


        try:
            cart_dict = db['Item']
        except:
            print("Error in retrieving Cart from shoppingcart.db.")

        Item.item_count += 1
        item = Item(add_shopping_cart.item_code.data, add_shopping_cart.item_name.data,
                    add_shopping_cart.item_amount.data,
                    add_shopping_cart.item_price.data)
        cart_dict[item.get_item_name()] = item
        db['Item'] = cart_dict

        db.close()

        return redirect(url_for('shoppingcart.retrieve_cart'))
    return render_template('addCart.html', form=add_shopping_cart)


@shoppingcart.route("/")
def index():
    return render_template('product.html')




@shoppingcart.route('/retrieveCart')
def retrieve_cart():
    cart_dict = {}
    db = shelve.open('storage.db', 'r')

    try:
        cart_dict = db['Item']
    except:
        print("Error in retrieving Items from storage.db.")
    db.close()

    Item_list = []
    for key in cart_dict:
        Item = cart_dict.get(key)
        Item_list.append(Item)
    print(Item_list)
    return render_template('retrieveCart.html', count=len(Item_list), Item_list=Item_list)

@shoppingcart.route('/addproduct')
def add_product():
    return render_template('addproduct.html')

@shoppingcart.route('/updateCart/<int:id>/', methods=['GET', 'POST'])
def update_cart(id):
    update_cart_form = AddshoppingcartForm(request.form)
    if request.method == 'POST' and update_cart_form.validate():
        cart_dict = {}
        db = shelve.open('storage.db', 'w')
        cart_dict = db['Item']

        Item = cart_dict.get(id)
        Item.set_item_name(update_cart_form.item_code.data)
        Item.set_item_code(update_cart_form.item_name.data)
        Item.set_item_amount(update_cart_form.item_amount.data)
        Item.set_item_price(update_cart_form.item_price.data)

        db['Item'] = cart_dict
        db.close()

        return redirect(url_for('retrieveCart'))
    else:
        cart_dict = {}
        db = shelve.open('storage.db', 'r')
        cart_dict = db['Item']
        db.close()

        item = cart_dict.get(id)
        update_cart_form.item_name.data = item.get_item_code()
        update_cart_form.item_code.data = item.get_item_name()
        update_cart_form.item_amount.data = item.item_amount()
        update_cart_form.item_price.data = item.item_price()

        return render_template('updateCart.html', form=update_cart_form)


@shoppingcart.route('/deleteCart/<int:id>', methods=['POST','GET'])
def remove_item(id):
    cart_dict = {}
    db = shelve.open('storage.db', 'w')
    cart_dict = db['Item']

    cart_dict.pop(id)

    db['Item'] = cart_dict
    db.close()

    return redirect(url_for('shoppingcart.retrieveCart'))

@shoppingcart.route('/final')
@login_required
def final():
    return render_template('final.html')

@shoppingcart.route('/checkout2')
def checkout2():
    return render_template('checkout2.html')
