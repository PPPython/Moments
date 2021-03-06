from flask import Flask
from flask.ext.login import LoginManager
from flask.ext.sqlalchemy import SQLAlchemy
import config
from flask.ext.pagedown import PageDown

db = SQLAlchemy()
pagedown = PageDown()

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'

def create_app(confi = None):
    app = Flask(__name__)
    app.config.from_object(config.DevelopmentConfig)
    db.init_app(app)
    pagedown.init_app(app)
    from api_1_0 import api as api_1_0_blueprint
    app.register_blueprint(api_1_0_blueprint,url_prefix='/api/v1.0')

    return app