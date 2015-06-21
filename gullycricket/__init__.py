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

# Create the dynamo table for our registered model
engine.create_schema()

for i in range(1, 10):
    player = engine.get(models.Player, playerid=str(i), fullname='Player:'+str(i))
    if player:
        print('record already present, updating: ', str(player))
    else:
        player = Player(i, 'Player:'+str(i), 'testplayer',
                        'someone@somewhere.com', '+1-000-000-0001')
        engine.save(player)
