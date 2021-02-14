from flask import Flask, render_template
from dashboard import dashboard
from inventory import inventory
from account import account
from posts import posts
from shoppingcart import shoppingcart
from product import product


app = Flask(__name__)
app.secret_key = 'any_random_string'
app.register_blueprint(inventory, url_prefix="/inventory")
app.register_blueprint(dashboard, url_prefix="/dashboard")
app.register_blueprint(account, url_prefix="/account")
app.register_blueprint(shoppingcart, url_prefix="/shcart")
app.register_blueprint(product, url_prefix="/product")
app.register_blueprint(posts, url_prefix="/forum")


@app.route('/')
@app.route('/index')
def home():
    return render_template('index.html')

@app.route('/checkout')
def checkout():
    return render_template('checkout.html')


@app.route('/cart')
def cart():
    return render_template('cart.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')
