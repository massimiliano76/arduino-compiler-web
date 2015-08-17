from flask import Flask, render_template 
from flask.ext.bootstrap import Bootstrap 
# from flask.ext.mail import Mail
from flask.ext.moment import Moment
from flask.ext.sqlalchemy import SQLAlchemy 
from config import config

bootstrap = Bootstrap()
#mail = Mail()
moment = Moment()
db = SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__) 
    app.config.from_object(config[config_name]) 
    config[config_name].init_app(app)
    bootstrap.init_app(app)
    #mail.init_app(app)
    moment.init_app(app)
    db.init_app(app)

    from .main import main as main_bp
    app.register_blueprint(main_bp)

    return app