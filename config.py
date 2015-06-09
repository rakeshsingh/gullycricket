import os
#sample config file
DEBUG=True
basedir = os.path.abspath(os.path.dirname(__file__))

#for forms
WTF_CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'

#for database
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
