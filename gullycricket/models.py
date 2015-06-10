# flywheel dynamodb
from datetime import datetime
from flywheel import Model, Field, GlobalIndex


class Player(Model):
    playerid = Field(hash_key=True)
    fullname = Field(range_key=True)
    nickname = Field()
    email = Field()
    phone = Field()
    dob = Field(data_type=datetime)
    playing_role = Field()
    batting_style = Field()
    bowling_style = Field()
    biography = Field()

    def __repr__(self):
        return '<User %r:%r>' % (self.playerid, self.fullname)

    def __init__(self, playerid, fullname, nickname, email, phone, dob,
                 playing_role, batting_style, bowling_style, biography):
        self.playerid = playerid
        self.fullname = fullname
        self.nickname = nickname
        self.email = email
        self.phone = phone
        self.batting_style = batting_style
        self.bowling_style = bowling_style
        self.biography = biography
