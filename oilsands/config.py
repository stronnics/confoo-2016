import os

GMAIL 			   = os.environ['GMAIL']
SENDGRID_LOGIN     = os.environ['SENDGRID_LOGIN']
SENDGRID_PASSWORD  = os.environ['SENDGRID_PASSWORD']

CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'

basedir = os.path.abspath(os.path.dirname(__file__))
