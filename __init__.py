from flask import Flask, render_template, request, redirect, url_for, session, flash
from Forms import CreatePostForm
from Posts import Posts
import shelve, shcart

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def home():
    return render_template('index.html')


@app.route('/account')
def account():
    return render_template('account.html')


@app.route('/checkout')
def checkout():
    return render_template('checkout.html')


@app.route('/cart')
def cart():
    return render_template('cart.html')


@app.route('/product')
def product():
    return render_template('product.html')


@app.route('/login')
def login():
    return render_template('index.html')



@app.route('/createPost', methods=['GET', 'POST'])
def create_user():
    create_post_form = CreatePostForm(request.form)
    if request.method == 'POST' and create_post_form.validate():
        posts_dict = {}
        db = shelve.open('storage.db', 'c')

        try:
            posts_dict = db['Posts']
        except KeyError:
            print("Error in retrieving Posts from storage.db.")

        post = Posts(create_post_form.Title.data, create_post_form.Content.data,)
        posts_dict[post.get_posts_id()] = post
        db['Posts'] = posts_dict
        # print(posts_dict)
        # Test Code

        print(f"{post.get_title()} {post.get_content()} was stored in storage.db "
              f"successfully with post_id == {post.get_posts_id()}")

        db.close()

        return redirect(url_for('home'))
    return render_template('createPost.html', form=create_post_form)

@app.route('/retrievePosts')
def retrive_posts():
    posts_dict = {}
    db = shelve.open('storage.db', 'r')
    posts_dict = db['Posts']
    db.close()

    posts_list = []
    for key in posts_dict:
        posts = posts_dict.get(key)
        posts_list.append(posts)

    return render_template('retrievePosts.html', count=len(posts_list), posts=posts_list)

@app.route('/inventory')
def inventory():
    return render_template('inventory.html')

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




if __name__ == '__main__':
    app.run(debug=True)
