from wtforms import Form, BooleanField, DateField, TextField, TextAreaField,PasswordField, validators

class LoginForm(Form):
    openid = TextField('openid', validators=[validators.DataRequired()])
    remember_me = BooleanField('remember_me', default=False)

class PlayerRegistrationForm(Form):
    email= TextField('Email Address', [validators.Length(min=6, max=50),validators.Email()])
    password = PasswordField('New Password', [
        validators.Required(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password')
