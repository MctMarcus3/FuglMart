from flask import Blueprint, render_template, request, url_for, redirect, session
from .Product import Product
from .Form import CreateInventoryForm, UpdateInventoryForm
import shelve

inventory = Blueprint("inventory", __name__, static_folder="static", template_folder="templates")

# Implement CSV upload, CSV Download, JSON Upload, JSON Download
# Implement FuzzySearch

# @inventory.route('/upload')
# def upload_file():
#     return render_template('upload.html')
#
#
# @inventory.route('/uploader', method=['GET', 'POST'])
# def uploader():
#     if request.method == 'POST':
#         f = request.files['file']
#         f.save(secure_filename(f.filename))
#         return 'file uploaded successfully'


@inventory.route('/createproduct', methods=['GET', 'POST'])
def createNewProduct():
    create_inventory_form = CreateInventoryForm(request.form)
    if request.method == 'POST' and create_inventory_form.validate():
        inventory_dict = {}
        invent = []
        inventory_list = []
        db = shelve.open('storage.db', 'c')
        try:
            invent = db['invent']
            inventory_dict = db['inventory']
        except KeyError:
            print("Error in retrieving inventory from storage.db.")
        product = Product(create_inventory_form.productName.data,
                          create_inventory_form.upc.data,
                          create_inventory_form.stock.data,
                          create_inventory_form.price.data)
        productT = {
            "upc": create_inventory_form.upc.data,
            "productName": create_inventory_form.productName.data,
            "stock": create_inventory_form.stock.data,
            "price": create_inventory_form.price.data
        }
        invent.append(product)
        inventory_list.append(productT)
        if inventory_dict.get(product.get_upc()) is None:
            inventory_dict[product.get_upc()] = product
        for i in invent:
            # if i.get_upc() == create_inventory_form.upc.data
            db['inventory'] = inventory_dict
            db['inventoryT'] = inventory_list
            return redirect(url_for('inventory.createNewProduct'))
        else:
            redirect(url_for('inventory.createNewProduct'))
        db.close()
    return render_template('/inventory/productInfo.html', form=create_inventory_form,
                           create=True)
    # return render_template('/inventory/productInfo.html', form=create_inventory_form,
    #                        create=True)


@inventory.route("/")
def retrieve_inventory():
    # print(session["user"]["_User__admin"])
    # if session.get("user") is None or session["user"]["_User__admin"] is False:
    #     return render_template("404.html")
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
    update_product_form = UpdateInventoryForm(request.form)
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
        return redirect(url_for('inventory.retrieve_inventory'))
    else:
        inventory_dict = {}
        db = shelve.open('storage.db', 'r')
        inventory_dict = db['inventory']
        db.close()
        product = inventory_dict.get(id)
        update_product_form.productName.data = product.get_name()
        update_product_form.stock.data = product.get_stock()
        update_product_form.price.data = product.get_price()
        return render_template('/inventory/productInfo.html', form=update_product_form, update=True)


@inventory.route('/deleteproduct/<string:id>', methods=['POST'])
def delete_product(id):
    inventory_dict = {}
    db = shelve.open('storage.db', 'w')
    inventory_dict = db['inventory']
    product = inventory_dict.pop(id)
    db['inventory'] = inventory_dict
    db.close()

    session['product_deleted'] = product.get_name()

    return redirect(url_for("inventory.retrieve_inventory"))


@inventory.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')
