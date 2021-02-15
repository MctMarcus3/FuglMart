from flask import Blueprint, render_template
from functools import wraps
import shelve

dashboard = Blueprint("dashboard", __name__)

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


@dashboard.route("/")
@dashboard.route("/index")
def index():
    return render_template("dashboard/dashboard.html")
