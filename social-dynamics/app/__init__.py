from flask import Flask
from flask.ext.basicauth import BasicAuth

app = Flask(__name__)
app.config.from_object('config')

from app import views

basic_auth = BasicAuth(app)