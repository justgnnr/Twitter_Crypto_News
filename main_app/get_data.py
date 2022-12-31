from flask import Blueprint
from flask import flash
from flask import g
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for
from werkzeug.exceptions import abort

from main_app.db import get_db


bp = Blueprint("get_data", __name__)


@bp.route("/")
def index():
    db = get_db()
    tweets = db.execute(
        "SELECT * from tweets"
    ).fetchall()
    coins = db.execute(
        "SELECT * FROM top_coins ORDER BY time_now LIMIT 10;"
    ).fetchall()
    return render_template("index.html", tweets=tweets, coins=coins)

@bp.route("/<name>")
def detail_view(name):
    db = get_db()
    coin = db.execute(
        "SELECT * FROM top_coins ORDER BY time_now LIMIT 10;"
    ).fetchone()
    tweets = db.execute(
        "SELECT * from tweets"
    ).fetchall()

    return render_template("detail.html", name=name, coin=coin, tweets=tweets)
