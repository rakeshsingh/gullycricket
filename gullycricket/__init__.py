# app.py or app/__init__.py
from flask import Flask
# for dynamodb
from flywheel import Engine


# begin app construction
app = Flask(__name__)
app.config.from_object('config')

# dynadbo connection
# Create an engine and connect to an AWS region
engine = Engine()
engine.connect_to_host(host='localhost',port=8000)


# Now we can access the configuration variables via app.config["VAR_NAME"].
from gullycricket import models, views, api

#register models to dynamodb
engine.register(models.Player)
