from werkzeug.utils import import_string
from webapp import settings
from flask import Flask
from webapp.signals import on_app_initialize


def create_app():
    app = Flask(__name__)
    app.config.from_object(settings)

    for module_name in app.config.get("LOAD_MODULES", []):
        import_string(module_name)

    on_app_initialize.send(app)

    return app