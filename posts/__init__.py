from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from .Form import CreatePostForm, CreateCommentForm, SearchForm
from .Post import Post, Comment
from functools import wraps
import shelve

posts = Blueprint("posts", __name__, static_folder="static", template_folder="templates")


def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash("You need to login first")
            return redirect(url_for('posts.retrieve_posts'))

    return wrap


@posts.route('/createPost', methods=['GET', 'POST'])
#@login_required
def create_post():
    create_post_form = CreatePostForm(request.form)
    if request.method == 'POST' and create_post_form.validate():
        posts_dict = {}
        users_dict = {}
        db = shelve.open('storage.db', 'c')

        try:
            users_dict = db['Users']
            posts_dict = db['Posts']
        except KeyError:
            print("Error in retrieving Users or Posts from storage.db.")
        user = users_dict.get(session['user_id']).get_username()
        session['username'] = user
        post = Post(create_post_form.title.data, create_post_form.content.data, user)
        posts_dict[post.get_id()] = post
        db['Posts'] = posts_dict
        db.close()

        return redirect(url_for('posts.retrieve_posts'))
    return render_template('/Forum/createPost.html', form=create_post_form)


@posts.route('/retrievePosts', methods=['POST', 'GET'])
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
        # print(key, posts)
    searchform = SearchForm(request.form)
    # if request.method == 'POST':
    #     search = searchform.search.data
    #     posts_list = [d for d in posts_list if any(search in v for v in d.get_title())]

    return render_template('/Forum/test5.html', count=len(posts_list), posts_list=posts_list, form=searchform)


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

        return redirect(url_for('posts.retrieve_posts'))
    else:
        posts_dict = {}
        db = shelve.open('storage.db', 'r')
        posts_dict = db['Posts']
        db.close()

        post = posts_dict.get(id)
        update_post_form.title.data = post.get_title()
        update_post_form.content.data = post.get_content()
        return render_template('/forum/updatePosts.html', form=update_post_form)


@posts.route('/deletePost/<int:id>', methods=['POST'])
def delete_post(id):
    posts_dict = {}
    db = shelve.open('storage.db', 'w')
    posts_dict = db['Posts']

    posts_dict.pop(id)

    db['Posts'] = posts_dict
    db.close()

    return redirect(url_for('posts.retrieve_posts'))


@posts.route('/retrieveThread/<int:id>/', methods=['GET', 'POST'])
def retrieve_thread(id):
    form = CreateCommentForm(request.form)
    posts_dict = {}
    db = shelve.open('storage.db', 'c')
    posts_dict = db['Posts']
    post = posts_dict.get(id)
    if request.method == 'POST' and form.validate():
        comment = Comment(form.comment.data, session['username'])
        post.add_comment(comment)
        db['Posts'] = posts_dict
        return redirect(url_for(f'posts.retrieve_thread', id=id))
    else:
        db.close()
        return render_template("forum/retrieveThread.html", post=post, form=form)


@posts.route('/updateComments/<int:id>/', methods=['GET', 'POST'])
def update_comments(id):
    update_comment_form = CreateCommentForm(request.form)
    if request.method == 'POST' and update_comment_form.validate():
        comments_dict = {}
        db = shelve.open('storage.db', 'w')
        comments_dict = db['comments']

        comment = comments_dict.get(id)
        comment.set_comment(update_comment_form.comment.data)
        comment.set_content(update_comment_form.content.data)
        db['Comments'] = comments_dict
        db.close()

        return redirect(url_for('posts.retrieve_thread'))
    else:
        comments_dict = {}
        db = shelve.open('storage.db', 'r')
        comments_dict = db['Comments']
        db.close()

        comment = comments_dict.get(id)
        update_comment_form.comment.data = comment.get_comments()
        return render_template('/forum/updateComments.html', form=update_comment_form)


@posts.route('/retrieveThread/<int:postid>/deleteComment/<int:commentid>', methods=['POST'])
def delete_comment(postid, commentid):
    posts_dict = {}
    db = shelve.open('storage.db', 'w')
    posts_dict = db['Posts']

    posts_dict.pop(id)

    db['Posts'] = posts_dict
    db.close()

    return redirect(url_for('posts.retrieve_thread'))