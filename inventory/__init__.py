from flask import (
                    Blueprint,
                    render_template,
                    request, url_for, redirect, session, abort, send_from_directory)
from functools import wraps
from .Product import Product
from .Form import InventoryForm, CreateInventoryForm

import shelve
import os
from PIL import Image
import csv
import json

# Wrapper function to test if user is Admin
def Restricted(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        db = shelve.open('storage.db', 'c')
        if session.get("user_id") is None or \
           db.get('Users') is None or \
           db.get('Users')[session["user_id"]].get_admin() is False:
            return render_template('404.html')
        db.close()
        val = func(*args, **kwargs)
        return val
    return wrapper


inventory = Blueprint("inventory", __name__, static_folder="static", template_folder="templates")
invIMGpath = os.path.join("inventoryimages")

# Implement CSV upload, CSV Download, JSON Upload, JSON Download
# Implement FuzzySearch


@inventory.route("/")
@Restricted
def retrieve_inventory():
    db = shelve.open('storage.db', 'c')
    inventory_dict = {}
    if db.get('inventory') is not None:
        inventory_dict = db['inventory']
    else:
        db['inventory'] = {}
    print(db['inventory'])
    db.close()

    inventory_list = []
    for key in inventory_dict:
        product = inventory_dict.get(key)
        inventory_list.append(product)

    return render_template('/inventory/retrieveInventory.html', count=len(inventory_list),
                           inventory_list=inventory_list)


@inventory.route('/createproduct', methods=['GET', 'POST'])
@Restricted
def createNewProduct():
    create_inventory_form = CreateInventoryForm()
    if request.method == 'POST' and create_inventory_form.validate_on_submit():
        inventory_dict = {}
        db = shelve.open('storage.db', 'c')
        try:
            inventory_dict = db['inventory']
        except KeyError:
            print("Error in retrieving inventory from storage.db.")
        product = Product(create_inventory_form.productName.data,
                          create_inventory_form.upc.data,
                          create_inventory_form.stock.data,
                          create_inventory_form.company.data,
                          create_inventory_form.category.data,
                          create_inventory_form.price.data)
        if inventory_dict.get(product.get_upc()) is None:
            f = Image.open(create_inventory_form.image.data)
            f = f.convert("RGB")
            path = os.path.join(invIMGpath, create_inventory_form.upc.data)
            try:
                os.makedirs(path)
            except FileExistsError:
                pass
            path = os.path.join(path, f"{create_inventory_form.upc.data}.jpg")
            f.save(path)
            inventory_dict[product.get_upc()] = product
            db['inventory'] = inventory_dict
            db.close()
            return redirect(url_for('inventory.createNewProduct'))

        else:
            db.close()
            redirect(url_for('inventory.createNewProduct'))
    return render_template('/inventory/productInfo.html', form=create_inventory_form, create=True)
    # return render_template('/inventory/productInfo.html', form=create_inventory_form,
    #                        create=True)


@inventory.route('updateproduct/<string:id>', methods=['GET', 'POST'])
@Restricted
def update_product(id):
    update_product_form = InventoryForm(request.form)
    if request.method == 'POST' and update_product_form.validate_on_submit():
        db = shelve.open('storage.db', 'w')
        inventory_dict = db['inventory']
        product = inventory_dict.get(id)
        product.set_name(update_product_form.productName.data)
        product.set_stock(update_product_form.stock.data)
        product.set_price(update_product_form.price.data)
        product.set_company(update_product_form.company.data)
        product.set_category(update_product_form.category.data)
        db['inventory'] = inventory_dict
        db.close()
        session['product_created'] = product.get_name()
        return redirect(url_for('inventory.retrieve_inventory'))
    else:
        inventory_dict = {}
        db = shelve.open('storage.db', 'r')
        inventory_dict = db['inventory']
        db.close()
        product = inventory_dict.get(id)
        if product is None:
            abort(404)
        update_product_form.productName.data = product.get_name()
        update_product_form.stock.data = product.get_stock()
        update_product_form.price.data = product.get_price()
        update_product_form.upc.data = product.get_upc()
        update_product_form.company.data = product.get_company()
        update_product_form.category.data = product.get_category()
        return render_template('/inventory/productInfo.html', form=update_product_form)


@inventory.route('/deleteproduct/<string:id>', methods=['POST'])
@Restricted
def delete_product(id):
    inventory_dict = {}
    db = shelve.open('storage.db', 'w')
    inventory_dict = db['inventory']
    product = inventory_dict.pop(id)
    db['inventory'] = inventory_dict
    db.close()

    session['product_deleted'] = product.get_name()

    return redirect(url_for("inventory.retrieve_inventory"))


@inventory.route('/img/<path:id>')
def image(id):
    return send_from_directory(f"{invIMGpath}/{id}", f"{id}.jpg")


@inventory.errorhandler(404)
def error(e):
    return render_template('inventory/404.html')
