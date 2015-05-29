from gullycricket import app, db

class Player(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fullname =  db.Column(db.String(64), index=True)
    nickname = db.Column(db.String(64), index=True)
    email = db.Column(db.String(120), index=True, unique=True)
    phone = db.Column(db.String(30))
    dob = db.Column(db.Date())
    batting_style = db.Column(db.String(120))
    bowling_style = db.Column(db.String(120))
    biography = db.Column(db.String(240))

    def __repr__(self):
        return '<User %r>' % (self.fullname)
