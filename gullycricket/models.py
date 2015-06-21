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

    def __repr__(self):
        return '<User %r:%r>' % (self.playerid, self.fullname)

    def __init__(self, playerid, fullname, nickname, email, phone):
        self.playerid = unicode(playerid)
        self.fullname = unicode(fullname)
        self.nickname = unicode(nickname)
        self.email = unicode(email)
        self.phone = unicode(phone)
        
    def __str__(self):
        return '<User %r:%r>' % (self.playerid, self.fullname)
