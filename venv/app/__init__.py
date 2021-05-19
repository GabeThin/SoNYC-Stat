import logging
from logging.handlers import SMTPHandler, RotatingFileHandler
import os
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from config import Config

app = Flask(__name__)


application = app

app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
bootstrap = Bootstrap(app)
#login_manager = LoginManager()

wsgi_app = app.wsgi_app

if __name__ == '__main__':
    from os import environ
    app.run(debug=False, port=environ.get("PORT", 5000), host='0.0.0.0')

from app import routes, models, errors