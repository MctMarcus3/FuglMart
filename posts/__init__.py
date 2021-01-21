from flask import Blueprint, render_template, request, redirect, url_for
from .Form import CreatePostForm
from .Posts import Posts
import shelve

posts = Blueprint("posts", __name__, static_folder="static", template_folder="templates")


@posts.route('/createPost', methods=['GET', 'POST'])
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
        db.close()
        return redirect(url_for('retrieve_posts'))
    return render_template('createPost.html', form=create_post_form)


@posts.route('/')
def retrieve_posts():
    posts_dict = {}
    db = shelve.open('storage.db', 'r')
    try:
        posts_dict = db['Posts']
    except:
        print("Error in retrieving Posts from storage.db.")
    db.close()

    posts_list = []
    for key in posts_dict:
        posts = posts_dict.get(key)
        posts_list.append(posts)

    return render_template('retrievePosts.html', count=len(posts_list), posts_list=posts_list)


@posts.route('/deletePost/<int:id>', methods=['POST'])
def delete_post(id):
    posts_dict = {}
    db = shelve.open('storage.db', 'w')
    posts_dict = db['Posts']

    posts_dict.pop(id)

    db['Posts'] = posts_dict
    db.close()

    return redirect(url_for('retrieve_posts'))


@posts.route('/updatePosts/<int:id>/', methods=['GET', 'POST'])
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