"""
The flask application package.
"""
import logging
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_session import Session


app = Flask(__name__)
app.config.from_object(Config)


# app.logger.setLevel(logging.DEBUG)
# StreamerHandler=logging.StreamHandler()
# StreamerHandler.setLevel(logging.DEBUG)
# app.logger.addHandler(StreamerHandler)



wsgi_app = app.wsgi_app
app.logger.setLevel(logging.INFO)
streamHandler = logging.StreamHandler()
streamHandler.setLevel(logging.INFO)
app.logger.addHandler(streamHandler)
app.config.from_object(Config)
logging.basicConfig(
    format="%(asctime)s %(levelname)-8s %(message)s",
    level=logging.INFO,
    datefmt="%Y-%m-%d %H:%M:%S"
)



Session(app)
db = SQLAlchemy(app)
login = LoginManager(app)
login.login_view = 'login'


import FlaskWebProject.views