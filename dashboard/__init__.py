from flask import Blueprint, render_template
import shelve

dashboard = Blueprint("dashboard", __name__, static_folder="static", template_folder="templates")


@dashboard.route("/")
@dashboard.route("/index")
def index():
    return render_template("dashboard/dashboard.html")
