import json
from flask import Blueprint, render_template

bp_facts = Blueprint("facts", __name__, url_prefix="/facts")


@bp_facts.route("/")
def index():
    return render_template("facts.html")


@bp_facts.route("/new")
def facts_new():
    return render_template("new_facts.html")
