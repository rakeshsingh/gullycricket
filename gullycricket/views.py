from gullycricket import app,engine
from gullycricket.models import Player
from gullycricket.forms import PlayerRegistrationForm
from gullycricket import utils

from flask import render_template,request

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Rakesh'}  # fake user
    posts = [  # fake array of posts
        {
            'author': {'nickname': 'John'},
            'body': 'Beautiful day in Portland!'
        }, {
            'author': {'nickname': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template("index.html", title='Home', user=user, posts=posts)


#login form
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('home'))
    return render_template('login.html', error=error)

#player registration
@app.route('/registerplayer',methods=['GET','POST'])
def register_player():
    form=PlayerRegistrationForm()
    if request.method == 'POST' and form.validate():
        playerid=utils.get_uuid()
        player = Player(playerid,email,password)\
            (playerid, form.email.data, form.password.data)
        engine.save(player)
        flash('Thanks for registering')
        return redirect(url_for('login'))
    return render_template('registerplayer.html', form=form)


@app.route('/players',methods=['GET'])
def getplayers():
    # Get the 10 most recent tweets by 'myuser'
    players = engine.scan(Player).gen()
    return render_template('players.html',players=players)

@app.route('/player/<playerid>',methods=['GET'])
def getplayer(playerid):
    return render_template('player.html')


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404
