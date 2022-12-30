from flask import Blueprint
from flask import flash
from flask import g
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for
from werkzeug.exceptions import abort

from main_app.db import get_db

    # a simple page that says hello

bp = Blueprint("get_data", __name__)


@bp.route("/data")
def index():
    db = get_db()
    tweets = db.execute(
        "SELECT * from tweets"
    ).fetchall()
    coins = db.execute(
        "SELECT * FROM top_coins ORDER BY time_now LIMIT 10;"
    ).fetchall()
    return render_template("index.html", tweets=tweets, coins=coins)
