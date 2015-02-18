# coding=utf-8
from webapp.app import create_app

app = create_app()

app.run(debug=True)