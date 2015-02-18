from flask import Blueprint
from webapp import signals

bp = Blueprint("mod_b", __name__, template_folder="templates")


@signals.on_app_initialize.connect
def initialize(app):
    print("init b")
    app.register_blueprint(bp, url_prefix="/b")


@bp.route("/")
def index():

    return "b"