# app.py or app/__init__.py
from flask import Flask
# for dynamodb
from flywheel import Engine


# begin app construction
app = Flask(__name__)
app.config.from_object('config')

# dynadbo connection, create an engine and connect to an AWS region or localhost
engine = Engine()
engine.connect_to_host(host='localhost',port=8000)
#engine.connect_to_region('us-west-2')
# Now we can access the configuration variables via app.config["VAR_NAME"].
from gullycricket import models, views, api,utils
#register models to dynamodb
engine.register(models.Player)
login_manager = utils.get_login_manager()

#below code should go into a init script
# Create the dynamo table for our registered model
engine.create_schema()

for i in range(1, 10):
    player = engine.get(models.Player, playerid=str(i), fullname='Player:'+str(i))
    if player:
        print('record already present, updating: ', str(player))
    else:
        player = models.Player(i, 'Player:'+str(i), 'testplayer',
                        'player'+str(i)+'@somewhere.com', '+1-000-000-0001')
        engine.save(player)