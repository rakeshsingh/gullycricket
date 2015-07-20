# flywheel dynamodb
from datetime import datetime
from flywheel import Model, Field, GlobalIndex


class Player(Model):
    playerid = Field(hash_key=True)
    fullname = Field(range_key=True)
    nickname = Field()
    email = Field()
    password = Field()
    phone = Field()
    dob = Field(data_type=datetime)
    playing_role = Field()
    batting_style = Field()
    bowling_style = Field()
    biography = Field()
    authenticated = True

    def __repr__(self):
        return '<User %r:%r>' % (self.playerid, self.fullname)

    def __init__(self, playerid, fullname, nickname, email, phone):
        self.playerid = unicode(playerid)
        self.fullname = unicode(fullname)
        self.nickname = unicode(nickname)
        self.email = unicode(email)
        self.phone = unicode(phone)
        self.batting_style='right-hand bat'
        self.bowling_style='right-arm medium-pace'
        self.authenticated = True
        
    def __str__(self):
        return '<User %r:%r>' % (self.playerid, self.fullname)

    #following methods are required for flask-login
    def is_active(self):
        """True, as all users are active."""
        return True

    def get_id(self):
        """Return the email address to satisfy Flask-Login's requirements."""
        return self.playerid

    def is_authenticated(self):
        """Return True if the user is authenticated."""
        return self.authenticated


    def is_anonymous(self):
        """False, as anonymous users aren't supported."""
        return False