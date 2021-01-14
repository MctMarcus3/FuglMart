from flask import Blueprint, render_template, request, url_for, redirect, session
from inventoryProduct import Product
from inventoryForm import CreateInventoryForm
import shelve

inventory = Blueprint("inventory", __name__, static_folder="static", template_folder="templates")


@inventory.route('/createproduct', methods=['GET', 'POST'])
def createNewProduct():
    create_inventory_form = CreateInventoryForm(request.form)
    if request.method == 'POST' and create_inventory_form.validate():
        inventory_dict = {}
        db = shelve.open('storage.db', 'c')
        try:
            inventory_dict = db['inventory']
        except KeyError:
            print("Error in retrieving inventory from storage.db.")

        product = Product(create_inventory_form.productName.data,
                          create_inventory_form.upc.data,
                          create_inventory_form.stock.data,
                          create_inventory_form.price.data)
        inventory_dict[product.get_upc()] = product
        db['inventory'] = inventory_dict

        db.close()
        return redirect('/inventory')
    return render_template('/inventory/productInfo.html', form=create_inventory_form, showUPC=True)


@inventory.route("/")
def retrieve_inventory():
    inventory_dict = {}

    db = shelve.open('storage.db', 'c')
    if db.get('inventory') is not None:
        inventory_dict = db['inventory']
    else:
        db['inventory'] = {}
    db.close()

    inventory_list = []
    for key in inventory_dict:
        product = inventory_dict.get(key)
        inventory_list.append(product)

    return render_template('/inventory/retrieveInventory.html', count=len(inventory_list),
                           inventory_list=inventory_list)


@inventory.route('updateproduct/<string:id>', methods=['GET', 'POST'])
def update_product(id):
    update_product_form = CreateInventoryForm(request.form)
    if request.method == 'POST' and update_product_form.validate():
        db = shelve.open('storage.db', 'w')
        inventory_dict = db['inventory']
        product = inventory_dict.get(id)
        product.set_name(update_product_form.productName.data)
        product.set_stock(update_product_form.stock.data)
        product.set_price(update_product_form.price.data)
        db['inventory'] = inventory_dict
        db.close()
        session['product_created'] = product.get_name()
        return redirect('/inventory')
    else:
        inventory_dict = {}
        db = shelve.open('storage.db', 'r')
        inventory_dict = db['inventory']
        db.close()
        product = inventory_dict.get(id)
        update_product_form.productName.data = product.get_name()
        update_product_form.stock.data = product.get_stock()
        update_product_form.price.data = product.get_price()
        update_product_form.upc.data = product.get_upc()
        return render_template('/inventory/productInfo.html', form=update_product_form)


@inventory.route('/deleteproduct/<string:id>', methods=['POST'])
def delete_product(id):
    inventory_dict = {}
    db = shelve.open('storage.db', 'w')
    inventory_dict = db['inventory']
    product = inventory_dict.pop(id)
    db['inventory'] = inventory_dict
    db.close()

    session['product_deleted'] = product.get_name()

    return redirect('/inventory/retrieveInventory')
