from flask import Flask, render_template, request, redirect, url_for, session
from dashboard import dashboard
from inventory import inventory
from Forms import CreatePostForm, CreateUserForm, createProduct_form
from Posts import Posts
from User import User
import shelve, shcart
from shcart import item


app = Flask(__name__)
app.secret_key = 'any_random_string'
app.register_blueprint(inventory, url_prefix="/inventory")
app.register_blueprint(dashboard, url_prefix="/dashboard")



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


@app.route('/product')
def product():
    return render_template('product.html')



@app.route('/account', methods=['POST', 'GET'])
def account():
    create_user_form = CreateUserForm(request.form)
    if request.method == 'POST' and create_user_form.validate():
        users_dict = {}
        db = shelve.open('storage.db', 'c')

        try:
            users_dict = db['Users']
        except:
            print("Error in retrieving Users from storage.db.")
        admin = False
        if create_user_form.email.data.split("@")[1] == "fugl.store":
            admin = True
        user = User(create_user_form.email.data, create_user_form.password.data, admin)
        users_dict[user.get_email()] = user
        db['Users'] = users_dict

        # Test codes
        users_dict = db['Users']
        user = users_dict[user.get_email()]
        print(user.get_email(), "was stored in storage.db successfully")
        print(user.get_admin(), "was stored in storage.db successfully")

        db.close()

        return redirect(url_for('home'))

    return render_template('account.html', form=create_user_form)

@app.route('/login', methods=['POST', 'GET'])
def login():
    login_user_form = CreateUserForm(request.form)
    if request.method == 'POST' and login_user_form.validate():
        # Access shelve to retrieve users_dict
        users_dict = {}
        db = shelve.open('storage.db', 'c')

        try:
            users_dict = db['Users']
        except:
            print("Error in retrieving Users from storage.db.")

        if users_dict.get(login_user_form.email.data) is not None:
            if (users_dict[login_user_form.email.data].get_password() ==
                    login_user_form.password.data):
                return redirect(url_for('profile'))
            else:
                return render_template('account.html', error=True, form=login_user_form)
        return render_template('account.html', error=True, form=login_user_form)
    return render_template('account.html', form=login_user_form)

@app.route('/profile')
def profile():
    update_user_form = CreateUserForm(request.form)
    if request.method == 'POST' and update_user_form.validate():

        return redirect(url_for('profile'))
    return render_template('login.html', form=update_user_form)

@app.route('/createPost', methods=['GET', 'POST'])
def create_post():
    create_post_form = CreatePostForm(request.form)
    if request.method == 'POST' and create_post_form.validate():
        posts_dict = {}
        db = shelve.open('storage.db', 'c')

        try:
            posts_dict = db['Posts']
        except:
            print("Error in retrieving Posts from storage.db.")

        post = Posts(create_post_form.title.data, create_post_form.content.data)
        posts_dict[post.get_posts_id()] = post
        db['Posts'] = posts_dict

    return render_template('createPost.html', form=create_post_form)


@app.route('/retrievePosts')
def retrieve_posts():
    posts_dict = {}
    db = shelve.open('storage.db', 'r')
    posts_dict = db['Posts']
    db.close()

    posts_list = []
    for key in posts_dict:
        posts = posts_dict.get(key)
        posts_list.append(posts)

    return render_template('retrievePosts.html', count=len(posts_list), posts_list=posts_list)


@app.route('/deletePost/<int:id>', methods=['POST'])
def delete_post(id):
    posts_dict = {}
    db = shelve.open('storage.db', 'w')
    posts_dict = db['Posts']

    posts_dict.pop(id)

    db['Posts'] = posts_dict
    db.close()

    return redirect(url_for('retrieve_posts'))


@app.route('/updatePosts/<int:id>/', methods=['GET', 'POST'])
def update_posts(id):
    update_post_form = CreatePostForm(request.form)
    if request.method == 'POST' and update_post_form.validate():
        posts_dict = {}
        db = shelve.open('storage.db', 'w')
        posts_dict = db['Posts']

        post = posts_dict.get(id)
        post.set_title(update_post_form.title.data)
        post.set_content(update_post_form.content.data)
        db['Posts'] = posts_dict
        db.close()

        return redirect(url_for('retrieve_posts'))
    else:
        posts_dict = {}
        db = shelve.open('storage.db', 'r')
        posts_dict = db['Posts']
        db.close()

        post = posts_dict.get(id)
        update_post_form.title.data = post.get_title()
        update_post_form.content.data = post.get_content()
        return render_template('updatePosts.html', form=update_post_form)




@app.route('/instantfood')
def instantfood():
    return render_template('instantfood.html')

@app.route('/staples')
def staples():
    return render_template('staples.html')

@app.route('/drinks')
def drinks():
    return render_template('drinks.html')

@app.route('/personalcare')
def personalcare():
    return render_template('personalcare.html')

@app.route('/householdessentials')
def householdessentials():
    return render_template('householdessentials.html')

@app.route('/snacks')
def snacks():
    return render_template('snacks.html')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')

@app.route('/createProduct', methods=['POST', 'GET'])
def create_product():
    create_product_form = createProduct_form(request.form)
    if request.method == 'POST' and create_product_form.validate():

        return redirect(url_for('home'))
    return render_template('createProduct.html', form = create_product_form)




if __name__ == '__main__':
    app.run(debug=True)
