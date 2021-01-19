from flask import Blueprint, render_template, request, url_for, redirect, session
from .Forms import createProduct_form
import shelve

product = Blueprint("product", __name__, static_folder="static", template_folder="templates")


@product.route("/")
def index():
    return render_template('product.html')


@product.route('/createProduct', methods=['POST', 'GET'])
def create_product():
    create_product_form = createProduct_form(request.form)
    if request.method == 'POST' and create_product_form.validate():

        return redirect(url_for('home'))
        return render_template('createProduct.html', form=create_product_form)


@product.route('/instantfood')
def instantfood():
    return render_template('instantfood.html')

@product.route('/staples')
def staples():
    return render_template('staples.html')

@product.route('/drinks')
def drinks():
    return render_template('drinks.html')

@product.route('/personalcare')
def personalcare():
    return render_template('personalcare.html')

@product.route('/householdessentials')
def householdessentials():
    return render_template('householdessentials.html')

@product.route('/snacks')
def snacks():
    return render_template('snacks.html')
