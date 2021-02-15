from flask import render_template, request, redirect, url_for, Blueprint, session, jsonify 
import shelve
from .Form import CreateUserForm, UserProfile
from .User import User

account = Blueprint("account", __name__,
                    static_folder="static",
                    template_folder="templates")


@account.route('/', methods=['GET'])
def index():
    if session['user_id'] is not None:
        return redirect(url_for('account.profile'))
    create_user_form = CreateUserForm(request.form)
    return render_template('account.html', form=create_user_form)



@account.route('/create', methods=['POST', 'GET'])
def create():
    create_user_form = CreateUserForm(request.form)
    if request.method == 'POST' and create_user_form.validate():
        users_dict = {}
        db = shelve.open('storage.db', 'c')

        try:
            users_dict = db['Users']
        except KeyError:
            print("Error in retrieving Users from storage.db.")

        try:
            User.count = db["UsersCount"]
        except KeyError:
            print("Error in retrieving UsersCount from storage.db.")
        admin = False
        if create_user_form.email.data.split("@")[1] == "fugl.store":
            admin = True
        for user in users_dict.values():
            if user.get_email() == create_user_form.email.data:
                return render_template('account.html', registererror=True, form=create_user_form)
        user = User(create_user_form.email.data, create_user_form.password.data, admin)
        users_dict[user.get_accountId()] = user
        db['Users'] = users_dict
        db["UsersCount"] = User.count
        session['user_id'] = user.get_accountId()
        # Test codes
        users_dict = db['Users']
        user = users_dict[user.get_accountId()]
        print(user.get_email(), "was stored in storage.db successfully")
        print(user.get_admin(), "was stored in storage.db successfully")
        print(db["UsersCount"], User.count)

        db.close()

        return redirect(url_for('account.profile'))
    return redirect(url_for('account.index'))

@account.route('/login', methods=['POST', 'GET'])
def login():
    login_user_form = CreateUserForm(request.form)
    if request.method == 'POST' and login_user_form.validate():
        # Access shelve to retrieve users_dict
        users_dict = {}
        db = shelve.open('storage.db', 'c')

        try:
            users_dict = db['Users']
        except KeyError:
            print("Error in retrieving Users from storage.db.")
        for user in users_dict.values():
            if user.get_email() == login_user_form.email.data:
                if user.get_password() == login_user_form.password.data:
                    session['user_id'] = user.get_accountId()
                    return redirect(url_for('account.profile'))
        # Check if email and password matches with database
        return render_template('account.html', error=True, form=login_user_form)
    return render_template('account.html', form=login_user_form)


@account.route('/profile')
def profile():
    user_id = session['user_id']
    update_user_form = UserProfile(request.form)
    if request.method == 'POST' and update_user_form.validate():
        return redirect(url_for('account.profile'))
    # update_user_form.title.data = user.get_email()
    return render_template('profile.html', form=update_user_form, user_id=user_id)


@account.route('/deleteUser/<int:id>', methods=['POST'])
def delete_user(id):
    users_dict = {}
    db = shelve.open('storage.db', 'w')
    users_dict = db['Users']

    users_dict.pop(id)

    db['Users'] = users_dict
    db.close()

    return redirect(url_for('account.login'))

@account.route('/logout')
def logout():
    session['user_id'] = None
    return redirect(url_for("home"))
