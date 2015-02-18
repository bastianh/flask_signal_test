from flask import Blueprint
from webapp import signals

bp = Blueprint("mod_a", __name__, template_folder="templates")

@signals.on_app_initialize.connect
def initialize(app):
    print("init a")
    app.register_blueprint(bp, url_prefix="/a")


@bp.route("/")
def index():
    return "a"