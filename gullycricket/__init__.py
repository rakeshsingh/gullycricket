# app.py or app/__init__.py
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app, use_native_unicode=True, session_options=None)

# Now we can access the configuration variables via app.config["VAR_NAME"].
from gullycricket import models, views, api
